"""Exact checks for the quintic cyclic trigonal 5-rank divisor.

Requires Python 3.9+ only. All symbolic coefficient arithmetic is modulo 5.
The proofs of the Cartier identities and irreducibility are given in RESULT.md;
finite-field enumeration is independent corroboration, not a proof of generality.
"""
from itertools import product

P = 5
Z = (0, 0, 0, 0, 0)

def symbolic_sum(x, y):
    out = dict(x)
    for m, c in y.items():
        out[m] = (out.get(m, 0) + c) % P
    return {m: c for m, c in out.items() if c}

def symbolic_product(x, y):
    out = {}
    for m, c in x.items():
        for n, d in y.items():
            key = tuple(a + b for a, b in zip(m, n))
            out[key] = (out.get(key, 0) + c * d) % P
    return {m: c for m, c in out.items() if c}

def pure(i, power=1, coef=1):
    m = tuple(power if j == i else 0 for j in range(5))
    return {m: coef % 5}

# The x-polynomial f is represented by a map from x-exponent to a_i.
f = {i: pure(i) for i in range(5)}
f[5] = {Z: 1}

def polynomial_product(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i+j] = symbolic_sum(out.get(i+j, {}), symbolic_product(u, v))
    return out

f3 = polynomial_product(polynomial_product(f, f), f)
alpha = [f3.get(4+5*i, {}) for i in range(3)]
assert alpha[2] == pure(4, 1, 3)
H = {}
for i in range(3):
    H = symbolic_sum(H, symbolic_product(alpha[i], pure(4-i, 5)))
expected = {
    (2,0,0,0,6):3, (1,1,0,1,5):1, (1,0,2,0,5):3,
    (1,0,0,5,1):1, (0,2,1,0,5):3, (0,1,0,6,0):1,
    (0,1,0,5,2):3, (0,0,5,0,1):3, (0,0,2,5,0):3,
    (0,0,1,6,1):1, (0,0,0,8,0):1,
}
assert H == expected, (H, expected)
assert all(sum((5-i)*e for i,e in enumerate(m)) == 16 for m in H)

# Irreducibility certificate: viewed as a quadratic in a0, coefficient
# of a0^2 is 3*a4^6, and after a1=a2=0,a4=1 the discriminant is
# a3^8*(a3^2+3), not a square even over an algebraically closed field.
assert H[(2,0,0,0,6)] == 3
special = {}
for mon, c in H.items():
    if mon[1] == mon[2] == 0:
        a0degree, a3degree = mon[0], mon[3]
        special[(a0degree, a3degree)] = (special.get((a0degree,a3degree), 0) + c) % 5
assert special == {(2,0):3,(1,5):1,(0,8):1}, special
assert any(m[4] == 0 for m in H)  # no a4 factor / primitive in a0

# Arithmetic in F25 = F5[t]/(t^2-3).
def gfadd(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def gfmul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def gfscalar(c,x):return (c*x[0]%5,c*x[1]%5)
F25 = [(i,j) for i in range(5) for j in range(5)]
assert len(set(F25)) == 25
powers = {x: [(1,0)] for x in F25}
for x in F25:
    for i in range(5):powers[x].append(gfmul(powers[x][-1],x))
cube_multiplicity = {x:0 for x in F25}
for y in F25:
    cube_multiplicity[powers[y][3]] += 1
assert sorted(set(cube_multiplicity.values())) == [0,1,3]

def h_value(coeff):
    z = 0
    for m,c in H.items():
        t=c
        for a,e in zip(coeff,m):t=t*pow(a,e,5)%5
        z=(z+t)%5
    return z

def count25(coeff):
    result=1  # unique point over infinity
    for x in F25:
        px=powers[x]
        val=px[5]
        for i,c in enumerate(coeff):val=gfadd(val,gfscalar(c,px[i]))
        result += cube_multiplicity[val]
    return result

def polynorm(c):
    c=list(c)
    while c and c[-1]==0:c.pop()
    return c

def polyrem(a,b):
    a=polynorm(a); b=polynorm(b)
    if not b:raise ZeroDivisionError
    inv=pow(b[-1],-1,5)
    while len(a)>=len(b) and a:
        c=a[-1]*inv%5
        off=len(a)-len(b)
        for i,z in enumerate(b):a[i+off]=(a[i+off]-c*z)%5
        a=polynorm(a)
    return a

def squarefree(coeff):
    f=list(coeff)+[1]
    d=[(i*f[i])%5 for i in range(1,6)]
    a,b=polynorm(f),polynorm(d)
    while b:a,b=b,polyrem(a,b)
    return len(a)==1

nonzero_total=0; nonordinary=0; smooth_total=0
for coeff in product(range(5),repeat=5):
    if not squarefree(coeff):continue
    smooth_total +=1
    h = h_value(coeff)
    n25 = count25(coeff)
    assert (n25-1+2*h)%5==0, (coeff,h,n25)
    if h == 0:nonordinary += 1
    else:nonzero_total += 1
assert h_value((0,1,1,0,0))==0
assert h_value((0,1,0,1,0))==2
assert squarefree((0,1,1,0,0)) and squarefree((0,1,0,1,0))
assert count25((0,1,1,0,0)) == 36
assert count25((0,1,0,1,0)) == 42
print('VERIFY_OK: coefficientwise Cartier scalar, irreducible quadratic discriminant, weighted-degree-16 Hasse polynomial')
print(f'F5 finite-field crosscheck: {smooth_total} squarefree monic quintics, {nonordinary} with H=0, {nonzero_total} with H!=0, all N25 congruences verified')
print('Example point counts N25: p-rank0 36; p-rank2 42')
