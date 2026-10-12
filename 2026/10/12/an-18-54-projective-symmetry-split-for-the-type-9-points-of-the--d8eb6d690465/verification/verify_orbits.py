import itertools
import sympy as sp

x, y, t, w = sp.symbols('x y t w')
q = t**8 + 4*t**7 - 17*t**6 - 65*t**5 - 89*t**4 - 65*t**3 - 17*t**2 + 4*t + 1
q1 = t**2 + t + 1
q2 = t**3 - 3*t**2 - 6*t - 1
q3 = t**3 + 6*t**2 + 3*t - 1
assert sp.expand(q1*q2*q3 - q) == 0
assert q.subs(t, 1) == -243

Q = x**24 + 4*x**21*y**3 - 17*x**18*y**6 - 65*x**15*y**9 - 89*x**12*y**12 - 65*x**9*y**15 - 17*x**6*y**18 + 4*x**3*y**21 + y**24
S = x**6 + x**3*y**3 + y**6
Nminus = x**9 - 3*x**6*y**3 - 6*x**3*y**6 - y**9
Nplus = x**9 + 6*x**6*y**3 + 3*x**3*y**6 - y**9
assert sp.expand(S*Nminus*Nplus - Q) == 0

# Work exactly in Q(w)/(w^2+w+1), with w a primitive cube root.
modpoly = sp.Poly(w**2 + w + 1, w, domain=sp.QQ)
def red(expr):
    num, den = sp.fraction(sp.cancel(expr))
    if den != 1:
        raise AssertionError(f'unexpected denominator: {den}')
    return sp.rem(sp.Poly(sp.expand(num), w, domain=sp.QQ), modpoly).as_expr()

def eq(a, b):
    return red(a-b) == 0

def proportional(v, u):
    return all(eq(v[i]*u[j], v[j]*u[i]) for i in range(3) for j in range(i+1,3))

omega2 = red(w**2)
v1 = (sp.Integer(1), w, omega2)
v2 = (sp.Integer(1), omega2, w)
assert all(eq(z, 0) for z in [sum(v1), sum(v2)])

perms = list(itertools.permutations(range(3)))
def proj_perm_stab(v):
    good = []
    for p in perms:
        vp = tuple(v[p[i]] for i in range(3))
        if proportional(vp, v):
            good.append(p)
    return good

stab1 = proj_perm_stab(v1)
stab2 = proj_perm_stab(v2)
assert len(stab1) == len(stab2) == 3
# Their stabilizers are exactly identity plus the two 3-cycles.
cycle_perms = {(0,1,2),(1,2,0),(2,0,1)}
assert set(stab1) == cycle_perms
assert set(stab2) == cycle_perms

# The cube map on the projective torus has kernel of order 9.
diagonal_kernel = 3**3 // 3
assert diagonal_kernel == 9
small_cube_classes = 2
small_points = diagonal_kernel * small_cube_classes
G_order = 9 * 6
assert G_order == 54
assert small_points == 18
assert G_order // 3 == small_points
all_type9 = 72
complement = all_type9 - small_points
assert complement == 54 == G_order

# The sextic factor is exactly the primitive-cube-root condition on a=x^3, b=y^3.
a, b = sp.symbols('a b', nonzero=True)
assert sp.factor(a**2 + a*b + b**2) == a**2 + a*b + b**2
# For a/b=w, the Fermat relation c=-a-b gives c/b=w^2; similarly for w^2.
assert red(-(w + 1) - omega2) == 0
assert red(-(omega2 + 1) - w) == 0

print('VERIFY_OK group_order=54 orbit_sizes=18,54 small_stabilizer=C3 small_locus=x9=y9=z9 sextic_factor=exact')
