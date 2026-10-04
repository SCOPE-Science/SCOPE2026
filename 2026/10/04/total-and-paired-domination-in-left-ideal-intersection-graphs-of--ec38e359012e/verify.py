#!/usr/bin/env python3
from itertools import product, combinations

def add(u,v,q):
    return tuple((a+b)%q for a,b in zip(u,v))

def smul(c,u,q):
    return tuple((c*a)%q for a in u)

def span(gens,q):
    if not gens:
        return frozenset({tuple(0 for _ in range(0))})
    n=len(gens[0])
    out={tuple(0 for _ in range(n))}
    for g in gens:
        old=list(out)
        for c in range(q):
            for v in old:
                out.add(add(v,smul(c,g,q),q))
    return frozenset(out)

def all_subspaces(n,q):
    zero=tuple(0 for _ in range(n))
    elems=list(product(range(q), repeat=n))
    subs={frozenset([zero])}
    frontier=[frozenset([zero])]
    while frontier:
        U=frontier.pop()
        for v in elems:
            if v in U:
                continue
            # span U and v
            W=set(U)
            for c in range(q):
                cv=smul(c,v,q)
                for u in U:
                    W.add(add(u,cv,q))
            W=frozenset(W)
            if W not in subs:
                subs.add(W); frontier.append(W)
    whole=frozenset(elems)
    return [U for U in subs if len(U)>1 and U!=whole]

def sum_subspaces(U,W,q):
    return frozenset(add(u,w,q) for u in U for w in W)

def graph(n,q):
    V=all_subspaces(n,q)
    whole_size=q**n
    adj=[set() for _ in V]
    for i,U in enumerate(V):
        for j in range(i+1,len(V)):
            W=V[j]
            # Matrix-left-ideal model: M_U adjacent M_W iff U+W != F_q^n.
            if len(sum_subspaces(U,W,q)) < whole_size:
                adj[i].add(j); adj[j].add(i)
    return V,adj

def dominates(S,adj):
    S=set(S)
    return all(v in S or bool(adj[v]&S) for v in range(len(adj)))

def total_dominates(S,adj):
    S=set(S)
    return all(bool(adj[v]&S) for v in range(len(adj)))

def has_perfect_matching(S,adj):
    S=set(S)
    if len(S)%2: return False
    if not S: return True
    v=next(iter(S))
    for u in adj[v]&S:
        if has_perfect_matching(S-{v,u},adj):
            return True
    return False

def paired_dominates(S,adj):
    return dominates(S,adj) and has_perfect_matching(S,adj)

def minimum(adj,pred,max_k):
    n=len(adj)
    for k in range(1,min(max_k,n)+1):
        for S in combinations(range(n),k):
            if pred(S,adj):
                return k
    return None

cases=[]
for n,q in [(2,2),(2,3),(3,2),(3,3)]:
    V,adj=graph(n,q)
    gamma=minimum(adj,dominates,q+2)
    gt=minimum(adj,total_dominates,q+2)
    gp=minimum(adj,paired_dominates,q+2)
    if n==2:
        assert gamma==q+1 and gt is None and gp is None
    else:
        assert gamma==q+1 and gt==q+1
        expected_gp=(q+1 if q%2 else q+2)
        assert gp==expected_gp
    cases.append((n,q,len(V),gamma,gt,gp))

print("VERIFY_OK")
for n,q,nv,g,gt,gp in cases:
    print(f"n={n} q={q} vertices={nv} gamma={g} gamma_t={gt} gamma_pr={gp}")
