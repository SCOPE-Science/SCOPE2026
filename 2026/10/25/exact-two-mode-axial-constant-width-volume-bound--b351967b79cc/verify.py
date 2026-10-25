from fractions import Fraction as F

# Polynomials in t are coefficient lists in ascending degree.
def add(p, q):
    n = max(len(p), len(q))
    out = [F(0) for _ in range(n)]
    for i, c in enumerate(p): out[i] += c
    for i, c in enumerate(q): out[i] += c
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

def scale(p, c):
    out = [F(c) * x for x in p]
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

def mul(p, q):
    out = [F(0) for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q): out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

def deriv(p):
    if len(p) == 1: return [F(0)]
    return [F(i) * p[i] for i in range(1, len(p))]

def integ_minus1_1(p):
    return sum((c * (F(1)-F((-1)**(i+1))) / F(i+1)
                for i, c in enumerate(p)), F(0))

def ev(p, x):
    total = F(0)
    for c in reversed(p): total = total*x + c
    return total

# P3=(5t^3-3t)/2; P5=(63t^5-70t^3+15t)/8.
P3 = [F(0), F(-3,2), F(0), F(5,2)]
P5 = [F(0), F(15,8), F(0), F(-35,4), F(0), F(63,8)]
tP3p = [F(0)] + deriv(P3)
tP5p = [F(0)] + deriv(P5)
A3 = add(P3, scale(tP3p, -1))
A5 = add(P5, scale(tP5p, -1))
# B_j = A_j + (1-t^2) P_j''.
one_minus_t2 = [F(1), F(0), F(-1)]
B3 = add(A3, mul(one_minus_t2, deriv(deriv(P3))))
B5 = add(A5, mul(one_minus_t2, deriv(deriv(P5))))

assert A3 == [F(0), F(0), F(0), F(-5)]
assert B3 == [F(0), F(15), F(0), F(-20)]
assert A5 == [F(0), F(0), F(0), F(35,2), F(0), F(-63,2)]
assert B5 == [F(0), F(-105,2), F(0), F(455,2), F(0), F(-189)]
assert (ev(B3,F(1)), ev(B5,F(1))) == (F(-5), F(-14))
assert (ev(B3,F(1,2)), ev(B5,F(1,2))) == (F(5), F(-119,32))

# Each dictionary maps the monomial a^i b^j to its polynomial in t.
def dadd(x, y):
    out = dict(x)
    for key, p in y.items(): out[key] = add(out.get(key,[F(0)]),p)
    return {k:p for k,p in out.items() if any(p)}

def dmul(x, y):
    out = {}
    for (i,j), p in x.items():
        for (k,l), q in y.items():
            key = (i+k,j+l)
            out[key] = add(out.get(key,[F(0)]), mul(p,q))
    return {k:p for k,p in out.items() if any(p)}

h = {(0,0):[F(1)], (1,0):P3, (0,1):P5}
ra = {(0,0):[F(1)], (1,0):A3, (0,1):A5}
rm = {(0,0):[F(1)], (1,0):B3, (0,1):B5}
integrand = dmul(dmul(h,ra),rm)
volume_coeffs = {k: v for k,p in integrand.items() if (v := integ_minus1_1(p)*F(2,3)) != 0}
expected = {(0,0):F(4,3), (2,0):F(-20,7), (0,2):F(-56,11)}
assert volume_coeffs == expected, (volume_coeffs, expected)

vertices = [
    (F(1,5),F(0)), (F(-1,5),F(0)),
    (F(-47,405),F(64,567)), (F(47,405),F(-64,567))
]
def deficit_over_pi(a,b): return F(20,7)*a*a + F(56,11)*b*b
values = [deficit_over_pi(a,b) for a,b in vertices]
assert values == [F(4,35),F(4,35),F(9668,93555),F(9668,93555)]
assert F(4,35)-F(9668,93555) == F(1024,93555)

# Endpoint curvature factorizations, expanded exactly.
plus_az = [F(1),F(0),F(0),F(-1)]
plus_az_factored = mul([F(1),F(-1)], [F(1),F(1),F(1)])
plus_mer = [F(1),F(3),F(0),F(-4)]
plus_mer_factored = mul([F(1),F(-1)], [F(1),F(4),F(4)])
minus_az = [F(1),F(0),F(0),F(1)]
minus_az_factored = mul([F(1),F(1)], [F(1),F(-1),F(1)])
minus_mer = [F(1),F(-3),F(0),F(4)]
minus_mer_factored = mul([F(1),F(1)], [F(1),F(-4),F(4)])
assert plus_az == plus_az_factored
assert plus_mer == plus_mer_factored
assert minus_az == minus_az_factored
assert minus_mer == minus_mer_factored

print('Exact rational checks passed.')
print('Volume: 4*pi/3 - (20*pi/7)*a^2 - (56*pi/11)*b^2')
print('Deficit/pi at vertices:', values)
print('Mixed-vertex deficit gap/pi:', F(1024,93555))
