#!/usr/bin/env python3
import itertools, math

def adj(n):
    N=2*n
    A=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                A[i].add(n+j); A[n+j].add(i)
    return A

def dominates(supp,A):
    return all(v in supp or bool(A[v] & supp) for v in range(len(A)))

def wrdf(f,A):
    for v,x in enumerate(f):
        if x: continue
        ok=False
        for u in A[v]:
            if f[u]>0:
                g=list(f); g[u]-=1; g[v]+=1
                supp={i for i,z in enumerate(g) if z>0}
                if dominates(supp,A):
                    ok=True; break
        if not ok: return False
    return True

def candidates_weight_at_most(N,W=4):
    # Enumerate all {0,1,2}-labelings of total weight at most W by choosing 2-positions and 1-positions.
    yield (0,)*N
    V=range(N)
    for twos in range(W//2+1):
        for T in itertools.combinations(V,twos):
            rem=[v for v in V if v not in T]
            for ones in range(W-2*twos+1):
                for O in itertools.combinations(rem,ones):
                    f=[0]*N
                    for v in T:f[v]=2
                    for v in O:f[v]=1
                    yield tuple(f)

def predicted(n,f):
    w=sum(f)
    A=f[:n]; B=f[n:]
    IA={i for i,x in enumerate(A) if x>0}; IB={i for i,x in enumerate(B) if x>0}
    A2={i for i,x in enumerate(A) if x==2}; B2={i for i,x in enumerate(B) if x==2}
    if n==3:
        if w!=3 or A2 or B2: return False
        if len(IA)==3 and not IB: return True
        if len(IB)==3 and not IA: return True
        if len(IA)==1 and len(IB)==2 and IA <= IB: return True
        if len(IB)==1 and len(IA)==2 and IB <= IA: return True
        return False
    if w!=4: return False
    if n==4:
        if not A2 and not B2:
            if len(IA)==4 and not IB: return True
            if len(IB)==4 and not IA: return True
            if len(IA)==1 and len(IB)==3 and IA <= IB: return True
            if len(IB)==1 and len(IA)==3 and IB <= IA: return True
            if len(IA)==2 and len(IB)==2: return True
            return False
        if len(A2)==1 and len(B2)==1 and len(IA)==len(IB)==1:
            return A2==B2
        if len(A2)==1 and len(IA)==1 and not B2 and len(IB)==2:
            return A2 <= IB
        if len(B2)==1 and len(IB)==1 and not A2 and len(IA)==2:
            return B2 <= IA
        return False
    # n>=5
    if len(A2)==1 and len(B2)==1 and len(IA)==len(IB)==1:
        return A2==B2
    if len(A2)==1 and len(IA)==1 and not B2 and len(IB)==2:
        return A2 <= IB
    if len(B2)==1 and len(IB)==1 and not A2 and len(IA)==2:
        return B2 <= IA
    if not A2 and not B2 and len(IA)==len(IB)==2:
        return bool(IA & IB)
    return False

def expected_count(n):
    if n==3:return 14
    if n==4:return 90
    return n*(2*n*n-n+1)//2

def expected_binary_count(n):
    if n==3:return 14
    if n==4:return 62
    return n*(n-1)*(2*n-3)//2

candidate_checks=0; wrdf_checks=0; classification_checks=0; count_checks=0; binary_checks=0
for n in range(3,13):
    G=adj(n)
    mins=[]
    best=99
    for f in candidates_weight_at_most(2*n,4):
        candidate_checks += 1
        w=sum(f)
        if w>best: continue
        wrdf_checks += 1
        if wrdf(f,G):
            if w<best: best=w; mins=[]
            if w==best: mins.append(f)
    expw=3 if n==3 else 4
    assert best==expw,(n,best)
    assert len(mins)==expected_count(n),(n,len(mins),expected_count(n))
    count_checks += 2
    for f in mins:
        assert predicted(n,f),(n,f)
        classification_checks += 1
    # converse among all weight-expw candidates
    pred=[]
    for f in candidates_weight_at_most(2*n,4):
        if sum(f)==expw and predicted(n,f):
            assert wrdf(f,G),(n,'predicted-not-wrdf',f)
            pred.append(f); classification_checks += 1
    assert len(pred)==len(mins)
    binary=sum(1 for f in mins if 2 not in f)
    assert binary==expected_binary_count(n),(n,binary,expected_binary_count(n))
    binary_checks += 1
print(f"VERIFY_OK n_range=3..12 candidate_checks={candidate_checks} wrdf_checks={wrdf_checks} classification_checks={classification_checks} count_checks={count_checks} binary_checks={binary_checks} max_order=24")
