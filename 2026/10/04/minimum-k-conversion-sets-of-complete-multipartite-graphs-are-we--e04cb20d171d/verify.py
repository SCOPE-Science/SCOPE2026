from itertools import product, combinations
from math import comb

def compositions(n):
    for mask in range(1, 1 << (n-1)):
        parts=[]; last=0
        cuts=[i+1 for i in range(n-1) if mask>>i & 1]
        prev=0
        for c in cuts+[n]:
            parts.append(c-prev); prev=c
        if len(parts)>=2: yield tuple(parts)

def graph(parts):
    part=[]
    for i,m in enumerate(parts): part += [i]*m
    N=len(part)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if part[u]!=part[v]: adj[u].add(v); adj[v].add(u)
    return part,adj

def converts(parts,k,S):
    part,adj=graph(parts); active=set(S)
    changed=True
    while changed:
        changed=[]
        for v in range(len(part)):
            if v not in active and len(adj[v]&active)>=k: changed.append(v)
        if not changed: break
        active.update(changed)
    return len(active)==len(part)

def criterion(parts,k,S):
    N=sum(parts)
    if N<=k: return len(S)==N
    # deficit parts degree < k
    offsets=[]; x=0
    for m in parts: offsets.append((x,x+m)); x+=m
    D=[i for i,m in enumerate(parts) if N-m<k]
    X=set()
    for i in D:
        a,b=offsets[i]; X.update(range(a,b))
    d=len(X)
    target=max(d,k)
    if len(S)!=target or not X.issubset(S): return False
    if d>=k: return set(S)==X
    # d<k, minimum size k. Profile on nondeficient parts.
    items=[]
    for i,m in enumerate(parts):
        if i in D: continue
        a,b=offsets[i]
        s=sum(v in S for v in range(a,b))
        u=m-s
        if u>0: items.append((s,u,i))
    if not items: return True
    items.sort(key=lambda z:z[0])
    U=0
    for s,u,i in items:
        if s>U: return False
        U += u
    return True

def profile_count(parts,k):
    N=sum(parts)
    if N<=k: return 1
    D=[i for i,m in enumerate(parts) if N-m<k]
    d=sum(parts[i] for i in D)
    if d>=k: return 1
    R=[i for i in range(len(parts)) if i not in D]
    need=k-d
    total=0
    for ss in product(*[range(parts[i]+1) for i in R]):
        if sum(ss)!=need: continue
        items=[]
        ways=1
        for idx,s in zip(R,ss):
            m=parts[idx]; ways*=comb(m,s)
            if s<m: items.append((s,m-s,idx))
        items.sort(key=lambda z:z[0])
        U=0; ok=True
        for s,u,_ in items:
            if s>U: ok=False; break
            U+=u
        if ok: total+=ways
    return total

def brute_min_sets(parts,k):
    N=sum(parts); good=[]
    for mask in range(1<<N):
        S={i for i in range(N) if mask>>i &1}
        if converts(parts,k,S): good.append(S)
    m=min(map(len,good))
    return m,[S for S in good if len(S)==m]

profiles=0; subset_checks=0; count_checks=0
for N in range(2,9):
    for parts in compositions(N):
        profiles+=1
        for k in range(1,N+1):
            m,mins=brute_min_sets(parts,k)
            X=sum(mm for mm in parts if N-mm<k)
            expected=N if N<=k else max(X,k)
            assert m==expected,(parts,k,m,expected)
            for S in mins:
                subset_checks+=1
                assert criterion(parts,k,S),(parts,k,S)
            # criterion must reject non-min sets and match all subsets at min size
            for C in combinations(range(N),m):
                S=set(C); subset_checks+=1
                assert criterion(parts,k,S)==converts(parts,k,S),(parts,k,S,criterion(parts,k,S),converts(parts,k,S))
            pc=profile_count(parts,k)
            assert pc==len(mins),(parts,k,pc,len(mins))
            count_checks+=1
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} count_checks={count_checks} max_order=8')
