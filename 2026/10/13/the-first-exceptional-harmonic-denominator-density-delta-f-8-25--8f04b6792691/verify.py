#!/usr/bin/env python3
from itertools import permutations, product
from math import gcd

# Polynomials use ascending coefficients.
def trim(a):
    a = list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b,p=None):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
        if p: c[i]%=p
    return trim(c)

def sub(a,b,p=None):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
        if p: c[i]%=p
    return trim(c)

def mul(a,b,p=None):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    if p: c=[x%p for x in c]
    return trim(c)

def scale(a,c,p=None):
    r=[c*x for x in a]
    if p: r=[x%p for x in r]
    return trim(r)

def divmod_poly(a,b,p):
    a=[x%p for x in trim(a)]; b=[x%p for x in trim(b)]
    q=[0]*max(1,(len(a)-len(b)+1))
    ib=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]*ib%p; q[k]=c
        for j in range(len(b)): a[j+k]=(a[j+k]-c*b[j])%p
        a=trim(a)
    return trim(q),trim(a)

def mod_poly(a,f,p): return divmod_poly(a,f,p)[1]
def gcd_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while b != [0]:
        _,r=divmod_poly(a,b,p); a,b=b,r
    inv=pow(a[-1],-1,p)
    return scale(a,inv,p)
def pow_poly(a,n,f,p):
    r=[1]; a=mod_poly(a,f,p)
    while n:
        if n&1: r=mod_poly(mul(r,a,p),f,p)
        a=mod_poly(mul(a,a,p),f,p); n//=2
    return r

def is_irreducible(f,p):
    f=[x%p for x in trim(f)]; n=len(f)-1
    inv=pow(f[-1],-1,p); f=scale(f,inv,p)
    x=[0,1]
    # Rabin: x^(p^n)=x and gcd(x^(p^(n/q))-x,f)=1 for q|n prime.
    z=pow_poly(x,p**n,f,p)
    if mod_poly(sub(z,x,p),f,p) != [0]: return False
    qs=[]; m=n; q=2
    while q*q<=m:
        if m%q==0:
            qs.append(q)
            while m%q==0: m//=q
        q+=1
    if m>1: qs.append(m)
    for q in qs:
        z=pow_poly(x,p**(n//q),f,p)
        if len(gcd_poly(sub(z,x,p),f,p))>1: return False
    return True

def prod_polys(fs,p=None):
    r=[1]
    for f in fs: r=mul(r,f,p)
    return r

# Build f_8 from its definition and translate x=z+4.
def linear_shift_poly(c): return [c,1]
def product_except(i,d):
    r=[1]
    for j in range(d+1):
        if j!=i: r=mul(r,[-j,1])
    return r
f8=[0]
for i in range(9): f8=add(f8,product_except(i,8))
# Horner substitution x=z+4.
g=[0]
for coeff in reversed(f8): g=add(mul(g,[4,1]),[coeff])
g=trim(g)
expected_g=[576,0,-2460,0,1365,0,-210,0,9]
assert g==expected_g, (g,expected_g)
h=[576,-2460,1365,-210,9]
assert [h[i//2] if i%2==0 else 0 for i in range(9)]==g

# Exact modular factorization certificates.
# h mod 17 = -8*(T^4+5T^3-7T^2-7T-4), irreducible.
f17=[-4,-7,-7,5,1]
assert [x%17 for x in scale(f17,-8,17)] == [x%17 for x in h]
assert is_irreducible(f17,17)
# h mod 11 = -2*(T+1)*(T^3+5T^2-2), cubic irreducible.
f11a=[1,1]; f11b=[-2,0,5,1]
assert scale(prod_polys([f11a,f11b],11),-2,11)==[x%11 for x in h]
assert is_irreducible(f11b,11)
# g mod 7 = 2*(z+3)*(z-3)*(z^2+1)*(z^4+z^2+3), with irreducible 2- and 4-factors.
f7=[[3,1],[-3,1],[1,0,1],[3,0,1,0,1]]
assert scale(prod_polys(f7,7),2,7)==[x%7 for x in g]
assert is_irreducible(f7[2],7) and is_irreducible(f7[3],7)

# Even signed permutations E semidirect S4 on signed roots +/-1,...,+/-4.
def signed_action(pi,e,v):
    s=1 if v>0 else -1; i=abs(v)-1
    if e[i]: s=-s
    return s*(pi[i]+1)
def cycle_type(pi,e):
    pts=list(range(1,5))+list(range(-1,-5,-1)); seen=set(); cs=[]
    for v in pts:
        if v in seen: continue
        w=v; n=0
        while w not in seen:
            seen.add(w); n+=1; w=signed_action(pi,e,w)
        cs.append(n)
    return tuple(sorted(cs,reverse=True))
def fixed_any(pi,e):
    return any(signed_action(pi,e,v)==v for v in list(range(1,5))+list(range(-1,-5,-1)))

els=[]; fixed=0
for pi in permutations(range(4)):
    for e in product((0,1), repeat=4):
        if sum(e)%2: continue
        els.append((pi,e))
        fixed += int(fixed_any(pi,e))
assert len(els)==192 and fixed==75

# The mod-7 cycle pattern is realized by a transposition with a negative 2-cycle,
# one negative fixed pair and one positive fixed pair; squaring gives a weight-2 kernel sign flip.
pi=(1,0,2,3); e=(1,0,1,0)
assert sum(e)%2==0 and cycle_type(pi,e)==(4,2,1,1)
# compose square and inspect its action: pair permutation is identity and signs are 1 on coordinates 0,1.
def compose(a,b):
    pi,e=a; pj,f=b
    # action a after b: permutation pi[pj[i]], sign f[i] xor e[pj[i]]
    return tuple(pi[pj[i]] for i in range(4)), tuple(f[i]^e[pj[i]] for i in range(4))
pi2,e2=compose((pi,e),(pi,e))
assert pi2==(0,1,2,3) and e2==(1,1,0,0)

from fractions import Fraction
assert Fraction(fixed,len(els))==Fraction(25,64)
print('VERIFY_OK centered_f8=yes h17=irreducible4 h11=1+3 g7=4+2+1+1 group_order=192 fixed=75 density=25/64')
