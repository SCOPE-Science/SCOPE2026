#!/usr/bin/env python3
import math

def bisect(f,a,b,n=100):
    fa=f(a); fb=f(b)
    assert fa*fb<=0
    for _ in range(n):
        m=(a+b)/2
        fm=f(m)
        if fa*fm<=0:
            b=m; fb=fm
        else:
            a=m; fa=fm
    return (a+b)/2

def data(J,gamma,D,B,beta):
    K=math.hypot(J,D)
    G=abs(J*gamma)
    Delta=math.hypot(B,G)
    q=math.cosh(K*beta)**2-(G*G/(Delta*Delta))*math.sinh(Delta*beta)**2
    f1=math.sinh(K*beta)-math.sqrt(1+(G*G/(Delta*Delta))*math.sinh(Delta*beta)**2)
    f2=(G/Delta)*math.sinh(Delta*beta)-math.cosh(K*beta)
    qp=K*math.sinh(2*K*beta)-(G*G/Delta)*math.sinh(2*Delta*beta)
    return K,G,Delta,q,f1,f2,qp

def qfun(J,gamma,D,B,beta):
    return data(J,gamma,D,B,beta)[3]

def qprime(J,gamma,D,B,beta):
    return data(J,gamma,D,B,beta)[6]

def beta_max(J,gamma,D,B):
    K,G,Delta,_,_,_,_=data(J,gamma,D,B,1.0)
    assert Delta>K
    lo=1e-12
    hi=1.0
    while qprime(J,gamma,D,B,hi)>0:
        hi*=2
    return bisect(lambda x:qprime(J,gamma,D,B,x),lo,hi)

def maximum(J,gamma,D,B):
    bm=beta_max(J,gamma,D,B)
    return qfun(J,gamma,D,B,bm),bm

def roots_level(J,gamma,D,B,level,limit=30.0,step=0.002):
    roots=[]
    x0=0.0
    f0=qfun(J,gamma,D,B,x0)-level
    n=int(limit/step)
    for i in range(1,n+1):
        x1=i*step
        f1=qfun(J,gamma,D,B,x1)-level
        if f0*f1<0:
            roots.append(bisect(lambda x:qfun(J,gamma,D,B,x)-level,x0,x1,80))
        x0,f0=x1,f1
    return roots

def main():
    sign_checks=0
    for J,gamma,D in [(1.0,0.2,0.3),(1.0,0.6,0.5),(1.3,0.4,0.8)]:
        K=math.hypot(J,D); G=abs(J*gamma)
        assert 0<G<K
        for B in [0.0,0.4,0.9,1.2,1.8,3.0,6.0]:
            for j in range(1,101):
                beta=j/25
                _,_,_,q,f1,f2,_=data(J,gamma,D,B,beta)
                assert (f1>0)==(q>2)
                assert (f2>0)==(q<0)
                sign_checks+=2

    J=1.0; gamma=0.6; D=0.5
    K=math.hypot(J,D); G=abs(J*gamma)
    B0=math.sqrt(K*K-G*G)

    lo=B0*(1+1e-8); hi=4.0
    for _ in range(90):
        mid=(lo+hi)/2
        m,_=maximum(J,gamma,D,mid)
        if m>2:
            lo=mid
        else:
            hi=mid
    Bstar=(lo+hi)/2
    mstar,betastar=maximum(J,gamma,D,Bstar)
    assert abs(mstar-2)<2e-12
    assert abs(Bstar-1.7495575301980955)<2e-12

    for B,expected2,expected0 in [
        (0.5,1,0),
        (1.5,2,1),
        (1.7,2,1),
        (1.8,0,1),
        (2.0,0,1),
    ]:
        assert len(roots_level(J,gamma,D,B,2))==expected2
        assert len(roots_level(J,gamma,D,B,0))==expected0

    monotone_checks=0
    for B in [0.0,0.3,0.6,0.9,B0]:
        last=qfun(J,gamma,D,B,0.0)
        for j in range(1,2001):
            beta=3*j/2000
            cur=qfun(J,gamma,D,B,beta)
            assert cur>last
            last=cur
            monotone_checks+=1

    asymptotic=[]
    for B in [10.0,20.0,50.0,100.0]:
        roots=roots_level(J,gamma,D,B,0,limit=3.0,step=0.0005)
        assert len(roots)==1
        Tc=1/roots[0]
        approx=B/math.log(2*B/G)
        asymptotic.append(Tc/approx)
    assert abs(asymptotic[-1]-1)<abs(asymptotic[0]-1)

    print("VERIFY_OK")
    print("sign_equivalence_checks =",sign_checks)
    print("monotonicity_checks =",monotone_checks)
    print("B0 =",B0)
    print("Bstar =",Bstar)
    print("beta_star =",betastar)
    print("T_star =",1/betastar)
    print("high_field_ratio_Tc_over_Blog =",asymptotic[-1])

if __name__=="__main__":
    main()
