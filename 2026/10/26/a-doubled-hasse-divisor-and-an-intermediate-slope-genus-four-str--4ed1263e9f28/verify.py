#!/usr/bin/env python3
"""Exact reproducibility checks for a genus-four cyclic trigonal family.

Uses only the Python standard library. No random sampling or numeric tolerances.
"""
from itertools import product
from math import comb
P = 7

def clean(d):
    return {key:val%P for key,val in d.items() if val%P}

def add(a,b,sign=1):
    o=dict(a)
    for k,v in b.items():o[k]=(o.get(k,0)+sign*v)%P
    return clean(o)

def mul(a,b):
    o={}
    for (x,y),v in a.items():
        for (z,w),u in b.items():
            k=(x+z,y+w)
            o[k]=(o.get(k,0)+v*u)%P
    return clean(o)

def determinant(M):
    if len(M)==1:return M[0][0]
    ans={}
    for j,t in enumerate(M[0]):
        minor=[row[:j]+row[j+1:] for row in M[1:]]
        ans=add(ans,mul(t,determinant(minor)),(-1)**j)
    return ans

def coeffs(power):
    # Polynomial in (x,a,b): x^5+a*x+b; no symbolic algebra system.
    terms={(5,0,0):1,(1,1,0):1,(0,0,1):1}
    h={(0,0,0):1}
    for _ in range(power):
        n={}
        for i,v in h.items():
            for j,w in terms.items():
                key=tuple(i[t]+j[t] for t in range(3))
                n[key]=(n.get(key,0)+v*w)%P
        h={k:v for k,v in n.items() if v}
    return h

def block(power,inds):
    h=coeffs(power)
    return [[clean({(a,b):v for (deg,a,b),v in h.items() if deg==P*(k+1)-1-i})
             for k in inds] for i in inds]

M1=block(2,[0]); M2=block(4,[0,1,2]); det=mul(determinant(M1),determinant(M2))
assert M1==[[{(1,0):2}]],M1
assert M2==[
    [{(1,2):5},{},{(0,0):1}],
    [{(0,3):4},{(2,0):6},{}],
    [{(4,0):1},{(1,1):5},{}]
],M2
assert det=={(7,0):2,(2,4):5},det
print('Cartier coefficient blocks verified; determinant = 2*a^2*(a^5-b^4).')

for a,b in product(range(P),repeat=2):
    singular=(pow(a,5,P)-pow(b,4,P))%P==0
    parametrized=any(pow(t,4,P)==a and pow(t,5,P)==b for t in range(P))
    assert singular==parametrized
assert sum((pow(a,5,P)-pow(b,4,P))%P !=0 and a==0 for a,b in product(range(P),repeat=2))==6
assert sum((pow(a,5,P)-pow(b,4,P))%P !=0 and a!=0 for a,b in product(range(P),repeat=2))==36
print('Discriminant cusp and F7 parameter counts verified.')

# At a=0,b=1: basis ordered (dx/y^2, x dx/y^2, x^2 dx/y^2).
# Source-to-target Cartier matrix has only entries M[0,2]=1, M[1,0]=4.
# Its second power is nonzero; its third power zero. Additional dx/y is killed.
N=[[0,0,1],[4,0,0],[0,0,0]]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%P for j in range(3)] for i in range(3)]
N2=mm(N,N);N3=mm(N2,N)
assert any(c for row in N2 for c in row)
assert all(c==0 for row in N3 for c in row)
print('Exceptional Cartier chain (length three) verified.')

# Finite field arithmetic, derived from exhaustive irreducibility searches.
# For degree <=4, absence of monic factors of degree <= floor(n/2) is sufficient.
def redpoly(a,mod):
    n=len(mod)-1
    a=list(a)+[0]*max(0,n-len(a))
    for h in range(len(a)-1,n-1,-1):
        c=a[h]%P
        if c:
            for k in range(n):a[h-n+k]=(a[h-n+k]-c*mod[k])%P
    return tuple(v%P for v in a[:n])

def field(n):
    if n==1:
        return P,lambda a,b:(a+b)%P,lambda a,b:(a*b)%P
    def divisible_by(f,g):
        z=list(f)
        while len(z)>=len(g):
            c=z[-1]%P
            if c:
                for k in range(len(g)):z[len(z)-len(g)+k]=(z[len(z)-len(g)+k]-c*g[k])%P
            while z and z[-1]%P==0:z.pop()
        return not z
    mod=None
    for coeffs in product(range(P),repeat=n):
        poly=coeffs+(1,)
        if all(not divisible_by(poly,g+(1,)) for d in range(1,n//2+1)
               for g in product(range(P),repeat=d)):
            mod=poly;break
    assert mod is not None
    q=P**n
    digits=[]
    for i in range(q):
        z=i; v=[]
        for _ in range(n):v.append(z%P);z//=P
        digits.append(tuple(v))
    def encode(v):return sum((c%P)*P**i for i,c in enumerate(v))
    def plus(a,b):return encode([(digits[a][i]+digits[b][i])%P for i in range(n)])
    def times(a,b):
        poly=[0]*(2*n-1)
        for i,x in enumerate(digits[a]):
            for j,y in enumerate(digits[b]):poly[i+j]=(poly[i+j]+x*y)%P
        return encode(redpoly(poly,mod))
    return q,plus,times

def nth_power(a,k,times):
    z=1
    while k:
        if k&1:z=times(z,a)
        a=times(a,a);k//=2
    return z

counts={}
for n in (1,2,3,4):
    q,plus,times=field(n)
    # One point at infinity because gcd(3,5)=1.
    total=1
    for x in range(q):
        v=plus(nth_power(x,5,times),1)
        if v==0:total+=1
        elif nth_power(v,(q-1)//3,times)==1:total+=3
    counts[n]=total
assert counts=={1:8,2:50,3:344,4:2094},counts
# Newton identities: c0=1 and nc_n=-sum_{i=1}^n c_{n-i} s_i.
sums={n:P**n+1-counts[n] for n in counts}
c=[1]
for n in (1,2,3,4):
    z=-sum(c[n-i]*sums[i] for i in range(1,n+1))
    assert z%n==0
    c.append(z//n)
c += [P**(j+1)*c[3-j] for j in range(4)]
assert c==[1,0,0,0,-77,0,0,0,2401],c
# Newton polygon of 1-77*T^4+7^4*T^8 is (0,0)->(4,1)->(8,4),
# with slope 1/4 four times and 3/4 four times.
assert (-77)%P==0 and (-77)%(P**2)!=0 and c[8]==P**4
print('Exceptional point counts:',counts)
print('Exceptional L polynomial coefficients:',c)
print('Newton slopes: (1/4)^4, (3/4)^4')
print('VERIFY_OK')
