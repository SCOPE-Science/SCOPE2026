from itertools import product, combinations
from math import comb

def cocktail_party(n):
    N=2*n
    adj=[set(range(N))-{v} for v in range(N)]
    for i in range(n):
        a,b=2*i,2*i+1
        adj[a].discard(b); adj[b].discard(a)
    return adj

def is_mdrdf(adj, lab):
    n=len(adj)
    Z={v for v,x in enumerate(lab) if x==0}
    # double Roman conditions
    for v,x in enumerate(lab):
        if x==0:
            if not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2):
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    # V0 must not dominate G (domination uses closed neighborhoods)
    dominated=set(Z)
    for z in Z:
        dominated.update(adj[z])
    return len(dominated)<n

def expected(n):
    N=2*n
    out=set()
    for z in range(N):
        mate=z^1
        eligible=[v for v in range(N) if v not in (z,mate)]
        for p,q in combinations(eligible,2):
            lab=[1]*N
            lab[z]=0
            lab[p]=lab[q]=2
            out.add(tuple(lab))
    return out

print('VERIFY_OK')
checked=0
for n in range(2,6):
    adj=cocktail_party(n)
    best=10**9
    mins=[]
    for lab in product(range(4), repeat=2*n):
        checked += 1
        w=sum(lab)
        if w>best:
            continue
        if is_mdrdf(adj,lab):
            if w<best:
                best=w; mins=[]
            mins.append(tuple(lab))
    exp=expected(n)
    assert best==2*n+1,(n,best)
    assert set(mins)==exp,(n,len(mins),len(exp),set(mins)^exp)
    assert len(mins)==2*n*comb(2*n-2,2)
    print(f'n={n}: gamma_m_dR={best}, minimum_functions={len(mins)}')
print('labelings_checked =',checked)
print('all minimum functions matched the singleton-zero/two-2 classification')
