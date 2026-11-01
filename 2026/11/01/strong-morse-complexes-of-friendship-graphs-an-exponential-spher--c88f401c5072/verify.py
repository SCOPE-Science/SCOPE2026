"""Finite, exhaustive checks for strong Morse complexes of friendship graphs.

Requires only Python 3.9+; run `python3 verify.py`.
The infinite-family classification is proven separately by the cone decomposition.
"""
from itertools import permutations, combinations, product
from math import factorial


def encode(m):
    c = 2*m
    edges = set()
    for i in range(m):
        a,b = 2*i,2*i+1
        for u,v in ((a,b),(a,c),(b,c)):
            edges.add(frozenset((u,v)))
    directed = sorted([(u,v) for e in edges for u in e for v in e if u != v])
    return edges, directed


def from_orders(m, edges, ids):
    n=2*m+1
    faces={0}
    order_count=0
    for order in permutations(range(n)):
        seen=set()
        s=0
        for u in order:
            earlier=[v for v in seen if frozenset((u,v)) in edges]
            if len(earlier)==1:
                s |= 1 << ids[(u, earlier[0])]
            seen.add(u)
        subs=s
        while True:
            faces.add(subs)
            if subs==0: break
            subs=(subs-1)&s
        order_count+=1
    assert order_count==factorial(n)
    return faces, order_count


def predicted(m, ids):
    c=2*m
    per=[]
    hubs=[]
    inward=[]
    for i in range(m):
        a,b=2*i, 2*i+1
        per.append([ids[(a,b)],ids[(b,a)],ids[(a,c)],ids[(b,c)]])
        inward.append([ids[(a,c)],ids[(b,c)]])
        hubs.append([ids[(c,a)],ids[(c,b)]])
    faces=set()
    for picks in product(*[[None]+g for g in per]):
        faces.add(sum(1<<x for x in picks if x is not None))
    for i in range(m):
        for h in hubs[i]:
            others=[[None]+inward[j] for j in range(m) if j!=i]
            for picks in product(*others):
                faces.add((1<<h) | sum(1<<x for x in picks if x is not None))
    return faces


def gf2_rank(cols):
    basis={}
    for v in cols:
        while v:
            t=v.bit_length()-1
            if t in basis: v^=basis[t]
            else:
                basis[t]=v
                break
    return len(basis)


def reduced_betti(faces):
    bydim={}
    for f in faces:
        if not f: continue
        d=f.bit_count()-1
        bydim.setdefault(d,[]).append(f)
    dim=max(bydim)
    ranks={-1:0,0:1,dim+1:0}
    for d in range(1,dim+1):
        rows={face:j for j,face in enumerate(bydim[d-1])}
        columns=[]
        for f in bydim[d]:
            v=0
            bits=f
            while bits:
                low=bits & -bits
                sub=f^low
                v^=1<<rows[sub]
                bits^=low
            columns.append(v)
        ranks[d]=gf2_rank(columns)
    return [len(bydim[d])-ranks[d]-ranks.get(d+1,0) for d in range(dim+1)], tuple(len(bydim[d]) for d in range(dim+1))


def main():
    for m in range(1,5):
        edges, directed=encode(m)
        ids={e:j for j,e in enumerate(directed)}
        exhaustive,norders=from_orders(m, edges, ids)
        expected=predicted(m,ids)
        assert exhaustive==expected, (m, len(exhaustive^expected))
        bettis,fvec=reduced_betti(expected)
        expected_b=[0]*m
        expected_b[m-1]=3**m+2*m
        if m==1:
            # Reduced degree-zero homology has one fewer generator than H_0.
            expected_b[0]=3**m+2*m
        assert bettis==expected_b,(m,bettis,expected_b)
        assert len(directed)==6*m
        assert max(f.bit_count() for f in expected)==m
        print('EXHAUSTIVE_OK', 'm=',m,'vertex_orders=',norders,
              'directed_pairs=',len(directed),'faces=',len(expected)-1,
              'f_vector=',fvec,'reduced_mod2_betti=',bettis)
    print('ALL_VERIFY_OK')

if __name__=='__main__': main()
