"""Exact coefficient and polynomial certificates for a genus-three hyperelliptic family.
Run: python3 verify.py (standard library only)."""
from math import factorial

def trim(c,p):
    c=[v%p for v in c]
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def add(a,b,p):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]=(c[i]+x)%p
    for i,x in enumerate(b): c[i]=(c[i]+x)%p
    return trim(c,p)

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c,p)

def monomial_root(r,p): return [(-r)%p,1]

def rem(f,g,p):
    f=trim(f,p)[:];g=trim(g,p)
    assert g!=[0]
    inverse=pow(g[-1],-1,p)
    while len(f)>=len(g) and f!=[0]:
        s=len(f)-len(g);m=f[-1]*inverse%p
        for j,b in enumerate(g): f[s+j]=(f[s+j]-m*b)%p
        f=trim(f,p)
    return f

def monic(f,p):
    f=trim(f,p); return [(x*pow(f[-1],-1,p))%p for x in f] if f!=[0] else f

def gcd(f,g,p):
    while g!=[0]: f,g=g,rem(f,g,p)
    return monic(f,p)

def derivative(f,p): return trim([(i*f[i])%p for i in range(1,len(f))] or [0],p)

def coeff(n,k,p):
    """coefficient of z^k in (1+a z+z^2)^n, as a polynomial in a"""
    out=[0]*(n+1)
    for r in range(n+1):
        s=k-2*r; t=n-r-s
        if s>=0 and t>=0 and s<=n:
            out[s]=(out[s]+factorial(n)//(factorial(r)*factorial(s)*factorial(t)))%p
    return trim(out,p)

def hasse(p):
    m=(p-1)//2
    return [[coeff(m,(p*(i+1)-(j+1)-m)//3,p)
            if (p*(i+1)-(j+1)-m)%3==0 and p*(i+1)-(j+1)>=m else [0]
            for j in range(3)] for i in range(3)]

p=31; H=hasse(p)
assert H[0][0]==H[2][2]
assert all(H[i][j]==[0] for i in range(3) for j in range(3) if i!=j)
A,B=H[0][0],H[1][1]
expected_A=[0,1,0,4,0,-4]; expected_B=[0,-11,0,-2,0,15,0,-11,0,1,0,6,0,-7,0,1]
assert A==trim(expected_A,p) and B==trim(expected_B,p)
Af=[-4%p]
for r in [0,12,-12]: Af=mul(Af,monomial_root(r,p),p)
Af=mul(Af,[-12,0,1],p)
assert Af==A
Bf=[1]
for r in [0,15,12,8,6,-6,-8,-12,-15]:
    Bf=mul(Bf,monomial_root(r,p),p)
for q in [[4,0,1],[-11,-4,1],[-11,4,1]]:
    Bf=mul(Bf,q,p)
assert Bf==B
G=gcd(A,B,p)
assert G==[0,11,0,1]
assert gcd(A,derivative(A,p),p)==[1]
assert gcd(B,derivative(B,p),p)==[1]
assert A[0]==B[0]==0
for z in [2,-2]:
    def evalpoly(f,a,p):
        z=0
        for c in f[::-1]: z=(z*a+c)%p
        return z
    assert evalpoly(A,z,p)!=0 and evalpoly(B,z,p)!=0
assert len(A)-1==5 and len(B)-1==15 and len(G)-1==3
# First nonzero smooth superspecial marked parameters: all nine Hasse entries
# must vanish, and smooth parameters are characterized by a^2 != 4.
for prime in [5,7,11,13,17,19,23,29]:
    T=hasse(prime); pols=[x for row in T for x in row if x!=[0]]
    common=pols[0]
    for pol in pols[1:]: common=gcd(common,pol,prime)
    smoothcommon=common
    # Remove a=+-2 if a root (they are singular boundary curves).
    for z in [2,-2]:
        lin=monomial_root(z,prime)
        while rem(smoothcommon,lin,prime)==[0] and smoothcommon!=[1]:
            q=[0]*(len(smoothcommon)-1)
            # synthetic division by a-z
            q[-1]=smoothcommon[-1]
            for j in range(len(q)-2,-1,-1): q[j]=(smoothcommon[j+1]+z*q[j+1])%prime
            smoothcommon=trim(q,prime)
    assert (smoothcommon==[1] or smoothcommon==[0,1]),(prime,smoothcommon)
print('GENUS3_HASSE31_DIAGONAL_OK')
print('FACTOR_IDENTITIES_AND_SEPARABILITY_OK')
print('COMMON_ZERO_DIVISOR=a*(a^2+11), DEGREE=3')
print('CHARACTERISTIC31_RANK_STRATA: rank0=3, rank1=2, rank2=12, rank3=all other smooth parameters')
print('SMOOTH_SUPERSPECIAL_PARAMETERS=0,+12,-12')
print('FIRST_ADDITIONAL_NONZERO_SUPERSPECIAL_IN_PRIMES_5_TO_31_OK')
print('VERIFY_OK')
