"""Direct finite homology checks from edge-by-edge admissible face generation.

Use Python 3: python3 homology_check.py. This does not use the
face generation or the matching construction from verify.py.
"""
from collections import defaultdict


def arcs(n):
    return [a for i in range(n) for a in (
        (0,2*i+1),(2*i+1,0),(0,2*i+2),(2*i+2,0),
        (2*i+1,2*i+2),(2*i+2,2*i+1))]


def valid(chosen):
    nxt = {}
    prev = {}
    for a,b in chosen:
        if a in nxt or b in prev:
            return False
        nxt[a] = b
        prev[b] = a
    for a in nxt:
        seen = set()
        while a in nxt:
            if a in seen:
                return False
            seen.add(a)
            a = nxt[a]
    return True


def all_faces(n):
    al = arcs(n)
    levels = defaultdict(list)
    levels[-1] = [0]
    # Enumerate in increasing cardinality, adding edges with increasing label.
    def rec(start,mask,chosen):
        for j in range(start,len(al)):
            extended=chosen+[al[j]]
            if valid(extended):
                m=mask|(1<<j)
                levels[len(extended)-1].append(m)
                rec(j+1,m,extended)
    rec(0,0,[])
    return levels


def rank_mod_two(columns, row_indices):
    pivots = {}
    for face in columns:
        x=face;vec=0
        while x:
            b=x&(-x);x-=b
            vec ^= 1<<row_indices[face^b]
        while vec:
            p=vec.bit_length()-1
            if p not in pivots:
                pivots[p]=vec
                break
            vec ^= pivots[p]
    return len(pivots)


def check(n):
    levels=all_faces(n)
    ds=sorted(k for k in levels if k>=0)
    counts={d:len(levels[d]) for d in ds}
    r={}
    for d in ds:
        if d>0:
            r[d]=rank_mod_two(levels[d],{f:k for k,f in enumerate(levels[d-1])})
    beta={d:counts[d]-r.get(d,0)-r.get(d+1,0) for d in ds}
    if n==1:
        assert beta=={0:2,1:2}
    else:
        assert beta[0]==1
        assert {k:v for k,v in beta.items() if k>0 and v}=={n-1:1,n:2*n}
    print('n=%d f_vector=%s mod2_betti=%s'% (n,[counts[d] for d in ds],beta))

if __name__=='__main__':
    for n in range(1,6):
        check(n)
    print('ALL_HOMOLOGY_CHECKS_PASSED')
