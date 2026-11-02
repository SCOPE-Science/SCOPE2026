#!/usr/bin/env python3
"""Finite diagnostics for magnetic quantum-cycle Bohr-gap identities.

Uses only the Python standard library. Numerical checks support the analytic
proof; no grid test is treated as a proof of global uniqueness.
"""
import cmath
import math

PI = math.pi
checks = 0

def check(condition, info):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(info)

def close(a, b, atol=2e-10, rtol=2e-10):
    return abs(a-b) <= atol+rtol*max(abs(a),abs(b))

def spectrum(n, flux, hopping=1.0):
    return [2*hopping*math.cos((2*PI*k+flux)/n) for k in range(n)]

def direct_gap(n, flux, hopping=1.0):
    e = spectrum(n,flux,hopping)
    return min(abs(e[j]-e[k]) for j in range(n) for k in range(j))

def analytic_gap(n, flux, hopping=1.0):
    alpha = PI/n
    theta = (flux % (2*PI))/n
    if n%2:
        delta = min(theta%alpha, alpha-(theta%alpha))
        return 4*hopping*math.sin(alpha)*math.sin(delta)
    theta = min(theta,2*alpha-theta)
    return 4*hopping*min(math.sin(alpha)*math.sin(alpha-theta),math.sin(2*alpha)*math.sin(theta))

def optimal(n, hopping=1.0):
    alpha=PI/n
    if n%2:
        return (PI/2,3*PI/2), 4*hopping*math.sin(alpha)*math.sin(alpha/2)
    theta=math.atan(math.tan(alpha)/3)
    flux=n*theta
    return (flux,2*PI-flux),4*hopping*math.sin(2*alpha)*math.sin(theta)

def channel_norm(n, flux, duration):
    e=spectrum(n,flux)
    return max(abs(math.sin((e[j]-e[k])*duration/2)/((e[j]-e[k])*duration/2))
               for j in range(n) for k in range(j) if abs(e[j]-e[k])>1e-12)

for n in range(3,41):
    for f in (0.00019,0.2,0.61,1.38,2.31,3.14159,3.93,5.49,6.28291):
        check(close(direct_gap(n,f),analytic_gap(n,f),atol=1e-12),('spectral gap',n,f))
    fluxes,best=optimal(n)
    for f in fluxes:
        check(close(direct_gap(n,f),best,atol=2e-12),('optimal gap',n,f))
    for j in range(221):
        f=2*PI*j/220
        check(direct_gap(n,f)<=best+1e-10,('sampled global bound',n,f))
    # Explicit Fourier mode eigenvector equation for the proposed hopping matrix.
    f=0.593
    theta=f/n
    for k in (0,n//2,n-1):
        q=2*PI*k/n
        wave=[cmath.exp(-1j*q*x) / math.sqrt(n) for x in range(n)]
        energy=2*math.cos(theta+q)
        # Eigenvalue set is invariant under k -> -k; this vector's phase convention
        # corresponds to cos(theta+q) for forward e^{i theta} hopping.
        for x in range(n):
            hx=cmath.exp(1j*theta)*wave[(x-1)%n]+cmath.exp(-1j*theta)*wave[(x+1)%n]
            check(abs(hx-energy*wave[x])<2e-12,('Fourier mode',n,k,x))
    # A sharp channel norm envelope is saturated by a minimum-gap matrix unit
    # at every odd half-period of its Bohr frequency.
    f=fluxes[0]
    min_gap=direct_gap(n,f)
    e=spectrum(n,f)
    diffs=[abs(e[j]-e[k]) for j in range(n) for k in range(j)]
    for m in (0,1,3,8):
        T=(2*m+1)*PI/min_gap
        norm=max(abs(math.sin(delta*T/2)/(delta*T/2)) for delta in diffs)
        check(close(T*norm,2/min_gap,atol=2e-10),('limsup saturation',n,m))
    if n%2==0:
        theta=fluxes[0]/n
        alpha=PI/n
        check(close(math.sin(alpha-theta),2*math.cos(alpha)*math.sin(theta)),('balance',n))

for n in (9,10,25,26,101,102,1001,1002):
    fluxes,best=optimal(n)
    scale=best*n*n
    expected=2*PI*PI if n%2 else 8*PI*PI/3
    check(abs(scale-expected)/expected < 5/(n*n),('large-n asymptotics',n))

print('PASS: %d finite independent numerical/algebraic diagnostics; n=3..40' % checks)
print('These diagnostics do not establish infinite-size global optimization; the proof does.')
