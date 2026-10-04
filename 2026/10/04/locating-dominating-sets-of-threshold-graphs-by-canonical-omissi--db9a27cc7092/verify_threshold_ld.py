from itertools import combinations
from collections import Counter

def compositions(n,k):
    if k==1:
        yield (n,); return
    for cuts in combinations(range(1,n),k-1):
        pts=(0,)+cuts+(n,)
        yield tuple(pts[i+1]-pts[i] for i in range(k))

def graph_from_blocks(a,b):
    verts=[]
    for i,(ai,bi) in enumerate(zip(a,b)):
        verts += [('A',i,t) for t in range(ai)]
        verts += [('B',i,t) for t in range(bi)]
    idx={v:i for i,v in enumerate(verts)}
    adj=[set() for _ in verts]
    for r,u in enumerate(verts):
        for s in range(r+1,len(verts)):
            v=verts[s]; tu,i,_=u; tv,j,_=v
            edge=(tu=='B' and tv=='B') or (tu=='A' and tv=='B' and i<=j) or (tu=='B' and tv=='A' and j<=i)
            if edge:
                adj[r].add(s); adj[s].add(r)
    return verts,adj

def is_ld(adj,S):
    S=set(S); traces=[]
    for v in range(len(adj)):
        if v in S: continue
        tr=frozenset(adj[v]&S)
        if not tr: return False
        traces.append(tr)
    return len(traces)==len(set(traces))

def admissible(a,b,P,Q):
    p=len(a); P=set(P); Q=set(Q)
    alpha=[a[i]-(i in P) for i in range(p)]
    beta=[b[i]-(i in Q) for i in range(p)]
    for i in P:
        if sum(beta[i:])==0: return False
    for j in Q:
        if sum(beta)-beta[j]+sum(alpha[:j+1])==0: return False
    ps=sorted(P)
    for i,j in zip(ps,ps[1:]):
        if sum(beta[i:j])==0: return False
    qs=sorted(Q)
    for i,j in zip(qs,qs[1:]):
        if sum(alpha[i+1:j+1])==0: return False
    for i in P:
        for j in Q:
            if sum(alpha[:j+1])+sum(beta[:i])==0: return False
    return True

def theorem_poly(a,b):
    p=len(a); N=sum(a)+sum(b); out=Counter()
    for ma in range(1<<p):
        P=[i for i in range(p) if ma>>i&1]
        for mb in range(1<<p):
            Q=[i for i in range(p) if mb>>i&1]
            if not admissible(a,b,P,Q): continue
            mult=1
            for i in P: mult*=a[i]
            for j in Q: mult*=b[j]
            out[N-len(P)-len(Q)] += mult
    return out

def brute_poly(a,b):
    _,adj=graph_from_blocks(a,b); n=len(adj); out=Counter()
    for mask in range(1<<n):
        S=[v for v in range(n) if mask>>v&1]
        if is_ld(adj,S): out[len(S)]+=1
    return out

def thick_poly(a,b):
    N=sum(a)+sum(b); p=len(a); out=Counter()
    for ma in range(1<<p):
        for mb in range(1<<p):
            omissions=ma.bit_count()+mb.bit_count(); mult=1
            for i in range(p):
                if ma>>i&1: mult*=a[i]
                if mb>>i&1: mult*=b[i]
            out[N-omissions]+=mult
    return out

profiles=subset_checks=coefficient_checks=0
for n in range(2,11):
    for p in range(1,n//2+1):
        for c in compositions(n,2*p):
            a=c[0::2]; b=c[1::2]
            brute=brute_poly(a,b); formula=theorem_poly(a,b)
            assert brute==formula,(a,b,brute,formula)
            if all(x>=2 for x in a+b):
                assert formula==thick_poly(a,b)
            profiles+=1; subset_checks+=1<<n
            coefficient_checks+=len(set(brute)|set(formula))
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} coefficient_checks={coefficient_checks} max_order=10')
