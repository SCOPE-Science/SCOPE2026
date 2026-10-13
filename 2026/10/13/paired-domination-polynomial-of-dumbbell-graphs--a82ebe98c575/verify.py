from collections import Counter
from math import comb


def graph(r,s):
    n=r+s
    adj=[0]*n
    for i in range(r):
        for j in range(i+1,r):
            adj[i]|=1<<j; adj[j]|=1<<i
    for i in range(r,n):
        for j in range(i+1,n):
            adj[i]|=1<<j; adj[j]|=1<<i
    u=0; v=r
    adj[u]|=1<<v; adj[v]|=1<<u
    return adj,u,v


def dominates(mask,adj):
    full=(1<<len(adj))-1
    cover=mask
    x=mask
    while x:
        b=x & -x; i=b.bit_length()-1; cover |= adj[i]; x-=b
    return cover==full


def has_perfect_matching(mask,adj,memo):
    if mask==0: return True
    if mask.bit_count()%2: return False
    if mask in memo: return memo[mask]
    b=mask & -mask; i=b.bit_length()-1
    candidates=adj[i] & (mask^b)
    while candidates:
        c=candidates & -candidates
        if has_perfect_matching(mask^b^c,adj,memo):
            memo[mask]=True; return True
        candidates-=c
    memo[mask]=False; return False


def predicted(mask,r,s,u,v):
    L=mask & ((1<<r)-1)
    R=(mask>>r) & ((1<<s)-1)
    a=L.bit_count(); b=R.bit_count()
    if a==0 or b==0: return False
    if a%2==0 and b%2==0: return True
    if a%2==1 and b%2==1:
        return bool(mask&(1<<u)) and bool(mask&(1<<v))
    return False


def poly_formula(r,s):
    c=Counter()
    for a in range(2,r+1,2):
        for b in range(2,s+1,2):
            c[a+b]+=comb(r,a)*comb(s,b)
    for a0 in range(0,r,2):
        for b0 in range(0,s,2):
            c[2+a0+b0]+=comb(r-1,a0)*comb(s-1,b0)
    return c

subset_checks=paired_sets=structural_checks=coefficient_checks=minimum_checks=0
for r in range(2,8):
    for s in range(2,8):
        if r+s>12: continue
        adj,u,v=graph(r,s); n=r+s; memo={}
        actual=Counter(); mins=[]
        for mask in range(1<<n):
            subset_checks+=1
            ok=dominates(mask,adj) and has_perfect_matching(mask,adj,memo)
            pred=predicted(mask,r,s,u,v)
            structural_checks+=1
            if ok!=pred:
                raise AssertionError(('criterion',r,s,mask,ok,pred))
            if ok:
                k=mask.bit_count(); actual[k]+=1; paired_sets+=1
                mins.append((k,mask))
        expected=poly_formula(r,s)
        if actual!=expected:
            raise AssertionError(('poly',r,s,actual,expected))
        coefficient_checks += len(set(actual)|set(expected))
        m=min(k for k,_ in mins)
        min_masks=[mask for k,mask in mins if k==m]
        if m!=2 or min_masks!=[(1<<u)|(1<<v)]:
            raise AssertionError(('minimum',r,s,m,min_masks))
        minimum_checks+=1
        total_formula=(2**(r-1)-1)*(2**(s-1)-1)+2**(r+s-4)
        if sum(actual.values())!=total_formula:
            raise AssertionError(('total',r,s,sum(actual.values()),total_formula))
print(f'VERIFY_OK pairs={minimum_checks} subset_checks={subset_checks} paired_sets={paired_sets} structural_checks={structural_checks} coefficient_checks={coefficient_checks} max_order=12')
