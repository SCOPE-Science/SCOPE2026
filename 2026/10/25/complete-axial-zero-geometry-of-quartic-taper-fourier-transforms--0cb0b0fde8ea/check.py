"""Independent numerical and symbolic consistency checks for the quartic-window zero theorem."""
import mpmath as mp
import sympy as sp

mp.mp.dps = 70
z, tau = sp.symbols('z tau')
s = sp.sin(z)/z
fourth = sp.diff(s, z, 4)
assert sp.simplify(fourth*z**5 - ((z**4 - 12*z**2 + 24)*sp.sin(z) + (4*z**3-24*z)*sp.cos(z))) == 0
assert sp.simplify(sp.series(s-tau*fourth,z,0,4).removeO() - (1-tau/sp.Integer(5) + (-sp.Rational(1,6)+tau/sp.Integer(14))*z**2)) == 0
print('symbolic_fourth_derivative: PASS')
print('symbolic_local_expansion: PASS')

def sinc(u):
    if abs(u) < mp.mpf('0.01'):
        return mp.fsum([(-1)**k*u**(2*k)/mp.factorial(2*k+1) for k in range(35)])
    return mp.sin(u)/u

def sinc4(u):
    if abs(u) < mp.mpf('0.01'):
        return mp.fsum([(-1)**k*u**(2*k)*mp.factorial(2*k+4) / (mp.factorial(2*k)*mp.factorial(2*k+5)) for k in range(35)])
    return ((u**4-12*u**2+24)*mp.sin(u)+(4*u**3-24*u)*mp.cos(u))/u**5

def R(u):return sinc4(u)/sinc(u)

# Direct numerical quadrature of the Fourier integral, at independent points.
for a in [mp.mpf('0.25'),mp.mpf('1.9'),mp.mpf('4.2'),mp.mpc('1.3','0.7')]:
    for t in [mp.mpf('0.7'),mp.mpf('1.5'),mp.mpf('6.5')]:
        value=2*(sinc(a)-t*sinc4(a))
        reference=mp.quad(lambda x: (1-t*x**4)*mp.exp(1j*a*x), [-1,0,1])
        assert abs(value-reference)<mp.mpf('1e-55')
print('independent_integrals: 12 PASS')

# Partial-fraction residues, evaluated without assuming the infinite tail vanishes.
for u in [mp.mpf('0.7'),mp.mpf('2'),mp.mpc('3','0.75')]:
    for N in [1000,5000,20000]:
        approx=1+mp.fsum([(8-48/(n*mp.pi)**2)/(u*u-(n*mp.pi)**2) for n in range(1,N+1)])
        assert abs(approx-R(u))<mp.mpf(1)/N
print('partial_fractions: 9 truncation checks PASS (with explicit O(1/N) tolerance)')

# Exact-location brackets using real monotonicity of R(w) on each spectral gap.
def Rw(w):
    u=mp.sqrt(w) if w>=0 else 1j*mp.sqrt(-w)
    return mp.re(R(u))
for t in [mp.mpf('.5'),mp.mpf('1'),mp.mpf('1.05'),mp.mpf('2'),mp.mpf('5'),mp.mpf('10')]:
    level=1/t
    for n in range(1,6):
        a=(n*mp.pi)**2+mp.mpf('0.01')
        b=((n+1)*mp.pi)**2-mp.mpf('0.01')
        assert Rw(a)>level>Rw(b)
        lo,hi=a,b
        for _ in range(240):
            mid=(lo+hi)/2
            if Rw(mid)>level:lo=mid
            else: hi=mid
        root=mp.sqrt((lo+hi)/2)
        assert abs(sinc(root)-t*sinc4(root))<mp.mpf('1e-50')
        assert n*mp.pi < root < (n+1)*mp.pi
print('high_real_roots: 30 PASS')

for t in [mp.mpf('1.1'),mp.mpf('2'),mp.mpf('4')]:
    level=1/t
    lo=mp.mpf('-100000');hi=mp.mpf('0')
    assert Rw(lo)>level>Rw(hi)
    for _ in range(240):
        mid=(lo+hi)/2
        if Rw(mid)>level:lo=mid
        else:hi=mid
    root=mp.sqrt(-((lo+hi)/2))
    assert abs(sinc(1j*root)-t*sinc4(1j*root))<mp.mpf('1e-40')
    assert root>0
print('imaginary_root_pairs: 3 PASS')
for t in [mp.mpf('6'),mp.mpf('10')]:
    level=1/t
    lo=mp.mpf('0');hi=mp.pi**2-mp.mpf('.00001')
    assert Rw(lo)>level>Rw(hi)
    for _ in range(240):
        mid=(lo+hi)/2
        if Rw(mid)>level:lo=mid
        else: hi=mid
    root=mp.sqrt((lo+hi)/2)
    assert abs(sinc(root)-t*sinc4(root))<mp.mpf('1e-50')
    assert 0<root<mp.pi
print('central_real_pairs: 2 PASS')
print('checks_complete: PASS')
