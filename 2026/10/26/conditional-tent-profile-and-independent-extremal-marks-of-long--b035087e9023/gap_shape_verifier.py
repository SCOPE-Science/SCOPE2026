"""Reproduce finite exact identities and limiting-constant sanity checks for root-gap morphology."""
from fractions import Fraction as Q
from math import comb, factorial

def v_moment(k,r):
    # minimum of k independent Uniform(0,1); k=0 means the constant 1
    ans=Q(1)
    for j in range(1,r+1):
        ans *= Q(j,k+j)
    return ans

def m_moment(n,r):
    return Q(n,n+r)

def weight(n,m):
    q=n-1-m
    vl1=v_moment(m,1); vr1=v_moment(q,1)
    vl2=v_moment(m,2); vr2=v_moment(q,2)
    return (m_moment(n,2)*vl1*vr1 - Q(1,2)*m_moment(n,3)*(vl2*vr1+vl1*vr2)
            + Q(1,4)*m_moment(n,4)*vl2*vr2)

def endpoint_numerator(n,m):
    # E[U_0 * 1_{E_n} | A_n,B=m] without E[M | A_n] denominator
    # conditional U0 integration = int_0^{S_L} u (1-u)du = S_L^2/2-S_L^3/3
    q=n-1-m
    return (Q(1,2)*m_moment(n,3)*v_moment(m,2)*v_moment(q,1)
            - Q(1,4)*m_moment(n,4)*v_moment(m,2)*v_moment(q,2)
            - Q(1,3)*m_moment(n,4)*v_moment(m,3)*v_moment(q,1)
            + Q(1,6)*m_moment(n,5)*v_moment(m,3)*v_moment(q,2))

for n in range(1,101):
    total=sum((comb(n-1,m)*weight(n,m) for m in range(n)),Q(0))
    wanted=Q(n*2**(n+1),(n+1)*(n+2)*(n+4))
    assert total==wanted, (n,total,wanted)
    for m in range(n):
        assert weight(n,m)==weight(n,n-1-m)
        assert weight(n,m)>0
print('Exact arithmetic: 100 gap probabilities, 5050 symmetric positive apex weights: PASS')
for n in (5,10,20,50,100,200):
    ws=[comb(n-1,m)*weight(n,m) for m in range(n)]
    den=sum(ws)
    loc_mean=sum(Q(m+1)*p for m,p in enumerate(ws))/den
    loc_var=sum((Q(m+1)-loc_mean)**2*p for m,p in enumerate(ws))/den
    endpoint_mean=sum(comb(n-1,m)*endpoint_numerator(n,m) for m in range(n))/den
    assert loc_mean==Q(n+1,2)
    assert 0<endpoint_mean<1
    print(f'n={n} exact E[K]={float(loc_mean):.5g} Var(K)/n={float(loc_var/n):.8f}, n E[U0]={float(n*endpoint_mean):.8f}')
print('Target variances: 0.25; target scaled endpoint mean: 2.0')
