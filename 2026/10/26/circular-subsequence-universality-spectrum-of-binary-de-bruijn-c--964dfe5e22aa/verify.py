"""Independent exhaustive verification of circular subsequence universality on binary de Bruijn cycles."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import sys


def cycles_via_windows(order):
    """Hamiltonian cycles on the binary order-`order` overlap graph.

    The all-zero window occurs once, so starting there fixes rotation.
    """
    mask = (1 << order) - 1
    highest = 1 << (order - 1)
    path = [0]

    def visit(v, used):
        if len(path) == 1 << order:
            if ((v << 1) & mask) == 0:
                yield ''.join('1' if u & highest else '0' for u in path)
            return
        for b in (0, 1):
            u = ((v << 1) & mask) | b
            if not (used >> u) & 1:
                path.append(u)
                yield from visit(u, used | (1 << u))
                path.pop()

    yield from visit(0, 1)


def cycles_via_edges(order):
    """Euler trails in the order-(order-1) overlap graph; remove rotations."""
    mask = (1 << (order - 1)) - 1
    visited = [False] * (1 << order)
    path = []

    def visit(v):
        if len(path) == 1 << order:
            if v == 0:
                w = ''.join(map(str, path))
                doubled = w + w
                z = doubled.index('0' * order)
                yield doubled[z:z + len(w)]
            return
        for b in (0, 1):
            e = (v << 1) | b
            if not visited[e]:
                visited[e] = True
                path.append(b)
                yield from visit(e & mask)
                path.pop()
                visited[e] = False

    yield from visit(0)


def valid_debruijn(w, order):
    n = 1 << order
    if len(w) != n or not w.startswith('0' * order):
        return False
    return len({(w + w[:order - 1])[i:i + order] for i in range(n)}) == n


def arch_index(w):
    seen = 0
    count = 0
    for b in w:
        seen |= 1 << int(b)
        if seen == 3:
            count += 1
            seen = 0
    return count


def absent_index(w):
    """Independent shortest-absent-subsequence dynamic program.

    dp[i] = length of a shortest binary word absent from suffix w[i:].
    An unavailable first symbol yields an absent word of length 1.
    """
    n = len(w)
    dp = [0] * (n + 1)
    dp[n] = 1
    nxt = [n, n]
    for i in range(n - 1, -1, -1):
        nxt[int(w[i])] = i
        dp[i] = 1 + min(dp[nxt[b] + 1] if nxt[b] < n else 0
                        for b in (0, 1))
    return dp[0] - 1


def spectrum(order, cross_check=True):
    words = list(cycles_via_windows(order))
    assert len(words) == len(set(words))
    assert all(valid_debruijn(w, order) for w in words)
    if cross_check:
        edges = list(cycles_via_edges(order))
        assert len(edges) == 2 * len(words), (order, len(edges), len(words))
        assert set(edges) == set(words)
    result = {}
    for w in words:
        n = len(w)
        rotations = (w[i:] + w[:i] for i in range(n))
        value = max(arch_index(v) for v in rotations)
        assert value == max(absent_index(w[i:] + w[:i]) for i in range(n))
        result[w] = value
    return result


def main():
    small = {k: Counter(spectrum(k).values()) for k in (1, 2, 3, 4)}
    assert small[1] == Counter({1: 1})
    assert small[2] == Counter({2: 1})
    assert small[3] == Counter({3: 2})
    assert small[4] == Counter({5: 8, 6: 8})
    res = spectrum(5)
    assert Counter(res.values()) == Counter({10: 512, 11: 1536})
    joint = Counter((arch_index(w), val) for w, val in res.items())
    assert joint == Counter({(9, 10): 256, (10, 10): 256,
                            (10, 11): 1152, (11, 11): 384})

    def canonical(w):
        doubled = w + w
        pos = doubled.index('00000')
        return doubled[pos:pos + len(w)]

    def opposite(w):
        return ''.join('1' if ch == '0' else '0' for ch in w)

    seen = set()
    orbits = Counter()
    for w, val in res.items():
        if w in seen:
            continue
        members = {canonical(t) for t in
                   (w, w[::-1], opposite(w), opposite(w)[::-1])}
        assert members <= set(res)
        assert {res[t] for t in members} == {val}
        seen |= members
        orbits[(val, len(members))] += 1
    assert seen == set(res)
    assert orbits == Counter({(10, 2): 16, (10, 4): 120,
                             (11, 2): 16, (11, 4): 376})
    rows = ['binary_word\tcircular_universality_index'] + [w + '\t' + str(res[w]) for w in sorted(res)]
    body = ('\n'.join(rows) + '\n').encode('ascii')
    path = Path(__file__).with_name('spectrum.tsv')
    if sys.argv[1:] == ['--build-certificate']:
        path.write_bytes(body)
    else:
        assert path.read_bytes() == body, 'Certificate data disagree with exhaustive search'
    print('ORDERS', sorted((k, dict(sorted(c.items()))) for k, c in small.items()))
    print('ORDER5', dict(sorted(Counter(res.values()).items())), 'total', len(res))
    print('CANONICAL_JOINT', dict(sorted(joint.items())))
    print('SYMMETRY_ORBITS', dict(sorted(orbits.items())))
    print('CERT_BYTES', len(body), 'CERT_SHA256', sha256(body).hexdigest())
    print('VERIFIED')


if __name__ == '__main__':
    main()
