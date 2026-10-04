#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import product

# ---------- tiny exact multivariate polynomial engine ----------
# Polynomial = dict[exponent_tuple] -> integer coefficient.

def clean(p):
    return {m:c for m,c in p.items() if c}

def add(p,q):
    r=dict(p)
    for m,c in q.items(): r[m]=r.get(m,0)+c
    return clean(r)

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    if not p or not q: return {}
    n=len(next(iter(p)))
    r={}
    for a,ca in p.items():
        for b,cb in q.items():
            m=tuple(a[i]+b[i] for i in range(n))
            r[m]=r.get(m,0)+ca*cb
    return clean(r)

def scale(p,k): return clean({m:k*c for m,c in p.items()})

def ppow(p,e):
    n=len(next(iter(p))) if p else 1
    r={(0,)*n:1}
    x=p
    while e:
        if e&1: r=mul(r,x)
        e//=2
        if e: x=mul(x,x)
    return r

def const(n,k): return {(0,)*n:k} if k else {}
def var(n,i):
    e=[0]*n; e[i]=1
    return {tuple(e):1}

def compose(p, subs):
    # subs[j] is a polynomial in the new variable set replacing old variable j.
    m=len(next(iter(subs[0])))
    out={}
    for exps,c in p.items():
        term=const(m,c)
        for j,e in enumerate(exps):
            if e: term=mul(term,ppow(subs[j],e))
        out=add(out,term)
    return clean(out)

# Build the cleared numerator for the split lower bounds.
# Variables are (A,b,d), N=A+b, P=(N-2)(N-1).
A,b,d = var(3,0), var(3,1), var(3,2)
one=const(3,1); two=const(3,2)
N=add(A,b)
Nm1=add(N,const(3,-1)); Nm2=add(N,const(3,-2))
P=mul(Nm2,Nm1)
D1=mul(A,P)
N1=add(add(mul(N,P),mul(A,Nm2)),scale(mul(A,d),2))
bp1=add(b,one)
D2=mul(mul(mul(d,P),b),bp1)
N2=add(add(mul(mul(mul(N,P),b),bp1), scale(mul(mul(mul(ppow(d,2),b),bp1),one),2)), mul(mul(mul(N,ppow(d,2)),P),one))
CERT=sub(sub(mul(N1,N2),mul(D1,N2)),scale(mul(D2,N1),2))

# Domain reparameterization: A=u+2, d=v+1, b=d+c=v+w+1.
u,v,w = var(3,0), var(3,1), var(3,2)
Au=add(u,const(3,2)); dv=add(v,const(3,1)); bw=add(add(v,w),const(3,1))
Q=compose(CERT,[Au,bw,dv])

# Cover the whole nonnegative quadrant by u>=v or v>=u.
# Case 1: u=v+z; variables become (v,w,z).
v1,w1,z1=var(3,0),var(3,1),var(3,2)
Q1=compose(Q,[add(v1,z1),v1,w1])
# Case 2: v=u+z; variables become (u,w,z).
u2,w2,z2=var(3,0),var(3,1),var(3,2)
Q2=compose(Q,[u2,add(u2,z2),w2])

assert Q1 and Q2
assert min(Q1.values()) > 0, min(Q1.values())
assert min(Q2.values()) > 0, min(Q2.values())

# ---------- exact formulas ----------
def exact_formula(a,c,x):
    # x = multiplicities on non-L0 pure-F2 projective lines, all positive.
    n=a+c+sum(x)+1
    r=len(x); dsum=sum(x)
    assert a>=1 and dsum>=1 and all(t>=1 for t in x)
    E1=Fraction(n,a+1)
    for t in x:
        E1 += Fraction(n,(n-t-1)*(n-t))
    E1 -= Fraction(r-1,n-1)
    E2=Fraction(n,dsum)
    for t in x:
        E2 += Fraction(n,(n-t-1)*(n-t))
        E2 += Fraction(n*t,(n-a-t)*(n-a))
        E2 -= Fraction(1,n-1)
    return E1,E2

