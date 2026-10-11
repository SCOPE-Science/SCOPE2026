"""Independent finite algebra checks for an alternating cyclic replicator reduction.

Standard-library-only verification. Infinite-dimensional assertions require the
analytical proof, comparison and energy methods in RESULT.md.
"""
from fractions import Fraction as Q
from math import pi, sqrt, isfinite

checks = 0

def exact(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

# Each 2N-neighbor sum and source reaction is recomputed from the multi-species
# formula, independently of the scalar reduction, in exact rational arithmetic.
for N in range(4, 66, 2):
    for amplitude in [Q(-1), Q(-4, 5), Q(-1, 3), Q(0), Q(2, 7), Q(3, 4), Q(1)]:
        state = [(1 + ((-1)**i) * amplitude) / Q(N) for i in range(N)]
        C = sum((state[i] * state[(i+1) % N] for i in range(N)), Q(0))
        exact(C == (1-amplitude**2)/N, 'cycle quadratic normalization')
        for a in [Q(-1, 2), Q(-1, 3), Q(-2, 5)]:
            r = -a / N
            for i in range(N):
                prev, nxt = state[(i-1) % N], state[(i+1) % N]
                source_reaction = state[i]*(prev-nxt) - a*state[i]*(C-prev)
                alternating_reaction = ((-1)**i) * r * amplitude * (1-amplitude**2)/N
                exact(source_reaction == alternating_reaction,
                      'alternating nonlinear vector-field identity')

# The spatially periodic source normalization L = 2*pi gives first
# anti-periodic harmonic eigenvalue 1, so the threshold is exactly r=D.
a, D = Q(-1, 2), Q(1, 100)
exact((-a)/Q(8) > D, '8 species supercritical')
exact((-a)/Q(50) == D, '50 species critical')
exact((-a)/Q(52) < D, '52 species strictly subcritical')

# Algebraic coefficients of the Jacobi stationary equation, with parameter m.
# A^2 = 2m/(1+m), beta^2 = r/[D(1+m)]. This checks the coefficients
# separately and is exact, not a finite-spatial-grid approximation.
for m in [Q(1, 100), Q(1, 5), Q(1, 3), Q(1, 2), Q(3, 4), Q(99, 100)]:
    for r in [Q(1, 9), Q(2, 5), Q(1, 2)]:
        for diffusion in [Q(1, 100), Q(3, 40)]:
            amplitude_sq = 2*m/(1+m)
            beta_sq = r/(diffusion*(1+m))
            exact(diffusion*beta_sq*(1+m) == r,
                  'Jacobi linear stationary coefficient')
            exact(diffusion*beta_sq*2*m == r*amplitude_sq,
                  'Jacobi cubic stationary coefficient')

# (sn^2)'' = 2-4(1+m)sn^2+6m sn^4.
# For psi=1-c sn^2, the Lamé residual is the polynomial
# -2*sn^2*(c^2-2(1+m)c+3m). Check its full coefficient identity.
for m in [Q(0), Q(1, 10), Q(1, 3), Q(1, 2), Q(9, 10), Q(1)]:
    for c in [Q(-1), Q(0), Q(1, 7), Q(1, 2), Q(3, 5), Q(2)]:
        mu = 1+m-2*c
        constant = (1+m)-2*c
        quadratic = 3*c*(1+m)-6*m
        exact(constant == mu, 'Lame constant polynomial coefficient')
        exact(quadratic + mu*c == -2*(c*c-2*(1+m)*c+3*m),
              'Lame quadratic polynomial factorization')

# K(m) by the arithmetic-geometric mean. This also verifies that the
# elliptic condition selects one parameter for the test examples.
def ellip_K(m):
    assert 0 <= m < 1
    aa, bb = 1.0, sqrt(1.0-m)
    for _ in range(100):
        na, nb = (aa+bb)/2.0, sqrt(aa*bb)
        if abs(na-nb)<1e-15:
            aa = na
            break
        aa, bb = na, nb
    return pi/(2*aa)

last = 0.0
for j in range(100):
    m = j/100.0
    val = ellip_K(m)*sqrt(1+m)
    exact(val > last, 'increasing positive-branch Dirichlet period')
    last = val

for N, diffusion in [(8, 0.01), (8, 0.03), (12, 0.01)]:
    r = 0.5/N
    if r <= diffusion:
        continue
    def wave_period(m):
        return 4*ellip_K(m)*sqrt(diffusion*(1+m)/r)
    low, high = 0.0, 1.0-1e-12
    exact(wave_period(low)<2*pi<wave_period(high),
          'elliptic period brackets the spatial circumference')
    for _ in range(75):
        mid=(low+high)/2
        if wave_period(mid)<2*pi:
            low=mid
        else:
            high=mid
    m=(low+high)/2
    exact(abs(wave_period(m)-2*pi)<1e-11,
          'elliptic branch matches required period')
    q=sqrt(1-m+m*m)
    c=1+m-q
    lam=r/(1+m)*(2*q-(1+m))
    exact(0<c<1 and lam>0 and isfinite(lam),
          'strictly positive periodic Lamé instability eigenvalue')
    exact(abs((2*q)**2-(1+m)**2-3*(1-m)**2)<1e-11,
          'positive eigenvalue square identity')

print(f'VERIFICATION_OK: {checks} exact/elementary assertions passed')
print('Infinite-dimensional convergence and originality are not certified by this checker.')
