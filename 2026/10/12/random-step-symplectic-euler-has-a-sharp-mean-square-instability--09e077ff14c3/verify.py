#!/usr/bin/env python3
"""Exact-arithmetic checks for the random-step oscillator mean-square theorem.

The infinite-horizon statement relies on the analytic argument, not these finite checks.
Pure Python 3.10+; no third-party dependencies.
"""
from fractions import Fraction as Q
from itertools import product


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return list(map(list, zip(*A)))


def T(h):
    return [[Q(1), h], [-h, Q(1) - h*h]]


def F(h):
    return [[Q(1), 2*h, h*h],
            [-h, Q(1) - 2*h*h, h - h**3],
            [h*h, 2*h**3 - 2*h, Q(1) - 2*h*h + h**4]]


def cov(v):
    x, y = v
    return [[x*x, x*y], [x*y, y*y]]


def arr(S):
    return [S[0][0], S[0][1], S[1][1]]


def apply(M, v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]


def avg(A, B):
    return [[(A[i][j]+B[i][j])/2 for j in range(len(A[0]))]
            for i in range(len(A))]


def det3(A):
    a,b,c=A[0]; d,e,f=A[1]; g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def charcoeff(A):
    tr=sum(A[i][i] for i in range(3))
    C=Q(0)
    for i,j in ((0,1),(0,2),(1,2)):
        C += A[i][i]*A[j][j]-A[i][j]*A[j][i]
    return [Q(1),-tr,C,-det3(A)]


def quadform(P,S):
    return sum(P[i][j]*S[j][i] for i in range(2) for j in range(2))


def verify():
    count=0
    for numerator in range(1,18):
        h=Q(numerator,10)
        Th=T(h)
        Sh=[[Q(1),-h/2],[-h/2,Q(1)]]
        assert mm(mm(Th,Sh),trans(Th))==Sh
        count+=1
        for x,y in ((Q(1),Q(0)), (Q(1,3),Q(2,7)), (Q(-2,5),Q(3,4))):
            S=cov((x,y))
            TS=mm(mm(Th,S),trans(Th))
            assert apply(F(h),arr(S))==arr(TS)
            count+=1
        # Second-order symmetric-noise eigenvalue perturbation coefficient.
        B=[[Q(1),-2*h],[-2*h,3*h*h-Q(1)]]
        invS=[[Q(1),h/2],[h/2,Q(1)]]
        invS=[[v/(Q(1)-h*h/4) for v in row] for row in invS]
        coefficient=quadform(invS,B)/2
        assert coefficient==2*h*h/(4-h*h)
        count+=1
    a,b=Q(1),Q(1,2)
    M=avg(F(a),F(b))
    assert M==[[Q(1),Q(3,2),Q(5,8)],
               [Q(-3,4),Q(-1,4),Q(3,16)],
               [Q(5,8),Q(-3,8),Q(9,32)]]
    count+=1
    assert [64*x for x in charcoeff(M)]==[64,-66,49,-49]
    count+=1
    # Compare the closed covariance recurrence to exhaustive finite product paths.
    for z0 in ((Q(1),Q(0)),(Q(1,3),Q(-2,5))):
        v=arr(cov(z0))
        for n in range(0,9):
            exact=[[Q(0),Q(0)],[Q(0),Q(0)]]
            for path in product((a,b),repeat=n):
                w=[[z0[0]],[z0[1]]]
                for h in path:
                    w=mm(T(h),w)
                S=cov((w[0][0],w[1][0]))
                exact=[[exact[i][j]+S[i][j] for j in range(2)] for i in range(2)]
            exact=[[t/(2**n) for t in row] for row in exact]
            assert arr(exact)==v
            count+=1
            v=apply(M,v)
    # Unique real root in (1,21/20), since derivative discriminant < 0.
    def poly(t):return 64*t**3-66*t**2+49*t-49
    assert poly(Q(1))==-2 and poly(Q(21,20))>0
    assert (-132)**2-4*192*49<0
    count+=2
    print('PASS: %d exact rational identities/finite-path comparisons' % count)
    print('Moment matrix:',M)
    print('Characteristic polynomial: 64*r^3 - 66*r^2 + 49*r - 49')
    print('Exact root isolation: 1 < r < 21/20 (unique real root)')

if __name__=='__main__':
    verify()
