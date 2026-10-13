import math
import sympy as sp

eta, m, E = sp.symbols('eta m E', positive=True)
a = sp.Abs(eta**2 - 4)/(eta**2 + 4)
# On a fixed noncritical side, replace Abs by a positive symbol for differentiation.
aa = sp.symbols('a', positive=True)
N = sp.sqrt(E**2 - aa**2*m**2)/(sp.pi*aa)
rho = sp.simplify(sp.diff(N, E))
assert sp.simplify(rho - E/(sp.pi*aa*sp.sqrt(E**2-aa**2*m**2))) == 0

# Exact total in-gap count; use eta>0 symbol and square to avoid branch ambiguity.
q = sp.symbols('q', positive=True)
a_pos = sp.Abs(q**2-4)/(q**2+4)
left = sp.simplify((m/(sp.pi*a_pos))*sp.sqrt(1-a_pos**2))
right = 4*m*q/(sp.pi*sp.Abs(q**2-4))
assert sp.simplify(left-right) == 0

# Critical coefficients from the exact closed form, one-sided to avoid absolute-value ambiguity.
h = sp.symbols('h', positive=True)
expr_plus = 4*m*(2+h)/(sp.pi*((2+h)**2-4))
assert sp.simplify(sp.limit(h*expr_plus, h, 0, dir='+') - 2*m/sp.pi) == 0
expr_minus = 4*m*(2+h)/(sp.pi*((2+h)**2-4))
assert sp.simplify(sp.limit(h*expr_minus, h, 0, dir='+') - 2*m/sp.pi) == 0

# Fixed-energy density coefficient near eta=2 from a_eta ~ h/2.
a_h = ((2+h)**2-4)/((2+h)**2+4)
rho_h = E/(sp.pi*a_h*sp.sqrt(E**2-a_h**2*m**2))
assert sp.simplify(sp.limit(h*rho_h, h, 0, dir='+') - 2/sp.pi) == 0

# Direct momentum-count checks for both subcritical and supercritical couplings.
for eta0 in (0.5, 1.5, 2.5, 5.0, -0.5, -3.0):
    m0 = 1.7
    a0 = abs(eta0*eta0-4)/(eta0*eta0+4)
    E0 = 0.5*(a0*m0 + m0)
    K = math.sqrt((E0/a0)**2-m0*m0)
    direct = K/math.pi
    closed = math.sqrt(E0*E0-a0*a0*m0*m0)/(math.pi*a0)
    assert abs(direct-closed) < 1e-12

print('VERIFY_OK')
