"""Independent numerical checks for directional localization of a quadratic cardinal spline projector.

Run: python checker.py (requires Python 3, numpy; the proof is in RESULT.md).
"""
import math
import numpy as np
from numpy.linalg import solve

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def near(a, b, tol=1e-10):
    check(abs(a-b) < tol, f"{a!r} != {b!r}")

def b3(x):
    if x <= 0 or x >= 3:
        return 0.0
    if x <= 1:
        return x*x/2
    if x <= 2:
        return -x*x+3*x-1.5
    return (3-x)*(3-x)/2

# Exact rational Gram entries, checked below by independent quadrature.
g = {0:11/20, 1:13/60, 2:1/120}
w1 = -13+math.sqrt(105)
w2 = -13-math.sqrt(105)
r = (w1+math.sqrt(w1*w1-4))/2
s = (w2+math.sqrt(w2*w2-4))/2
polyprime = lambda z:4*z**3+78*z*z+132*z+26
A = 120*r/polyprime(r)
B = 120*s/polyprime(s)
xstar = (math.sqrt(-r)-r)/(1-r)
F = lambda z,x: b3(x)+z*b3(x+1)+z*z*b3(x+2)
Phi = lambda z,t: z*z*b3(t)+z*b3(t+1)+b3(t+2)
h = lambda k: A*r**abs(k)+B*s**abs(k)

check(-.5<r<0 and -.5<s<0 and abs(s)<abs(r), "root order")
check(0<xstar<1 and A>0 and B<0 and F(s,xstar)>0, "root and residue signs")
near(F(r,xstar), 0.0, 1e-14)
near(r**4+26*r**3+66*r*r+26*r+1,0,1e-12)
near(s**4+26*s**3+66*s*s+26*s+1,0,1e-12)

# Numerically recover gram overlaps without using the formula for their entries.
for k in range(3):
    N=24000
    dx=(3-k)/N
    q = dx * (sum(b3(k+j*dx)*b3(j*dx)*(4 if j%2 else 2)
                    for j in range(1,N)) + 4*b3(k)*b3(0) + b3(3)*b3(3-k)) / 3
    # The endpoint term above is harmless because the basis vanishes there.
    near(q,g[k],1e-10)

for k in range(-30,31):
    actual=sum(g[abs(j)]*h(k-j) for j in [-2,-1,0,1,2])
    near(actual, 1.0 if k==0 else 0.0, 2e-12)

# Independent finite Gram inversion in the middle of a long Toeplitz section.
N=121
T=np.zeros((N,N))
for i in range(N):
    for j in range(max(0,i-2),min(N,i+3)):
        T[i,j]=g[abs(i-j)]
v=solve(T,np.eye(N)[N//2])
for k in range(-20,21):
    near(v[N//2+k],h(k),2e-11)

def direct_kernel(x,y):
    m=math.floor(y)
    return sum(b3(x-j)*h(j-k)*b3(y-k)
               for j in [-2,-1,0] for k in [m-2,m-1,m])

def formula(x,m,t):
    return A*F(r,x)*r**(m-2)*Phi(r,t) + B*F(s,x)*s**(m-2)*Phi(s,t)

for x in (0, .07, .23, .5, xstar, .84, 1):
    for m in (3,4,5,7,10):
        for t in (0,.17,.37,.67,.91):
            near(direct_kernel(x,m+t),formula(x,m,t),3e-12)

# The exceptional point has an exact fast-mode cell supremum, not merely a fitted rate.
for m in range(3,12):
    expected=abs(B*F(s,xstar))*(abs(s)**(m-2))*(1+s)/2
    values=[abs(formula(xstar,m,t)) for t in np.linspace(0,1,401)]
    near(max(values),expected,5e-14)

# The generic large-cell decay, evaluated at a nonexceptional x, has slow rate |r|.
x=.35
for m in (15,18,21):
    actual=max(abs(formula(x,m,t)) for t in np.linspace(0,1,501))
    asymptotic=abs(A*F(r,x))*abs(r)**(m-2)*(1+r)/2
    check(abs(actual/asymptotic-1)<1e-6, "generic rate")

print(f"PASS: {checks} finite numerical assertions")
print(f"r={r:.15f}, s={s:.15f}, xstar={xstar:.15f}")
print(f"A={A:.15f}, B={B:.15f}, F_s(xstar)={F(s,xstar):.15f}")
