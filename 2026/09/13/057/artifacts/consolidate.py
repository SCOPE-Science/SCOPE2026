#!/usr/bin/env python3
"""Bounded consolidation test: Ore-factor neighbours + cubic-order branching.
Part A: cubic order O = A + l*OK branching (commutative algebra over F4).
Part B: L=GF4 rational l-neighbours via Ore right-division (no splitting field).
"""
import json
print("start", flush=True)
# GF4
mod4 = 7
def m4(a,b):
    p=0
    while b:
        if b&1: p^=a
        a<<=1
        if a>>2: a^=mod4
        b>>=1
    while p.bit_length()>2: p^=mod4<<(p.bit_length()-3)
    return p&3
def a4(a,b): return a^b
def p4(a,e):
    r=1
    while e:
        if e&1: r=m4(r,a)
        a=m4(a,a); e>>=1
    return r
def i4(a): return p4(a,2)
def f4(a): return m4(a,a)
# Part A: O = F2+? model: OK/lOK = F4^3, O/lOK = diagonal(F2)? Count intermediate rings.
# Minimal overorders of O=A+lOK <-> subalgebras of V=F4^3 containing diagonal F2*1?
# Brute force: V has 64 elems (i,j,k in 0..3). Obar = {(a,a,a): a in {0,1}} (size 2).
# Intermediate subrings W with Obar < W < V, W an F2-subalgebra (closed +,*), W an A/l-module?
# Minimal overorders <-> maximal proper subalgebras? Actually index-l overorders <-> dim?
# [OK:O]=? OK/lOK dim over F2 = 6, O/lOK dim=1, quotient dim 5. Overorders O' with [O':O]=4 (l has deg2, N(l)=4)?
# l=T^2+T+1 has residue degree 2, N=4. Index [O':O] = N(l)=4 <-> dim jump by 2.
# Enumerate F2-subspaces W of V containing Obar with dim 3 (2 extra dims) that are subrings.
import itertools
V=[(i,j,k) for i in range(4) for j in range(4) for k in range(4)]
def add(u,v): return (u[0]^v[0],u[1]^v[1],u[2]^v[2])
def mul(u,v): return (m4(u[0],v[0]),m4(u[1],v[1]),m4(u[2],v[2]))
one=(1,1,1); e0=(1,0,0); e1=(0,1,0); e2=(0,0,1)
obar=[(0,0,0),(1,1,1)]
def span(basis):
    s={(0,0,0)}
    for b in basis:
        s=s|{add(x,b) for x in s}|{add(x,add(b,b)) for x in s}
    # proper closure
    changed=True
    while changed:
        changed=False
        for b in basis:
            for x in list(s):
                for y in [b,add(b,b)]:
                    z=add(x,y)
                    if z not in s: s.add(z); changed=True
    return s
# candidate W = span(obar + two extra vecs), test subring
seen=set(); rings=[]
cands=[v for v in V if v not in obar]
for a in cands:
    for b in cands:
        if b==a or b==add(a,a): continue
        W=span([one,a,b])
        if len(W)!=8: continue
        # subring?
        ok=True
        for x in W:
            for y in W:
                if mul(x,y) not in W: ok=False; break
            if not ok: break
        if not ok: continue
        key=tuple(sorted(W))
        if key not in seen:
            seen.add(key); rings.append(W)
print(f"PART_A: index-N(l) intermediate subrings (candidate minimal overorders): {len(rings)}", flush=True)
for W in rings[:6]:
    print("  ring:", sorted(W), flush=True)
# Part B: Ore neighbours over GF4
class GF:
    def __init__(s,n,md): s.n=n;s.mod=md;s.N=1<<n
    def add(s,a,b): return a^b
    def mul(s,a,b):
        p=0;aa=a;bb=b
        while bb:
            if bb&1: p^=aa
            aa<<=1
            while aa.bit_length()>s.n: aa^=s.mod<<(aa.bit_length()-s.n-1)
            bb>>=1
        while p.bit_length()>s.n: p^=s.mod<<(p.bit_length()-s.n-1)
        return p&(s.N-1)
    def sq(s,a): return s.mul(a,a)
    def pw(s,a,e):
        r=1
        while e:
            if e&1: r=s.mul(r,a)
            a=s.mul(a,a);e>>=1
        return r
    def inv(s,a): return s.pw(a,s.N-2)
F=GF(2,7)
def omul(A,B):
    R=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        if a:
            for j,b in enumerate(B):
                # a * frob^i(b)
                fb=b
                for _ in range(i): fb=F.sq(fb)
                R[i+j]^=F.mul(a,fb)
    while len(R)>1 and R[-1]==0: R.pop()
    return R
