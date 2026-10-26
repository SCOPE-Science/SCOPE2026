"""Self-contained independent checks for two-marker deletion descendants.
Run: python3 check.py. Requires only the Python standard library.
"""
from itertools import combinations
from math import comb


def c2(k):
    return comb(k, 2) if k >= 2 else 0


def polynomial_coefficient(gaps, t):
    coeff = [1]
    for a in gaps:
        out = [0] * (len(coeff) + a)
        for i, v in enumerate(coeff):
            for j in range(a + 1):
                out[i + j] += v
        coeff = out
    return coeff[t] if t < len(coeff) else 0


def formula(a, b, c, t):
    n = a+b+c+2
    assert 0 <= t <= n
    L = n-t
    v2 = polynomial_coefficient((a,b,c), t)
    v1 = 0
    if t >= 1 and L >= 1:
        v1 = L-max(0,a-t+1)-max(0,b-t)-max(0,c-t+1)
    return v2+v1+(t >= 2)


def direct(a,b,c,t):
    w = '0'*a+'1'+'0'*b+'1'+'0'*c
    L=len(w)-t
    return len({''.join(w[i] for i in I) for I in combinations(range(len(w)),L)})


def aggregate(n,t):
    L=n-t
    return comb(t+2,2)*c2(L)+t*L*L+comb(t,2)*L+(comb(n,2) if t>=2 else 0)


def canonical(n):
    q,r=divmod(n-2,3)
    return ((q,q,q),(q,q+1,q),(q+1,q+1,q))[r]


def plateau(t):
    return comb(t+2,2)+2*t+(t>=2)


if __name__ == '__main__':
    cases=0
    for n in range(2,13):
        for t in range(n+1):
            total=0
            for a in range(n-1):
                for b in range(n-1-a):
                    c=n-2-a-b
                    v=direct(a,b,c,t)
                    w=formula(a,b,c,t)
                    assert v==w,(n,t,a,b,c,v,w)
                    total+=v
                    cases+=1
            assert total==aggregate(n,t),(n,t,total,aggregate(n,t))
    # All finite-n maxima and the stable plateau are checked independently
    # against the pointwise gap formula, beyond the direct small-word census.
    max_cases=0
    for n in range(2,55):
        S=n-2
        for t in range(n+1):
            values=[]
            for a in range(S+1):
                for b in range(S-a+1):
                    c=S-a-b
                    values.append((formula(a,b,c,t),(a,b,c)))
                    max_cases+=1
            if t>=1:
                M=max(v for v,g in values)
                assert M==formula(*canonical(n),t),(n,t,M)
                if n>=3*t+2:
                    assert M==plateau(t),(n,t,M,plateau(t))
                    winners={g for v,g in values if v==M}
                    expected={g for v,g in values if min(g)>=t}
                    assert winners==expected,(n,t,winners,expected)
    print('PASS: direct subsequence enumeration instances =',cases)
    print('PASS: all-length aggregate formula for n=2..12')
    print('PASS: finite-length maxima and plateau classification instances =',max_cases)
