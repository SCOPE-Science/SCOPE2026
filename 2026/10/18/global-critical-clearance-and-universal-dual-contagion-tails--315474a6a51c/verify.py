"""Reproduce algebraic identities and finite-time checks for a symmetric interacting SIS model.

The symbolic checks verify the formulas entering the mathematical proof.
The numerical integrations do not prove infinite-time asymptotics.
"""
from math import sqrt
from sympy import symbols, factor, simplify
from scipy.integrate import solve_ivp

u, v, h = symbols('u v h', positive=True)
z = u + 3*v/2
phi = u + 2*h*v
f = factor((1-3*u-v)*phi + h*v-u)
g = factor(2*u*phi-2*h*v)
assert simplify(f - (3*h*v - 3*u*u - (1+6*h)*u*v - 2*h*v*v)) == 0
assert simplify(g - (2*u*u + 4*h*u*v - 2*h*v)) == 0
assert simplify(f + 3*g/2 + v*(u+2*h*v)) == 0
# At v=0, v' >= 0; at u=0, u' >= 0; at 2u+v=1, susceptible flux is nonnegative.
assert simplify(g.subs(v,0) - 2*u*u) == 0
assert simplify(f.subs(u,0) - h*v*(3-2*v)) == 0
assert simplify((2*f+g).subs(v,1-2*u) + 2*u) == 0
# The claimed exact scalar equations for the two asymptotic ratios.
qdot = simplify(g/z-v*(f+3*g/2)/z**2)
q_rhs = 2*u*u/z + (v/z)*(-2*h+4*h*u+v*(u+2*h*v)/z)
assert simplify(qdot-q_rhs) == 0
rdot = simplify(g/z**2-2*v*(f+3*g/2)/z**3)
r_rhs = 2*(u/z)**2 + (v/z**2)*(-2*h+4*h*u+2*v*(u+2*h*v)/z)
assert simplify(rdot-r_rhs) == 0
print('All symbolic rate, boundary, Lyapunov and ratio identities: PASS')

for hh in (0.35, 0.75, 1.0, 2.0, 4.0):
    def vector_field(t, x):
        a,b = x
        return [3*hh*b-3*a*a-(1+6*hh)*a*b-2*hh*b*b,
                2*a*a+4*hh*a*b-2*hh*b]
    for initial in ((0.1,0.05), (0.0,0.3), (0.3,0.0)):
        sol = solve_ivp(vector_field,(0,100000),initial,method='LSODA',
                        rtol=3e-11,atol=1e-13)
        assert sol.success
        a,b = sol.y[:,-1]
        assert a > 0 and b > 0 and 2*a+b <= 1+1e-8
        aa = sqrt(100000)*a/sqrt(hh/2)
        bb = 100000*b/(0.5)
        assert abs(aa-1)<0.09 and abs(bb-1)<0.15, (hh, initial, aa, bb)
        print('h=',hh,'initial=',initial,'u-scale=',round(aa,5),
              'v-scale=',round(bb,5))
print('All numerical spot checks: PASS')
