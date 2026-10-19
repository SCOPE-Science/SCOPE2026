"""Reproducible algebraic and numerical checks for the directed two-hop sine ring.

Requires Python 3 with sympy, numpy and scipy. This is a diagnostic checker,
not a substitute for the all-parameter analytical proof.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

z, c = sp.symbols('z c')
u = (z + 1 / z) / 2
h = c / ((1 + u) * (1 - 2 * c))
d = lambda k: z**k - 1
ell = lambda k: d(k) - d(2*k) / (2*(1+u))
B11 = -(d(1)**2 + h * d(2)**2)
Bm12 = -(d(-1)*d(2) + h*d(-2)*d(4))
C11m1 = -(d(1)**2*d(-1) - d(2)**2*d(-2)/(2*(1+u)))
G_over_a = sp.cancel(C11m1 + (1-c)/c * B11*Bm12/(2*ell(1)-ell(2)))
real_G_over_a = sp.factor((G_over_a + G_over_a.subs(z,1/z))/2)
expected = 2*(1-u)*(1+2*u)*(1+u-2*c)/(1-2*c)**2
assert sp.cancel(real_G_over_a - expected) == 0
print('Exact rational-identity check: PASS')

z6 = (1+sp.I*sp.sqrt(3))/2
G6 = sp.simplify(sp.Rational(1,2)*G_over_a.subs({z:z6,c:sp.Rational(1,4)}))
assert sp.simplify(G6-(4-3*sp.I*sp.sqrt(3))) == 0
print('Exact six-site Hopf coefficient: PASS')

cases = 0
for N in range(5,101):
    phase = 2*math.pi/N
    u_float = math.cos(phase)
    delta_h = math.tan(math.pi/N)**2
    for q in range(1,N//2+1):
        theta = 2*math.pi*q/N
        if not (math.pi/4+1e-12<theta<math.pi/2-1e-12):
            continue
        a,b = math.cos(theta),math.cos(2*theta)
        c_float = a*a
        rho_h = a/(4*(-b)*math.cos(math.pi/N)**2)
        def eigen(k):
            ph = phase*k
            return a*(np.exp(1j*ph)-1)+rho_h*b*(np.exp(2j*ph)-1)
        lam1 = eigen(1)
        assert abs(lam1.real) < 5e-12
        assert abs(lam1.imag-a*math.tan(math.pi/N)) < 5e-12
        assert all(eigen(k).real < -1e-12 for k in range(2,N-1))
        def dd(r,k): return np.exp(1j*r*phase*k)-1
        def B(k,j): return -sum(w*math.sin(r*theta)*dd(r,k)*dd(r,j) for r,w in ((1,1),(2,rho_h)))
        def C(k,j,l): return -sum(w*math.cos(r*theta)*dd(r,k)*dd(r,j)*dd(r,l) for r,w in ((1,1),(2,rho_h)))
        G = C(1,1,-1)+B(-1,2)*B(1,1)/(2*lam1-eigen(2))
        closed = 2*a*(1-u_float)*(1+2*u_float)*(1+u_float-2*c_float)/(1-2*c_float)**2
        assert abs(G.real-closed) < 1e-8*max(1,closed)
        assert closed>0
        cases+=1
print(f'Fourier, strict spectral and cubic-sign checks: PASS ({cases} cases)')

# Finite-time drift near Hopf, from a second-order center-manifold predictor.
for N,q in ((6,1),(12,2),(7,1)):
    theta=2*math.pi*q/N; phase=2*math.pi/N
    a=math.cos(theta); b=math.cos(2*theta)
    rho=a/(4*(-b)*math.cos(math.pi/N)**2)
    omega=a*math.tan(math.pi/N)
    unit=np.exp(1j*phase*np.arange(N))
    def dd(r,k): return np.exp(1j*r*phase*k)-1
    def B(k,l): return -sum(w*math.sin(r*theta)*dd(r,k)*dd(r,l) for r,w in ((1,1),(2,rho)))
    def C(k,l,m): return -sum(w*math.cos(r*theta)*dd(r,k)*dd(r,l)*dd(r,m) for r,w in ((1,1),(2,rho)))
    eig=lambda k:a*dd(1,k)+rho*b*dd(2,k)
    G=C(1,1,-1)+B(-1,2)*B(1,1)/(2*eig(1)-eig(2))
    h20=B(1,1)/(2*eig(1)-eig(2))
    radius=0.004
    initial=(2*radius*unit.real+radius**2*np.real(h20*unit**2)).real
    def vector_field(time,x):
        return np.sin(theta+np.roll(x,-1)-x)+rho*np.sin(2*theta+np.roll(x,-2)-x)-math.sin(theta)-rho*math.sin(2*theta)
    period=2*math.pi/omega
    sol=solve_ivp(vector_field,(0,period),initial,method='DOP853',rtol=3e-12,atol=3e-14)
    assert sol.success
    final_mode=np.vdot(unit,sol.y[:,-1])/N
    measured=(abs(final_mode)-radius)/(period*radius**3)
    assert abs(measured-G.real/2)/ (G.real/2) < 0.012,(N,q,measured,G.real/2)
print('Nonlinear one-cycle cubic-drift diagnostics: PASS (3 rings)')
