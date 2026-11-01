#!/usr/bin/env python3
"""Reproducible finite checks of the ordinary 3-cut Alexander dual for Cartesian products of cliques.
No external packages are required; the all-parameter proof is in RESULT.md.
"""
from itertools import combinations, product
from math import comb, prod


def mod2_rank(columns):
    pivot = {}
    for x in columns:
        while x:
            k = x.bit_length()-1
            if k in pivot:
                x ^= pivot[k]
            else:
                pivot[k] = x
                break
    return len(pivot)


def verify(sizes):
    d = len(sizes)
    vertices = list(product(*(range(q) for q in sizes)))
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    dist = lambda x,y: sum(a != b for a,b in zip(vertices[x],vertices[y]))
    connected3 = set()
    for t in combinations(range(n),3):
        a,b,c=t
        if (dist(a,b)==1 and dist(a,c)==1) or (dist(a,b)==1 and dist(b,c)==1) or (dist(a,c)==1 and dist(b,c)==1):
            connected3.add(t)
    # Independent direct test of every possible 3-wise-connected subset.
    faces={1: set((i,) for i in range(n)),
           2: set(combinations(range(n),2)),
           3: connected3}
    highest=max(max(sizes),4)
    for k in range(4, highest+2):
        faces[k] = {t for t in combinations(range(n),k) if all(s in connected3 for s in combinations(t,3))}
    assert not faces[highest+1]
    lines=[]
    for i,q in enumerate(sizes):
        other=[j for j in range(d) if j!=i]
        for fixed in product(*(range(sizes[j]) for j in other)):
            line=[]
            for z in range(q):
                v=list(fixed)
                v.insert(i,z)
                line.append(index[tuple(v)])
            lines.append(tuple(sorted(line)))
    squares=set()
    for i,j in combinations(range(d),2):
        other=[k for k in range(d) if k not in (i,j)]
        for fixed in product(*(range(sizes[k]) for k in other)):
            for ai in combinations(range(sizes[i]),2):
                for aj in combinations(range(sizes[j]),2):
                    sq=[]
                    for a,b in product(ai,aj):
                        v=list(fixed)
                        v.insert(i,a)
                        v.insert(j,b)
                        sq.append(index[tuple(v)])
                    squares.add(tuple(sorted(sq)))
    long_edges={e for e in combinations(range(n),2) if dist(*e)>=3}
    expected_facets=[set(s) for s in lines]+[set(s) for s in squares]+[set(s) for s in long_edges]
    for k, observed in faces.items():
        expected={s for facet in expected_facets if len(facet)>=k for s in combinations(sorted(facet),k)}
        assert observed==expected, (sizes, k, len(observed), len(expected),len(observed^expected))
    edges = n*sum(q-1 for q in sizes)//2
    fans = sum(n//q*comb(q-1,2) for q in sizes)
    nsquares = sum(n//(sizes[i]*sizes[j])*comb(sizes[i],2)*comb(sizes[j],2) for i,j in combinations(range(d),2))
    mu=n-1-edges+fans+nsquares
    h = sum(1 for e in combinations(range(n),2) if dist(*e)>=3)
    h_formula = n*sum(prod(sizes[i]-1 for i in S) for k in range(3,d+1) for S in combinations(range(d),k))//2
    assert h==h_formula and len(squares)==nsquares
    ranks={}
    for k in range(2,highest+1):
        domain=sorted(faces[k]); basis={t:i for i,t in enumerate(sorted(faces[k-1]))}
        cols=[sum(1<<basis[s] for s in combinations(t,k-1)) for t in domain]
        ranks[k]=mod2_rank(cols)
    beta1=comb(n,2)-ranks[2]-ranks[3]
    beta2=len(faces[3])-ranks[3]-ranks.get(4,0)
    assert (beta1,beta2)==(h,mu), (sizes,beta1,beta2,h,mu)
    for k in range(3,highest):
        # Reduced homology in every dimension >=3 is zero.
        betti=len(faces[k+1])-ranks[k+1]-ranks.get(k+2,0)
        assert betti==0,(sizes,k,betti)
    print(f'FACTORS={sizes}; N={n}; f-vector='+str([len(faces[k]) for k in range(1,highest+1)])+
          f'; squares={nsquares}; mod2 H1={beta1}; H2={beta2}; higher=0; PASS')


if __name__=='__main__':
    for sizes in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,3,4),(2,2,5)]:
        verify(sizes)
    print('CARTESIAN_CLIQUE_ORDINARY_THREE_CUT_DUAL_CHECK_OK')
