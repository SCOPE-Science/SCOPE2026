#!/usr/bin/env python3
import math

def divisors(n):
    out=[]
    r=math.isqrt(n)
    for d in range(1,r+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return out

def sigma_s(n,s):
    return sum(d**s for d in divisors(n))

def E_direct(n,s):
    ev=od=0.0
    for d in divisors(n):
        if d%2==0: ev+=d**s
        else: od+=d**s
    return ev-od

def v2(n):
    a=0
    while n%2==0:
        n//=2; a+=1
    return a,n

def E_formula(n,s):
    a,m=v2(n)
    g=sum(2.0**(j*s) for j in range(1,a+1))
    return sigma_s(m,s)*(g-1.0)

def threshold(s):
    g=0.0; a=0
    while g<1.0:
        a+=1; g+=2.0**(a*s)
    return a,g

def zeta_tail(t,N=500000):
    sm=sum(k**(-t) for k in range(1,N+1))
    return sm + N**(1-t)/(t-1)

def summatory_swapped(x,s):
    return sum((1.0 if d%2==0 else -1.0)*(d**s)*(x//d) for d in range(1,x+1))

def main():
    for s in [-2.0,-1.0,-0.5,0.0,0.5,1.0,2.0]:
        for n in range(1,5001):
            a=E_direct(n,s); b=E_formula(n,s)
            assert abs(a-b)<=1e-9*max(1.0,abs(a),abs(b)),(s,n,a,b)
    for n in range(1,5001):
        a,_=v2(n)
        assert E_formula(n,-2.0)<0 and E_formula(n,-1.0)<0
        if a==0:
            assert E_formula(n,0.0)<0 and E_formula(n,0.5)<0
        elif a==1:
            assert abs(E_formula(n,0.0))<1e-12 and E_formula(n,0.5)>0
        else:
            assert E_formula(n,0.0)>0 and E_formula(n,0.5)>0
    A,G=threshold(-0.5)
    assert A==2 and G>1
    for n in range(1,5001):
        a,_=v2(n)
        assert (E_formula(n,-0.5)<0) if a<A else (E_formula(n,-0.5)>0)
    for s in [-2.0,-1.0,-0.5,-0.25]:
        x=200000
        total=summatory_swapped(x,s)
        c=(2.0**s-1.0)*zeta_tail(1.0-s)
        assert abs(total/x-c)<0.03,(s,total/x,c)
        assert total<0
    print('VERIFY_OK')
    print('pointwise_n_max=5000')
    print('summatory_x=200000')
    print('threshold_s_minus_half=2')

if __name__=='__main__': main()
