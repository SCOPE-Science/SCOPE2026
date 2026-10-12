"""Checks for sharp deterministic descent envelope in sketched quadratic minimization.
Finite checks illustrate the separately supplied analytic proof; they do not prove its universal assertions.
"""
from fractions import Fraction as F
import math
import random

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(M,v): return tuple(sum(row[j]*v[j] for j in range(2)) for row in M)
def build(eps, delta):
    t=math.sqrt(delta)
    a,b=1/(1+eps),1/(1-eps)
    kminus=(t*t-t*math.sqrt(t*t+4))/2
    v=(1,kminus/t)
    norm=math.hypot(*v)
    v=tuple(z/norm for z in v)
    def proj(c,d):
        return tuple(tuple((c if i==j else 0)+(d-c)*v[i]*v[j] for j in range(2)) for i in range(2))
    L=proj(math.sqrt(a),math.sqrt(b))
    S=proj(1/math.sqrt(a),1/math.sqrt(b))
    z=mv(L,(1.,0.)); h=mv(L,(0.,t))
    return z,h,S

def target(eps,delta):
    return (delta-eps*math.sqrt(delta*(delta+4)))/(1-eps**2)

def check_exact():
    A=(F(-3,2),F(1)); b=(F(-2),F(-1,3)); x0=F(1)
    S=((F(2,5),F(3,5)),(F(-1,5),F(6,5)))
    r1=tuple(-z for z in b)
    r0=tuple(A[i]*x0-b[i] for i in range(2))
    assert mv(S,r1)==(F(1),F(0))
    assert mv(S,A)==(F(0),F(3,2))
    assert dot(r1,r1)==F(37,9)
    assert dot(r0,r0)==F(73,36)
    assert dot(r0,r0)-dot(r1,r1)==F(-25,12)
    assert dot(mv(S,A),mv(S,A))/dot(mv(S,r1),mv(S,r1))==F(9,4)
    # S^T S eigenvalues exactly 1/5 and 9/5: trace 2, determinant 9/25.
    sts=((S[0][0]**2+S[1][0]**2,S[0][0]*S[0][1]+S[1][0]*S[1][1]),
         (S[0][0]*S[0][1]+S[1][0]*S[1][1],S[0][1]**2+S[1][1]**2))
    assert sts[0][0]+sts[1][1]==2
    assert sts[0][0]*sts[1][1]-sts[0][1]**2==F(9,25)
    assert F(9,4)-F(4,5)*F(3,2)*F(5,2)==F(-3,4)
    assert F(-3,4)/(1-F(4,5)**2)==F(-25,12)
    return 1

def check_random():
    rng=random.Random(340026)
    n=5000
    for k in range(n):
        eps=rng.uniform(.0001,.985)
        delta=10**rng.uniform(-4,2)
        z,h,S=build(eps,delta)
        zsk=mv(S,z);hsk=mv(S,h)
        g=dot(zsk,zsk)
        delta_obs=dot(hsk,hsk)/g
        assert abs(dot(zsk,hsk))<1e-9*(1+delta)
        assert abs(delta_obs-delta)<2e-10*(1+delta)
        lhs=(dot(h,h)+2*dot(z,h))/g
        rhs=target(eps,delta)
        assert abs(lhs-rhs)<5e-9*(1+abs(rhs)),(k,lhs,rhs)
        # Any admissible isotropic or intermediate metric has difference >= sharp bound.
        a,bb=1/(1+eps),1/(1-eps)
        theta=rng.uniform(0,2*math.pi)
        v=(math.cos(theta),math.sin(theta))
        u1,u2=rng.random(),rng.random()
        m11=a+(bb-a)*(u1*v[0]**2+u2*v[1]**2)
        m22=a+(bb-a)*(u1*v[1]**2+u2*v[0]**2)
        m12=(bb-a)*(u1-u2)*v[0]*v[1]
        test=m22*delta+2*m12*math.sqrt(delta)
        assert test>=rhs-1e-9*(1+abs(rhs)),(k,test,rhs)
        # The sign of the envelope changes at the exact threshold.
        threshold=4*eps*eps/(1-eps*eps)
        assert (rhs>=-1e-10)==(delta>=threshold-1e-10),(eps,delta,rhs,threshold)
    return n

if __name__=='__main__':
    e=check_exact();n=check_random()
    print(f'VERIFY_OK rational_witness={e} sharp_extremizers_and_comparisons={n}')
