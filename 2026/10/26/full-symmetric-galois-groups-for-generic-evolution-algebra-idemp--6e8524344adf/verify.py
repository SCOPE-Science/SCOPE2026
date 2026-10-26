"""Exact modular checks for a sparse evolution-algebra Galois example.
Python >=3.9; no third-party packages.
"""

def trim(f):
    f=list(f)
    while len(f)>1 and f[-1]==0: f.pop()
    return f

def divmodp(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b]); assert b!=[0]
    q=[0]*max(1,(len(a)-len(b)+1))
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b); v=a[-1]*pow(b[-1],-1,p)%p; q[k]=v
        for j,co in enumerate(b): a[k+j]=(a[k+j]-v*co)%p
        a=trim(a)
    return trim(q),a

def gcdp(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while b!=[0]:a,b=b,divmodp(a,b,p)[1]
    return trim([x*pow(a[-1],-1,p)%p for x in a])

def mulp(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]=(c[i+j]+u*v)%p
    return trim(c)

def powmodp(a,k,f,p):
    r=[1]
    while k:
        if k&1:r=divmodp(mulp(r,a,p),f,p)[1]
        a=divmodp(mulp(a,a,p),f,p)[1];k//=2
    return r

def subp(a,b,p):
    return trim([((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])

def irreducible_small(f,p):
    d=len(f)-1; x=[0,1]
    for k in range(1,d//2+1):
        if gcdp(f,subp(powmodp(x,p**k,f,p),x,p),p)!=[1]:return False
    return powmodp(x,p**d,f,p)==x

# The degree-7 specialization a=3 has factorization types 7 and 2+5.
f=[-1,0,0,3,0,0,0,1]
assert irreducible_small(f,2)
a=[3,1,1]; b=[2,-3,-2,-2,-1,1]
assert mulp(a,b,7)==trim([v%7 for v in f])
assert irreducible_small(a,7) and irreducible_small(b,7)
# Unramified reductions: squarefreeness follows from irreducible factors.
# Check coprime derivative for each reduction without dropping the zero term.
for p in (2,7):
    der=[i*f[i] for i in range(1,len(f))]
    assert gcdp(f,der,p)==[1]
# For n>=2, gcd(2^n-1,2^(n-1)-1)=1;
# critical values of t^(-M)-t^(N-M) are pairwise distinct.
import math
for n in range(2,25):
    N=2**n-1; M=2**(n-1)-1
    assert N==2*M+1 and math.gcd(N,M)==1
print('VERIFY_OK: n=3 finite-field cycle certificates; all tested critical-value gcd identities')
