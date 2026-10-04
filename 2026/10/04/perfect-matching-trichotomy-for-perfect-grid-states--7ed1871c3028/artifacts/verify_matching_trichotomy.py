#!/usr/bin/env python3
import itertools

def perms(n):
    return itertools.permutations(range(n))

def rowcol_numbers(M):
    n=len(M)
    rmins=[min(M[i]) for i in range(n)]
    cmins=[min(M[i][j] for i in range(n)) for j in range(n)]
    R=-sum(rmins); C=-sum(cmins)
    return R,C,rmins,cmins

def direct_perfect_states(M):
    n=len(M)
    R,C,_,_=rowcol_numbers(M)
    target=min(R,C)
    out=[]
    for p in perms(n):
        A=-sum(M[p[j]][j] for j in range(n))
        if A==target:
            out.append(tuple(p))
    return sorted(out)

def matching_states(M):
    n=len(M)
    R,C,rmins,cmins=rowcol_numbers(M)
    out=[]
    if C<=R:
        allowed={(i,j) for i in range(n) for j in range(n) if M[i][j]==cmins[j]}
    else:
        allowed={(i,j) for i in range(n) for j in range(n) if M[i][j]==rmins[i]}
    for p in perms(n):
        if all((p[j],j) in allowed for j in range(n)):
            out.append(tuple(p))
    return sorted(out), allowed

def alternating_cycle_exists(p, allowed):
    n=len(p)
    inv=[None]*n
    for j,i in enumerate(p): inv[i]=j
    # Contract each matched edge to its column index. A nonmatching allowed edge
    # from column j to row i points to the matched column inv[i].
    adj=[[] for _ in range(n)]
    for i,j in allowed:
        if p[j]!=i:
            adj[j].append(inv[i])
    color=[0]*n
    def dfs(v):
        color[v]=1
        for w in adj[v]:
            if color[w]==1: return True
            if color[w]==0 and dfs(w): return True
        color[v]=2
        return False
    return any(color[v]==0 and dfs(v) for v in range(n))

def check_matrix(M):
    direct=direct_perfect_states(M)
    match, allowed=matching_states(M)
    assert direct==match, (M,direct,match)
    if not match:
        cls=0
    elif len(match)==1:
        cls=1
        assert not alternating_cycle_exists(match[0], allowed)
    else:
        cls=2
        assert alternating_cycle_exists(match[0], allowed)
    brute=0 if len(direct)==0 else (1 if len(direct)==1 else 2)
    assert cls==brute
    return cls

total=0
hist={0:0,1:0,2:0}
for n in range(1,5):
    cells=n*n
    for bits in range(1<<cells):
        M=[[0]*n for _ in range(n)]
        for k in range(cells):
            i,j=divmod(k,n)
            M[i][j]=(bits>>k)&1
        hist[check_matrix(M)]+=1
        total+=1
    print(f'n={n}: checked={1<<cells}')
print('histogram_zero_unique_multiple=', hist)
print(f'VERIFY_OK matrices_checked={total}')
