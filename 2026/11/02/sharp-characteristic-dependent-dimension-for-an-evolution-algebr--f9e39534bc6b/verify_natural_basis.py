"""Finite-field checks for a natural-basis/automorphism theorem.

Run with Python 3 standard library. The proof is algebraic and does not
use the finite tests to deduce statements about infinite fields.
"""
from itertools import product
from fractions import Fraction


def det(matrix, p):
    n = len(matrix)
    a = [list(row) for row in matrix]
    d = 1
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k] % p), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            d = -d
        t = a[k][k] % p
        d = d * t % p
        inv = pow(t, -1, p)
        for j in range(k,n):
            a[k][j] = a[k][j] * inv % p
        for i in range(k+1,n):
            c = a[i][k]
            for j in range(k,n):
                a[i][j] = (a[i][j] - c*a[k][j]) % p
    return d % p


def times(x,y,p):
    if len(x) == 2:
        return ((x[0]*y[0] + x[1]*y[1]) % p, 0)
    a = (x[0]*y[0] + x[1]*y[1]) % p
    b = (x[2]*y[2]) % p
    return (a, b, (a+b)%p)


def test_automorphisms(n,p):
    standard = tuple(tuple(int(i == j) for i in range(n)) for j in range(n))
    originals = [times(v,v,p) for v in standard]
    num_invertible = num_auto = 0
    for flat in product(range(p), repeat=n*n):
        columns = [flat[n*j:n*(j+1)] for j in range(n)]
        rows = tuple(tuple(columns[j][i] for j in range(n)) for i in range(n))
        if det(rows,p) == 0:
            continue
        num_invertible += 1
        if any(any(times(columns[i],columns[j],p)) for i in range(n) for j in range(i+1,n)):
            continue
        ok = True
        for i in range(n):
            lhs = tuple(sum(originals[i][j]*columns[j][k] for j in range(n))%p for k in range(n))
            if lhs != times(columns[i],columns[i],p):
                ok = False
                break
        if ok:
            num_auto += 1
            assert columns == list(standard), ('unexpected automorphism',n,p,columns)
    assert num_auto == 1
    return (num_invertible,num_auto)

for n,p in [(2,2),(3,2),(3,3)]:
    a,b = test_automorphisms(n,p)
    print(f'AUT_DIM_{n}_FIELD_{p}: GL={a}, AUT={b}')

# Explicit distinct rational rotations give natural bases of the 3D algebra.
def check_ratrot(t):
    t=Fraction(t)
    c=(1-t*t)/(1+t*t)
    s=2*t/(1+t*t)
    e1=(c,s,Fraction(0))
    e2=(-s,c,Fraction(0))
    e3=(Fraction(0),Fraction(0),Fraction(1))
    def mult(x,y):
        a=x[0]*y[0]+x[1]*y[1]
        b=x[2]*y[2]
        return (a,b,a+b)
    assert mult(e1,e2) == mult(e1,e3) == mult(e2,e3) == (0,0,0)
    assert mult(e1,e1) == mult(e2,e2) == (1,0,1)
    assert mult(e3,e3) == (0,1,1)
    return (c,s)
rotations={check_ratrot(t) for t in range(1,24)}
assert len(rotations)==23
print(f'RATIONAL_ROTATIONS: {len(rotations)} distinct tested')

# The 2D characteristic-two family is checked with the exact identities
# over F_2[t] / 2, not by a finite search over possible parameters.
# (a,1+a) and (1+a,a) are orthogonal of norm one in characteristic two.
# Symbolically: a*(1+a) + (1+a)*a == 0, and a^2+(1+a)^2 == 1.
# Polynomial coefficient vectors over the integers: all coefficients
# of the orthogonality polynomial vanish modulo 2, and both norms
# are equal to 1 modulo 2. The determinant is 1 modulo 2 as well.
def add(a,b):
    return [x+y for x,y in zip(a,b)]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c
A=[0,1]
B=[1,1]
orth=add(mul(A,B),mul(B,A))
norm=add(mul(A,A),mul(B,B))
determ=add(mul(A,A),[-x for x in mul(B,B)])
assert all(x%2 == 0 for x in orth)
assert norm[0]%2 == 1 and all(x%2 == 0 for x in norm[1:])
assert determ[0]%2 == 1 and all(x%2 == 0 for x in determ[1:])
print('CHAR_TWO_FAMILY: polynomial identities checked modulo 2')
print('VERIFY_OK')
