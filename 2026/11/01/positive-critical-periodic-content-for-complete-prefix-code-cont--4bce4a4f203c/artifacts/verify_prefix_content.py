"""Reproducibility checks for complete prefix-code periodic content theorem.

Checks selected finite orders; the general claim follows from the proof.
No external modules required.
"""

def de_bruijn(b, k):
    a = [0] * (b * k + 1)
    seq = []
    def db(t, p):
        if t > k:
            if k % p == 0:
                seq.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, b):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    assert len(seq) == b ** k
    return tuple(seq)


def prefix_checker(code):
    assert code and len(set(code)) == len(code)
    for i, w in enumerate(code):
        for j, z in enumerate(code):
            if i != j:
                assert not z[:len(w)] == w
    L = max(map(len, code))
    b = max(max(w) for w in code) + 1
    assert sum(b ** -len(w) for w in code) == 1
    return b, L


def parse_cycle(B, code):
    M = len(B)
    code_lookup = {tuple(w): i for i, w in enumerate(code)}
    L = max(map(len, code))
    def step(j):
        for length in range(1, L + 1):
            w = tuple(B[(j + t) % M] for t in range(length))
            if w in code_lookup:
                return (j + length) % M, code_lookup[w], length
        raise AssertionError('code did not parse')
    f = [step(j) for j in range(M)]
    # Every forward orbit has an eventually periodic tail; take a cycle.
    seen = {}
    trail = []
    at = 0
    while at not in seen:
        seen[at] = len(trail)
        trail.append(at)
        at = f[at][0]
    residues = trail[seen[at]:]
    symbols = tuple(f[j][1] for j in residues)
    lengths = tuple(f[j][2] for j in residues)
    assert len(residues) == len(set(residues))
    assert sum(lengths) % M == 0
    assert M <= sum(lengths) <= L * M
    assert M / L <= len(symbols) <= M
    return residues, symbols, lengths


def test_code(code, maximum_order):
    b, L = prefix_checker(code)
    for k in range(1, maximum_order + 1):
        B = de_bruijn(b, k)
        M = b ** k
        words = {tuple(B[(j+t)%M] for t in range(k)) for j in range(M)}
        assert len(words) == M
        residues, symbols, lens = parse_cycle(B, code)
        n = len(symbols)
        # A shorter symbol period would give a repeated codeword boundary.
        assert all(symbols != symbols[d:] + symbols[:d] for d in range(1, n))
        assert len({tuple(B[(j + t) % M] for t in range(k)) for j in residues}) == n
        # Explicitly check all pairs' maximal weighted common symbol prefix.
        max_weight = 0
        for x in range(n):
            for y in range(x + 1, n):
                i = 0
                weight = 0
                while i < k and symbols[(x+i)%n] == symbols[(y+i)%n]:
                    weight += len(code[symbols[(x+i)%n]])
                    i += 1
                assert weight <= k - 1, (k, x, y, weight)
                max_weight = max(max_weight, weight)
        assert n * b ** (-max_weight) >= b / L - 1e-12
        print('alphabet', b, 'lengths', [len(w) for w in code],
              'order', k, 'binary/digit period', M,
              'symbol period', n, 'max common code-length', max_weight,
              'n * eta_symbol^s', round(n * b ** (-max_weight), 8))

if __name__ == '__main__':
    test_code([(0,), (1,0), (1,1)], 7)
    test_code([(0,), (1,0), (1,1,0), (1,1,1)], 7)
    test_code([(0,), (1,), (2,0), (2,1), (2,2)], 4)
    print('VERIFY_OK')
