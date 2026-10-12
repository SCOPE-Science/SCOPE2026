from collections import Counter
from itertools import product
from math import comb


def graph(r, m):
    n = 1 + r*m
    adj = [set() for _ in range(n)]
    c = 0
    blades = []
    for i in range(r):
        B = list(range(1+i*m, 1+(i+1)*m))
        blades.append(B)
        for v in B:
            adj[c].add(v); adj[v].add(c)
        for a in range(m):
            for b in range(a+1,m):
                u,v=B[a],B[b]
                adj[u].add(v); adj[v].add(u)
    return adj, blades


def dominating(S, adj):
    S=set(S)
    return all(v in S or any(u in S for u in adj[v]) for v in range(len(adj)))


def secure(S, adj):
    S=set(S)
    if not dominating(S, adj): return False
    for v in range(len(adj)):
        if v in S: continue
        ok=False
        for u in adj[v] & S:
            T=(S-{u})|{v}
            if dominating(T,adj):
                ok=True; break
        if not ok: return False
    return True


def structural(S, blades):
    S=set(S)
    occ=[sum(v in S for v in B) for B in blades]
    if 0 not in S:
        return all(a>=1 for a in occ)
    return sum(a==0 for a in occ)<=1


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def poly_pow(a,k):
    r=[1]
    for _ in range(k): r=poly_mul(r,a)
    return r


def formula(r,m):
    # A=(1+x)^m-1
    A=[0]+[comb(m,k) for k in range(1,m+1)]
    Ar=poly_pow(A,r)
    Arm1=poly_pow(A,r-1)
    out=[0]*(1+r*m+1)
    for k,v in enumerate(Ar): out[k]+=v
    for k,v in enumerate(Ar): out[k+1]+=v
    for k,v in enumerate(Arm1): out[k+1]+=r*v
    return out

pairs=[]
subset_checks=0
secure_sets=0
structural_checks=0
coefficient_checks=0
max_order=0
for r in range(2,5):
    for m in range(2,5):
        n=1+r*m
        if n>13: continue
        pairs.append((r,m))
        max_order=max(max_order,n)
        adj,blades=graph(r,m)
        cnt=Counter()
        for mask in range(1<<n):
            S={v for v in range(n) if (mask>>v)&1}
            subset_checks += 1
            a=secure(S,adj)
            b=structural(S,blades)
            structural_checks += 1
            assert a==b, (r,m,S,a,b)
            if a:
                cnt[len(S)]+=1
                secure_sets += 1
        f=formula(r,m)
        for k in range(n+1):
            coefficient_checks += 1
            assert cnt[k]==f[k], (r,m,k,cnt[k],f[k])
        minimum=min(cnt)
        assert minimum==r
        assert cnt[r]==m**(r-1)*(m+r)

print(f"VERIFY_OK parameter_pairs={len(pairs)} subset_checks={subset_checks} secure_sets={secure_sets} structural_checks={structural_checks} coefficient_checks={coefficient_checks} max_order={max_order}")
