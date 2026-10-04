import itertools
from functools import lru_cache
from scipy.optimize import linprog

def partitions(n,r,lo=1):
    if r==0:
        if n==0:
            yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1):
            break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def is_fort(mask,L):
    if mask==0:
        return False
    n=len(L)
    for v in range(n):
        if (mask>>v)&1:
            continue
        neighbors=sum(1 for u in range(n)
                      if ((mask>>u)&1) and L[u]!=L[v])
        if neighbors==1:
            return False
    return True

def minimal_forts_direct(parts):
    L=labels(parts)
    n=len(L)
    forts=[m for m in range(1,1<<n) if is_fort(m,L)]
    fortset=set(forts)
    out=[]
    for m in forts:
        sub=(m-1)&m
        minimal=True
        while sub:
            if sub in fortset:
                minimal=False
                break
            sub=(sub-1)&m
        if minimal:
            out.append(m)
    return out

def predicted_forts(parts):
    L=labels(parts)
    n=len(L)
    singleton_parts={i for i,a in enumerate(parts) if a==1}
    out=[]
    # Two vertices from one non-singleton part, or two singleton parts.
    for a,b in itertools.combinations(range(n),2):
        if L[a]==L[b] or (L[a] in singleton_parts and L[b] in singleton_parts):
            out.append((1<<a)|(1<<b))
    # Three distinct parts, at most one singleton part.
    for tri in itertools.combinations(range(n),3):
        ps=[L[v] for v in tri]
        if len(set(ps))==3 and sum(p in singleton_parts for p in ps)<=1:
            mask=0
            for v in tri:
                mask |= 1<<v
            out.append(mask)
    return sorted(set(out))

def count_formula(parts):
    q=sum(a==1 for a in parts)
    m=[a for a in parts if a>=2]
    e2=sum(m[i]*m[j] for i in range(len(m)) for j in range(i+1,len(m)))
    e3=sum(m[i]*m[j]*m[k]
           for i in range(len(m))
           for j in range(i+1,len(m))
           for k in range(j+1,len(m)))
    c2=sum(a*(a-1)//2 for a in m)+q*(q-1)//2
    c3=q*e2+e3
    return c2,c3

def fort_number_formula(parts):
    q=sum(a==1 for a in parts)
    m=[a for a in parts if a>=2]
    base=sum(a//2 for a in m)+q//2
    odd=sum(a%2 for a in m)
    eps=q%2
    return base+(odd+eps)//3

def fractional_formula(parts):
    N=sum(parts)
    q=sum(a==1 for a in parts)
    return (N-1)/2 if q==1 else N/2

def matching_number(n,edges):
    byv=[[] for _ in range(n)]
    for e in edges:
        for v in range(n):
            if (e>>v)&1:
                byv[v].append(e)
    @lru_cache(None)
    def dp(avail):
        if not avail:
            return 0
        low=avail & -avail
        v=low.bit_length()-1
        best=dp(avail & ~low)
        for e in byv[v]:
            if e & avail == e:
                best=max(best,1+dp(avail ^ e))
        return best
    return dp((1<<n)-1)

def fractional_number(n,edges):
    A=[]
    for e in edges:
        A.append([-1.0 if (e>>v)&1 else 0.0 for v in range(n)])
    res=linprog([1.0]*n,A_ub=A,b_ub=[-1.0]*len(A),
                bounds=[(0.0,None)]*n,method="highs")
    assert res.success
    return res.fun

types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            direct=minimal_forts_direct(parts)
            pred=predicted_forts(parts)
            subsets += (1<<N)-1
            assert direct==pred, (parts,direct,pred)

            c2,c3=count_formula(parts)
            assert sum(m.bit_count()==2 for m in direct)==c2
            assert sum(m.bit_count()==3 for m in direct)==c3
            assert all(m.bit_count() in (2,3) for m in direct)

            ft=matching_number(N,direct)
            assert ft==fort_number_formula(parts), (parts,ft,fort_number_formula(parts))

            zstar=fractional_number(N,direct)
            target=fractional_formula(parts)
            assert abs(zstar-target)<1e-8, (parts,zstar,target)
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("nonempty_vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("minimal-fort classification matched exactly")
print("size-2 and size-3 count formulas matched")
print("fort-number matching formula matched")
print("fractional zero-forcing LP formula matched")
