from itertools import product

def acyclic(f):
    n=len(f)
    for s in range(n):
        seen=set(); u=s
        while u is not None:
            if u in seen: return False
            seen.add(u); u=f[u]
    return True

def depths(f):
    n=len(f); pred=[[] for _ in range(n)]
    for u,v in enumerate(f):
        if v is not None: pred[v].append(u)
    memo={}
    def d(v):
        if v in memo:return memo[v]
        memo[v]=max([d(u)+1 for u in pred[v]] or [0])
        return memo[v]
    return [d(v) for v in range(n)]

def supports(f):
    n=len(f); S=[None,set(range(n))]
    # enough until zero: predicted max 2^(n-1)+1
    maxk=(1<<(n-1))+1
    for k in range(2,maxk+1):
        t=set()
        for a in range(1,k):
            b=k-a
            if a>=len(S) or b>=len(S): continue
            for u in S[a] & S[b]:
                if f[u] is not None: t.add(f[u])
        S.append(t)
    return S

def check(f):
    ds=depths(f); S=supports(f); L=max(ds, default=0)
    for k in range(1,len(S)):
        expected={v for v,d in enumerate(ds) if k <= (1<<d)}
        assert S[k]==expected,(f,ds,k,S[k],expected)
    assert S[1<<L]
    assert not S[(1<<L)+1]

cases=0
for n in range(1,7):
    vals=[None]+list(range(n))
    for tup in product(vals, repeat=n):
        if any(tup[i]==i for i in range(n)): continue
        if not acyclic(tup): continue
        check(tup); cases+=1
print(f'VERIFY_OK cases={cases}')
