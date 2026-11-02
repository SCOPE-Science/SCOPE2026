"""Independent finite checks for the circular BWT of dyadic paperfolding prefixes.

Only standard-library Python is required. This tests finite ranks, not the induction.
"""
from collections import defaultdict
from itertools import groupby


def paperfolding(k):
    n = 1 << k
    return ''.join('1' if (i // (i & -i)) % 4 == 1 else '0'
                   for i in range(1, n + 1))


def cyclic_sa(w):
    n = len(w)
    ranks = [int(c) for c in w]
    h = 1
    sa = list(range(n))
    while h < n:
        sa.sort(key=lambda i: (ranks[i], ranks[(i + h) % n]))
        new = [0] * n
        for j in range(1, n):
            old, cur = sa[j - 1], sa[j]
            new[cur] = new[old] + (
                (ranks[old], ranks[(old + h) % n]) !=
                (ranks[cur], ranks[(cur + h) % n]))
        ranks = new
        h *= 2
    assert ranks[sa[-1]] == n - 1  # distinct rotations
    return sa


def bwt(w, sa):
    return ''.join(w[(i - 1) % len(w)] for i in sa)


def A(j):
    assert j >= 7
    t = 1 << (j - 7)
    return '1' * t + '0' * (t - 1) + '1' * t + '0' * (t + 1)


def B(k):
    assert k >= 6
    s = '1011'
    for j in range(7, k + 1):
        s = A(j) + s
    return s


def predicted(k):
    assert k >= 6
    q = 1 << (k - 5)
    blocks = [
        '1' * (2*q-1),
        '1' * (2*q) + '0' * (2*q-1),
        '1' * (2*q+1),
        '0' * (2*q),
        '1' * q, '0' * q, '1' * q, '0' * (q-1),
        '0' * (2*q+1),
        '1' * q + '0' * (q-1),
        '1' * (2*q),
        '1' * q + '0' * (q+1),
        '1' * (2*q),
        '0' * q,
        A(k+1),
        '0' * q,
        B(k),
        '0' * (2*q+1)
    ]
    assert sum(map(len, blocks)) == (1 << k)
    return ''.join(blocks)


def local_table(k):
    """Frequency distribution from all 64 short macroblock cases, symbolically.

    Each (parity, trailing-bit) macrotype occurs the specified number
    of times. A length-seven window crosses at most one macro boundary,
    and its next block contributes only its six constant leading bits.
    """
    assert k >= 6
    r = 1 << (k - 6)
    freq = {(0,0): r, (0,1): r, (1,0): r-1, (1,1): r+1}
    K = lambda e,x: ('110110011100100' if e == 0 else '110110001100100')+str(x)
    totals = defaultdict(int)
    preceding = defaultdict(set)
    origins = defaultdict(set)
    for (e,x), count in freq.items():
        s = K(e,x)+K(1-e,0)
        for j in range(16):
            u=s[j:j+7]
            assert len(u)==7
            totals[u] += count
            origins[u].add(j)
            if j != 0:
                preceding[u].add(s[j-1])
    assert len(totals) == 28
    assert {u for u,v in preceding.items() if len(v) > 1} == {'1000110','1001110','1100100'}
    assert origins['1101100'] == {0}
    return dict(totals),dict(origins)


def main():
    # Naive comparison validates cyclic suffix-doubling independently.
    for k in range(2,10):
        w=paperfolding(k)
        slow=sorted(range(len(w)),key=lambda i:w[i:]+w[:i])
        fast=cyclic_sa(w)
        assert slow==fast, (k,'suffix array')

    # Exact macroblock enumeration and BWT formula checks.
    for k in range(6,15):
        w=paperfolding(k)
        sa=cyclic_sa(w)
        observed=bwt(w,sa)
        expected=predicted(k)
        assert observed==expected,(k,'BWT',next((i for i,(a,b) in enumerate(zip(observed,expected)) if a!=b),None))
        assert len(list(groupby(observed))) == 4*k-4,(k,'runs')
        cnt,origins=local_table(k)
        observed_cnt=defaultdict(int)
        for i in range(len(w)):
            observed_cnt[''.join(w[(i+j)%len(w)] for j in range(7))]+=1
        assert dict(observed_cnt)==cnt,(k,'seven-gram frequency')
        assert origins['1000110']=={4,12} and origins['1001110']=={4,12}
        assert origins['1100100']=={8} and origins['1101100']=={0}
        print(f'rank {k}: length {len(w)}, BWT runs {4*k-4}, 28 local classes, all checks passed')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
