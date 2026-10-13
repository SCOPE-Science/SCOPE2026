"""Reproduce Gaussian IDS scalar reductions and exact moment algebra."""
from fractions import Fraction
import math
import random

rng = random.Random(27361)


def direct(g, h, r, ms, mu):
    a = sum(x*x for x in g[:r])
    b = sum(g[i]*h[i] for i in range(r))
    assert a > 0
    x = b/a
    out = [x]
    for m in ms:
        grad = sum(g[i]*(g[i]*x-h[i]) for i in range(m))/m
        x -= mu*r*grad/a
        out.append(x)
    return out


def scalar(g, h, r, ms, mu):
    a = sum(x*x for x in g[:r])
    b = sum(g[i]*h[i] for i in range(r))
    x = b/a
    out = [x]
    for m in ms:
        c = sum(g[i]**2 for i in range(r,m))
        d = sum(g[i]*h[i] for i in range(r,m))
        q = mu*r/m
        x = (1-q-q*c/a)*x + q*(b+d)/a
        out.append(x)
    return out


def poly_update(P,R,q,c,d):
    """Polynomials in u=1/a, P for Z and R for other noise."""
    n = max(len(P)+1, len(R)+1, 2)
    outp = [0.0]*n
    outr = [0.0]*n
    for j,v in enumerate(P):
        outp[j] += (1-q)*v
        outp[j+1] -= q*c*v
    outp[0] += q
    for j,v in enumerate(R):
        outr[j] += (1-q)*v
        outr[j+1] -= q*c*v
    outr[1] += q*d
    return outp,outr


def evaluate(coeffs,u):
    return sum(v*u**j for j,v in enumerate(coeffs))

# Unaltered source Algorithm 1 versus scalar recurrence on random Gaussian prefixes.
for _ in range(200):
    N=rng.randrange(8,30)
    r=rng.randrange(1,N-3)
    T=rng.randrange(1,5)
    ms=sorted(rng.randrange(r+1,N) for __ in range(T))
    mu=rng.uniform(.03,1.7)
    g=[rng.gauss(0,1) for __ in range(N)]
    h=[rng.gauss(0,1) for __ in range(N)]
    xs=direct(g,h,r,ms,mu)
    ys=scalar(g,h,r,ms,mu)
    for x,y in zip(xs,ys):
        assert math.isclose(x,y,rel_tol=2e-11,abs_tol=1e-8)
    a=sum(v*v for v in g[:r])
    Z=sum(g[i]*h[i] for i in range(r))/math.sqrt(a)
    u=1/a
    P,R=[1.0],[0.0]
    lead=1.0
    assert math.isclose(evaluate(P,u)*Z/math.sqrt(a)+evaluate(R,u),xs[0],rel_tol=2e-11,abs_tol=1e-8)
    for j,m in enumerate(ms):
        c=sum(g[i]*g[i] for i in range(r,m))
        d=sum(g[i]*h[i] for i in range(r,m))
        q=mu*r/m
        P,R=poly_update(P,R,q,c,d)
        lead*=(-q*c)
        assert math.isclose(P[j+1],lead,rel_tol=3e-12,abs_tol=1e-12)
        z = evaluate(P,u)*Z/math.sqrt(a)+evaluate(R,u)
        assert math.isclose(z,xs[j+1],rel_tol=3e-10,abs_tol=1e-7)

# Exact rational nonasymptotic one-update chi-square moment calculation.
for r in (7,8,10,15,30):
    for k in (1,2,5,11):
        for q in (Fraction(1,3),Fraction(1,2),Fraction(1,1)):
            I1=Fraction(1,r-2)
            I2=Fraction(1,(r-2)*(r-4))
            I3=Fraction(1,(r-2)*(r-4)*(r-6))
            expanded=I1-2*q*k*I2+q*q*k*(k+2)*I3+q*q*k*I2
            formula=I1+q*(q-2)*k*I2+q*q*k*(k+2)*I3
            assert expanded==formula
            assert formula>0

# Strict all-p integrability threshold, including exact equality.
for r in range(1,31):
    for t in range(0,5):
        for p in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(3),Fraction(4)):
            s=p*(2*t+1)/2
            predicted=r>p*(2*t+1)
            chi_density_integral_converges=(Fraction(r,2)-s)>0
            assert predicted==chi_density_integral_converges

# Check the asymptotically dominant power with a path of increasingly small a.
r=4
ms=(6,8,10)
mu=.6
N=12
h=[0.0]*N
g=[0.0]*N
for i in range(r,N):
    g[i]=.8+.03*(i-r)
    h[i]=.1-.02*(i-r)
h[0]=1.0
lead=1.0
for m in ms:
    c=sum(g[i]*g[i] for i in range(r,m))
    q=mu*r/m
    lead*=(-q*c)
for a in (1e-3,1e-4,1e-5,1e-6):
    g[0]=math.sqrt(a)
    vals=direct(g,h,r,ms,mu)
    scaled=vals[-1]*a**(len(ms)+0.5)
    assert math.isclose(scaled,lead,rel_tol=.04,abs_tol=.04*abs(lead))

print('IDS Gaussian moment verification passed')
