"""Reproducibility checks for the sharp one-step sketched residual envelope.
Only standard-library Python is required. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import sqrt, hypot
from random import Random


def mm(A, v):
    return (A[0][0]*v[0] + A[0][1]*v[1], A[1][0]*v[0] + A[1][1]*v[1])


def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]


def residual_ratio(A, B, r):
    w=mm(A,r)
    bw=mm(B,w)
    alpha=dot(r,bw)/dot(w,bw)
    rr=(r[0]-alpha*w[0], r[1]-alpha*w[1])
    return sqrt(float(dot(rr,rr)/dot(r,r)))


def epsilon_matrix(e, u, v):
    h=sqrt(1-e*e)
    # Orthogonal similarity of [[-e**2, e*h], [e*h, e**2]]
    U=((u[0],v[0]),(u[1],v[1]))
    d00,d01,d11=-e*e,e*h,e*e
    return tuple(tuple(float(i==j) +
        d00*U[i][0]*U[j][0]+d01*(U[i][0]*U[j][1]+U[i][1]*U[j][0])+d11*U[i][1]*U[j][1]
        for j in range(2)) for i in range(2))


def exact_witnesses():
    A=((F(1),F(0)),(F(0),F(9)))
    r=(F(3),F(1))
    for e, B, desired_square in [
        (F(3,5),((F(197,125),F(21,125)),(F(21,125),F(53,125))),F(1)),
        (F(4,5),((F(9,5),F(0)),(F(0),F(1,5))),F(16,9)),
    ]:
        w=mm(A,r)
        bw=mm(B,w)
        a=dot(r,bw)/dot(w,bw)
        rr=(r[0]-a*w[0],r[1]-a*w[1])
        got=dot(rr,rr)/dot(r,r)
        expected=(F(9-1,9+1)**2)/(1-e*e)
        assert got==desired_square==expected, (e,got,expected)
        # Matrix symmetric and has eigenvalues 1+e, 1-e.
        tr=B[0][0]+B[1][1]; det=B[0][0]*B[1][1]-B[0][1]**2
        assert tr==2 and det==1-e*e


def numeric_extremizers():
    for kappa in [1.01,1.2,1.75,2,3,9,40,1000]:
        A=((1.0,0.0),(0.0,kappa))
        r=(sqrt(kappa),1.0)
        w=mm(A,r)
        wn=hypot(*w)
        u=(w[0]/wn,w[1]/wn)
        c=dot(r,w)/(hypot(*r)*wn)
        perp=(r[0]-c*hypot(*r)*u[0],r[1]-c*hypot(*r)*u[1])
        pn=hypot(*perp)
        v=(perp[0]/pn,perp[1]/pn)
        for e in [0.0,0.05,0.2,0.4,0.6,0.85,0.975]:
            B=epsilon_matrix(e,u,v)
            got=residual_ratio(A,B,r)
            wanted=(kappa-1)/(kappa+1)/sqrt(1-e*e)
            assert abs(got-wanted)<1e-10*max(1,wanted),(kappa,e,got,wanted)


def random_upper_bound():
    random=Random(20261009)
    checks=0
    for kappa in [1,1.01,2,3,9,50,100]:
        A=((1.0,0.0),(0.0,float(kappa)))
        for eps in [0,0.01,0.3,0.7,0.9,0.98]:
            for _ in range(250):
                a=random.uniform(-2,2);b=random.uniform(-2,2)
                if abs(a)+abs(b)<1e-8:continue
                r=(a,b)
                phi=random.uniform(-3.14159,3.14159)
                ct,st=__import__('math').cos(phi),__import__('math').sin(phi)
                d1=random.uniform(-eps,eps);d2=random.uniform(-eps,eps)
                B=((1+d1*ct*ct+d2*st*st,(d1-d2)*ct*st),
                   ((d1-d2)*ct*st,1+d1*st*st+d2*ct*ct))
                got=residual_ratio(A,B,r)
                expected=(kappa-1)/(kappa+1)/sqrt(1-eps*eps) if kappa>1 else 0.0
                assert got<=expected+2e-11,(kappa,eps,got,expected)
                checks+=1
    return checks

if __name__=='__main__':
    exact_witnesses()
    numeric_extremizers()
    n=random_upper_bound()
    print('VERIFY_OK: 2 exact-rational sharp equality witnesses, 56 independent extremizer evaluations,', n, 'random two-mode bounds')
