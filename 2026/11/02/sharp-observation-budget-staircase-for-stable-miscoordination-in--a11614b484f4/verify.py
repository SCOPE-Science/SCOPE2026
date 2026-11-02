#!/usr/bin/env python3
"""Exact-arithmetic checks for a sharp sampling-budget theorem."""
from fractions import Fraction as Q
from math import comb, floor


def poly_add(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out

def poly_scale(a,c): return [x*c for x in a]

def poly_mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def polynomial_tail(k,m):
    ans=[Q(0)]*(k+1)
    for j in range(m,k+1):
        coeff=comb(k,j)
        for z in range(k-j+1):ans[j+z]+=coeff*comb(k-j,z)*(-1)**z
    return ans

def eval_poly(coeff,p): return sum((a*p**i for i,a in enumerate(coeff)),Q(0))

def bin_tail(k,m,p):
    return sum((Q(comb(k,j))*p**j*(1-p)**(k-j) for j in range(m,k+1)),Q(0))

def check_odds(k,alpha):
    f=[Q(0),Q(2),Q(-1)]
    F=polynomial_tail(k,2)
    g=poly_add(poly_add(poly_scale(f,alpha),poly_scale(F,1-alpha)),[Q(0),Q(-1)])
    # Evaluate two equivalent exact rational functions at a grid; coefficients
    # in the odds-polynomial are independently computed by Pascal's formula.
    coef=[2*alpha-1]+[Q(comb(k-2,j))+(1-alpha)*comb(k-2,j+1) for j in range(1,k-1)]
    assert all(t>0 for t in coef[1:])
    def cb(n,j): return comb(n,j) if 0<=j<=n else 0
    # Coefficients of the same odds polynomial from the raw binomial-tail sum.
    direct=[(2*alpha-1)*cb(k-2,j)+(alpha-1)*cb(k-2,j-1)
            +(1-alpha)*cb(k,j+1)*(j>=1) for j in range(k)]
    assert direct[-1]==0
    assert direct[:-1]==coef
    for v in (Q(1,47),Q(1,11),Q(2,5),Q(3,4),Q(18,19)):
        y=v/(1-v)
        lhs=eval_poly(g,v)*(1+y)**(k-2)/(v*(1-v))
        rhs=eval_poly(coef,y)
        assert lhs==rhs,(k,alpha,v,lhs,rhs)


def proof_witness(k,m):
    C=comb(k,3)
    eps=Q(1,4*C)
    alpha=Q(1,2)+eps**2/8
    f=2*eps-eps**2
    F=bin_tail(k,m,eps)
    half=(f+F)/2-eps
    selected=alpha*f+(1-alpha)*F-eps
    assert F<=C*eps**3==eps**2/4
    assert half<=-3*eps**2/8
    assert selected<=-eps**2/4
    assert Q(1,2)<alpha<1
    return alpha,eps


def main():
    checks=0
    for k in range(3,31):
        for alpha in (Q(0),Q(1,3),Q(1,2),Q(3,4),Q(1)):
            check_odds(k,alpha);checks+=1
    tests=(Q(6,5),Q(7,5),Q(3,2),Q(7,4),Q(2),Q(5,2),Q(3),Q(9,2),Q(17,2))
    for u in tests:
        k_min=floor(2*(u+1))+1
        for k in range(2,k_min+3):
            m=(k*(u.denominator)+(u.numerator+u.denominator)-1)//(u.numerator+u.denominator)
            # Independent exact ceiling check by inequalities.
            assert Q(m-1)<Q(k)/(u+1)<=m
            assert (m>=3)==(k>=k_min)
            if m>=3: proof_witness(k,m)
            checks+=1
    print('PASS:',checks,'exact coefficient, payoff-boundary, and constructive-witness checks')

if __name__=='__main__':main()
