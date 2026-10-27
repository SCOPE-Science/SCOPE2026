"""Exhaustive verification of BWT run spectrum of binary order-five de Bruijn cycles.

Self-contained Python 3; no external packages.
"""
from collections import Counter

TARGET = {20: 38, 22: 426, 24: 840, 26: 608, 28: 130, 30: 6}


def canonical(word):
    """Unique rotation with the sole length-five 00000 cyclic factor at index zero."""
    doubled = word + word
    hits = [i for i in range(len(word)) if doubled[i:i+5] == '00000']
    assert len(hits) == 1
    i = hits[0]
    return doubled[i:i+len(word)]


def ordinary_bwt(word):
    n = len(word)
    doubled = word + word
    order = sorted(range(n), key=lambda i: doubled[i:i+n])
    return ''.join(word[(i-1) % n] for i in order)


def is_order_five_cycle(word):
    if len(word) != 32:
        return False
    twice = word+word
    return len({twice[i:i+5] for i in range(32)}) == 32


def lf_inverse_primitive(mask):
    """Return canonical de Bruijn word if the inverse BWT has one cycle."""
    orientation = [(mask >> u) & 1 for u in range(16)]
    last = [bit for x in orientation for bit in (x, 1-x)]
    ranks = [0, 0]
    lf = []
    for bit in last:
        lf.append((16 if bit else 0) + ranks[bit])
        ranks[bit] += 1
    assert ranks == [16, 16] and sorted(lf) == list(range(32))
    seen = set()
    i = 0
    for _ in range(32):
        if i in seen:
            return None
        seen.add(i)
        i = lf[i]
    if i != 0 or len(seen) != 32:
        return None
    inv = [None] * 32
    for j, pos in enumerate(lf):
        inv[pos] = j
    pos = 0
    word = []
    for _ in range(32):
        word.append('0' if pos < 16 else '1')
        pos = inv[pos]
    word = ''.join(word)
    assert pos == 0 and is_order_five_cycle(word)
    assert canonical(word) == word
    assert ordinary_bwt(word) == ''.join(map(str, last))
    runs = 1 + sum(last[i] != last[i-1] for i in range(1, 32))
    formula = 17 + sum(orientation[i] == orientation[i+1] for i in range(15))
    assert runs == formula
    return word, runs


def exhaustive_bwt():
    results = {}
    counts = Counter()
    for mask in range(1 << 16):
        data = lf_inverse_primitive(mask)
        if data is None:
            continue
        word, runs = data
        assert word not in results
        results[word] = runs
        counts[runs] += 1
    return results, counts


def exhaustive_euler():
    """Independent recursion in edges of B(2,4), rooted at 00000."""
    used_full = (1 << 32) - 1
    path = ['0']
    results = {}
    def visit(vertex, used):
        if used == used_full:
            if vertex == 0:
                word = canonical(''.join(path))
                assert is_order_five_cycle(word)
                assert word not in results
                transform = ordinary_bwt(word)
                runs = 1+sum(transform[i]!=transform[i-1] for i in range(1,32))
                results[word] = runs
            return
        for bit in (0,1):
            edge = (vertex << 1) | bit
            if (used >> edge) & 1:
                continue
            path.append(str(bit))
            visit(edge & 15, used | (1 << edge))
            path.pop()
    visit(0,1)  # distinguished edge 00000 already used, starting 0 symbol emitted
    return results



def small_order_histogram(k):
    """Rooted-edge Euler enumeration for k=2,3,4 (independent baseline)."""
    m = 1 << k
    used_full = (1 << m) - 1
    path = ['0']
    counts = Counter()
    def visit(vertex, used):
        if used == used_full:
            if vertex == 0:
                word = ''.join(path)
                twice = word+word
                assert len({twice[i:i+k] for i in range(m)}) == m
                transformed = ordinary_bwt(word)
                runs = 1 + sum(transformed[i]!=transformed[i-1] for i in range(1,m))
                counts[runs] += 1
            return
        for bit in (0,1):
            edge = (vertex<<1) | bit
            if (used>>edge)&1:
                continue
            path.append(str(bit))
            visit(edge & ((1<<(k-1))-1), used | (1<<edge))
            path.pop()
    visit(0,1)
    return counts


def main():
    for k, expected in [(2,{4:1}),(3,{6:2}),(4,{10:4,12:4,14:8})]:
        result = dict(small_order_histogram(k))
        assert result == expected
        assert min(result) == (1 << (k-1)) + 2
        print('ORDER', k, 'histogram:', sorted(result.items()))
    bwt, counts = exhaustive_bwt()
    graph = exhaustive_euler()
    assert bwt == graph
    assert len(bwt) == 2048
    assert dict(counts) == TARGET, (counts, TARGET)
    assert set(counts) == set(TARGET)
    assert min(counts) == 20 and max(counts) == 30
    print('ORDER 5:', len(bwt), 'cycles, histogram:', sorted(counts.items()))
    for runs in sorted(TARGET):
        example = min(w for w in bwt if bwt[w] == runs)
        print('runs:', runs, 'count:', TARGET[runs], 'example:', example)
    print('PASS: independent exhaustive BWT/LF and Euler-cycle enumerations agree')


if __name__ == '__main__':
    main()
