#!/usr/bin/env python3
"""Exact finite cross-checks for the one-Frobenius number of a repunit-derived triple."""

def predicted_second(b, r):
    a = b*b+b+1
    g = a+b
    h = 2*a-1
    H = g+b*h
    if r == 0:
        return H
    if r > b*b:
        return (a-r)*h+b*a
    c = (r+b-1)//b
    u = b*c-r
    B = c*g+u*h
    if u:
        return B+b*a
    if c < b:
        return B+H
    return B+(b+1)*a


def direct_second_by_pairs(b):
    a = b*b+b+1
    g = a+b
    h = 2*a-1
    T = b*g+(b-1)*h+b*a
    pairs = [[] for _ in range(a)]
    for u in range(T//g+1):
        for v in range((T-u*g)//h+1):
            w=u*g+v*h
            pairs[w%a].append(w)
    return [sorted(p)[1] for p in pairs]


def dp_first_failure(b):
    a=b*b+b+1; g=a+b; h=2*a-1
    F=4*b**3+2*b*b-2
    N=F+a
    count=[0]*(N+1)
    count[0]=1
    for coin in (a,g,h):
        for n in range(coin,N+1):
            count[n] += count[n-coin]
    failures=[n for n,c in enumerate(count) if c<=1]
    assert failures[-1] == F, (b,failures[-1],F)
    assert count[F]==1, (b,count[F])
    assert min(count[F+1:])>=2
    return F


def main():
    nres=0
    for b in range(2,61):
        a=b*b+b+1
        g=a+b
        h=2*a-1
        observed=direct_second_by_pairs(b)
        expected=[predicted_second(b,r) for r in range(a)]
        assert observed==expected, (b,[(i,observed[i],expected[i]) for i in range(a) if observed[i]!=expected[i]][:3])
        maximum=max(observed)
        expected_max=b*g+(b-1)*h+b*a
        assert maximum==expected_max
        assert [r for r,w in enumerate(observed) if w==maximum]==[a-2*b]
        assert maximum-a == 4*b**3+2*b*b-2
        assert ((b+1)*g == b*a+h)
        nres += a
        if b<=32:
            dp_first_failure(b)
    print('VERIFIED: second Apéry thresholds in bases 2..60 ({} residues); independent full denumerant DP for bases 2..32'.format(nres))

if __name__=='__main__': main()
