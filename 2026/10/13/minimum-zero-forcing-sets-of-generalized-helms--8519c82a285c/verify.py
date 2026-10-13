from itertools import combinations
from math import comb


def generalized_helm(m,s):
    # 0=center; 1..m=cycle/spokes; leaves after that, bundle i belongs to spoke i+1
    N=1+m+m*s
    adj=[set() for _ in range(N)]
    def add(u,v):
        adj[u].add(v); adj[v].add(u)
    for i in range(m):
        v=1+i
        add(0,v)
        add(v,1+((i+1)%m))
        base=1+m+i*s
        for j in range(s): add(v,base+j)
    return adj


def closure(adj,S):
    blue=set(S); N=len(adj)
    while len(blue)<N:
        force=None
        for u in tuple(blue):
            white=[v for v in adj[u] if v not in blue]
            if len(white)==1:
                force=white[0]; break
        if force is None: return blue
        blue.add(force)
    return blue


def zf(adj,S): return len(closure(adj,S))==len(adj)


def propagation_time(adj,S):
    blue=set(S); N=len(adj); t=0
    while len(blue)<N:
        targets=set()
        for u in blue:
            white=[v for v in adj[u] if v not in blue]
            if len(white)==1: targets.add(white[0])
        if not targets: return None
        blue |= targets; t += 1
    return t


def kind(m,s,S):
    S=set(S); Z=m*(s-1)+1
    if len(S)!=Z: return None
    if S & set(range(1,m+1)): return None
    counts=[]
    for i in range(m):
        base=1+m+i*s
        counts.append(sum((base+j) in S for j in range(s)))
    if 0 in S and all(c==s-1 for c in counts): return 'center'
    if 0 not in S and counts.count(s)==1 and counts.count(s-1)==m-1: return 'saturated'
    return None


def run():
    profiles=[(3,2),(4,2),(5,2),(6,2),(7,2),(3,3),(4,3),(5,3),(3,4),(4,4)]
    subset_checks=0; classification_checks=0; lower_checks=0; propagation_checks=0
    for m,s in profiles:
        adj=generalized_helm(m,s); N=len(adj); Z=m*(s-1)+1
        counts={'center':0,'saturated':0}
        for S in combinations(range(N),Z):
            subset_checks+=1
            a=zf(adj,S); k=kind(m,s,S)
            if a!=(k is not None): raise AssertionError(('criterion',m,s,S,a,k))
            if a:
                classification_checks += 1; counts[k]+=1
                pt=propagation_time(adj,S); propagation_checks += 1
                expect=2 if k=='center' else 3
                if pt!=expect: raise AssertionError(('pt',m,s,S,k,pt,expect))
        if counts['center']!=s**m: raise AssertionError(('center-count',m,s,counts['center'],s**m))
        if counts['saturated']!=m*s**(m-1): raise AssertionError(('sat-count',m,s,counts['saturated'],m*s**(m-1)))
        expected=s**(m-1)*(s+m)
        if sum(counts.values())!=expected: raise AssertionError(('count',m,s,counts,expected))
        if comb(N,Z-1)<=100000:
            for S in combinations(range(N),Z-1):
                lower_checks+=1
                if zf(adj,S): raise AssertionError(('lower',m,s,S))
    print(f'VERIFY_OK profiles={len(profiles)} subset_checks={subset_checks} classification_checks={classification_checks} propagation_checks={propagation_checks} lower_checks={lower_checks} max_order={max(len(generalized_helm(m,s)) for m,s in profiles)}')

if __name__=='__main__': run()
