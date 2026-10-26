"""Independent numerical checks of a one-weak-link phase-ring threshold.
Requires Python 3, NumPy. Finite tests do not establish the theorem.
"""
import math
import numpy as np
P=math.pi

def bisect(fun,lo,hi,steps=95):
    f=fun(lo); g=fun(hi)
    assert f*g < 0, (lo,hi,f,g)
    for _ in range(steps):
        md=(lo+hi)/2
        if fun(md)*f>0: lo,f=md,fun(md)
        else: hi=md
    return (lo+hi)/2

def ratio(n,b):
    return math.sin((2*P-b)/(n-1))/math.sin(b)

def der_log_ratio(n,b):
    A=(2*P-b)/(n-1)
    return -1/((n-1)*math.tan(A))-1/math.tan(b)

def theta_weak(n,b):
    A=(2*P-b)/(n-1)
    return A,b

def eigs(n,w,a,b):
    lap=np.zeros((n,n))
    for i in range(n):
        j=(i+1)%n
        weight=math.cos(a) if i<n-1 else w*math.cos(b)
        lap[i,i]+=weight;lap[j,j]+=weight
        lap[i,j]-=weight;lap[j,i]-=weight
    return np.linalg.eigvalsh(lap)

checks=0
for n in range(5,43):
    bc=P/2
    bstar=bisect(lambda b:der_log_ratio(n,b),bc+1e-9,P-1e-6)
    wstar=ratio(n,bstar);wc=ratio(n,bc)
    assert 0<wstar<wc<1
    assert der_log_ratio(n,bc+1e-6)<0<der_log_ratio(n,P-1e-6)
    checks+=4
    for frac in (0.15,0.52,0.85):
        w=wstar+(wc-wstar)*frac
        bstable=bisect(lambda b:ratio(n,b)-w,bc,bstar)
        bunstable=bisect(lambda b:ratio(n,b)-w,bstar,P-1e-8)
        for b,stable in ((bstable,True),(bunstable,False)):
            a,b=theta_weak(n,b)
            assert abs((n-1)*a+b-2*P)<1e-12
            assert abs(math.sin(a)-w*math.sin(b))<1e-12
            ev=eigs(n,w,a,b)
            # Laplacian has one mandatory zero eigenvalue.
            assert abs(ev[0])<1e-10 if stable else ev[0]<-1e-9
            if stable: assert ev[1]>1e-9, (n,w,ev)
            if not stable: assert abs(ev[1])<1e-10 and ev[2]>1e-9, (n,w,ev)
            checks+=5
    # The right endpoint has one zero-conductance weak edge but remains strictly stable.
    a,b=theta_weak(n,bc); ev=eigs(n,wc,a,b)
    assert abs(ev[0])<1e-10 and ev[1]>1e-9
    checks+=2
    # Immediately above the endpoint the first-winding branch has an acute weak phase.
    w=(1+wc)/2
    b=bisect(lambda b:ratio(n,b)-w,1e-7,bc)
    a,b=theta_weak(n,b)
    ev=eigs(n,w,a,b)
    assert abs(ev[0])<1e-10 and ev[1]>1e-9
    checks+=2

# Exact sharp limiting threshold: tan(t)=pi+t and c_*=sec(t).
t=bisect(lambda u:math.tan(u)-P-u,0.8,1.52)
c=1/math.cos(t)
assert abs(c-4.603338848751699)<1e-11
for n in (100,250,500):
    bstar=bisect(lambda b:der_log_ratio(n,b),P/2+1e-9,P-1e-6)
    assert abs((n-1)*ratio(n,bstar)-c)<16/(n-1)**2
    checks+=1
print('VERIFY_OK n_range=5..42 checks=',checks,'constant=',format(c,'.15f'))
