#!/usr/bin/env python3
"""Reproducible checks for diameter-three Kneser powered-distance spectral formulas.
Standard-library only. Finite tests illustrate, but do not replace, the analytic proof.
"""
from collections import deque
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from math import comb


def C(n,r):
    return comb(n,r) if 0 <= r <= n else 0


def jdata(k,j):
    a = (-1)**j * C(2*k-2-j,k-j)
    b = sum((-1)**h*C(j,h)*C(k-j,k-1-h)*C(2*k-2-j,k-1-h)
            for h in range(k))
    # above is the exact incidence-operator inclusion/exclusion expansion
    expect = Fraction(a,1) * (Fraction((k-j)**2,k-1)-j)
    assert b == expect, (k,j,a,b,expect)
    return a,b


def f_j(mask,j):
    result = 1
    for i in range(j):
        a,b = (mask>> (2*i))&1, (mask>> (2*i+1))&1
        result *= a-b
    return result


def independent_graph_check(k):
    n=3*k-2
    masks=[sum(1<<i for i in S) for S in combinations(range(n),k)]
    scores={}
    for j in range(1,k+1):
        vectors=[f_j(x,j) for x in masks]
        assert any(vectors)
        a,b=jdata(k,j)
        scores[j]=(a,b)
        # Entire matrix-action check of two orbital adjacency operators
        for ix,x in enumerate(masks):
            ac=bc=0
            for iy,y in enumerate(masks):
                t=(x&y).bit_count()
                if t==0: ac+=vectors[iy]
                if t==1: bc+=vectors[iy]
            assert ac==a*vectors[ix], (k,j,ix,'a',ac,a*vectors[ix])
            assert bc==b*vectors[ix], (k,j,ix,'b',bc,b*vectors[ix])
    # graph distance check (all sources for k=3, four sources for k>=4)
    neighbors=[[] for _ in masks]
    for ix,x in enumerate(masks):
        neighbors[ix]=[iy for iy,y in enumerate(masks) if (x&y)==0]
    for source in range(len(masks) if k==3 else min(4,len(masks))):
        distances=[-1]*len(masks)
        distances[source]=0
        queue=deque([source])
        while queue:
            i=queue.popleft()
            for ii in neighbors[i]:
                if distances[ii]<0:
                    distances[ii]=distances[i]+1
                    queue.append(ii)
        assert all(d>=0 for d in distances)
        for ix,d in enumerate(distances):
            t=(masks[source]&masks[ix]).bit_count()
            expected=0 if ix==source else 1 if t==0 else 3 if t==1 else 2
            assert d==expected, (k,source,ix,d,expected)
    return len(masks),scores


def positivity_bound_check(k):
    assert k>=8
    r2=Fraction((k-2)**2,k-1)-2
    r3=Fraction((k-3)**2,k-1)-3
    assert r2>=Fraction(22,7) and r3>=Fraction(4,7)
    assert Fraction(117,112) / (r2-Fraction(7,4))<=Fraction(3,4)
    a2=C(2*k-4,k-2)
    for j in range(2,k+1):
        aj=abs(jdata(k,j)[0])
        assert aj*2**(j-2)<=a2
        rj=Fraction((k-j)**2,k-1)-j
        assert rj<=r2
        if j>=3:
            assert rj>=r3-3*(j-3)
        if j%2 and j>=3:
            # Rational bound on the dangerous odd sectors uniformly in p
            h=j-3
            rhs=Fraction(33,28)+3*h
            assert aj*(Fraction(7,4)-rj)<=a2*rhs/2**(h+1)
            assert rhs/2**(h+1)<=Fraction(117,112)


def roots_and_signs(k):
    with localcontext() as c:
        c.prec=90
        z=lambda v: Decimal(v)
        ln2=z(2).ln(); ln32=z(3).ln()-ln2
        a2=z(C(2*k-4,k-2))
        r2=z(k-2)**2/z(k-1)-2
        def ex(p,x): return (p*x).exp()
        def H(p):
            return a2*(r2*(ex(p,ln32)-1)-(1-ex(-p,ln2)))
        left=z(0); right=z(1)
        assert H(left)==0 and H(right)>1
        for _ in range(290):
            mid=(left+right)/2
            if H(mid)<1: left=mid
            else:right=mid
        p=(left+right)/2
        v=ex(p,ln32)-1
        w=1-ex(-p,ln2)
        assert abs(H(p)-1)<z('1e-60'),(k,H(p))
        for j in range(1,k+1):
            a,b=jdata(k,j)
            lam=z(a)*((z(b)/z(a))*v-w)-1
            if j==2: assert abs(lam)<z('1e-60'),(k,j,lam)
            else: assert lam<z('-1e-4'),(k,j,lam)
        return str(+p), str(+(p * a2 * (r2*ln32-ln2)))


def main():
    print('Independent orbital-eigenvector and graph-distance checks')
    for k in (3,4,5):
        N, data = independent_graph_check(k)
        print(f'k={k}, n={3*k-2}, vertices={N}, orbital eigenpairs={data}')
    print('Exact rational all-harmonic inequalities')
    for k in range(8,181):
        positivity_bound_check(k)
    print('Pass, 173 family instances and all Johnson harmonic sectors')
    print('High precision limiting-sector boundary checks')
    for k in (8,9,10,12,16,20,24,32):
        p,ratio=roots_and_signs(k)
        print(f'k={k} critical_p={p} asymptotic_first_order_ratio={ratio}')
    print('KNESE R_DIAMETER_THREE_NEGATIVE_TYPE_CERTIFICATE_OK'.replace(' ',''))

if __name__=='__main__': main()
