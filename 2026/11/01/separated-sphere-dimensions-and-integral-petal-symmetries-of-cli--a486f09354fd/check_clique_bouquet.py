"""Reproducible finite checks of clique-free complexes of clique bouquets.

No external packages are required. All ranks are exact over the field of two
and the signed simplicial Lefschetz traces are computed over the integers.
"""
from math import comb
from itertools import permutations


def faces_for(sizes, t):
    blocks = []
    v = 1
    for s in sizes:
        assert s >= t >= 3
        blocks.append(tuple(range(v, v+s-1)))
        v += s-1
    out = {i: [] for i in range(-1,v)}
    for mask in range(1<<v):
        hub = bool(mask & 1)
        if all(sum((mask >> u)&1 for u in b) <= t-1-int(hub) for b in blocks):
            out[mask.bit_count()-1].append(mask)
    return out, blocks, v


def gf2_rank(columns):
    pivots = {}
    for column in columns:
        a = column
        while a:
            k = a.bit_length()-1
            if k in pivots:
                a ^= pivots[k]
            else:
                pivots[k] = a
                break
    return len(pivots)


def betti_mod_two(sizes, t):
    fs, _, _ = faces_for(sizes, t)
    dims = sorted(k for k in fs if k >= 0)
    ranks = {}
    for k in dims:
        if k == 0:
            ranks[k] = 1
            continue
        row_index = {s: i for i,s in enumerate(fs[k-1])}
        cols = []
        for s in fs[k]:
            col = 0
            remaining = s
            while remaining:
                lsb = remaining & -remaining
                col ^= 1 << row_index[s ^ lsb]
                remaining ^= lsb
            cols.append(col)
        ranks[k] = gf2_rank(cols)
    return {k: len(fs[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in dims}


def expected_betti(sizes,t):
    m = len(sizes)
    low = 1
    high = 1
    for s in sizes:
        low *= comb(s-2,t-2)
        high *= comb(s-2,t-1) if s-2>=t-1 else 0
    return {m*(t-2):low, m*(t-1)-1:high}


def permutation_trace_exterior_augmentation(p,r):
    n = len(p)
    cycles = []
    visited=set()
    for i in range(n):
        if i in visited: continue
        j=i; L=0
        while j not in visited:
            visited.add(j);j=p[j]; L+=1
        cycles.append(L)
    poly=[1]+[0]*r
    for L in cycles:
        if L<=r:
            coeff=-(-1)**L
            for d in range(r,L-1,-1):
                poly[d] += coeff*poly[d-L]
    qprev = 0
    for d in range(r+1):
        q = poly[d]-qprev
        qprev=q
    return qprev


def wreath_character(block_perm, inner_perms, r):
    m=len(block_perm); n=len(inner_perms[0])
    seen=set(); total=1
    for i in range(m):
        if i in seen: continue
        cycle=[];j=i
        while j not in seen:
            seen.add(j);cycle.append(j);j=block_perm[j]
        p=list(range(n))
        for b in cycle:
            p=[inner_perms[b][p[z]] for z in range(n)]
        total *= (-1)**(r*(len(cycle)-1))*permutation_trace_exterior_augmentation(p,r)
    return total


def sign_induced(mask, vertex_perm):
    domain=[i for i in range(len(vertex_perm)) if mask & (1<<i)]
    dest=[vertex_perm[i] for i in domain]
    if sorted(dest)!=domain:
        return 0
    inv=sum(dest[i]>dest[j] for i in range(len(dest)) for j in range(i+1,len(dest)))
    return (-1)**inv


def lefschetz_reduced(fs,vertex_perm):
    return sum(((-1) if k == -1 else (-1)**k)*sign_induced(mask,vertex_perm)
               for k,faces in fs.items() for mask in faces)


def wreath_to_vertices(block_perm,inner_perms):
    m=len(block_perm); n=len(inner_perms[0]); out=[0]*(1+m*n)
    for i in range(m):
        for a in range(n):
            out[1+i*n+a]=1+block_perm[i]*n+inner_perms[i][a]
    return out


def test_homology():
    cases=[((3,3),3),((4,4),3),((4,4,4),3),((5,6),3),
           ((4,5),4),((5,5),4),((5,5,5),4),((5,4,6),3)]
    for sizes,t in cases:
        got=betti_mod_two(sizes,t)
        exp=expected_betti(sizes,t)
        assert all(got.get(d,0)==exp.get(d,0) for d in set(got)|set(exp)),(sizes,t,got,exp)
        print('HOMOLOGY',sizes,'t=',t,'nonzero=',{d:v for d,v in got.items() if v})
    return len(cases)


def test_characters():
    count=0
    for m,s,t in [(2,4,3),(3,4,3),(2,5,4),(3,4,4)]:
        fs,_,_=faces_for((s,)*m,t)
        inner_choices=[tuple(range(s-1)), tuple(reversed(range(s-1))),
                       tuple(list(range(1,s-1))+[0])]
        for bperm in permutations(range(m)):
            for inner_idx in range(len(inner_choices)**m):
                k=inner_idx; inners=[]
                for _ in range(m):
                    inners.append(inner_choices[k%len(inner_choices)])
                    k//=len(inner_choices)
                pv=wreath_to_vertices(bperm,inners)
                actual=lefschetz_reduced(fs,pv)
                chigh=wreath_character(bperm,inners,t-1)
                clow=wreath_character(bperm,inners,t-2)
                predicted=(-1)**(m*(t-1)-1)*chigh+(-1)**(m*(t-2))*clow
                assert actual==predicted,(m,s,t,bperm,inners,actual,predicted)
                count+=1
        print('CHARACTERS',m,s,t,'passed')
    return count


if __name__=='__main__':
    a=test_homology();b=test_characters()
    print('SUCCESS:',a,'integral-formula mod-2 homology checks;',b,'integer equivariant Lefschetz checks')
