"""Deterministic arithmetic checks of the exact bath-memory averaging formulas.

Run: python3 CHECK.py
No external packages are required. Finite checks supplement analytical arguments.
"""
from fractions import Fraction as F
from math import exp, sqrt, isclose

checks = 0

def insist(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)

def linear_solve(a, b):
    a = [list(row) + [rhs] for row, rhs in zip(a, b)]
    n = len(b)
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j] != 0)
        a[j], a[k] = a[k], a[j]
        p = a[j][j]
        a[j] = [v / p for v in a[j]]
        for k in range(n):
            if k != j:
                c = a[k][j]
                a[k] = [v - c * w for v, w in zip(a[k], a[j])]
    return tuple(row[-1] for row in a)

def stationary_exact(r, g):
    return linear_solve(
        [[2+r, -2, F(0)], [-1/g, 1+r+1/g, -1], [F(0), -1, 1]],
        [F(2), F(0), F(1)])

def formulas(r, g):
    den = r*(g*(r+2)+1)
    x = 2*(g*(r+1)+1)/den
    c = (g*(r+2)+2)/den
    q = (r+2)*(g*(r+1)+1)/den
    integrated = (x+g*c)/r
    return x,c,q,integrated

def spectral(r, g):
    r,g = float(r),float(g)
    x,c,q,integrated = map(float, formulas(F(r),F(g)))
    tr = 1+r+1/g
    disc = sqrt(tr*tr-4*r/g)
    fast = (tr+disc)/2
    slow = (2*r/g)/(tr+disc)  # cancellation-free slow eigenvalue
    derivative = -(1+r)*x+c
    slow_weight = (derivative+fast*x)/(fast-slow)
    fast_weight = x-slow_weight
    return fast,slow,fast_weight,slow_weight,x,integrated

def kernel(z):
    if abs(z) < 1e-5:
        return 1/2-z/6+z*z/24-z**3/120+z**4/720
    return (z+exp(-z)-1)/(z*z)

def avgvar(r, g, t):
    a,b,wa,wb,_,_ = spectral(r,g)
    return 2*wa*kernel(a*t)+2*wb*kernel(b*t)

for r0 in (F(1,7),F(1,2),F(1),F(3,2),F(3),F(11)):
    for g0 in (F(1,13),F(1,2),F(1),F(4),F(13)):
        x,c,q,integrated = formulas(r0,g0)
        direct = stationary_exact(r0,g0)
        insist((x,c,q)==direct, ('stationary',r0,g0))
        # Direct Poisson resolvent: (-B)h=first stationary covariance column.
        h0,h1 = linear_solve([[1+r0,-1],[-1/g0,1/g0]],[x,c])
        insist(integrated==h0, ('integrated',r0,g0))
        insist(integrated==F(2)/(r0*r0)+g0*g0*(r0+2)/(r0*r0*(g0*(r0+2)+1)),('excess',r0,g0))
        insist(x==F(2)/r0-F(2)*g0/(r0*(g0*(r0+2)+1)),('variance',r0,g0))
        insist(x<F(2)/r0 and integrated>F(2)/(r0*r0),('strict reversal',r0,g0))
        a,b,wa,wb,xf,inte = spectral(r0,g0)
        insist(a> b>0 and wa>0 and wb>0,('spectrum',r0,g0))
        insist(isclose(wa+wb,float(x),rel_tol=1e-10),('weights',r0,g0))
        insist(isclose(wa/a+wb/b,float(integrated),rel_tol=3e-10),('resolvent spectral',r0,g0))

for r in (0.3,1.0,5.0):
    g=3.0
    for t in (.5,1.5,5,15):
        a,b,wa,wb,x,inte=spectral(r,g)
        # Independently integrate the two-time covariance with composite Simpson.
        n=4000
        dt=t/n
        acc=0.0
        for j in range(n+1):
            z=j*dt
            cc=wa*exp(-a*z)+wb*exp(-b*z)
            acc += (1 if j==0 or j==n else 4 if j%2 else 2)*(t-z)*cc
        simpson=2*dt*acc/(3*t*t)
        insist(isclose(simpson,avgvar(r,g,t),rel_tol=2e-8,abs_tol=2e-10),('quadrature',r,t))

for r in (0.4,1.,3.):
    k=r/(1+r)
    p=1/(r*(1+r))
    for s in (.3,1.,3.,10.):
        z=k*s
        target=2*p*kernel(z)
        measured=avgvar(r,1_000_000.,1_000_000.*s)
        insist(isclose(measured,target,rel_tol=2e-4,abs_tol=2e-8),('slow bath crossover',r,s,measured,target))
    # The normal Brownian resetting limit has covariance (2/r) exp(-r t).
    for t in (.3,1.,5.):
        a,b,wa,wb,x,inte=spectral(r,0.00001)
        c=wa*exp(-a*t)+wb*exp(-b*t)
        insist(isclose(c,2/r*exp(-r*t),rel_tol=1e-3,abs_tol=1e-6),('fast bath',r,t))


# Fourth-degree stationary moment recursion, independent of the covariance formulas.
# Moment index (p,k) corresponds to E[X**p Q**k].
def degree_four_moments(r,g):
    lower={(0,0): F(1), (2,0): stationary_exact(r,g)[0],
           (1,1): stationary_exact(r,g)[1], (0,2): stationary_exact(r,g)[2]}
    idx=[(p,4-p) for p in range(5)]
    a=[];b=[]
    for p,k in idx:
        row=[]
        for pp,kk in idx:
            coeff= F(0)
            if (pp,kk)==(p,k):coeff+=p+F(k)/g+(r if p else 0)
            if (pp,kk)==(p-1,k+1):coeff-=p
            if (pp,kk)==(p+1,k-1):coeff-=F(k)/g
            row.append(coeff)
        a.append(row)
        b.append(F(p*(p-1))*lower.get((p-2,k),0)+F(k*(k-1))/g*lower.get((p,k-2),0))
    return dict(zip(idx,linear_solve(a,b)))

def frozen_moments(r):
    a=(r+1)/r
    def ez(k):return r/(r+k)
    c=[1+a,-2*a,a-1]
    x4=3*sum(c[i]*c[j]*ez(i+j) for i in range(3) for j in range(3))
    q4=3*a*a
    x2q2=3*a*a*(1-2*ez(1)+ez(2))+a*(1-ez(2))
    return x4,q4,x2q2

for r in (F(1,2),F(1),F(3)):
    g=F(100000)
    fourth=degree_four_moments(r,g)
    lim=frozen_moments(r)
    for actual,target in zip((fourth[(4,0)],fourth[(0,4)],fourth[(2,2)]),lim):
        insist(abs(float(actual/target)-1)<0.001,('fourth moment joint frozen limit',r,actual,target))

print(f'PASS including higher joint moments: {checks} total checks')
