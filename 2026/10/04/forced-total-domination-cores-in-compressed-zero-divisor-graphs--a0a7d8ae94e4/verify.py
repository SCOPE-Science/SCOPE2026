#!/usr/bin/env python3
from itertools import product, combinations

def vertices(lengths):
    allv = list(product(*[range(L+1) for L in lengths]))
    zero = tuple(0 for _ in lengths)       # unit class
    top = tuple(lengths)                    # zero class
    return [a for a in allv if a != zero and a != top]

def graph(lengths):
    V = vertices(lengths)
    idx = {v:i for i,v in enumerate(V)}
    N = [set() for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            b=V[j]
            if all(a[k]+b[k] >= lengths[k] for k in range(len(lengths))):
                N[i].add(j); N[j].add(i)
    return V,idx,N

def is_total(D,N):
    D=set(D)
    return all(bool(N[v] & D) for v in range(len(N)))

def is_dominating(D,N):
    D=set(D)
    return all(v in D or bool(N[v] & D) for v in range(len(N)))

def perfect_matching(D,N):
    D=frozenset(D)
    memo={}
    def rec(S):
        if not S:
            return True
        if len(S)%2:
            return False
        if S in memo:
            return memo[S]
        v=next(iter(S))
        T=S-{v}
        for u in T:
            if u in N[v] and rec(T-{u}):
                memo[S]=True
                return True
        memo[S]=False
        return False
    return rec(D)

def is_paired(D,N):
    return is_dominating(D,N) and perfect_matching(D,N)

def minima(N, pred, max_k):
    for k in range(max_k+1):
        ans=[]
        for C in combinations(range(len(N)),k):
            if pred(C,N):
                ans.append(C)
        if ans:
            return k,ans
    return None,[]

def expected(lengths):
    r=len(lengths)
    Vn=1
    for L in lengths:
        Vn*=L+1
    Vn-=2
    if r==1:
        L=lengths[0]
        if L==1:
            return ("empty",0,0,0)
        if L==2:
            return ("isolated",None,None,0)
        return ("local",2,2,L-2)
    gt=r
    gp=r if r%2==0 else r+1
    paired_count=1 if r%2==0 else Vn-r
    return ("product",gt,gp,paired_count)

def check_tuple(lengths, exhaustive=True):
    V,idx,N=graph(lengths)
    r=len(lengths)

    # Check the forced core and unique-neighbor witnesses when r>=2.
    if r>=2:
        core=[]
        for i,L in enumerate(lengths):
            w=tuple(1 if j==i else 0 for j in range(r))
            d=tuple((lengths[j]-1) if j==i else lengths[j] for j in range(r))
            wi=idx[w]; di=idx[d]
            assert N[wi]=={di}, (lengths,w,[V[j] for j in N[wi]],d)
            core.append(di)
        core=set(core)
        assert is_total(core,N)
        for i,j in combinations(core,2):
            assert j in N[i]
        for v,a in enumerate(V):
            assert any(i in N[v] for i in core), (lengths,a)

    kind,egt,egp,epc=expected(lengths)
    if kind=="empty":
        assert len(V)==0
        return f"{lengths}: empty graph"
    if kind=="isolated":
        assert len(V)==1 and not N[0]
        assert not any(is_total(C,N) for k in range(2) for C in combinations(range(len(V)),k))
        return f"{lengths}: one isolated vertex; no total/paired domination"

    if exhaustive:
        kt,Ts=minima(N,is_total,min(len(N),max(egt or 0,egp or 0)+1))
        kp,Ps=minima(N,is_paired,min(len(N),max(egt or 0,egp or 0)+1))
        assert kt==egt, (lengths,kt,egt)
        assert kp==egp, (lengths,kp,egp)
        if r>=2:
            assert len(Ts)==1, (lengths,len(Ts))
        else:
            assert len(Ts)==lengths[0]-2, (lengths,len(Ts))
        assert len(Ps)==epc, (lengths,len(Ps),epc)
        return f"{lengths}: |V|={len(V)} gamma_t={kt} min_total={len(Ts)} gamma_pr={kp} min_paired={len(Ps)}"
    return f"{lengths}: structural checks OK"

def v2_mod(x,L):
    mod=2**L
    x%=mod
    if x==0:
        return L
    a=0
    while x%2==0:
        x//=2
        a+=1
    return a

def direct_ring_check(lengths):
    mods=[2**L for L in lengths]
    elems=list(product(*[range(m) for m in mods]))
    zero=tuple(0 for _ in mods)
    one=tuple(1 for _ in mods)
    def mul(x,y):
        return tuple((x[i]*y[i])%mods[i] for i in range(len(mods)))
    ann={}
    for x in elems:
        ann[x]=frozenset(y for y in elems if mul(x,y)==zero)
    classes={}
    for x in elems:
        classes.setdefault(ann[x],[]).append(x)
    # Annihilator classes of nonzero zero-divisors should be indexed by valuations.
    val_to_ann={}
    for x in elems:
        vals=tuple(v2_mod(x[i],lengths[i]) for i in range(len(lengths)))
        val_to_ann.setdefault(vals,ann[x])
        assert val_to_ann[vals]==ann[x]
    Vvals=set(vertices(lengths))
    class_vals=set()
    for A,cls in classes.items():
        rep=cls[0]
        vals=tuple(v2_mod(rep[i],lengths[i]) for i in range(len(lengths)))
        if vals in Vvals:
            class_vals.add(vals)
    assert class_vals==Vvals
    V,idx,N=graph(lengths)
    for i,a in enumerate(V):
        xa=next(x for x in elems if tuple(v2_mod(x[j],lengths[j]) for j in range(len(lengths)))==a)
        for j,b in enumerate(V):
            if i==j: continue
            xb=next(x for x in elems if tuple(v2_mod(x[k],lengths[k]) for k in range(len(lengths)))==b)
            assert ((j in N[i]) == (mul(xa,xb)==zero))
    return f"direct R=product Z/(2^L), L={lengths}: {len(V)} compressed vertices OK"

cases=[]
for L in range(1,7):
    cases.append((L,))
for a in range(1,4):
    for b in range(1,4):
        cases.append((a,b))
for a in range(1,3):
    for b in range(1,3):
        for c in range(1,3):
            cases.append((a,b,c))
cases += [(1,1,1,1),(1,1,1,2),(1,1,2,2)]

for Ls in cases:
    print(check_tuple(Ls, exhaustive=True))

for Ls in [(3,),(2,1),(2,2),(3,1),(3,2),(2,2,1)]:
    print(direct_ring_check(Ls))

print("VERIFY_OK")
