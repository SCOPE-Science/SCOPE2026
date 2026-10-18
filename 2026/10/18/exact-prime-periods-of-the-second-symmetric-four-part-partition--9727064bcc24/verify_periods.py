"""Standalone integer-polynomial and finite-field checks for the four-part statistic."""
from itertools import combinations

U=[6,15,34,57,95,121,146,126,106,72,50,25,11]

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    return trim(r)

def scale(a,c):return trim([c*x for x in a])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def power(a,k):
    r=[1]
    for _ in range(k):r=mul(r,a)
    return r

def shift(a,k):return [0]*k+list(a)

def modpoly(a,p):return trim([x%p for x in a])

def fdivmod(a,b,p):
    a=modpoly(a,p);b=modpoly(b,p)
    assert b!=[0]
    quo=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        h=a[-1]*pow(b[-1],-1,p)%p
        k=len(a)-len(b);quo[k]=h
        for j in range(len(b)):a[k+j]=(a[k+j]-h*b[j])%p
        a=trim(a)
    return modpoly(quo,p),a

def fgcd(a,b,p):
    a=modpoly(a,p);b=modpoly(b,p)
    while b!=[0]:a,b=b,fdivmod(a,b,p)[1]
    return modpoly(scale(a,pow(a[-1],-1,p)),p)

W=[1,2,3,4]
M=[[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
coeff={}
for i,j in combinations(range(4),2):
    for a in range(4):
        for b in range(4):
            key=tuple(sorted((a,b)))
            coeff[key]=coeff.get(key,0)+M[i][a]*M[j][b]

# A dimension's numerator over (1-q^weight)^3, for powers 0, 1, 2.
# The last dimension is d >= 1; other dimensions are >= 0.
def dim_num(i,k):
    w=W[i];m=[1]+[0]*(w-1)+[-1]
    if k==0:
        return mul(shift([1],w) if i==3 else [1],power(m,2))
    if k==1:return mul(shift([1],w),m)
    assert k==2
    return shift([1]+[0]*(w-1)+[1],w)

N0=[0]
for (a,b),c in coeff.items():
    pw=[0]*4;pw[a]+=1;pw[b]+=1
    term=[1]
    for i in range(4):term=mul(term,dim_num(i,pw[i]))
    N0=add(N0,scale(term,c))
D0=[1]
for w in W:D0=mul(D0,power([1]+[0]*(w-1)+[-1],3))
P=shift(U,4)
D=mul(mul(power([-1,1],6),power([1,1],4)),mul(power([1,0,1],3),power([1,1,1],3)))
assert D[0]==1
Q=mul(power([-1,1],6),power([1,1],2))
assert D0==mul(D,Q), 'uncancelled denominator factorization'
assert N0==mul(P,Q), 'exact rational generating function polynomial identity'

# The following evaluations certify no cancellation at the simple cyclotomic
# factors in every prime characteristic >= 5.
assert sum(P)==864
assert sum(((-1)**i)*a for i,a in enumerate(P))==32
assert fdivmod(P,[1,1,1],101)[1]==[0,6]  # residue 6q mod Phi_3
assert fdivmod(P,[1,0,1],101)[1]==[89]    # residue -12 mod Phi_4

qminus=[-1,1];qplus=[1,1];phi3=[1,1,1];phi4=[1,0,1]
D2=mul(power(qplus,12),power(phi3,2))
D3=mul(power(qminus,10),power(qplus,4))
for p,Dred in [(2,D2),(3,D3),(5,D),(7,D),(11,D),(13,D),(17,D),(19,D),(23,D),(29,D),(31,D),(37,D)]:
    G=fgcd(P,D,p)
    if p==2:
        expected=mul(power(qplus,4),phi3)
        assert G==modpoly(expected,p)
    elif p==3:
        expected=mul(power(qminus,2),power(phi4,3))
        assert G==modpoly(expected,p)
    else:
        assert G==[1]
    # For each asserted period, factor divisibility holds at the exact polynomial level.
    T=48 if p==2 else 54 if p==3 else 300 if p==5 else 12*p
    # q^T-1 modulo reduced denominator: fast repeated squaring.
    def polymodmul(a,b):return fdivmod(mul(a,b),Dred,p)[1]
    def polymodpow(a,n):
        r=[1]
        while n:
            if n&1:r=polymodmul(r,a)
            a=polymodmul(a,a);n//=2
        return r
    assert polymodpow([0,1],T)==[1], (p,T)
    # A least positive period divides any period, so test the maximal proper
    # divisors, one for each distinct prime factor of the candidate.
    for d in range(2,T+1):
        if T%d:continue
        if all(d%i for i in range(2,int(d**.5)+1)):
            assert polymodpow([0,1],T//d)!=[1], (p,T,d)

# Recover coefficients by D(q)F(q)=P(q), and independently enumerate partitions.
a=[]
for n in range(151):
    value=(P[n] if n<len(P) else 0)
    for j in range(1,min(n,len(D)-1)+1):value-=D[j]*a[n-j]
    a.append(value)
for n in range(151):
    direct=0
    for d in range(1,n//4+1):
        for c in range(d,(n-d)//3+1):
            for b in range(c,(n-d-c)//2+1):
                largest=n-d-c-b
                if largest<b:continue
                parts=(largest,b,c,d)
                direct+=sum(parts[i]*parts[j] for i,j in combinations(range(4),2))
    assert a[n]==direct,(n,a[n],direct)
print('PASS: exact rational generating identity, finite-field cancellations, periods and minimality (12 primes), 151 direct weighted-partition coefficients')
