# Direct verifier for self- and solid-locating-dominating codes on crown graphs.
from math import comb

def crown_closed(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return [{v}|adj[v] for v in range(2*n)]

def is_dld(n,C):
    if not C: return False
    closed=crown_closed(n); out=[v for v in range(2*n) if v not in C]
    Is={v:closed[v]&C for v in out}
    if any(not Is[v] for v in out): return False
    return all(u==v or bool(Is[u]-Is[v]) for u in out for v in out)

def is_sld(n,C):
    if not C: return False
    closed=crown_closed(n)
    for u in range(2*n):
        if u in C: continue
        iu=closed[u]&C
        if not iu: return False
        inter=set(range(2*n))
        for c in iu: inter &= closed[c]
        if inter!={u}: return False
    return True

def pred_dld(n,C):
    P={i for i in range(n) if i not in C}
    Q={i for i in range(n) if n+i not in C}
    if P==Q and len(P)==1: return True
    if P&Q: return False
    if len(P)==1:
        i=next(iter(P))
        if Q==set(range(n))-{i}: return False
    if len(Q)==1:
        i=next(iter(Q))
        if P==set(range(n))-{i}: return False
    return True

def pred_sld(n,C):
    P={i for i in range(n) if i not in C}
    Q={i for i in range(n) if n+i not in C}
    return (not P) or (not Q) or (P==Q and len(P)==1)

def formula(n,kind):
    a=[0]*(2*n+1)
    if kind=="dld":
        for j in range(n+1): a[n+j]+=comb(n,j)*2**(n-j)
        a[n]-=2*n
        a[2*n-2]+=n
    else:
        for j in range(n+1): a[n+j]+=2*comb(n,j)
        a[2*n]-=1
        a[2*n-2]+=n
    return a

total=0
print("VERIFY_OK")
for n in range(3,9):
    cd=[0]*(2*n+1); cs=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
        C={v for v in range(2*n) if mask>>v & 1}
        d=is_dld(n,C); s=is_sld(n,C)
        assert d==pred_dld(n,C),(n,mask,d,pred_dld(n,C))
        assert s==pred_sld(n,C),(n,mask,s,pred_sld(n,C))
        if d: cd[len(C)]+=1
        if s: cs[len(C)]+=1
        total+=1
    assert cd==formula(n,"dld")
    assert cs==formula(n,"sld")
    gd=next(i for i,c in enumerate(cd) if c)
    gs=next(i for i,c in enumerate(cs) if c)
    print(f"n={n}: DLD_min={gd}, DLD_bases={cd[gd]}, SLD_min={gs}, SLD_bases={cs[gs]}")
print("vertex_subsets_checked =",total)
