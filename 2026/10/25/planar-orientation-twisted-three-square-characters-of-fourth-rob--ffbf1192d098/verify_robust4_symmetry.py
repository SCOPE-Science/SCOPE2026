"""Exact homotopy and symmetry checks for the small fourth robust grid complexes.
Run: python3 verify_robust4_symmetry.py
Only Python standard library required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

CASES = ((3, 3, 4, 389, 192), (3, 4, 20, 1415, 697), (3, 5, 56, 3641, 1792), (4, 4, 84, 4811, 2363))

def graph(m, n):
    edges = {(i*n+j, (i+1)*n+j) for i in range(m-1) for j in range(n)}
    edges |= {(i*n+j, i*n+j+1) for i in range(m) for j in range(n-1)}
    return edges

def cells(m, n):
    N=m*n; edges=graph(m,n)
    independent_four = []
    for S in combinations(range(N), 4):
        if all((a,b) not in edges for a,b in combinations(S,2)):
            independent_four.append(sum(1<<v for v in S))
    faces={s for s in range(1,1<<N) if not any((s & b)==b for b in independent_four)}
    assert faces and all(s > 0 for s in faces)
    return faces, independent_four

def matching(faces, N):
    free=set(faces);pairs=[]
    for vertex in range(N):
        bit=1<<vertex
        for a in sorted(free):
            if not (a&bit) and (a|bit) in free:
                free.remove(a);free.remove(a|bit);pairs.append((a,a|bit))
    assert len(faces)==2*len(pairs)+len(free)
    return pairs,free

def verify_acyclic(faces,pairs):
    pairset=set(pairs)
    assert len(pairset)==len(pairs)
    assert all(a in faces and b in faces and (b^a).bit_count()==1 and a.bit_count()+1==b.bit_count() for a,b in pairs)
    assert len(set(v for pair in pairs for v in pair))==2*len(pairs)
    out=defaultdict(list);indegree={s:0 for s in faces};edgecount=0
    for high in faces:
        for bit in (1<<i for i in range(high.bit_length()) if high & (1<<i)):
            low=high ^ bit
            if low not in faces:
                continue
            source,target=(low,high) if (low,high) in pairset else (high,low)
            out[source].append(target);indegree[target]+=1;edgecount+=1
    queue=deque(s for s in faces if not indegree[s]);visited=0
    while queue:
        source=queue.popleft();visited+=1
        for target in out[source]:
            indegree[target]-=1
            if indegree[target]==0:queue.append(target)
    assert visited==len(faces), f'cyclic Morse graph: {visited} of {len(faces)}'
    return edgecount

def coordinate_maps(m,n):
    maps={'identity': lambda i,j: (i,j),
          'horizontal': lambda i,j: (m-1-i,j),
          'vertical': lambda i,j: (i,n-1-j),
          'half_turn': lambda i,j: (m-1-i,n-1-j)}
    if m==n:
        maps.update({'quarter_turn': lambda i,j:(j,n-1-i),
                     'three_quarter_turn': lambda i,j:(n-1-j,i),
                     'main_diagonal': lambda i,j:(j,i),
                     'other_diagonal': lambda i,j:(n-1-j,n-1-i)})
    return maps

def permutation(m,n,mapping):
    return tuple((lambda x: x[0]*n+x[1])(mapping(i,j)) for i in range(m) for j in range(n))

def signed_cell_lefschetz(faces,vertex_perm):
    total=0
    for face in faces:
        v=[i for i in range(len(vertex_perm)) if face & (1<<i)]
        pv=[vertex_perm[i] for i in v]
        if sum(1<<w for w in pv)!=face:
            continue
        inv=sum(pv[i]>pv[j] for i in range(len(pv)) for j in range(i+1,len(pv)))
        total+=(-1 if (len(v)-1+inv)%2 else 1)
    return total

def square_fixed_triples(m,n,mapping):
    # Label each elementary square by its upper-left grid coordinate.
    square_count=(m-1)*(n-1)
    squares=[{(i,j),(i+1,j),(i,j+1),(i+1,j+1)} for i in range(m-1) for j in range(n-1)]
    perm=[]
    for sq in squares:
        image={mapping(*ij) for ij in sq}
        perm.append(squares.index(image))
    fixed=0
    for triple in combinations(range(square_count),3):
        if {perm[i] for i in triple}==set(triple):fixed+=1
    return fixed

def main():
    expected={
       (3,3):{'identity':4,'horizontal':0,'vertical':0,'half_turn':0,'quarter_turn':0,'three_quarter_turn':0,'main_diagonal':-2,'other_diagonal':-2},
       (3,4):{'identity':20,'horizontal':0,'vertical':-4,'half_turn':0},
       (3,5):{'identity':56,'horizontal':0,'vertical':0,'half_turn':0},
       (4,4):{'identity':84,'horizontal':-10,'vertical':-10,'half_turn':4,'quarter_turn':0,'three_quarter_turn':0,'main_diagonal':-10,'other_diagonal':-10},
    }
    for m,n,b,face_count,match_count in CASES:
        faces,indep=cells(m,n)
        assert len(faces)==face_count
        pairs,critical=matching(faces,m*n)
        assert len(pairs)==match_count
        assert Counter(x.bit_count()-1 for x in critical)=={0:1,5:b}
        incidences=verify_acyclic(faces,pairs)
        char={}
        for name,mapping in coordinate_maps(m,n).items():
            p=permutation(m,n,mapping)
            assert len(set(p))==m*n
            edges=graph(m,n)
            assert {(min(p[a],p[b]),max(p[a],p[b])) for a,b in edges}==edges
            # Only H_5 contributes to reduced Lefschetz number.
            top_trace=1-signed_cell_lefschetz(faces,p)
            # Euclidean orientation: identity and rotations +1, reflections -1.
            determinant=-1 if name in ('horizontal','vertical','main_diagonal','other_diagonal') else 1
            triplet_trace=determinant*square_fixed_triples(m,n,mapping)
            assert top_trace==triplet_trace==expected[(m,n)][name]
            char[name]=top_trace
        print(f'{m}x{n}: independent-four={len(indep)} faces={len(faces)} '
              f'matched={len(pairs)} critical=(1 vertex,{b} five-cells) '
              f'face-incidences={incidences} character={char}')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    main()
