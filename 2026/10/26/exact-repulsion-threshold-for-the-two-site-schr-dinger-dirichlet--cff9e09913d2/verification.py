"""Reproducibility checks for the two-mode, two-boson nonlinear energy classification.
Uses the Python standard library only. Tests supplement, not replace, the proof.
"""
import cmath
import math
import random

SEED = 20261024
rng = random.Random(SEED)
CHECKS = 0


def check(ok, what):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(what)


def energy(x, y, z, U, g, mu):
    a, b, c = abs(x)**2, abs(y)**2, abs(z)**2
    quartic = (a*a + b*b + c*c)/4 + a*b + b*c + c*a + (x.conjugate()*y*y*z.conjugate()).real
    return (U/2-mu)*(a+c)-mu*b-g*quartic


def energy_red(b, U, g, mu):
    return -mu + U/2 - 3*g/8 - (U/2+3*g/4)*b + 7*g*b*b/8


def exact_min(U, g, mu):
    return -mu - g/4 - max(0., 2*g-U)**2/(14*g)


def ground(U, g, mu, th_p=0., th_q=0.):
    if U >= 2*g:
        return 0j, 1.+0j, 0j
    a=(2*g-U)/(7*g)
    b=1-2*a
    return (math.sqrt(a)*cmath.exp(2j*th_p),
            math.sqrt(b)*cmath.exp(1j*(th_p+th_q)),
            math.sqrt(a)*cmath.exp(2j*th_q))


def nonlinear_rhs(x,y,z,U,g,mu):
    a,b,c=abs(x)**2,abs(y)**2,abs(z)**2
    return ((U-2*mu)*x-g*((a+2*b+2*c)*x+z.conjugate()*y*y),
            -2*mu*y-g*((2*a+b+2*c)*y+2*x*y.conjugate()*z),
            (U-2*mu)*z-g*((2*a+2*b+c)*z+x.conjugate()*y*y))


# Formula and phase optimization for random normalized triples.
for _ in range(1200):
    U=10**rng.uniform(-2,2)
    g=10**rng.uniform(-2,2)
    mu=rng.uniform(0,2)
    raw=[complex(rng.gauss(0,1),rng.gauss(0,1)) for j in range(3)]
    norm=math.sqrt(sum(abs(z)**2 for z in raw))
    x,y,z=(v/norm for v in raw)
    a,b,c=abs(x)**2,abs(y)**2,abs(z)**2
    r=math.sqrt(a*c)
    cross=(x.conjugate()*y*y*z.conjugate()).real
    phase_gap=g*((a-c)**2/8 + b*(math.sqrt(a)-math.sqrt(c))**2/2 + b*r-cross)
    # Last two terms are b r (1-cos(theta)) and cannot be negative.
    check(phase_gap>-1e-12,'phase nonnegative')
    check(abs((energy(x,y,z,U,g,mu)-energy_red(b,U,g,mu))-phase_gap)<3e-11,
          'exact phase-deficit identity')
    check(energy(x,y,z,U,g,mu)>=exact_min(U,g,mu)-3e-11,
          'global ground-state lower bound')

# The attaining states and critical continuity for independent parameter draws.
for _ in range(500):
    g=10**rng.uniform(-2,2)
    U=g*rng.uniform(0.005,4.)
    mu=rng.uniform(0,4)
    th_p,th_q=rng.uniform(-10,10),rng.uniform(-10,10)
    x,y,z=ground(U,g,mu,th_p,th_q)
    check(abs(sum(abs(v)**2 for v in (x,y,z))-1)<2e-14,'normalization')
    check(abs(energy(x,y,z,U,g,mu)-exact_min(U,g,mu))<6e-12,'attained energy')
    b=abs(y)**2
    if U<2*g:
        check(abs(b-(3*g+2*U)/(7*g))<2e-14,'ground state population')
        check(abs(abs(x)**2-abs(z)**2)<2e-14,'ground state symmetry')
    else:
        check(abs(b-1)<2e-14,'single-Fock-state phase')

# Quadratic energy cusp and order parameter: exact slopes on both sides.
for g in (0.13,0.87,1.,5.,17.):
    for delta in (1e-2,1e-3,1e-4):
        U=2*g-delta*g
        check(abs(exact_min(U,g,0)+g/4+g*delta*delta/14)<1e-12*g,
              'critical energy curvature')
        x,y,z=ground(U,g,0)
        check(abs(abs(x)**2-delta/7)<1e-13,'order parameter slope')

# Linearization in a rotating frame around the number-balanced |1,1> state.
# The transverse Bogoliubov matrix is [[U-g,-g],[g,-(U-g)]].
for _ in range(120):
    U=10**rng.uniform(-2,2)
    g=10**rng.uniform(-2,2)
    mu=rng.uniform(0,1)
    dx=complex(rng.uniform(-1,1),rng.uniform(-1,1))
    dz=complex(rng.uniform(-1,1),rng.uniform(-1,1))
    eps=1e-5
    x,z=eps*dx,eps*dz
    y=math.sqrt(1-abs(x)**2-abs(z)**2)+0j
    fx,fy,fz=nonlinear_rhs(x,y,z,U,g,mu)
    omega=2*mu+g
    predicted_x=(U-g)*x-g*z.conjugate()
    predicted_z=(U-g)*z-g*x.conjugate()
    check(abs(fx+omega*x-predicted_x)<2e-7*eps*max(U,g,1),
          'rotating-frame x linearization')
    check(abs(fz+omega*z-predicted_z)<2e-7*eps*max(U,g,1),
          'rotating-frame z linearization')
    check(abs((U-g)**2-g*g-U*(U-2*g))<1e-11*max(U,g,1)**2,
          'Bogoliubov discriminant')

print(f'PASS: {CHECKS} independent finite checks; seed={SEED}.')
