#!/usr/bin/env python3
"""Point-count certificate over F_(7^n), n<=4, independent of Cartier matrices."""
from itertools import product
P=7
MOD={1:(0,1), 2:(1,0,1), 3:(1,0,1,1), 4:(1,0,0,1,1)}

def irreducible(f):
    n=len(f)-1
    # An F_7 polynomial of degree <=4 is irreducible iff it has no
    # monic divisor of degree 1 or 2.
    def modf(A,B):
        A=list(A)
        while len(A)>=len(B):
            c=A[-1]*pow(B[-1],-1,P)%P
            offset=len(A)-len(B)
            for i,b in enumerate(B):A[offset+i]=(A[offset+i]-c*b)%P
            while A and A[-1]==0:A.pop()
        return A
    for d in range(1,n//2+1):
        for coeff in product(range(P),repeat=d):
            if not modf(f,tuple(coeff)+(1,)):
                return False
    return True

for n in range(2,5):
    assert irreducible(MOD[n]), (n,MOD[n])

def field(n):
    mod=MOD[n]; q=P**n
    digits=[]
    for a in range(q):
        z=a; d=[]
        for _ in range(n):d.append(z%P);z//=P
        digits.append(tuple(d))
    def pack(a):return sum((z%P)*(P**i) for i,z in enumerate(a))
    def add(a,b):return pack([(digits[a][i]+digits[b][i])%P for i in range(n)])
    def mul(a,b):
        f=digits[a];g=digits[b]; h=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):h[i+j]=(h[i+j]+f[i]*g[j])%P
        for i in range(2*n-2,n-1,-1):
            t=h[i]
            for j in range(n):h[i-n+j]=(h[i-n+j]-t*mod[j])%P
        return pack(h[:n])
    def powf(a,n):
        r=1
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n>>=1
        return r
    return q,add,mul,powf

def count(q,add,mul,powf,a):
    cube_frequency=[0]*q
    for y in range(q):cube_frequency[mul(mul(y,y),y)]+=1
    N=1
    for x in range(q):
        x2=mul(x,x)
        x5=mul(mul(x2,x2),x)
        N+=cube_frequency[add(add(x5,mul(a,x2)),1)]
    return N

counts={a:[] for a in range(P) if a != P-1}
for n in range(1,5):
    q,add,mul,powf=field(n)
    # Irreducibility of the chosen field moduli is exhaustively tested above.
    for a in counts:
        counts[a].append(count(q,add,mul,powf,a))

for a,Ns in sorted(counts.items()):
    s=[0]+[(P**n+1-Ns[n-1]) for n in range(1,5)]
    c=[1]
    for k in range(1,5):
        c.append((-sum(c[k-i]*s[i] for i in range(1,k+1))*pow(k,-1,P))%P)
    rank=max((i for i in range(5) if c[i]%P),default=0)
    expected=0 if a==0 else (1 if a==1 else 2)
    assert rank==expected, (a,rank,expected,Ns,c)
    assert all(ci%P==0 for ci in c[rank+1:]), (a,c)
    print(f'a={a} counts={Ns} zeta_mod7_first5={c} rank={rank}')
print('INDEPENDENT_POINT_COUNTS_OK')
