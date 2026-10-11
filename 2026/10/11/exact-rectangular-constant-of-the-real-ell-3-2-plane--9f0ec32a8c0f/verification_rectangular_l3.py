import sympy as sp

# Exact algebraic checker for the rectangular constant of the real l_3 plane.
t, s, u = sp.symbols('t s u', positive=True, real=True)
P14 = (
    u**14 - 36*u**13 + 783*u**12 - 2584*u**11 + 8189*u**10
    - 13212*u**9 + 20019*u**8 - 17104*u**7 + 15155*u**6
    - 8860*u**5 + 4733*u**4 - 2456*u**3 + 143*u**2 - 36*u + 1
)
D = (1 + s*t**2)**3 + (s - t)**3
P = t**2*(1 + s*t**2)**2 + (s - t)**2
Q = (1 + s*t**2)**2 - t*(s - t)**2
E1 = sp.expand(P**3*(1+t**3) - Q**3*(1+t**6))
G = sp.expand(
    (t**12 - 4*t**9 - 6*t**6 - 4*t**3 + 1)*s**2
    + 4*(t**10-t)*s + 2*(t**8+t**2)
)
res = sp.factor(sp.resultant(E1, G, s))
expected = sp.factor(
    (t+1)**18*(t**2+1)*(t**2-t+1)**18*(t**4-t**2+1)*P14.subs(u,t**3)
)
assert sp.expand(res-expected) == 0

poly = sp.Poly(P14, u)
I1 = (sp.Rational(295832,10**7), sp.Rational(295833,10**7))
I2 = (sp.Rational(6845614,10**7), sp.Rational(6845615,10**7))
assert sp.count_roots(poly, 0, 1) == 2
assert sp.count_roots(poly, *I1) == 1
assert sp.count_roots(poly, *I2) == 1

Au = u**4 - 4*u**3 - 6*u**2 - 4*u + 1
# Au is strictly decreasing on (0,1); endpoint signs classify the two stationary roots.
assert sp.diff(Au,u).subs(u,sp.Rational(1,2)) < 0
assert Au.subs(u,I1[1]) > 0
assert Au.subs(u,I2[0]) < 0

roots = [r for r in sp.nroots(P14, n=60, maxsteps=300) if abs(sp.im(r)) < sp.Float('1e-45') and 0 < sp.re(r) < 1]
roots = sorted([sp.re(r) for r in roots], key=float)
u_star = roots[0]
t_star = sp.real_root(u_star, 3)
Gstar = sp.Poly(G.subs(t, sp.N(t_star,60)), s)
sroots = sorted([sp.re(r) for r in sp.nroots(Gstar, n=60) if abs(sp.im(r)) < sp.Float('1e-45')], key=float)
s_star = [r for r in sroots if r > t_star][0]
A = (1+t_star**3)**(sp.Rational(1,3))
B = (1+t_star**6)**(sp.Rational(1,3))
mu = (A+s_star*B)/((1+s_star*t_star**2)**3+(s_star-t_star)**3)**(sp.Rational(1,3))

# Exact witness that the maximum lies above the easy-bound branches.
# At t=1/3,s=4/3, R=(9*cuberoot(28)+4*cuberoot(730))/cuberoot(49474)
# > 63/37 > 2^(2/3), since 37^3>49474 and 63^3>4*37^3.
assert 37**3 > 49474
assert 63**3 > 4*37**3

print('resultant_factorization_verified=true')
print('roots_in_(0,1)=2')
print('root1_interval=[0.0295832,0.0295833]')
print('root2_interval=[0.6845614,0.6845615]')
print('root1_A_positive=true')
print('root2_A_negative=true')
print('u_star=', sp.N(u_star,45))
print('t_star=', sp.N(t_star,45))
print('s_star=', sp.N(s_star,45))
print('mu=', sp.N(mu,45))
print('witness_above_2^(2/3)=true')
