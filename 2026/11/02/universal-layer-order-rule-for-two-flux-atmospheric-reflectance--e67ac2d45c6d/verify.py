"""Reproduce the reciprocal two-flux layer ordering result with exact fractions.

No external scientific packages required. The analytic proof is in RESULT.md;
finite tests here are independent checks, not a replacement for that proof.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random


def flux(r, t, x):
    assert 0 < r < 1 and 0 < t and r + t <= 1
    assert 0 <= x <= 1
    return r + t*t*x/(1-r*x)


def parameter(r,t):
    return (1+r*r-t*t)/r


def reflect(stack, backing):
    x=backing
    for r,t in reversed(stack):
        x=flux(r,t,x)
    return x


def matrix(r,t):
    return ((t*t-r*r,r),(-r,F(1)))


def mult(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def test_exact():
    A=(F(1,5),F(7,10)); B=(F(2,5),F(2,5)); C=(F(1,4),F(1,2))
    assert parameter(*A)==F(11,4)
    assert parameter(*B)==F(5,2)
    assert parameter(*C)==F(13,4)
    vals={''.join('ABC'[(A,B,C).index(x)] for x in p):reflect(p,F(1,5)) for p in permutations((A,B,C))}
    assert vals['BAC']==F(204,437), vals
    assert vals['CAB']==F(159,428), vals
    assert vals['BAC']==max(vals.values()), vals
    assert vals['CAB']==min(vals.values()), vals
    return vals


def test_pairs():
    rng=Random(861045)
    total=0
    for _ in range(1200):
        a,b=sorted([F(rng.randint(1,39),50),F(rng.randint(1,39),50)])
        # Random passive layers, preserving scattering and absorption.
        r1=F(rng.randint(1,45),100)
        t1=F(rng.randint(1,95-int(r1*100)),100)
        r2=F(rng.randint(1,45),100)
        t2=F(rng.randint(1,95-int(r2*100)),100)
        for x in (F(0),F(1),F(1,5),F(rng.randint(0,100),100)):
            lhs=flux(r1,t1,flux(r2,t2,x))
            rhs=flux(r2,t2,flux(r1,t1,x))
            w1,w2=parameter(r1,t1),parameter(r2,t2)
            assert (lhs > rhs)-(lhs<rhs)==(w2>w1)-(w2<w1), (r1,t1,r2,t2,x,lhs,rhs,w1,w2)
            A=matrix(r1,t1); B=matrix(r2,t2)
            AB=mult(A,B); BA=mult(B,A)
            h=r1*r2*(w2-w1)
            assert AB[0][0]-BA[0][0]==AB[1][1]-BA[1][1]==0
            assert AB[0][1]-BA[0][1]==h
            assert AB[1][0]-BA[1][0]==h
            total+=1
    return total


def test_perm():
    rng=Random(309526)
    checks=0
    for n in range(2,6):
        for _ in range(24):
            stack=[]
            for i in range(n):
                r=F(rng.randint(1,45),100)
                t=F(rng.randint(1,98-int(r*100)),100)
                stack.append((r,t))
            ordered=sorted(stack,key=lambda rt: parameter(*rt))
            reverse=list(reversed(ordered))
            for x in (F(0),F(1),F(rng.randint(0,100),100)):
                lo=reflect(reverse,x)
                hi=reflect(ordered,x)
                for p in permutations(stack):
                    v=reflect(p,x)
                    assert lo <= v <= hi, (n,stack,x,p,v,lo,hi)
                    checks+=1
    return checks


def test_identical_type():
    # Every finite homogeneous K-M sheet of the same K/S has the same index.
    r1,t1=F(1,3),F(1,3) # w = 3
    r2,t2=F(1,5),F(1,5) # w = 5, so distinct (noncommuting)
    assert parameter(r1,t1)==3
    assert parameter(r2,t2)==5
    # Two transparent conservative sheets each have w=2 and commute.
    p=(F(1,3),F(2,3))
    q=(F(1,5),F(4,5))
    assert parameter(*p)==parameter(*q)==2
    for x in (F(0), F(1,7), F(1)):
        assert reflect([p,q],x)==reflect([q,p],x)


if __name__=='__main__':
    demo=test_exact()
    pair_checks=test_pairs()
    perm_checks=test_perm()
    test_identical_type()
    print('PASS exact three-layer example:',', '.join(k+'='+str(v) for k,v in sorted(demo.items())))
    print('PASS exact two-layer commutator/sign tests:',pair_checks)
    print('PASS exhaustive permutations of sampled stacks:',perm_checks)
    print('PASS conservative-layer commuting identities')