def split_lower(a,c,x):
    n=a+c+sum(x)+1; dsum=sum(x); btot=n-a-1
    beta=Fraction(2,(n-2)*(n-1))
    E1=Fraction(n,a+1)+Fraction(1,n-1)+dsum*beta
    E2=Fraction(n,dsum)+dsum*(beta+Fraction(n,btot*(btot+1)))
    return E1,E2

for a0 in range(1,8):
    for c0 in range(0,8):
        for xs in [(1,), (2,), (1,1), (3,1), (2,2), (1,1,1), (4,2,1)]:
            E1,E2=exact_formula(a0,c0,xs)
            L1,L2=split_lower(a0,c0,xs)
            assert E1>=L1 and E2>=L2
            assert Fraction(1,E1)+Fraction(2,E2) <= 1

# ---------- independent finite-field Markov checks ----------
def invmod(x,p): return pow(x%p,-1,p)

def rref(rows,p):
    rows=[list(r) for r in rows if any(x%p for x in r)]
    if not rows: return ()
    m=len(rows); n=len(rows[0]); i=0
    for j in range(n):
        pivot=next((k for k in range(i,m) if rows[k][j]%p),None)
        if pivot is None: continue
        rows[i],rows[pivot]=rows[pivot],rows[i]
        z=invmod(rows[i][j],p)
        rows[i]=[(z*x)%p for x in rows[i]]
        for k in range(m):
            if k!=i and rows[k][j]%p:
                t=rows[k][j]%p
                rows[k]=[(rows[k][ell]-t*rows[i][ell])%p for ell in range(n)]
        i+=1
        if i==m: break
    rows=rows[:i]
    return tuple(tuple(r) for r in rows)

def addvec(S,v,p): return rref(list(S)+[v],p)

def contains(S,v,p): return addvec(S,v,p)==S

def contains_target(S,target_basis,p): return all(contains(S,v,p) for v in target_basis)

def expected(columns,target_basis,p):
    n=len(columns)
    @lru_cache(None)
    def E(S):
        S=tuple(S)
        if contains_target(S,target_basis,p): return Fraction(0)
        counts={}
        for col in columns:
            T=addvec(S,col,p)
            counts[T]=counts.get(T,0)+1
        selfc=counts.pop(S,0)
        rhs=Fraction(1)
        for T,cnt in counts.items(): rhs += Fraction(cnt,n)*E(T)
        return rhs/Fraction(n-selfc,n)
    return E(())

def line_rep2(t,p):
    # Lines in F_p^2: slope t gives (1,t), plus infinity (0,1).
    if t==p: return (0,1)
    return (1,t)

def check_case(p,a,c,x,wline,other_lines):
    w2=line_rep2(wline,p)
    cols=[]
    cols += [(1,0,0)]*a
    cols += [(0,w2[0],w2[1])]*c
    for mult,L in zip(x,other_lines):
        z=line_rep2(L,p)
        cols += [(0,z[0],z[1])]*mult
    cols += [(1,w2[0],w2[1])]
    # rank-three requirement and file target checks
    assert len(rref(cols,p))==3
    e1=(1,0,0); e2=(0,1,0); e3=(0,0,1)
    M1=expected(tuple(cols),(e1,),p)
    M2=expected(tuple(cols),(e2,e3),p)
    F1,F2=exact_formula(a,c,x)
    assert M1==F1,(p,a,c,x,M1,F1)
    assert M2==F2,(p,a,c,x,M2,F2)
    assert Fraction(1,M1)+Fraction(2,M2)<=1

check_case(2,1,1,(1,),0,(2,))
check_case(3,1,1,(1,),0,(3,))
check_case(3,2,1,(2,),0,(3,))
check_case(3,1,0,(1,1),1,(0,3))
check_case(5,2,1,(2,1),0,(1,5))

print('VERIFY_OK')
print('certificate_case_u_ge_v_terms=',len(Q1),'min_coefficient=',min(Q1.values()))
print('certificate_case_v_ge_u_terms=',len(Q2),'min_coefficient=',min(Q2.values()))
print('finite_field_cases=5')
