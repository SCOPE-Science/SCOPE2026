"""Reproducible exact-arithmetic checks for random quadratic quadrature.

Run: python verify.py. Supplementary checks only; proofs cover all real q and n.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, log
from random import Random


def coeff(n):
    """Integer coefficients of (a+b)^(n-2)-(2-a-b)^(n-2)."""
    k = n - 2
    out = {}
    for r in range(k + 1):
        out[(r, k-r)] = out.get((r, k-r), 0) + comb(k, r)
    for j in range(k + 1):
        for r in range(j + 1):
            idx = (r, j-r)
            out[idx] = out.get(idx, 0) - comb(k, j) * 2**(k-j) * (-1)**j * comb(j, r)
    return {key:val for key,val in out.items() if val}


def monomial_moment(r,s,q):
    """Integrate a^r*b^s over q <= a*b <= 1.

    Return exact A,B with integral=A+B*log(q).
    """
    v = (1-q**(r+1))/F(r+1)
    if r == s:
        return v/F(s+1), q**(r+1)/F(s+1)
    v -= q**(s+1)*(1-q**(r-s))/F(r-s)
    return v/F(s+1), F(0)


def exact_probability(n,q):
    A=B=F(0)
    for (r,s),c in coeff(n).items():
        u,v=monomial_moment(r,s,q)
        A+=c*u
        B+=c*v
    scale=F(n*(n-1),2**n)
    return A*scale,B*scale


def feasible_extremes(xs,q):
    negative = [-x for x in xs if x < 0]
    positive = [x for x in xs if x > 0]
    return bool(negative and positive and min(negative)*min(positive)<=q<=max(negative)*max(positive))


def feasible_triples(xs,q):
    if len(xs)==2:
        a,b=xs
        return a*b==-q and a*b<0
    for a,b,c in combinations(xs,3):
        ws = [(q+b*c)/((a-b)*(a-c)),
              (q+a*c)/((b-a)*(b-c)),
              (q+a*b)/((c-a)*(c-b))]
        if min(ws) >= 0 and sum(ws)==1 and sum(w*x for w,x in zip(ws,(a,b,c)))==0 and sum(w*x*x for w,x in zip(ws,(a,b,c)))==q:
            return True
    return False


def main():
    grid=[F(i,12) for i in range(-12,13) if i!=0]
    rng=Random(20261027)
    tests=0
    for n in range(2,8):
        for q in [F(1,12),F(1,5),F(1,3),F(1,2),F(3,4)]:
            for _ in range(160):
                xs = rng.sample(grid,n)
                e=feasible_extremes(xs,q)
                t=feasible_triples(xs,q)
                assert e==t, (n,q,xs,e,t)
                tests+=1
    # Closed-form minimal sample and dimension-two combinatorial identity.
    for q in [F(1,7),F(1,3),F(2,5),F(3,4)]:
        a3,b3=exact_probability(3,q)
        a4,b4=exact_probability(4,q)
        assert (a3,b3)==(F(3,2)*(q*q-q), -F(3,2)*q)
        assert (a4,b4)==(2*a3,2*b3)
    numeric=[]
    for n in range(2,13):
        a,b=exact_probability(n,F(1,3))
        p=float(a)+float(b)*log(1/3)
        assert -1e-10<=p<=1+1e-10
        numeric.append((n,p))
    assert all(numeric[i][1]<numeric[i+1][1] for i in range(1,len(numeric)-1))
    print('EXACT_FEASIBILITY_TRIPLE_CHECKS',tests)
    print('SYMBOLIC_N3_N4_CHECKS',4)
    print('UNIFORM_SAMPLE_PROBABILITIES',numeric)
    print('CHECKS_OK')

if __name__ == '__main__':
    main()
