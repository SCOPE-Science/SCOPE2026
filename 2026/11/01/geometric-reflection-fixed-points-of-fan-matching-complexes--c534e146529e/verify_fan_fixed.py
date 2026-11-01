#!/usr/bin/env python3
"""Independent finite orbit enumeration for reflection fixed sets of fan matching complexes."""
from itertools import combinations

def run(n):
    assert n >= 3
    edges = {('s', i): frozenset((0, i)) for i in range(1, n+1)}
    edges.update({('e', i): frozenset((i, i+1)) for i in range(1, n)})
    def reflect(x):
        return 0 if x == 0 else n+1-x
    def re(x):
        return next(k for k,v in edges.items() if v==frozenset(reflect(a) for a in edges[x]))
    unseen=set(edges)
    orbits=[]
    while unseen:
        a=min(unseen)
        b=re(a)
        orbit=tuple(sorted({a,b}))
        unseen.difference_update(orbit)
        if len(set().union(*(edges[e] for e in orbit)))==2*len(orbit):
            orbits.append(orbit)
    orbits.sort()
    masksets=[set().union(*(edges[e] for e in orbit)) for orbit in orbits]
    adj=set()
    for i,j in combinations(range(len(orbits)),2):
        if masksets[i] & masksets[j]:adj.add((i,j))
    expected=[]
    if n%2==0:
        m=n//2
        labels=[('e',i) for i in range(1,m+1)]
    else:
        m=(n-1)//2
        labels=[('e',i) for i in range(1,m)]+[('s',m+1)]
    for label in labels:
        found=next((idx for idx,o in enumerate(orbits) if label in o),None)
        assert found is not None, (n,label,orbits)
        expected.append(found)
    assert set(expected)==set(range(len(orbits)))
    for a,b in combinations(range(len(expected)),2):
        must=(a<len(expected)-int(n%2) and b<len(expected)-int(n%2) and b==a+1) if n%2 else (b==a+1)
        assert ((min(expected[a],expected[b]),max(expected[a],expected[b])) in adj)==must, (n,a,b,orbits,adj,must)
    fixed_face_count=0
    alternating=0
    for bits in range(1<<len(orbits)):
        chosen=[i for i in range(len(orbits)) if (bits>>i)&1]
        if any((i,j) in adj for i,j in combinations(chosen,2)):continue
        fixed_face_count+=1
        alternating+=(-1)**len(chosen)
    # The reduced Lefschetz number of a simplicial automorphism is minus
    # the signed count of invariant faces, including the empty face.
    red_lefschetz=-alternating
    # Independently evaluate graph independence polynomial on the model.
    size=m if n%2==0 else m-1
    path_alt=0
    for bits in range(1<<size):
        if bits & (bits<<1):continue
        path_alt+=(-1)**bits.bit_count()
    model_alt=path_alt if n%2==0 else 0
    assert alternating==model_alt, (n,alternating,model_alt)
    return n,len(orbits),len(adj),fixed_face_count,red_lefschetz

if __name__=='__main__':
    for n in range(3,25):
        print('n,orbits,conflicts,faces,reduced_L',*run(n))
    print('ALL TESTS PASSED')

# Additional independent finite simplicial homology check, with augmented chains.
def ranks_mod2(n):
    # Use the closed-form model only to determine the expected chain ranks;
    # admissibility was independently verified against original fan edges above.
    k=n//2 if n%2==0 else (n-3)//2
    cone=n%2==1
    q=k+int(cone)
    faces=[bits for bits in range(1<<q) if not ((bits&((1<<k)-1))&((bits&((1<<k)-1))<<1))]
    dims={d:[] for d in range(-1,q)}
    for bits in faces:dims[bits.bit_count()-1].append(bits)
    def rank_mod2(rows):
        basis={}
        for a in rows:
            while a:
                p=a.bit_length()-1
                if p not in basis:
                    basis[p]=a;break
                a^=basis[p]
        return len(basis)
    bs={}
    for d in range(0,q):
        lo={b:i for i,b in enumerate(dims[d-1])}
        rows=[]
        for face in dims[d]:
            boundary=0
            for j in range(q):
                if face>>j&1:boundary ^= 1<<lo[face^(1<<j)]
            rows.append(boundary)
        bs[d]=rank_mod2(rows)
    betti={}
    for d in range(0,q):
        b=len(dims[d])-bs.get(d,0)-bs.get(d+1,0)
        if b:betti[d]=b
    reduced_zero = len(dims[0])-bs.get(0,0)-bs.get(1,0)
    if reduced_zero:betti[0]=reduced_zero
    # Above chain includes empty face; degree 0 returns reduced Betti.
    return betti

if __name__=='__main__':
    for n in range(3,19):
        got=ranks_mod2(n)
        if n%2:
            expected={}
        else:
            m=n//2
            expected={} if m%3==1 else ({m//3-1:1} if m%3==0 else {m//3:1})
        assert got==expected, (n,got,expected)
        print('n,mod2_reduced_homology',n,got)
    print('HOMOLOGY CHECKS PASSED')