def oadd(A,B):
    n=max(len(A),len(B)); return [(A[i] if i<len(A) else 0)^(B[i] if i<len(B) else 0) for i in range(n)]
def rmod(A,B):
    A=list(A); db=len(B)-1
    while len(A)>db+1 or (len(A)==db+1 and not (len(A)==1 and A[0]==0)):
        da=len(A)-1
        if da<db: break
        if A[da]==0: A.pop(); continue
        c=A[da]  # B monic
        k=da-db
        for j in range(db+1): A[k+j]^=F.mul(c,F.sq(B[j]) if k==1 else (B[j] if k==0 else __frob(B[j],k)))
        while len(A)>1 and A[-1]==0: A.pop()
        if len(A)==1 and A[0]==0: break
    return A
def __frob(b,k):
    for _ in range(k): b=F.sq(b)
    return b
def odiv(A,B):
    return rmod(A,B)==[0] or rmod(A,B)==[0]*len(rmod(A,B))
def velu(T,D):
    dd=len(D)-1; LHS=omul(D,T)
    # unknowns b1..b3 (b0=T0)
    import copy
    rows=[];rhs=[]
    for k in range(dd+4):
        row=[0]*3; val=LHS[k] if k<len(LHS) else 0
        for j in range(1,4):
            i=k-j; d=D[i] if 0<=i<=dd else 0
            row[j-1]^=__frob(d,j)
        # subtract b0*D_k term (j=0): b0*D[k]
        sub=F.mul(T[0],D[k] if k<=dd else 0)
        rows.append(row); rhs.append(val^sub)
    # drop k=0 eq (0=0 since D monic? keep all, solve 3 unknowns, overdetermined; use first 3 indep rows via brute force)
    # brute force over 4^3=64 possibilities
    for b1 in range(4):
        for b2 in range(4):
            for b3 in range(4):
                ok=True
                for k in range(dd+4):
                    v=F.add(F.add(F.mul(b1,rows[k][0]),F.mul(b2,rows[k][1])),F.mul(b3,rows[k][2])) if False else 0
                    # rows entries are already frob'd D coeffs; term = b_j * frob^j(D)
                    v=F.mul(rows[k][0],b1)^F.mul(rows[k][1],b2)^F.mul(rows[k][2],b3)
                    # careful: multiplication commutes in GF4, ok
                    # but equation is sum b_j * frob^j(D) with b_j on LEFT: F.mul(b_j, frob) same (commutative)
                    if v!=rhs[k]: ok=False; break
                if ok:
                    P=[T[0],b1,b2,b3]
                    assert omul(D,T)==omul(P,D)
                    return P
    return None
def jis(T):
    g1,g2,g3=T[1],T[2],T[3]
    j1=F.div(g1,F.pw(g1,0)) if False else (F.mul(F.pw(g1,3),F.pw(g1,3))//1 if False else None)
    j1=F.mul(F.pw(g1,7),F.inv(g3)) if g1 else 0
    j2=F.mul(F.pw(g2,7),F.inv(F.pw(g3,3))) if g2 else 0
    return (j1,j2)
# enumerate phi, l=T^2+T+1 -> phi_l = phiT^2+phiT+1
best=None; total=0; nrat_dist=[]
for g1 in range(4):
    for g2 in range(4):
        for g3 in [1,2,3]:
            T=[0,g1,g2,g3]
            T2=omul(T,T); Ll=oadd(oadd(T2,T),[1])
            n=0; qs=[]
            for d1 in range(4):
                for d0 in [1,2,3]:
                    D=[d0,d1,1]
                    if all(v==0 for v in rmod(Ll,D)):
                        n+=1
                        P=velu(T,D)
                        qs.append(((d1,d0),P,jis(P) if P else None))
            total+=1
            nrat_dist.append(n)
            if n>=2 and best is None:
                best={'T':T,'n':n,'qs':qs,'j':jis(T)}
print(f"PART_B: enumerated {total} modules; neighbour-count distribution: {sorted(set(nrat_dist))}", flush=True)
import collections
print(collections.Counter(nrat_dist), flush=True)
if best: print("example vertex:", best, flush=True)
with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1714/output/artifacts/consolidation.json','w') as f:
    json.dump({'n_overorders':len(rings),'rings_sample':[sorted(W) for W in rings[:4]],'neigh_dist':dict(collections.Counter(nrat_dist)),'example':best},f,indent=1)
print("done", flush=True)
