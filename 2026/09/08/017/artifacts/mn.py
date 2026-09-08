import sys, json, math, itertools, hashlib
from functools import lru_cache
from fractions import Fraction

def partitions(n, max_part=None):
    if n==0:
        yield ()
        return
    if max_part is None: max_part=n
    for first in range(min(max_part,n),0,-1):
        for rest in partitions(n-first, first):
            yield (first,)+rest

def part_list(n):
    return list(partitions(n))

def z_of(mu):
    from collections import Counter
    c=Counter(mu)
    z=1
    for i,m in c.items():
        z*= (i**m)*math.factorial(m)
    return z

def class_size(n, mu):
    return math.factorial(n)//z_of(mu)

def square_type(mu, n):
    from collections import Counter
    c=Counter(mu)
    out=[]
    # for each cycle length i with mult m: contributes
    for i,m in c.items():
        if i%2==1:
            out.extend([i]*m)
        else:
            j=i//2
            out.extend([j]*(2*m))
    out.sort(reverse=True)
    assert sum(out)==n
    return tuple(out)

# Murnaghan-Nakayama: chi^lam(mu)
# lam tuple, mu tuple (cycle type, order matters: take first part)

def conjugate(lam):
    if not lam: return ()
    m=max(lam)
    cols=[sum(1 for p in lam if p>c) for c in range(m)]
    return tuple(cols)

def rim_hooks(lam, k):
    # enumerate partitions nu subset lam with lam\nu rim hook of size k
    # brute force: subsets via cells; n<=12 so fine
    cells=[(r,c) for r in range(len(lam)) for c in range(lam[r])]
    S=set(cells)
    results=set()
    # rim hook = connected skew diagram with no 2x2 block
    # enumerate subsets of size k contained in lam
    from itertools import combinations
    if k==0:
        yield lam
        return
    seen=set()
    for combo in combinations(cells, k):
        T=set(combo)
        R=S-T
        # R must be Young diagram (partition): rows left-justified, cols top-justified, i.e. Ferrers
        # check: for each cell in R, all cells above and left in bounding? simpler: build row lengths
        # R rows: for each r, cells must be 0..a_r-1 contiguous
        ok=True
        rowlen={}
        for (r,c) in R:
            rowlen[r]=rowlen.get(r,0)+1
        for (r,c) in R:
            if c>=rowlen[r]: ok=False;break
            # all rows 0..c present? since contiguous from 0 needed: check min/max
        if not ok: continue
        # contiguity: row cells must be {0..a-1}
        for r,a in rowlen.items():
            for c in range(a):
                if (r,c) not in R: ok=False;break
            if not ok: break
        if not ok: continue
        # column condition: row lengths nonincreasing and rows consecutive from 0
        if R:
            maxr=max(r for r,c in R)
            for r in range(maxr+1):
                if r not in rowlen: ok=False;break
            if not ok: continue
            lens=[rowlen.get(r,0) for r in range(maxr+1)]
            for i in range(len(lens)-1):
                if lens[i]<lens[i+1]: ok=False;break
            if not ok: continue
        else:
            lens=[]
        nu=tuple(lens)
        # T connected (edge-adjacency)
        # BFS
        stack=[next(iter(T))]
        vis={stack[0]}
        while stack:
            r,c=stack.pop()
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nb=(r+dr,c+dc)
                if nb in T and nb not in vis:
                    vis.add(nb); stack.append(nb)
        if len(vis)!=k: continue
        # no 2x2 block in T
        bad=False
        for (r,c) in T:
            if (r+1,c) in T and (r,c+1) in T and (r+1,c+1) in T:
                bad=True;break
        if bad: continue
        # height = #rows occupied -1
        rows={r for r,c in T}
        ht=len(rows)-1
        key=(nu,ht)
        if key in seen: continue
        seen.add(key)
        yield (nu,ht)

_chi_cache={}
def chi(lam, mu):
    key=(lam,mu)
    if key in _chi_cache: return _chi_cache[key]
    if not lam and not mu:
        _chi_cache[key]=1; return 1
    if not mu:
        v=1 if not lam else 0
        _chi_cache[key]=v; return v
    if not lam:
        _chi_cache[key]=0; return 0
    if sum(lam)!=sum(mu):
        _chi_cache[key]=0; return 0
    k=mu[0]; rest=mu[1:]
    total=0
    for (nu,ht) in rim_hooks(lam,k):
        total+= ((-1)**ht)*chi(nu, rest)
    _chi_cache[key]=total
    return total

def char_table(n):
    parts=part_list(n)
    idx={p:i for i,p in enumerate(parts)}
    T=[[0]*len(parts) for _ in parts]
    for i,lam in enumerate(parts):
        for j,mu in enumerate(parts):
            T[i][j]=chi(lam,mu)
    return parts,T

def verify_orth(n, parts, T):
    fn=math.factorial(n)
    # row orthogonality: sum_mu |C| T[i][mu]T[j][mu] = fn delta
    import collections
    cs=[class_size(n,mu) for mu in parts]
    for i in range(len(parts)):
        for j in range(i,len(parts)):
            s=sum(cs[k]*T[i][k]*T[j][k] for k in range(len(parts)))
            if i==j:
                if s!=fn: return False,(i,j,s,fn)
            else:
                if s!=0: return False,(i,j,s,0)
    return True,None

def kron_g(n, parts, T, a, b, c):
    # g(a,b,c)
    fn=math.factorial(n)
    cs=[class_size(n,mu) for mu in parts]
    ia={p:i for i,p in enumerate(parts)}  # not needed
    s=sum(cs[k]*T[a][k]*T[b][k]*T[c][k] for k in range(len(parts)))
    assert s%fn==0, s
    return s//fn

def sym_split(n, parts, T, li, nu):
    # returns (g, m, s, a) with certificate sums
    fn=math.factorial(n)
    cs=[class_size(n,mu) for mu in parts]
    sq=[square_type(mu,n) for mu in parts]
    sqidx=[parts.index(t) for t in sq]
    g=sum(cs[k]*T[li][k]*T[li][k]*T[nu][k] for k in range(len(parts)))
    m=sum(cs[k]*T[li][sqidx[k]]*T[nu][k] for k in range(len(parts)))
    assert g%fn==0 and m%fn==0, (g,m)
    g//=fn; m//=fn
    assert (g+m)%2==0 and (g-m)%2==0
    return g,m,(g+m)//2,(g-m)//2

if __name__=="__main__":
    for n in [8,9,10,11,12]:
        _chi_cache.clear()
        parts,T=char_table(n)
        ok,info=verify_orth(n,parts,T)
        print(f"n={n} p={len(parts)} orth={ok} {info if not ok else ''}", flush=True)
        # dimension check: sum chi(1)^2
        # identity class is (1^n) which is last partition
        idx=parts.index(tuple([1]*n))
        dims=[T[i][idx] for i in range(len(parts))]
        print("  sumdimsq=",sum(d*d for d in dims),"n!=",math.factorial(n))
