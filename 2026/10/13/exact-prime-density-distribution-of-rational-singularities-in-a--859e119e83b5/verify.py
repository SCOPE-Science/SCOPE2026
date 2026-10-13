"""Exact arithmetic and finite-field checks for a plane-filling curve density theorem.

Run: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction
from math import factorial, comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def polynomial_remainder(a, b, p):
    a = trim([v % p for v in a[:]])
    b = trim([v % p for v in b[:]])
    assert b != [0]
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        offset = len(a) - len(b)
        factor = a[-1] * inv % p
        for j, value in enumerate(b):
            a[offset+j] = (a[offset+j] - factor*value) % p
        trim(a)
    return a


def polynomial_product(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j]=(out[i+j]+u*v)%p
    return trim(out)


f = [-1,0,0,1,0,0,0,1]
# Every reducible degree-seven polynomial over F_2 has a factor of degree <=3.
# The complete monic irreducible degree-one, -two and -three candidates:
small_irreducibles = [([0,1], [1]),([1,1],[1]),([1,1,1],[0,1]),
                      ([1,1,0,1],[1,1]),([1,0,1,1],[1,0,1])]
for divisor,expected in small_irreducibles:
    assert polynomial_remainder(f,divisor,2)==expected

p=467
roots=[123,135,150,163,196]
product=[1]
for r in roots:
    product=polynomial_product(product,[r,1],p)
product=polynomial_product(product,[111,167,1],p)
assert product == trim([v%p for v in f])
quad_disc=(167*167-4*111)%p
assert pow(quad_disc,(p-1)//2,p)==p-1   # irreducible quadratic

# In degree seven, transitive + transposition implies the full symmetric group.
# The Chebotarev frequencies are combinatorial densities of fixed points in S_7.
D=[1,0]
for n in range(2,8):
    D.append((n-1)*(D[-1]+D[-2]))
counts={j:comb(7,j)*D[7-j] for j in range(8)}
assert counts=={0:1854,1:1855,2:924,3:315,4:70,5:21,6:0,7:1}
assert sum(counts.values())==factorial(7)
assert Fraction(counts[0],factorial(7))==Fraction(103,280)

# Directly test rational singularities against roots of T^7+T^3-1.
def normalized_projective_points(q):
    yield (0,0,1)
    for z in range(q):
        yield (0,1,z)
    for y in range(q):
        for z in range(q):
            yield (1,y,z)


def arithmetic_singularities(q):
    pts=[]
    for x,y,z in normalized_projective_points(q):
        # F = A*x^q+B*y^q+C*z^q, with Ax+By+Cz=0 identically.
        # Hence at rational points the gradient of F equals (-A,-B,-C).
        A=(x*x*y-z*z*z-x*x*z)%q
        B=(y*y*z-x*x*x)%q
        C=(x*z*z+x*x*x-y*y*y)%q
        if A==B==C==0:
            pts.append((x,y,z))
    return pts

for q in [5,7,11,13,17,19,23,29,31,37,41,43,47]:
    roots=[u for u in range(q) if (pow(u,7,q)+pow(u,3,q)-1)%q==0]
    pts=arithmetic_singularities(q)
    assert len(pts)==len(roots)
    assert sorted(pts)==sorted((1,pow(u,-1,q),pow(u,2,q)) for u in roots)
print('VERIFY_OK irreducible_mod2=True transposition_mod467=True Galois=S7')
print('singularity_distribution',','.join(f'{j}:{counts[j]}/5040' for j in range(8)))
print('smooth_rational_prime_density=103/280 finite_field_checks=13')
