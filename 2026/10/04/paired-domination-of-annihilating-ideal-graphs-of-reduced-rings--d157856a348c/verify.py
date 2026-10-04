#!/usr/bin/env python3
from itertools import combinations

def graph(m):
    full=(1<<m)-1
    V=[s for s in range(1,full) if s!=full]
    adj={s:{t for t in V if t!=s and (s&t)==0} for s in V}
    return V,adj

def dominates(D,V,adj):
    D=set(D)
    return all(v in D or any(u in adj[v] for u in D) for v in V)

def has_perfect_matching(D,adj):
    D=tuple(D)
    if len(D)%2: return False
    def rec(rem):
        if not rem: return True
        v=rem[0]
        for j in range(1,len(rem)):
            w=rem[j]
            if w in adj[v] and rec(rem[1:j]+rem[j+1:]):
                return True
        return False
    return rec(D)

def paired(D,V,adj):
    return dominates(D,V,adj) and has_perfect_matching(D,adj)

def exact_gamma_pr(m):
    V,adj=graph(m)
    target=m if m%2==0 else m+1
    for k in range(2,target,2):
        assert not any(paired(C,V,adj) for C in combinations(V,k)), (m,k)
    # Construct the theorem's set: singleton supports A_i; for odd m add P_1.
    D=[1<<i for i in range(m)]
    if m%2:
        D.append(((1<<m)-1)^1)
    assert len(D)==target and paired(D,V,adj)
    return target,len(V)

for m in range(2,6):
    gpr,nv=exact_gamma_pr(m)
    print(f'm={m} vertices={nv} gamma_pr={gpr}')
print('VERIFY_OK')
