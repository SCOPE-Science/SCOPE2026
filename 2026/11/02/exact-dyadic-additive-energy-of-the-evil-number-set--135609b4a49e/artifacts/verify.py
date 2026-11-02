#!/usr/bin/env python3
"""Exact arithmetic reproduction of the evil-set additive-energy theorem (stdlib only)."""
from itertools import product
from fractions import Fraction

def mat(mask):
    M=[[0]*4 for _ in range(4)]
    for u,v in product((0,1),repeat=2):
        for bits in product((0,1),repeat=4):
            a,b,c,d=bits
            h=a+b+u; k=c+d+v
            if (h-k)%2: continue
            M[2*u+v][2*(h//2)+k//2] += (-1)**sum(x*y for x,y in zip(mask,bits))
    return M

def mm(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def add(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]

def scale(A,s):
    return [[s*x for x in a] for a in A]

def ident(n=4):return [[int(i==j) for j in range(n)] for i in range(n)]

def power(A,n):
    P=ident(len(A))
    for _ in range(n):P=mm(P,A)
    return P

def F(A,n):
    B=power(A,n); return B[0][0]+B[0][3]

def conv_energy(r):
    N=1<<r
    S=[i for i in range(N) if i.bit_count()%2==0]
    counts=[0]*(2*N-1)
    for a in S:
        for b in S:counts[a+b]+=1
    return sum(v*v for v in counts)

def GF_coeffs(n,den,num):
    """den[0] must equal one; coefficient solver over integers."""
    out=[]
    for k in range(n):
        v=(num[k] if k<len(num) else 0)
        for j in range(1,min(k+1,len(den))):v-=den[j]*out[k-j]
        out.append(v)
    return out

representatives={
    (0,0,0,0):(1,[1,-10,16],[1,-4]),
    (0,0,0,1):(4,[1],[1,0,-4]),
    (0,0,1,1):(2,[1,2],[1]),
    (0,1,0,1):(4,[1,-2],[1]),
    (0,1,1,1):(4,[1,0,-8],[1,0,-4]),
    (1,1,1,1):(1,[1,-2,-16],[1,4]),
}
# The 0000 denominator is (1-2z)(1-8z) = 1-10z+16z^2.
all_matrices={mask:mat(mask) for mask in product((0,1),repeat=4)}
for mask,(mult,den,num) in representatives.items():
    M=all_matrices[mask]
    # Check the first sixteen exact terms of the rational resolvent.
    # The all-orders identity follows mathematically from the resolvent
    # and can be checked by a symbolic four-by-four adjugate expansion.
    vals=[F(M,n) for n in range(16)]
    expected=GF_coeffs(16,den,num)
    assert vals==expected,(mask,vals,expected)
    # Check matrix annihilation q(M) for q(lambda)=lambda^d den(1/lambda)
    # when the denominator degree is <4, scalar recurrence after first d.
    degree=len(den)-1
    assert all(sum(den[j]*vals[n-j] for j in range(degree+1))==
        (num[n] if n<len(num) else 0) for n in range(degree,16))
# Check orbit-by-orbit equality for all 16 masks using 12 coefficients.
groups={}
for mask,M in all_matrices.items():
    key=tuple(F(M,r) for r in range(12))
    groups[key]=groups.get(key,0)+1
assert sorted(groups.values())==[1,1,2,4,4,4],groups

def derived(r):
    g=(1 if r==0 else 6)
    if r>1:
        a,b=1,6
        for _ in range(2,r+1):a,b=b,2*b+16*a
        g=b
    u=(2*8**r+2**r)//3
    small=1 if r==0 else (-4 if r==2 else 0)
    triple=1 if r==0 else ((8**(r//2))//2 if r%2==0 else 0)
    numerator=u+4*small+2*(-2)**r+4*2**r+4*triple+g
    assert numerator%16==0
    return numerator//16

# Independent state machine checks all sixteen exact sign masks, without
# relying on the orbit table.
for r in range(17):
    independent=sum(F(M,r) for M in all_matrices.values())
    assert independent%16==0
    assert independent//16==derived(r),(r,independent,derived(r))
# Independent integer-sum convolution does not use any carry state.
for r in range(11):
    assert conv_energy(r)==derived(r),(r,conv_energy(r),derived(r))
print('VERIFY_OK: 16 signed matrices; 6 exact generating functions; 17 dyadic levels; 11 direct integer-sum energy enumerations')
