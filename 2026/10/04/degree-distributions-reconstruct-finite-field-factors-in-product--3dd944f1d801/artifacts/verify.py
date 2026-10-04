from itertools import product, combinations
from collections import Counter
from math import isqrt

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a ^ b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        # F4 = F2[t]/(t^2+t+1), bits encode a0+a1*t.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)

def mats(q,n):
    return list(product(range(q), repeat=n*n))

def trprod(F,A,B,n):
    s=0
    for i in range(n):
        for j in range(n):
            s=F.add(s,F.mul(A[i*n+j],B[j*n+i]))
    return s

def zero(n):
    return (0,)*(n*n)

def exhaustive_kernel_check(q):
    n=2
    F=Field(q)
    M=mats(q,n)
    Z=zero(n)
    for A in M:
        k=sum(trprod(F,A,B,n)==0 for B in M)
        assert k==(q**4 if A==Z else q**3)
    print("kernels",q,"OK")

def complete_graph_q2_22():
    q=2; a=b=2
    F=Field(q)
    MA=mats(q,a); MB=mats(q,b)
    ZA=zero(a); ZB=zero(b)
    V=[(A,B) for A in MA for B in MB if not (A==ZA and B==ZB)]
    adj=[0]*len(V)
    for i,X in enumerate(V):
        A,B=X
        for j in range(i+1,len(V)):
            C,D=V[j]
            if trprod(F,A,C,a)==0 and trprod(F,B,D,b)==0:
                adj[i]+=1; adj[j]+=1
    T=a*a+b*b
    allowed={q**(T-1)-2,q**(T-1)-1,q**(T-2)-2,q**(T-2)-1}
    assert set(adj)==allowed
    support1=sum(1 for A,B in V if (A==ZA) ^ (B==ZB))
    C=Counter(adj)
    assert C[q**(T-1)-2]+C[q**(T-1)-1]==support1
    assert C[q**(T-2)-2]+C[q**(T-2)-1]==len(V)-support1
    print("full_graph_q2_22",C)

def qtrace_zero_count(q,n):
    # Enumerate self-orthogonality only; used to build exact degree multiplicities.
    F=Field(q); M=mats(q,n); Z=zero(n)
    I=0
    for A in M:
        if A!=Z and trprod(F,A,A,n)==0:
            I+=1
    return I

def elementary(vals,s):
    total=0
    for idx in combinations(range(len(vals)),s):
        p=1
        for i in idx: p*=vals[i]
        total+=p
    return total

def degree_distribution(q,sizes):
    k=len(sizes); T=sum(n*n for n in sizes)
    X=[q**(n*n)-1 for n in sizes]
    I=[qtrace_zero_count(q,n) for n in sizes]
    C=Counter()
    for s in range(1,k+1):
        low=0
        total=0
        for S in combinations(range(k),s):
            pI=1; pX=1
            for i in S:
                pI*=I[i]; pX*=X[i]
            low+=pI; total+=pX
        C[q**(T-s)-2]=low
        C[q**(T-s)-1]=total-low
        assert C[q**(T-s)-2]>0 and C[q**(T-s)-1]>0
        assert total==elementary(X,s)
    return q**T-1,C

def kth_root_exact(x,k):
    lo,hi=1,2
    while hi**k < x: hi*=2
    while lo<=hi:
        m=(lo+hi)//2; y=m**k
        if y==x: return m
        if y<x: lo=m+1
        else: hi=m-1
    raise AssertionError(("not kth power",x,k))

def poly_eval(coefs,x):
    y=0
    for c in coefs: y=y*x+c
    return y

def synthetic_div(coefs,x):
    out=[coefs[0]]
    for c in coefs[1:-1]:
        out.append(c+x*out[-1])
    rem=coefs[-1]+x*out[-1]
    assert rem==0
    return out

def reconstruct(v,C):
    D=sorted(C)
    assert len(D)%2==0
    k=len(D)//2
    delta=D[0]
    ratio=(v+1)//(delta+2)
    assert ratio*(delta+2)==v+1
    q=kth_root_exact(ratio,k)

    # Recover T from q^T=v+1.
    T=0; z=1
    while z<v+1:
        z*=q; T+=1
    assert z==v+1

    E=[]
    for s in range(1,k+1):
        d0=q**(T-s)-2
        d1=d0+1
        assert d0 in C and d1 in C
        E.append(C[d0]+C[d1])

    coefs=[1]
    for s,e in enumerate(E,1):
        coefs.append((-1 if s%2 else 1)*e)

    sizes=[]
    P=coefs[:]
    maxn=isqrt(T)
    for n in range(2,maxn+1):
        x=q**(n*n)-1
        while len(P)>1 and poly_eval(P,x)==0:
            P=synthetic_div(P,x)
            sizes.append(n)
    assert P==[1]
    assert len(sizes)==k
    return q,tuple(sorted(sizes))

def run_case(q,sizes):
    v,C=degree_distribution(q,sizes)
    got=reconstruct(v,C)
    want=(q,tuple(sorted(sizes)))
    assert got==want,(got,want)
    print({"q":q,"sizes":sizes,"vertices":v,"degrees":sorted(C),"recovered":got})

for q in (2,3,4,5):
    exhaustive_kernel_check(q)

complete_graph_q2_22()

for case in [
    (2,(2,3)),
    (3,(2,2,3)),
    (4,(2,3,3)),
    (5,(2,2,3,3)),
]:
    run_case(*case)

print("VERIFY_OK")
