"""Exact independent factorial/arborescence census of cyclic three-gram types.
Requires Python 3 standard library only. Run next to profile_census.csv.
"""
from collections import Counter
from math import factorial
from pathlib import Path
import csv

N = 16
FAC = [factorial(i) for i in range(N + 1)]


def cycle_count(p, trees):
    """Edge-indistinguishable BEST formula for fixed indexed rotations."""
    a, b, c, d, e, f, g, h = p
    degree = (a + b, c + d, e + f, g + h)
    numerator = N * trees
    for v in degree:
        if v:
            numerator *= FAC[v - 1]
    denominator = 1
    for multiplicity in p:
        denominator *= FAC[multiplicity]
    assert numerator % denominator == 0
    return numerator // denominator


def compute():
    answer = {}
    strata = Counter()

    def record(p, trees, stratum):
        assert p not in answer and sum(p) == N
        answer[p] = cycle_count(p, trees)
        strata[stratum] += 1

    # Every vertex present, b>0 and d>0.
    # Flow conservation forces e=b, g=d, f=c+d-b.
    for b in range(1, N + 1):
        for d in range(1, N + 1):
            for c in range(N + 1):
                f = c + d - b
                if f < 0:
                    continue
                remainder = N - b - 2 * c - 3 * d
                if remainder < 0:
                    continue
                for a in range(remainder + 1):
                    h = remainder - a
                    record((a,b,c,d,b,f,d,h), b*d*(c+d), 'four-vertex')

    # The 00-vertex is absent: b=0, d>0 and necessarily a=0.
    for d in range(1, N + 1):
        for c in range(N + 1):
            f = c + d
            h = N - 2*c - 3*d
            if h >= 0:
                record((0,0,c,d,0,f,d,h), d*(c+d), 'three-vertex-no-00')

    # The 11-vertex is absent: d=0, b>0 and necessarily h=0.
    for b in range(1, N + 1):
        for c in range(b, N + 1):
            f = c - b
            a = N - b - 2*c
            if a >= 0:
                record((a,b,c,0,b,f,0,0), b*c, 'three-vertex-no-11')

    # No 001, 011: alternating two-cycle or one constant loop.
    record((0,0,N//2,0,0,N//2,0,0), N//2, 'alternating')
    record((N,0,0,0,0,0,0,0), 1, 'constant-0')
    record((0,0,0,0,0,0,0,N), 1, 'constant-1')
    return answer, strata


def main():
    out, strata = compute()
    assert len(out) == 271, len(out)
    assert sum(out.values()) == (1 << N)
    assert strata['four-vertex'] == 226
    assert sum(v for k,v in strata.items() if k!='four-vertex') == 45
    maxima = sorted(out.values(), reverse=True)
    assert maxima[:3] == [1296, 1280, 1152]
    assert [p for p,x in out.items() if x==1296] == [(2,)*8]
    assert [p for p,x in out.items() if x==1280] == [(1,2,3,2,2,3,2,1)]

    csv_path = Path(__file__).with_name('profile_census.csv')
    with csv_path.open(newline='', encoding='utf-8') as fh:
        rows = list(csv.reader(fh))
    assert rows[0] == ['000','001','010','011','100','101','110','111','fiber_size']
    expected = [list(map(str, (*p, out[p]))) for p in sorted(out)]
    assert rows[1:] == expected, 'profile census differs from exact Eulerian formula'
    print('EULER_OK n=16 profiles=271 four_vertex=226 degenerate=45 maximum=1296 unique; second=1280 unique; sum=65536')


if __name__=='__main__':
    main()
