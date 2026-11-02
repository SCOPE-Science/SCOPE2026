"""Deterministic numerical checks for the radial power-phase Fock theorem.

Python 3 standard library only. Run: python3 CHECK.py
Checks are finite corroboration, not proofs of infinite asymptotics.
"""
import cmath
import math

checks = 0

def verify(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)

def gamma_integral(n, d, alpha, samples=16000, sigmas=12):
    """Midpoint quadrature for E exp(i G^alpha), G~Gamma(n+d,1)."""
    k = n + d
    low = max(0.0, k - sigmas * math.sqrt(k))
    high = k + sigmas * math.sqrt(k)
    step = (high-low) / samples
    total = 0j
    mass = 0.0
    for j in range(samples):
        t = low + (j + 0.5)*step
        w = math.exp((k-1)*math.log(t) - t - math.lgamma(k))*step
        total += w*cmath.exp(1j*t**alpha)
        mass += w
    return total, mass

# Radial gamma normalization and the exact exponential characteristic function.
for d in (1,2,4):
    for n in (12,30,60):
        v,mass = gamma_integral(n,d,1.0)
        verify(abs(mass-1) < 2e-8, ('Gamma normalization',n,d,mass))
        exact = (1-1j)**(-(n+d))
        verify(abs(v-exact) < 2e-8, ('Exact alpha=1',n,d,v,exact))

# Quadrature refinement on distinct phase-velocity regimes.
for n,alpha in ((20,.25),(100,.5),(100,.75),(24,1.0)):
    a,_ = gamma_integral(n,2,alpha,samples=10000)
    b,_ = gamma_integral(n,2,alpha,samples=20000)
    verify(abs(a-b) < 3e-7, ('Quadrature stability',n,alpha,a,b))

# Subcritical phases retain unit modulus asymptotically.
for d in (1,2,3):
    early,_ = gamma_integral(30,d,.25)
    late,_ = gamma_integral(500,d,.25)
    verify(abs(late)>abs(early), ('Subcritical amplitude',d,early,late))
    verify(abs(late)>0.998, ('Subcritical near one',d,late))

# The central-limit threshold has the universal damping e^{-1/8}.
c = math.exp(-1/8)
for d in (1,2,4):
    for n in (120,400):
        v,_ = gamma_integral(n,d,.5)
        verify(abs(abs(v)-c)<.003, ('Critical damping',n,d,v,c))

# Supercritical phases are strongly suppressed.
for d in (1,2,3):
    a,_=gamma_integral(60,d,.75)
    b,_=gamma_integral(400,d,.75)
    verify(abs(b)<.12*abs(a), ('Supercritical suppression',d,a,b))

# Homogeneous-degree dimensions and finite equidistribution sanity checks.
for d in (1,2,3,5):
    for N in (1,2,5,15,50):
        count=sum(math.comb(n+d-1,d-1) for n in range(N+1))
        verify(count==math.comb(N+d,d), ('Dimension sum',d,N))

for a in (.5,.75):
    for m in (1,2,3):
        N=60000
        avg=sum(cmath.exp(1j*m*(n+2)**a) for n in range(1,N+1))/N
        verify(abs(avg)<.025, ('Phase equidistribution check',a,m,avg))

print(f'PASS: {checks} deterministic assertions; independent proof remains required.')
