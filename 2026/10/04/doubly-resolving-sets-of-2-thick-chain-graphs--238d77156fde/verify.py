from itertools import product
from collections import deque, Counter
from math import prod

MAX_ORDER=12

def compositions_extra(total, k):
    if k==1:
        yield (total,); return
    for x in range(total+1):
        for rest in compositions_extra(total-x,k-1):
            yield (x,)+rest

def profiles(max_order):
    for p in range(2,max_order//4+1):
        for n in range(4*p,max_order+1):
            e=n-4*p
            for extras in compositions_extra(e,2*p):
                vals=tuple(2+x for x in extras)
                yield vals[:p], vals[p:]

def build(a,b):
    ai=[]; bj=[]; idx=0
    for m in a:
        c=list(range(idx,idx+m)); idx+=m; ai.append(c)
    for m in b:
        c=list(range(idx,idx+m)); idx+=m; bj.append(c)
    adj=[set() for _ in range(idx)]
    p=len(a)
    for i in range(p):
        for j in range(p):
            if j<=i:
                for u in ai[i]:
                    for v in bj[j]:
                        adj[u].add(v); adj[v].add(u)
    return adj,ai,bj

def distances(adj):
    n=len(adj); D=[[999]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v]==999:
                    D[s][v]=D[s][u]+1; q.append(v)
    return D

def brute_dr(mask,D):
    n=len(D)
    S=[s for s in range(n) if (mask>>s)&1]
    if len(S)<2: return False
    for u in range(n):
        for v in range(u+1,n):
            first=None; varied=False
            for s in S:
                z=D[u][s]-D[v][s]
                if first is None: first=z
                elif z!=first:
                    varied=True; break
            if not varied: return False
    return True

def theorem(mask,a,b,ai,bj):
    # condition (i)
    for c in ai+bj:
        if sum(1 for v in c if not ((mask>>v)&1))>1:
            return False
    # left boundary obstruction
    if b[0]==2:
        omitA1=any(not ((mask>>v)&1) for v in ai[0])
        omitB1=any(not ((mask>>v)&1) for v in bj[0])
        if omitA1 and omitB1:
            return False
    # right boundary obstruction
    if a[-1]==2:
        omitAp=any(not ((mask>>v)&1) for v in ai[-1])
        omitBp=any(not ((mask>>v)&1) for v in bj[-1])
        if omitAp and omitBp:
            return False
    return True

def poly_mul(P,Q):
    R=Counter()
    for i,a in P.items():
        for j,b in Q.items(): R[i+j]+=a*b
    return R

def factor_f(m): return Counter({m:1,m-1:m})
def factor_e(m): return Counter({m-1:m})

def theorem_poly(a,b):
    p=len(a)
    F=Counter({0:1})
    for m in a+b: F=poly_mul(F,factor_f(m))
    ans=F.copy()
    if b[0]==2:
        L=Counter({0:1})
        for i,m in enumerate(a): L=poly_mul(L,factor_e(m) if i==0 else factor_f(m))
        for j,m in enumerate(b): L=poly_mul(L,factor_e(m) if j==0 else factor_f(m))
        ans.subtract(L)
    if a[-1]==2:
        R=Counter({0:1})
        for i,m in enumerate(a): R=poly_mul(R,factor_e(m) if i==p-1 else factor_f(m))
        for j,m in enumerate(b): R=poly_mul(R,factor_e(m) if j==p-1 else factor_f(m))
        ans.subtract(R)
    if b[0]==2 and a[-1]==2:
        I=Counter({0:1})
        for i,m in enumerate(a): I=poly_mul(I,factor_e(m) if i in (0,p-1) else factor_f(m))
        for j,m in enumerate(b): I=poly_mul(I,factor_e(m) if j in (0,p-1) else factor_f(m))
        ans.update(I)
    return +ans

def min_formula(a,b):
    p=len(a);N=sum(a)+sum(b)
    l=int(b[0]==2); r=int(a[-1]==2)
    psi=N-2*p+l+r
    count=1
    for i in range(p):
        if i==0 and l:
            count*=a[0]+b[0]
        elif i==p-1 and r:
            count*=a[-1]+b[-1]
        else:
            count*=a[i]*b[i]
    return psi,count

graph_profiles=subset_checks=coefficient_checks=0
for a,b in profiles(MAX_ORDER):
    adj,ai,bj=build(a,b);D=distances(adj);n=len(adj)
    brute=Counter()
    for mask in range(1<<n):
        got=brute_dr(mask,D); pred=theorem(mask,a,b,ai,bj)
        subset_checks+=1
        if got!=pred:
            raise AssertionError((a,b,mask,got,pred))
        if got: brute[mask.bit_count()]+=1
    predp=theorem_poly(a,b)
    if brute!=predp:
        raise AssertionError(('poly',a,b,brute,predp))
    coefficient_checks += len(set(brute)|set(predp))
    if brute:
        mn=min(brute)
        psi,cnt=min_formula(a,b)
        if (mn,brute[mn])!=(psi,cnt):
            raise AssertionError(('min',a,b,(mn,brute[mn]),(psi,cnt)))
    graph_profiles+=1
print(f'VERIFY_OK profiles={graph_profiles} subset_checks={subset_checks} coefficient_checks={coefficient_checks} max_order={MAX_ORDER}')
