from itertools import product
from math import comb
from collections import Counter

MAX_ORDER = 9

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n+1):
        for rest in partitions(n-first, first):
            yield (first,)+rest

def part_index(profile):
    out=[]
    for i,n in enumerate(profile): out += [i]*n
    return out

def literal_ir(profile, lab):
    r=len(profile); pi=part_index(profile)
    pos=[v for v,a in enumerate(lab) if a>0]
    if any(pi[u]!=pi[v] for a,u in enumerate(pos) for v in pos[a+1:]):
        return False
    twos=[v for v,a in enumerate(lab) if a==2]
    for v,a in enumerate(lab):
        if a==0 and not any(pi[u]!=pi[v] for u in twos):
            return False
    return True

def criterion(profile, lab):
    pi=part_index(profile)
    pos=[v for v,a in enumerate(lab) if a>0]
    if not pos: return False
    i=pi[pos[0]]
    if any(pi[v]!=i for v in pos): return False
    verts=[v for v,p in enumerate(pi) if p==i]
    if any(lab[v]==0 for v in verts): return False
    if any(lab[v]!=0 for v,p in enumerate(pi) if p!=i): return False
    return any(lab[v]==2 for v in verts)

def formula(profile):
    c=Counter()
    for n in profile:
        for k in range(n+1):
            # choose k labels 2, n-k labels 1; exclude k=0
            if k:
                c[n+k]+=comb(n,k)
    return c

def reconstruct(poly):
    p=Counter({d:a for d,a in poly.items() if a})
    rec=[]
    while p:
        L=max(p)//2
        if 2*L!=max(p): raise AssertionError(('odd top degree',p))
        mult=p[2*L]
        if mult<=0: raise AssertionError(('bad multiplicity',L,mult))
        rec += [L]*mult
        for k in range(1,L+1):
            p[L+k]-=mult*comb(L,k)
            if p[L+k]==0: del p[L+k]
            elif p[L+k]<0: raise AssertionError(('negative residual',L,k,p))
    return tuple(sorted(rec))

profiles=labelings=valid=coefficient_checks=min_checks=reconstruction_checks=0
for n in range(2,MAX_ORDER+1):
    for prof in partitions(n):
        if len(prof)<2: continue
        profiles+=1
        got=Counter()
        for lab in product((0,1,2), repeat=n):
            labelings+=1
            a=literal_ir(prof,lab); b=criterion(prof,lab)
            if a!=b: raise AssertionError(('criterion',prof,lab,a,b))
            if a:
                valid+=1; got[sum(lab)]+=1
        want=formula(prof)
        for d in range(0,2*n+1):
            coefficient_checks+=1
            if got[d]!=want[d]: raise AssertionError(('coefficient',prof,d,got[d],want[d]))
        m=min(prof)
        min_checks+=1
        if min(got)!=m+1: raise AssertionError(('minimum',prof,min(got),m+1))
        cmin=sum(1 for x in prof if x==m)
        if got[m+1] != m*cmin: raise AssertionError(('min count',prof,got[m+1],m*cmin))
        reconstruction_checks+=1
        if reconstruct(want)!=prof: raise AssertionError(('reconstruct',prof,reconstruct(want)))
print(f'VERIFY_OK profiles={profiles} labelings={labelings} valid_functions={valid} coefficient_checks={coefficient_checks} min_checks={min_checks} reconstruction_checks={reconstruction_checks} max_order={MAX_ORDER}')
