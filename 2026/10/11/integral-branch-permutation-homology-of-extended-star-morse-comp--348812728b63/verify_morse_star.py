"""Exact finite checks for the natural branch-permutation action on the
integral top homology of the discrete Morse complex of a two-edge spider.
Python 3, standard library only. No external data files.
"""
from itertools import permutations, combinations
from math import factorial


def make_complex(n):
    """A Morse face is a Hasse-graph matching because the underlying graph is a tree."""
    c = ('c', -1)
    edges = []
    for i in range(n):
        a,b = ('a',i),('b',i)
        edges.extend([(c,a),(a,b)])
    vertices = [(v,e) for e in edges for v in e]
    masks = [0]*len(vertices)
    for i,(v,e) in enumerate(vertices):
        for j,(w,f) in enumerate(vertices):
            if i != j and (v==w or e==f):
                masks[i] |= 1<<j
    faces = [0]
    for i in range(len(vertices)):
        faces += [F|(1<<i) for F in list(faces) if F&masks[i]==0]
    assert len(set(faces)) == len(faces)
    return vertices, faces


def permute_node(v,p):
    return v if v[0]=='c' else (v[0],p[v[1]])


def induced_perm(vertices,p):
    lookup = {v:i for i,v in enumerate(vertices)}
    perm = []
    for v,e in vertices:
        v2 = permute_node(v,p)
        e2 = tuple(permute_node(w,p) for w in e)
        perm.append(lookup[(v2,e2)])
    return perm


def inversion_sign(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))


def face_character(vertices, faces, p):
    pi=induced_perm(vertices,p)
    total=-1  # augmented empty face degree -1
    for F in faces[1:]:
        indices=[i for i in range(len(vertices)) if F>>i&1]
        mapped=[pi[i] for i in indices]
        if set(indices)==set(mapped):
            total+=(-1)**(len(indices)-1)*inversion_sign(mapped)
    return total


def permutation_sign(p):
    return inversion_sign(p)


def gf2_rank(columns):
    pivots={}
    for vec in columns:
        while vec:
            p=vec.bit_length()-1
            if p in pivots: vec ^= pivots[p]
            else:
                pivots[p]=vec
                break
    return len(pivots)


def betti_mod2(faces):
    face_by_dimension={}
    for F in faces:
        k=F.bit_count()-1
        face_by_dimension.setdefault(k,[]).append(F)
    ranks={}
    for k in range(0,max(face_by_dimension)+1):
        prev=face_by_dimension[k-1]
        index={f:i for i,f in enumerate(prev)}
        columns=[]
        for F in face_by_dimension.get(k,[]):
            v=0
            indices=[i for i in range(F.bit_length()) if F>>i&1]
            for i in indices:
                v |= 1<<index[F^(1<<i)]
            columns.append(v)
        ranks[k]=gf2_rank(columns)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in face_by_dimension.items()}


def check():
    cases=0
    for n in range(2,6):
        vertices,faces=make_complex(n)
        assert len(faces)==5**n+n*3*5**(n-1), (n,len(faces))
        if n<=4:
            b=betti_mod2(faces)
            assert {i:r for i,r in b.items() if r}=={n:n-1}, (n,b)
        for p in permutations(range(n)):
            actual=(-1)**n * face_character(vertices,faces,p)
            fixed=sum(i==p[i] for i in range(n))
            expected=permutation_sign(p)*(fixed-1)
            assert actual==expected,(n,p,actual,expected)
            cases+=1
    print('VERIFY_OK', 'all_group_elements=',cases,'mod2_complete_for_n=',list(range(2,5)))

if __name__=='__main__':
    check()
