from itertools import combinations, permutations, product
from math import factorial


def supports(r):
    return [m for m in range(1, (1<<r)-1)]

def incomparable(a,b):
    return (a & ~b) != 0 and (b & ~a) != 0

def h_graph(r):
    V=supports(r); idx={m:i for i,m in enumerate(V)}
    A=[[False]*len(V) for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            b=V[j]; A[i][j]=A[j][i]=incomparable(a,b)
    return V,A

def count_aut(A):
    n=len(A); deg=[sum(row) for row in A]
    cand=[[j for j in range(n) if deg[j]==deg[i]] for i in range(n)]
    order=sorted(range(n), key=lambda i:(len(cand[i]),-deg[i]))
    used=[False]*n; mp=[-1]*n; total=0
    def rec(k):
        nonlocal total
        if k==n:
            total+=1; return
        i=order[k]
        for j in cand[i]:
            if used[j]: continue
            ok=True
            for t in range(k):
                u=order[t]; v=mp[u]
                if A[i][u]!=A[j][v]: ok=False; break
            if ok:
                mp[i]=j; used[j]=True; rec(k+1); used[j]=False; mp[i]=-1
    rec(0); return total

def expanded(qs):
    r=len(qs); V=[]
    for S in supports(r):
        w=1
        for i,q in enumerate(qs):
            if S>>i & 1: w*=q-1
        for k in range(w): V.append((S,k))
    n=len(V); A=[[False]*n for _ in V]
    for i,(S,_) in enumerate(V):
        for j in range(i+1,n):
            T=V[j][0]; A[i][j]=A[j][i]=incomparable(S,T)
    return V,A

def false_twin_classes(A):
    d={}
    for i,row in enumerate(A):
        key=tuple(j for j,x in enumerate(row) if x)
        d.setdefault(key,[]).append(i)
    return sorted((tuple(v) for v in d.values()), key=lambda x:(len(x),x))

def predicted_order(qs):
    r=len(qs); a=[q-1 for q in qs]
    internal=1
    for S in supports(r):
        w=1
        for i,x in enumerate(a):
            if S>>i&1:w*=x
        internal*=factorial(w)
    # quotient weighted symmetries
    from collections import Counter
    c=Counter(a); perm=1
    for v in c.values(): perm*=factorial(v)
    if r==2:
        # H_2 only swaps the two cells when weights equal
        B=2 if a[0]==a[1] else 1
    else:
        B=perm*(2 if all(x==1 for x in a) else 1)
    return internal*B

def graph_iso(A,B):
    if len(A)!=len(B): return False
    n=len(A); da=[sum(x) for x in A]; db=[sum(x) for x in B]
    if sorted(da)!=sorted(db): return False
    cand=[[j for j in range(n) if db[j]==da[i]] for i in range(n)]
    order=sorted(range(n), key=lambda i:(len(cand[i]),-da[i]))
    used=[False]*n; mp=[-1]*n
    def rec(k):
        if k==n:return True
        i=order[k]
        for j in cand[i]:
            if used[j]:continue
            good=True
            for t in range(k):
                u=order[t]; v=mp[u]
                if A[i][u]!=B[j][v]:good=False;break
            if good:
                mp[i]=j;used[j]=True
                if rec(k+1):return True
                used[j]=False;mp[i]=-1
        return False
    return rec(0)

# quotient automorphism counts: expected 2*r! for r>=3, 2 for r=2
for r in [2,3,4]:
    V,A=h_graph(r); got=count_aut(A); exp=2 if r==2 else 2*factorial(r)
    assert got==exp,(r,got,exp)
    print('H_AUT',r,got)

# false-twin quotient and exact automorphism orders for small expanded graphs
for qs in [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,3,3)]:
    V,A=expanded(qs)
    cls=false_twin_classes(A)
    assert len(cls)==(1<<len(qs))-2
    sizes=sorted(len(c) for c in cls)
    expect=[]
    for S in supports(len(qs)):
        w=1
        for i,q in enumerate(qs):
            if S>>i&1:w*=q-1
        expect.append(w)
    assert sizes==sorted(expect)
    if len(A)<=10:
        got=count_aut(A); exp=predicted_order(qs)
        assert got==exp,(qs,got,exp)
        print('G_AUT',qs,len(A),got)
    else:
        print('G_TWINS',qs,len(A),sizes)

# Reconstruction test for all small products whose expanded graph has <=10 vertices.
cases=[]
for r in [2,3]:
    for qs in product([2,3,4], repeat=r):
        if tuple(sorted(qs))!=tuple(qs): continue
        V,A=expanded(qs)
        if len(A)<=10: cases.append((qs,A))
for i,(q,A) in enumerate(cases):
    for q2,B in cases[i:]:
        iso=graph_iso(A,B)
        same=tuple(sorted(q))==tuple(sorted(q2))
        assert iso==same,(q,q2,iso,same)
print('RECON_CASES',len(cases),'OK')
print('VERIFY_OK')
