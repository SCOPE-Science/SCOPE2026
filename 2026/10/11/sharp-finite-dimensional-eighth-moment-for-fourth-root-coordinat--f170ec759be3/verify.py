from fractions import Fraction
from itertools import product

ROOTS=((1,0),(0,1),(-1,0),(0,-1))

def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def cpow4(a):
    z=(1,0)
    for _ in range(4):
        z=cmul(z,a)
    return z

def moment_exact(coeffs):
    n=len(coeffs)
    total=0
    for ks in product(range(4), repeat=n):
        re=im=0
        for a,k in zip(coeffs,ks):
            z=cmul(a,ROOTS[k])
            re += z[0]; im += z[1]
        total += (re*re+im*im)**4
    return Fraction(total,4**n)

def identity(coeffs):
    mods=[a*a+b*b for a,b in coeffs]
    S=sum(mods); Q=sum(x*x for x in mods); R=sum(x**3 for x in mods); U=sum(x**4 for x in mods)
    T=(0,0)
    for a in coeffs:
        q=cpow4(a)
        T=(T[0]+q[0],T[1]+q[1])
    return 24*S**4-72*S*S*Q+18*Q*Q+64*S*R-34*U+(T[0]*T[0]+T[1]*T[1])

cases=[
    [(1,0),(1,1)],
    [(1,2),(2,-1)],
    [(1,0),(0,1),(1,1)],
    [(2,1),(-1,2),(1,-1)],
    [(1,0),(1,1),(2,-1),(-1,-2)],
]
for c in cases:
    assert moment_exact(c)==identity(c), (c,moment_exact(c),identity(c))

extremizers=0
for n in range(2,7):
    c=[ROOTS[j%4] for j in range(n)]
    got=moment_exact(c)
    C=Fraction(24)-Fraction(72,n)+Fraction(83,n*n)-Fraction(34,n**3)
    target=C*n**4
    assert got==target,(n,got,target)
    extremizers += 1

# An unequal-modulus example is strictly below the sharp normalized value.
c=[(1,0),(1,0),(2,0)]
got=moment_exact(c)
n=3
S=sum(a*a+b*b for a,b in c)
C=Fraction(24)-Fraction(72,n)+Fraction(83,n*n)-Fraction(34,n**3)
assert got < C*S**4
print(f"VERIFY_OK identity_cases={len(cases)} extremizers={extremizers} max_states={4**6}")
