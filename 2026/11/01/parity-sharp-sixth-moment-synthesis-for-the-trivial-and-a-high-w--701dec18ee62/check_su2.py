"""Reproduce exact central-character moments and extremal root checks.

Run: python3 check_su2.py. Uses only Python standard library.
The finite checks corroborate, but do not replace, the all-degree proof.
"""
from collections import defaultdict
from math import comb, cos, pi, sin, sqrt, isclose

checks=0

def require(condition, description):
    global checks
    assert condition, description
    checks += 1

def central_moment(n, p):
    if n*p % 2:
        return 0
    T=n*p//2
    ans=0
    for j in range(p+1):
        m=T-j*(n+1)
        if m>=0:
            ans+=(-1)**j*comb(p,j)*comb(m+p-2,p-2)
    return ans

def representation_moments(n, upto=6):
    coeffs={0:1}; out={0:1}
    for p in range(1,upto+1):
        new=defaultdict(int)
        for j,c in coeffs.items():
            for h in range(abs(n-j),n+j+1,2):
                new[h]+=c
        coeffs=dict(new)
        out[p]=coeffs.get(0,0)
    return out

def explicit_moments(n):
    odd=(n%2)
    return {0:1,1:0,2:1,3:0 if odd else 1,
            4:n+1,5:0 if odd else (5*n*n+10*n+8)//8,
            6:(n+1)*(n*n+2*n+2)//2}

def P(x,n):
    mu=explicit_moments(n)
    return x**6+15*x**4+20*mu[3]*x**3+15*mu[4]*x**2+6*mu[5]*x+mu[6]

def Q(x,n):
    return P(x,n)/(1+x*x)**3

def derivative_half(x,n):
    mu=explicit_moments(n)
    z=mu[5]; S=mu[6]
    return z+(5*(n+1)-S)*x+(10-5*z)*x*x-10*n*x**3-10*x**4-4*x**5

def optimum_even(n):
    require(n>=2 and n%2==0,'even input')
    lo=0.; hi=1.
    while derivative_half(hi,n)>0:
        hi*=2
    for _ in range(85):
        mid=(lo+hi)/2
        if derivative_half(mid,n)>0: lo=mid
        else: hi=mid
    return (hi+lo)/2

# Two algebraically independent routes to each of the character moments.
for n in range(2,61):
    m=representation_moments(n)
    e=explicit_moments(n)
    for p in range(2,7):
        require(m[p]==e[p],f'Clebsch-Gordan n={n},p={p}')
        require(central_moment(n,p)==e[p],f'Weyl constant term n={n},p={p}')

# Discrete Weyl integration samples the full trigonometric polynomial exactly
# when the sample count exceeds its maximal Fourier frequency.
for n in range(2,13):
    for p in (4,5,6):
        N=2*(p*n+4)+1
        total=0.
        for k in range(N):
            th=2*pi*k/N
            chi=sin((n+1)*th)/sin(th) if abs(sin(th))>1e-9 else (-1)**(n*k//N)*(n+1)
            total+=(1-cos(2*th))*chi**p
        require(abs(total/N-explicit_moments(n)[p]) <1e-7*max(1,explicit_moments(n)[p]),
                f'Weyl grid n={n},p={p}')

for n in range(2,101):
    if n%2:
        require(Q(0,n)==explicit_moments(n)[6],f'odd pure extremum {n}')
        require(all(Q(j/50,n) <= Q(0,n)+1e-9 for j in range(1,301)),
                f'odd grid no enhancement {n}')
    else:
        x=optimum_even(n)
        require(0<x<1,f'even positive maximizer {n}')
        require(abs(derivative_half(x,n)) < 1e-8*max(1,explicit_moments(n)[6]),f'stationarity {n}')
        require(Q(x,n)>Q(0,n),f'even strict gain {n}')
        require(all(Q(j/300,n)<=Q(x,n)+1e-7 for j in range(1,2001)),
                f'even grid unique max {n}')

for n in (100,300,1000,3000):
    x=optimum_even(n)
    S=explicit_moments(n)[6]
    require(abs(n*x-1.25)<5.0/n,f'asymptotic mixing n={n}')
    require(abs((Q(x,n)-S)/n-75/32)<7.0/n,f'asymptotic gain n={n}')

print('PASS:',checks,'deterministic checks; exact identities, Weyl quadrature, stationarity and asymptotics')
