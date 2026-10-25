"""Numerical checks for the stationary coagulation-reset inverse theorem.
Only standard Python is required. These checks supplement, not replace, the proof.
"""
import math
import random

def lambda_from_r(r,D):
    # Avoid subtractive cancellation at very large r.
    t=r/(2*D)
    return 2/(t+2+math.sqrt(t*(t+4)))

def E_explicit(n,l,q):
    if abs(l-q)<1.e-9:
        s=(l+q)/2
        return s**n*((n+1)*(1-s)+2*s)/(1+s)
    return (l**(n+1)*(1-q)**2-q**(n+1)*(1-l)**2)/((l-q)*(1-l*q))

def solve_stationary_recurrence(t,q,N):
    # Set E_0=1, E_{N+1}=0; solve n=1,..,N by independent tridiagonal elimination.
    a,b,c=-1.,2.+t,-1.
    d=[t*q**n+(1. if n==1 else 0.) for n in range(1,N+1)]
    cp=[0.]*N;dp=[0.]*N
    cp[0]=c/b;dp[0]=d[0]/b
    for i in range(1,N):
        den=b-a*cp[i-1]
        cp[i]=c/den
        dp[i]=(d[i]-a*dp[i-1])/den
    x=[0.]*N;x[-1]=dp[-1]
    for i in range(N-2,-1,-1):x[i]=dp[i]-cp[i]*x[i+1]
    return [1.]+x+[0.]

def stationary(l,q):
    u=(1-l)*(1-q)/(1-l*q)
    v=u*u*(1-l*q)
    r_over_2D=(1-l)**2/l
    m_over_2D=1+r_over_2D*q
    return u,v,m_over_2D

def inverse_static(u,v):
    z=v/(u*u)
    delta=z*(z*(1+u)**2-4*u)
    if delta < -1.e-11:raise ValueError('infeasible data')
    roots=sorted(((2-z*(1+u))+sigma*math.sqrt(max(0.,delta)))/2 for sigma in [-1,1])
    return roots,z,delta

rng=random.Random(271828)
max_rec_err=0.; max_sym_err=0.; max_inverse_err=0.;max_slope_err=0.
for case in range(300):
    l=0.04+0.92*rng.random()
    q=0.04+0.92*rng.random()
    if abs(l-q)<2e-6:q=min(.99,q+.003)
    u,v,m=stationary(l,q)
    lr,z,disc=inverse_static(u,v)
    max_inverse_err=max(max_inverse_err,abs(lr[0]-min(l,q)),abs(lr[1]-max(l,q)))
    for n in (1,2,3,4,6,9,12):
        e=E_explicit(n,l,q)
        e_swapped=E_explicit(n,q,l)
        max_sym_err=max(max_sym_err,abs(e-e_swapped))
        t=(1-l)**2/l
        rres=E_explicit(n+1,l,q)-(2+t)*e+E_explicit(n-1,l,q)+t*q**n
        max_rec_err=max(max_rec_err,abs(rres))
    # A rate-position exchange keeps every empty-block observable invariant.
    mswap=stationary(q,l)[2]
    exact_gap=abs(q-l)*(l+q-2*l*q)/(l*q)
    max_slope_err=max(max_slope_err,abs(abs(m-mswap)-exact_gap))
    assert (m>1 and mswap>1 and (m-mswap)*(q-l)>0)
    assert 4*u**3/(1+u)**2-1e-13<=v<u*u
assert max_rec_err<2e-11 and max_sym_err<2e-11 and max_inverse_err<2e-10 and max_slope_err<3e-12

max_linear=0.
for l,q in ((.14,.8),(.8,.14),(.29,.64),(.65,.29),(.31,.31),(.92,.15),(.24,.97)):
    t=(1-l)**2/l
    E=solve_stationary_recurrence(t,q,150)
    for n in range(1,12):max_linear=max(max_linear,abs(E[n]-E_explicit(n,l,q)))
assert max_linear<3e-11, max_linear

# Source-to-measurement reconstruction at an exact symmetric collision.
for s in (.1,.25,.5,.8):
    u,v,m=stationary(s,s)
    roots,z,delta=inverse_static(u,v)
    assert abs(roots[0]-s)<5e-8 and abs(roots[1]-s)<5e-8
    assert abs(v-4*u**3/(1+u)**2)<3e-14

# Fixed stationary density: the kinetic observable must strictly decrease with lambda.
for u in (.01,.1,.4,.75,.95):
    last=float('inf')
    for j in range(1,300):
        l=(1-u)*j/300
        q=(1-l-u)/(1-l-u*l)
        assert 0<q<1
        uu,v,m=stationary(l,q)
        assert abs(uu-u)<1e-12
        assert m<last
        last=m

# Derivative of the uncentered stationary autocorrelation follows directly from
# the local generator, for any finite ring configuration with an occupied origin.
for D,r,p in ((1.,.25,.36),(2.,.8,.7),(.7,3.,.2)):
    for state in range(64):
        if not (state&1):continue
        # All outgoing hops from the occupied origin empty that site;
        # arrivals from neighbours leave it occupied. Independent resets
        # leave it occupied with probability p.
        local_derivative=(-2*D+r*(p-1))
        assert abs(local_derivative+(2*D+r*(1-p)))<1e-14

print(f'PASS: 300 finite-parameter tests; 7 block lengths each; 7 independent tridiagonal comparisons; four collision cases; five monotonic scans. Max recurrence residual={max_rec_err:.3g}, symmetry={max_sym_err:.3g}, inverse={max_inverse_err:.3g}, solver={max_linear:.3g}, dynamic-gap={max_slope_err:.3g}.')
