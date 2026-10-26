#!/usr/bin/env python3
"""Exact finite checks for cyclically symmetric degree-two del Pezzo models over F2.

The algebraic geometry used to infer the zeta function from point counts
is explained in the accompanying proof. This script needs Python 3 only.
"""
from itertools import product

# Polynomials over F2 represented by integer bit masks.
def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

def pdivmod(a,b):
    assert b
    q=0
    while a and a.bit_length()>=b.bit_length():
        k=a.bit_length()-b.bit_length()
        q^=1<<k;a^=b<<k
    return q,a

def pgcd(a,b):
    while b: a,b=b,pdivmod(a,b)[1]
    return a

def pdiff(a):
    out=0
    for k in range(1,a.bit_length(),2):
        if (a>>k)&1:out|=1<<(k-1)
    return out

def ppow(a,n):
    r=1
    while n:
        if n&1:r=pmul(r,a)
        a=pmul(a,a);n>>=1
    return r

# The cyclic orbit sums of degree-four ternary monomials (A,B,C,D,E).
MONOMIALS=[[(4,0,0),(0,4,0),(0,0,4)],
 [(3,1,0),(0,3,1),(1,0,3)],
 [(3,0,1),(1,3,0),(0,1,3)],
 [(2,2,0),(0,2,2),(2,0,2)],
 [(2,1,1),(1,2,1),(1,1,2)]]

def monomials(mask):
    exps=[]
    for k,orbit in enumerate(MONOMIALS):
        if mask & (1<<k):exps += orbit
    return exps

def poly_evaluate(exps, xx,yy,zz, mult):
    val=0
    for a,b,c in exps:
        term=1
        for v,p in ((xx,a),(yy,b),(zz,c)):
            for _ in range(p):term=mult[term][v]
        val^=term
    return val

def restricted_poly(exps, which=None):
    # On the smooth branch conic q=0, u=1,v=t:
    # (x,y,z)=(1+t,t+t^2,t).
    X,Y,Z=0b11,0b110,0b10
    out=0
    for a,b,c in exps:
        if which is not None:
            power=(a,b,c)[which]
            if (power&1)==0:continue
            aa,bb,cc=([a,b,c][:3])
            if which==0:aa-=1
            if which==1:bb-=1
            if which==2:cc-=1
        else:aa,bb,cc=a,b,c
        out ^= pmul(pmul(ppow(X,aa),ppow(Y,bb)),ppow(Z,cc))
    return out

def smooth(mask):
    # Translation w -> w+(x+y+z)^2 adds A+B+C+E (bitmask 23).
    if mask&1: mask^=23
    assert not mask&1
    exps=monomials(mask)
    # Both chart endpoints [1:0:0] and [0:1:0] are singular
    # exactly if B=C=0 for normalized quartics.
    if not (mask&6):return False
    p=restricted_poly(exps)
    fx=restricted_poly(exps,0)
    # t != 0 singular points iff p'(t)=0 and
    # fx(t)^2+t^4*p(t)=0.  A polynomial has no nonzero
    # algebraic root iff it is a power of t or a constant.
    g=pgcd(pdiff(p), pmul(fx,fx) ^ (p<<4))
    return g and (g&(g-1))==0

EXPECTED_SMOOTH={2,4,6,10,12,14,17,19,21,25,27,29}
assert {m for m in range(32) if smooth(m)}==EXPECTED_SMOOTH
# The translation formula and the C3 orbit decomposition are identities.
A,B,C,D,E = [monomials(1<<i) for i in range(5)]
assert len(set(tuple(t) for arr in MONOMIALS for t in arr))==15
# On all homogeneous quartic polynomials over F2, q*r+r^2=A+B+C+E.
from collections import Counter
qterms=[(1,1,0),(1,0,1),(0,1,1)]
rterms=[(2,0,0),(0,2,0),(0,0,2)]
identity=Counter()
for a,b in product(qterms,rterms):identity[tuple(a[i]+b[i] for i in range(3))]+=1
for t in [(4,0,0),(0,4,0),(0,0,4)]:identity[t]+=1
for t in monomials(23):identity[t]+=1
assert all(v%2==0 for v in identity.values())

