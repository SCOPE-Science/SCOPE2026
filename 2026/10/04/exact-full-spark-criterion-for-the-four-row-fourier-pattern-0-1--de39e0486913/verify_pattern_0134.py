#!/usr/bin/env python3
from itertools import permutations, combinations
from math import gcd, isqrt

# Sparse multivariate integer polynomials in x0,x1,x2,x3.
ZERO = {}
ONE = {(0,0,0,0): 1}

def add(a,b):
    c=dict(a)
    for m,v in b.items():
        c[m]=c.get(m,0)+v
        if c[m]==0: del c[m]
    return c

def mul(a,b):
    c={}
    for ma,va in a.items():
        for mb,vb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb))
            c[m]=c.get(m,0)+va*vb
    return {m:v for m,v in c.items() if v}

def mon(var,pow=1,coef=1):
    e=[0]*4; e[var]=pow
    return {tuple(e):coef}

def sign_perm(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv&1 else 1

# det(x_j^{r_i}) for row exponents r=(0,1,3,4)
rows=(0,1,3,4)
det={}
for p in permutations(range(4)):
    term=ONE
    for i,j in enumerate(p):
        term=mul(term, mon(j,rows[i]))
    if sign_perm(p)==1:
        det=add(det,term)
    else:
        det=add(det,{m:-v for m,v in term.items()})

# Vandermonde product prod_{i<j}(x_j-x_i)
vand=ONE
for i in range(4):
    for j in range(i+1,4):
        vand=mul(vand, add(mon(j), mon(i,coef=-1)))

# e2=sum_{i<j}x_i x_j
e2={}
for i in range(4):
    for j in range(i+1,4):
        e2=add(e2,mul(mon(i),mon(j)))

rhs=mul(vand,e2)
assert det==rhs or det=={m:-v for m,v in rhs.items()}
print('FACTORIZATION_OK', len(det), 'terms')

def divisors(n):
    ds=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ds.append(d)
            if d*d!=n: ds.append(n//d)
    return sorted(ds)

def uniform_0134(n):
    M=(0,1,3,4)
    for d in divisors(n):
        q,r=divmod(len(M),d)
        counts=[0]*d
        for m in M: counts[m%d]+=1
        if any(c not in (q,q+1) for c in counts):
            return False
    return True

for n in range(5,5001):
    formula=(n%3!=0 and n%4!=0)
    assert uniform_0134(n)==formula, (n,uniform_0134(n),formula)
print('UNIFORMITY_OK N<=5000')

# exact modular certificates for the nonvanishing side on a substantial range.
def isprime(p):
    if p<2:return False
    if p%2==0:return p==2
    d=3
    while d*d<=p:
        if p%d==0:return False
        d+=2
    return True

def factorint(n):
    out=[];d=2;m=n
    while d*d<=m:
        if m%d==0:
            out.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1: out.append(m)
    return out

def primitive_root(p):
    fac=factorint(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac):
            return g
    raise RuntimeError

def primes_1mod(n,count=10):
    out=[]; k=1
    while len(out)<count:
        p=k*n+1
        if isprime(p): out.append(p)
        k+=1
    return out

def e2_mod(vals,p):
    return sum(vals[i]*vals[j] for i in range(4) for j in range(i+1,4))%p

# If a complex cyclotomic value were zero, every reduction at a primitive Nth root
# modulo a prime p == 1 (mod N) would also be zero. Thus one nonzero reduction
# certifies nonvanishing. We allow several primes because a nonzero algebraic integer
# can vanish modulo an individual prime.
checked=0
max_primes_used=0
for n in range(5,121):
    if gcd(n,6)!=1:
        continue
    unresolved=set(combinations(range(1,n),3))
    used=0
    for p in primes_1mod(n,10):
        g=primitive_root(p)
        z=pow(g,(p-1)//n,p)
        assert pow(z,n,p)==1 and all(pow(z,n//q,p)!=1 for q in factorint(n))
        powers=[pow(z,k,p) for k in range(n)]
        unresolved={abc for abc in unresolved
                    if e2_mod((1,powers[abc[0]],powers[abc[1]],powers[abc[2]]),p)==0}
        used+=1
        if not unresolved:
            break
    assert not unresolved, (n,len(unresolved))
    checked += (n-1)*(n-2)*(n-3)//6
    max_primes_used=max(max_primes_used,used)
print('MODULAR_NONZERO_OK', checked, 'normalized quadruples, N<=120, gcd(N,6)=1, max_primes', max_primes_used)

# Exact obstruction witnesses: for even N, roots {1,t,t^2,-t}; for 3|N,
# roots {1,w,w^2,t}. The six pair-products cancel algebraically.
for n in range(6,501):
    if n%2==0:
        exps=(0,1,2,1+n//2)
        assert len(set(e%n for e in exps))==4
    if n%3==0:
        exps=(0,n//3,2*n//3,1)
        assert len(set(e%n for e in exps))==4
print('WITNESS_INDEX_OK N<=500')
print('VERIFY_OK')
