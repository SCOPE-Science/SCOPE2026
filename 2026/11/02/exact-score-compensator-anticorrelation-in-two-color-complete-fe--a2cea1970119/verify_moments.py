#!/usr/bin/env python3
"""Finite-deck exact checks and Brownian-bridge moment quadrature."""
from itertools import combinations
from fractions import Fraction
from math import comb, log, pi, sqrt, asin


def finite_exact(m):
    N=2*m
    s_sum=Fraction(0); s2_sum=Fraction(0)
    t_sum=Fraction(0); t2_sum=Fraction(0); st_sum=Fraction(0)
    m2_sum=Fraction(0)
    for reds in combinations(range(N),m):
        red_positions=set(reds)
        r=b=m
        S=Fraction(0)
        Q=Fraction(0)
        tie=0
        for i in range(N):
            t=r+b
            S += Fraction(max(r,b),t)
            actual_red=i in red_positions
            if r==b:
                Q += Fraction(1,2)
                tie += 1
            else:
                Q += int(actual_red == (r>b))
            if actual_red:r-=1
            else:b-=1
        assert r==b==0
        s_sum+=S;s2_sum+=S*S
        t_sum+=Q;t2_sum+=Q*Q+Fraction(tie,4)
        st_sum+=S*Q
        m2_sum+=Q*Q+Fraction(tie,4)-2*S*Q+S*S
    n=comb(N,m)
    ES=s_sum/n; EST=t_sum/n
    VS=s2_sum/n-ES*ES
    VT=t2_sum/n-EST*EST
    CS_M=st_sum/n-s2_sum/n
    EM2=m2_sum/n
    H=sum((Fraction(1,j) for j in range(1,N+1)),Fraction(0))
    expected=Fraction(m,2)-Fraction(m,2*(2*m-1))*(H-1)
    assert EM2==expected,(m,EM2,expected)
    assert VT==VS+EM2+2*CS_M
    assert ES==EST
    return float(VS/m),float(CS_M/m),float(VT/m),float(EM2/m)

# Integral J(t)=int_0^infinity [(1+y)(1+t*y)]^-2 dy.
# At t=1-z, expand (1-z*y/(1+y))^-2 against (1+y)^-4.
# Coefficient (k+1)*Beta(k+1,3)=(k+1)*2/[(k+1)(k+2)(k+3)]=2/[(k+2)(k+3)].
def jstable(t):
    if t == 0: return 1.0
    if t>=.98:
        z=1-t
        return sum(2*z**k/((k+2)*(k+3)) for k in range(40))
    return (t+1)/(t-1)**2-2*t*log(t)/(t-1)**3

def simpson(f,n=60000):
    assert n%2==0
    h=1/n
    ans=f(0)+f(1)
    for k in range(1,n): ans+=(4 if k%2 else 2)*f(k*h)
    return ans*h/3

def bridge_integrals():
    # t=z^2 removes the square-root endpoint at 0.
    a=simpson(lambda z: 2*sqrt(max(0,1-z*z))*jstable(z*z),60000)
    b=simpson(lambda z: 2*z*asin(z)*jstable(z*z),60000)
    assert abs(a-pi/3)<1.0e-7,(a,pi/3)
    assert abs(b-pi*(log(2)-7/12))<1.0e-7,(b,pi*(log(2)-7/12))
    second=2*(a+b)/pi
    target=2*log(2)-.5
    assert abs(second-target)<1e-7,(second,target)
    print('bridge_integral_A',f'{a:.12f}','exact pi/3')
    print('bridge_integral_B',f'{b:.12f}','exact pi*(log(2)-7/12)')
    print('bridge_second_moment',f'{second:.12f}','exact 2log(2)-1/2')

if __name__=='__main__':
    checks=0
    for m in range(1,9):
        v,c,t,e=finite_exact(m)
        print('m',m,'Var(S)/m',f'{v:.8f}','Cov(S,M)/m',f'{c:.8f}','Var(T)/m',f'{t:.8f}','E(M^2)/m',f'{e:.8f}')
        checks+=5
    bridge_integrals()
    print('limits', 'Var(S)/m',2*log(2)-.5-pi/4,'Cov(S,M)/m',.5-log(2),'Corr(S,M)',(.5-log(2))/sqrt(.5*(2*log(2)-.5-pi/4)))
    print('checks_passed',checks+3)
