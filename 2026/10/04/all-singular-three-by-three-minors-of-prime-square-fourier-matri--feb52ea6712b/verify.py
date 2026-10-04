#!/usr/bin/env python3
from itertools import combinations, permutations

def rvec(e,p):
    N=p*p; d=p*(p-1); e%=N
    v=[0]*d
    if e<d:
        v[e]=1
    else:
        # e=d+j, 0<=j<p. X^(p(p-1)+j) = -sum_{q=0}^{p-2} X^(qp+j)
        j=e-d
        for q in range(p-1):
            v[q*p+j]-=1
    return tuple(v)

def add_scaled(acc,v,s):
    for i,x in enumerate(v):
        acc[i]+=s*x

def det_zero(R,C,p,rv):
    acc=[0]*len(rv[0])
    perms=((0,1,2,1),(0,2,1,-1),(1,0,2,-1),(1,2,0,1),(2,0,1,1),(2,1,0,-1))
    N=p*p
    for a,b,c,s in perms:
        e=(R[0]*C[a]+R[1]*C[b]+R[2]*C[c])%N
        add_scaled(acc,rv[e],s)
    return all(x==0 for x in acc)

def rank_exact(R,C,p,rv):
    if not det_zero(R,C,p,rv): return 3
    N=p*p
    for i,j in combinations(range(3),2):
        for a,b in combinations(range(3),2):
            if (R[i]*C[a]+R[j]*C[b]-R[i]*C[b]-R[j]*C[a])%N:
                return 2
    return 1

def typ(S,p):
    occ={}
    for x in S: occ[x%p]=occ.get(x%p,0)+1
    vals=sorted(occ.values(),reverse=True)
    return 'A' if vals==[1,1,1] else ('B' if vals==[2,1] else 'C')

def pred(rt,ct):
    if rt=='C' and ct=='C': return 1
    if (rt=='C' and ct=='B') or (rt=='B' and ct=='C'): return 2
    return 3

def check(p):
    N=p*p; rv=[rvec(e,p) for e in range(N)]
    norm=[(0,a,b) for a in range(1,N) for b in range(a+1,N)]
    pairs=0
    for R in norm:
        rt=typ(R,p)
        for C in norm:
            got=rank_exact(R,C,p,rv); want=pred(rt,typ(C,p)); pairs+=1
            if got!=want:
                raise AssertionError((p,R,C,rt,typ(C,p),got,want))
    allS=list(combinations(range(N),3))
    B=sum(typ(S,p)=='B' for S in allS); Cn=sum(typ(S,p)=='C' for S in allS)
    Bf=p**3*(p-1)**2//2; Cf=p**2*(p-1)*(p-2)//6
    assert (B,Cn)==(Bf,Cf),(p,B,Cn,Bf,Cf)
    sing=2*B*Cn+Cn*Cn
    formula=p**4*(p-1)**2*(p-2)*(6*p*p-5*p-2)//36
    assert sing==formula
    return len(norm),pairs,B,Cn,sing

parts=[]
for p in (3,5):
    n,pairs,B,C,s=check(p); parts.append(f"p={p} normalized_sets={n} normalized_pairs={pairs} B={B} C={C} singular_count={s}")
print("; ".join(parts))
print("VERIFY_OK")
