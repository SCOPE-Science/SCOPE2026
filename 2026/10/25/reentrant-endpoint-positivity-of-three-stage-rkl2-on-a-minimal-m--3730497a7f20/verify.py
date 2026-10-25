"""Exact-rational regression checks for positivity of three-stage RKL2.

Requires only the Python standard library. The accompanying proof establishes
universal statements; this program checks identities and representative cases.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def pol(q,h,three=True):
    n=len(q)
    a2=mm(q,q)
    a3=mm(a2,q) if three else [[F(0)]*n for _ in range(n)]
    return [[F(i==j)+h*q[i][j]+h*h*a2[i][j]/2+
             (h*h*h*a3[i][j]/15 if three else F(0))
             for j in range(n)] for i in range(n)]


def r(h):
    return 1-h+h*h/2-h*h*h/15


def direct3(h):
    return [[r(h),h*(1-h+h*h/5),h*h*(F(1,2)-2*h/15)],
            [F(0),r(h),1-r(h)],
            [F(0),F(0),F(1)]]


def check():
    assertions=0
    Q=[[-F(1),F(1),F(0)],[F(0),-F(1),F(1)],[F(0),F(0),F(0)]]
    grid=[F(i,32) for i in range(0,193)]
    for h in grid:
        X=pol(Q,h)
        assert X==direct3(h)
        assertions+=9
        assert all(sum(row)==1 for row in X)
        assertions+=3
        if h <=F(5):
            assert r(h)>=0 and r(h)<=1
            assertions+=2
        if h==F(3):
            assert X[0][1]<0
            assertions+=1
        if h==F(15,4):
            assert X[0][2]==0 and X[0][1]>0
            assertions+=2
    for h,should in [(F(1),True),(F(3),False),
                     (F(37,10),True),(F(4),False),(F(5),False)]:
        X=pol(Q,h)
        assert all(x>=0 for row in X for x in row)==should
        assertions+=1
    assert pol(Q,F(3))[0][1]==F(-3,5)
    assertions+=1
    assert pol(Q,F(4))[0][2]==-F(8,15)
    assertions+=1
    rng=Random(1729)
    for _ in range(1400):
        n=rng.randrange(2,9)
        W=[[F(rng.randrange(0,7),rng.randrange(1,8)) if i!=j else F(0)
             for j in range(n)] for i in range(n)]
        Qn=[[W[i][j] if i!=j else -sum(W[i]) for j in range(n)]
            for i in range(n)]
        h=F(rng.randrange(0,71),rng.randrange(1,16))
        B=pol(Qn,h,three=False)
        for i in range(n):
            assert B[i][i]>0
            assertions+=1
            for j in range(n):
                if i!=j:
                    C=mm(Qn,Qn)[i][j]
                    assert B[i][j]==h*(Qn[i][j]+h*C/2)
                    assertions+=1
    for _ in range(1400):
        a,b=F(rng.randrange(0,11),7),F(rng.randrange(0,11),5)
        Q2=[[-a,a],[b,-b]]
        h=F(rng.randrange(0,200),rng.randrange(1,11))
        X=pol(Q2,h)
        if a+b:
            z=(a+b)*h
            scalar=(1-r(z))/(a+b)
            assert X==[[F(i==j)+scalar*Q2[i][j] for j in range(2)] for i in range(2)]
            assertions+=4
        assert X[0][1]>=0 and X[1][0]>=0
        assertions+=2
        assert all(sum(row)==1 for row in X)
        assertions+=2
    # Negative-to-positive return is robust under small unequal rate perturbations.
    for rate in (F(99,100),F(101,100)):
        Qp=[[-rate,rate,F(0)],[F(0),-F(1),F(1)],[F(0),F(0),F(0)]]
        for h,should in [(F(3),False),(F(37,10),True),(F(4),False)]:
            B=pol(Qp,h)
            assert (all(x>=0 for row in B for x in row))==should
            assertions+=1
    print(f"PASS exact-rational assertions={assertions}; simple witnesses and perturbations confirmed")
    print(f"alpha={(5-sqrt(5))/2:.12f} beta={(5+sqrt(5))/2:.12f} gamma={15/4:.12f}")
    print('note: finite checks are not proofs of universal quantifiers')

if __name__=='__main__':
    check()
