"""Independent finite checks of the directed one-shortcut cycle multipath theorem.
Run with Python 3; no nonstandard packages.
"""
from itertools import combinations
from math import comb

def arcs(n,k):
    return [(i,(i+1)%n) for i in range(n)]+[(0,k)]

def is_forest(es):
    src, tgt, nxt = set(),set(),{}
    for u,v in es:
        if u in src or v in tgt: return False
        src.add(u);tgt.add(v);nxt[u]=v
    for u in nxt:
        v=u
        visited=set()
        while v in nxt:
            if v in visited: return False
            visited.add(v)
            v=nxt[v]
    return True

def predicted_ok(mask,n,k):
    bit=lambda q:bool(mask&(1<<q))
    if not bit(n):return (mask&((1<<n)-1)) != (1<<n)-1
    if bit(0) or bit(k-1):return False
    return not all(bit(q) for q in range(k,n))

def faces(n,k):
    es=arcs(n,k)
    f={}
    for mask in range(1<<(n+1)):
        chosen=[e for j,e in enumerate(es) if mask & (1<<j)]
        actual=is_forest(chosen)
        prediction=predicted_ok(mask,n,k)
        assert actual==prediction, ('predicate mismatch',n,k,mask,actual,prediction)
        if actual:f[mask]=mask.bit_count()-1
    return f

def rank_gf2(cols):
    piv={}
    for c in cols:
        while c:
            i=c.bit_length()-1
            if i in piv:c^=piv[i]
            else:piv[i]=c;break
    return len(piv)

def homology(faces):
    dims={d:[m for m,v in faces.items() if v==d] for d in set(faces.values())}
    max_d=max(dims)
    ranks={}
    for d in range(1,max_d+1):
        rows={m:i for i,m in enumerate(dims.get(d-1,[]))}
        cs=[]
        for m in dims.get(d,[]):
            boundary=0
            for j in range(m.bit_length()):
                if m & (1<<j):boundary^=1<<rows[m^(1<<j)]
            cs.append(boundary)
        ranks[d]=rank_gf2(cs)
    # d=0 reduced: subtract one dimension for augmentation rank.
    return {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d,v in dims.items() if d>=0}

def check_relative_collapse(f,n,k):
    # The vertex indexed 1 is the cone apex of the link of the added shortcut.
    # Descending-dimension elementary collapses pair each shortcut face lacking
    # index 1 with its enlargement by index 1.
    assert k>=3
    active=set(f)
    shortcut=1<<n
    apex=1<<1
    lows=sorted((mask for mask in f if mask&shortcut and not(mask&apex)),
                key=lambda m:(-m.bit_count(),-m))
    for lo in lows:
        hi=lo|apex
        assert hi in active and lo in active
        cof=[m for m in active if m!=lo and m&lo==lo]
        assert cof==[hi],(n,k,lo,cof)
        active.remove(lo);active.remove(hi)
    assert active=={m for m in f if not(m&shortcut)}
    return len(lows)

def run():
    checks=0;total_nonempty=0;collapse_pairs=0
    for n in range(4,11):
        for k in range(2,n):
            fs=faces(n,k)
            betti=homology(fs)
            exp={n-2:1}
            if k==2:exp[n-3]=1
            observed={d:b for d,b in betti.items() if b}
            assert observed==exp,(n,k,observed,exp)
            assert len(fs)==((1<<n)-1)+( (1<<(k-2)) * ((1<<(n-k))-1))
            # Exact formula: unchorded cycle has all proper subsets, and chord-containing faces exclude full upper block.
            if k>=3:collapse_pairs+=check_relative_collapse(fs,n,k)
            checks+=1;total_nonempty+=len(fs)-1
    print(f'PASS graph-independent validity predicates and full reduced mod-two Betti vectors in {checks} cases (n=4..10, 2<=k<n).')
    print(f'PASS exact face counts; {total_nonempty} nonempty faces enumerated.')
    print(f'PASS explicit elementary collapses for k>=3: {collapse_pairs} free-face pairs, leaving exactly the original cycle boundary.')
    print('VERIFY_OK')
if __name__=='__main__':run()