IRR={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,
     6:0b1000011,7:0b10001001,8:0b100011101}

def gf_mul(a,b,n,poly):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&(1<<n):a^=poly
    return r

def point_traces(n):
    N=1<<n;M=[[gf_mul(i,j,n,IRR[n]) for j in range(N)] for i in range(N)]
    # Verify that each nonzero element is invertible; ensures correct field.
    inv=[0]*N
    for a in range(1,N):
        inv[a]=next((j for j in range(1,N) if M[a][j]==1),0)
        assert inv[a]!=0
    sq=[M[a][a] for a in range(N)]
    trace=[]
    for a in range(N):
        x=a;t=a
        for _ in range(n-1):x=sq[x];t^=x
        assert t in(0,1)
        trace.append(t)
    reps=[2,4,6,10,12,14]
    counts={mask:0 for mask in reps}
    polys={mask:monomials(mask) for mask in reps}
    def handle(x,y,z):
        q=M[x][y]^M[y][z]^M[z][x]
        if q==0:
            for mask in reps:counts[mask]+=1
        else:
            fac=sq[inv[q]]
            for mask in reps:
                f=poly_evaluate(polys[mask],x,y,z,M)
                counts[mask] += (0 if trace[M[f][fac]] else 2)
    for y in range(N):
        for z in range(N):handle(1,y,z)
    for z in range(N):handle(0,1,z)
    handle(0,0,1)
    # Independent direct 0,1,2-solution calculation in the smallest fields.
    if n<=3:
        counts_direct={mask:0 for mask in reps}
        def direct(x,y,z):
            q=M[x][y]^M[y][z]^M[z][x]
            for mask in reps:
                f=poly_evaluate(polys[mask],x,y,z,M)
                counts_direct[mask]+=sum(sq[w]^M[q][w]^f==0 for w in range(N))
        for y in range(N):
            for z in range(N):direct(1,y,z)
        for z in range(N):direct(0,1,z)
        direct(0,0,1)
        assert counts_direct==counts
    return {mask: (counts[mask]-1-N*N)//N for mask in reps}, counts

def charpoly(traces):
    coeff=[1]
    for k in range(1,9):
        numer=-sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
        assert numer%k==0
        coeff.append(numer//k)
    return coeff

alltr={m:[] for m in [2,4,6,10,12,14]}
for n in range(1,9):
    tr,counts=point_traces(n)
    for m,t in tr.items():alltr[m].append(t)
    print('n=',n,'traces=',tr)

# Coefficients in descending powers.  These are expanded products:
# B,C:           (T-1)(T+1)(T^2-T+1)(T^2+T+1)^2
# B+C:           (T-1)^4(T+1)^2(T^2-T+1)
# B+D,C+D:       (T-1)^2(T^2-T+1)^2(T^2+T+1)
# B+C+D:         (T-1)^3(T+1)^3(T^2+T+1)
def imul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def ipow(a,n):
    r=[1]
    for _ in range(n):r=imul(r,a)
    return r
T1=[1,-1];Tminus=[1,1];phi3=[1,1,1];phi6=[1,-1,1]
expected={
 2:imul(imul(T1,Tminus),imul(phi6,ipow(phi3,2))),
 4:imul(imul(T1,Tminus),imul(phi6,ipow(phi3,2))),
 6:imul(imul(ipow(T1,4),ipow(Tminus,2)),phi6),
 10:imul(imul(ipow(T1,2),ipow(phi6,2)),phi3),
 12:imul(imul(ipow(T1,2),ipow(phi6,2)),phi3),
 14:imul(imul(ipow(T1,3),ipow(Tminus,3)),phi3),
}
for m,tr in alltr.items():
    assert charpoly(tr)==expected[m]
    print('mask=',m,'traces=',tr,'charpoly coeffs=',expected[m])
assert len({tuple(expected[m]) for m in expected})==4
# Swapping two coordinates interchanges the two Klein orbit forms B,C.
assert sorted(tuple(a[0] if k==0 else a[2] if k==1 else a[1] for k in range(3)) for a in B)==sorted(C)
print('VERIFY_OK: 32 cyclic models, 12 smooth, 4 zeta types; fields degrees 1..8 and low-degree direct lifts')
