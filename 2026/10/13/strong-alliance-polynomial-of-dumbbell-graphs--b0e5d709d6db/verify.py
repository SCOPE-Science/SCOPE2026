from collections import Counter
from math import comb

def h(m): return (m+2)//2

def g(m): return (m+3)//2

def predicted(r,s):
    c=Counter()
    for k in range(h(r),r): c[k]+=comb(r-1,k)
    for k in range(g(r),r+1): c[k]+=comb(r-1,k-1)
    for k in range(h(s),s): c[k]+=comb(s-1,k)
    for k in range(g(s),s+1): c[k]+=comb(s-1,k-1)
    for a in range(h(r),r+1):
        for b in range(h(s),s+1):
            c[a+b]+=comb(r-1,a-1)*comb(s-1,b-1)
    return c

def make_graph(r,s):
    N=r+s
    adj=[set() for _ in range(N)]
    for start,m in ((0,r),(r,s)):
        for i in range(start,start+m):
            for j in range(i+1,start+m):
                adj[i].add(j); adj[j].add(i)
    adj[0].add(r); adj[r].add(0)
    return adj

def is_strong_connected(mask,adj):
    verts=[i for i in range(len(adj)) if (mask>>i)&1]
    if not verts: return False
    seen={verts[0]}; stack=[verts[0]]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if ((mask>>y)&1) and y not in seen:
                seen.add(y); stack.append(y)
    if len(seen)!=len(verts): return False
    S=set(verts)
    for v in verts:
        inside=sum(w in S for w in adj[v])
        if inside < len(adj[v])-inside: return False
    return True

subset_checks=coefficient_checks=minimum_checks=0
max_order=0
for r in range(3,8):
    for s in range(3,8):
        adj=make_graph(r,s); N=r+s; max_order=max(max_order,N)
        actual=Counter()
        for mask in range(1,1<<N):
            subset_checks+=1
            if is_strong_connected(mask,adj): actual[mask.bit_count()]+=1
        pred=predicted(r,s)
        for k in range(N+1):
            coefficient_checks+=1
            assert actual[k]==pred[k], (r,s,k,actual[k],pred[k])
        assert min(actual)==min(h(r),h(s)), (r,s,min(actual))
        minimum_checks+=1

def is_unimodal_coefficients(c,r,s):
    lo=min(k for k,v in c.items() if v)
    vals=[c[k] for k in range(lo,r+s+1)]
    for mode in range(len(vals)):
        if all(vals[i] <= vals[i+1] for i in range(mode)) and all(vals[i] >= vals[i+1] for i in range(mode,len(vals)-1)):
            return True
    return False

formula_unimodality_checks=0
exceptions={(3,3),(3,5),(3,7)}
for r in range(3,41):
    for s in range(r,41):
        got=is_unimodal_coefficients(predicted(r,s),r,s)
        want=(r,s) in exceptions
        assert got==want, (r,s,got,want)
        formula_unimodality_checks+=1
print(f'VERIFY_OK pairs=25 subset_checks={subset_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} formula_unimodality_checks={formula_unimodality_checks} max_order={max_order}')
