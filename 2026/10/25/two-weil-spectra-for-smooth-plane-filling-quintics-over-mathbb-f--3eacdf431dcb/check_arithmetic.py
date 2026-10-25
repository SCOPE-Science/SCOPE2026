"""Exact algebraic checks for two plane-filling quintic Weil numerators.

Requires Python 3 standard library only. No geometric assumptions are
encoded in the polynomial arithmetic.
"""
from itertools import product

F = [tuple(c) for c in product(range(3), repeat=3)
     if all((t**3+c[0]*t*t+c[1]*t+c[2]) % 3 for t in range(3))]
assert len(F) == 8, F

def transform(c, scale, shift):
    # Monic characteristic polynomial after t -> scale*t+shift.
    # Compute affine substitution coefficients directly using binomial theorem.
    a,b,c0=c
    coeffs = [(scale**3)%3,
              (3*scale**2*shift+a*scale**2)%3,
              (3*scale*shift**2+2*a*scale*shift+b*scale)%3,
              (shift**3+a*shift**2+b*shift+c0)%3]
    inv=pow(coeffs[0],-1,3)
    return tuple((v*inv)%3 for v in coeffs[1:])

def orbit(c):
    return {transform(c,k,m) for k in (1,2) for m in range(3)}
assert sorted(set(map(tuple,F))) == sorted({(0,2,1),(0,2,2),
 (1,0,2),(1,1,2),(1,2,1),(2,0,1),(2,1,1),(2,2,2)})
O1=orbit((0,2,1)); O2=orbit((1,0,2))
assert O1=={(0,2,1),(0,2,2)}
assert O2==set(F)-O1 and len(O2)==6


# The six quotient rings used in the C++ enumeration are all fields.
modulus = {
 1: [0,1], 2: [1,0,1], 3: [1,0,2,1],
 4: [1,0,1,1,1], 5: [1,0,0,0,2,1],
 6: [1,0,0,0,1,1,1]}

def remainder(f,g):
    a=f[:]
    while len(a)>=len(g):
        if a[-1]:
            z=a[-1]
            for j in range(len(g)):a[len(a)-len(g)+j]=(a[len(a)-len(g)+j]-z*g[j])%3
        while a and a[-1]==0:a.pop()
    return a

for n,f in modulus.items():
    assert f[-1]==1
    if n==1: continue
    for d in range(1,n//2+1):
        for t in product(range(3), repeat=d):
            g=list(t)+[1]
            assert remainder(f,g), (n,d,g)

# Binary polynomial representation, bit i = coefficient of T^i.
def deg(f):return f.bit_length()-1

def rem(a,b):
    while deg(a)>=deg(b):a^=b<<(deg(a)-deg(b))
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def mul_mod(a,b,f):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if deg(a)>=deg(f):a^=f
    return rem(r,f)

def pow2x(k, f):
    v=2
    for _ in range(k):v=mul_mod(v,v,f)
    return v

q4 = [1,3,5,9,9]
l12=[1,9,42,131,308,601,1067,1803,2772,3537,3402,2187,729]
q4_2=sum((v%2)<<i for i,v in enumerate(q4))
l12_2=sum((v%2)<<i for i,v in enumerate(l12))
assert deg(q4_2)==4 and pow2x(4,q4_2)==2 and gcd(q4_2,pow2x(2,q4_2)^2)==1
assert deg(l12_2)==12 and pow2x(12,l12_2)==2
assert gcd(l12_2,pow2x(6,l12_2)^2)==1
assert gcd(l12_2,pow2x(4,l12_2)^2)==1

# Newton power sums and functional equation for smooth genus-six curves.
N_A=[13,13,55,13,208,913]
N_B=[13,13,16,117,273,640]

def weil_coeffs(counts):
    p=[0]+[3**i+1-counts[i-1] for i in range(1,7)]
    c=[1]
    for k in range(1,7):
        s=sum(c[k-j]*p[j] for j in range(1,k+1))
        assert s%k==0
        c.append(-s//k)
    c += [3**(k-6)*c[12-k] for k in range(7,13)]
    return c

def multiply_polys(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c
assert weil_coeffs(N_A)==multiply_polys(multiply_polys(q4,q4),q4)
assert weil_coeffs(N_B)==l12
assert l12_2 != q4_2
print('ORBIT_AND_WEIL_CHECK_OK')
