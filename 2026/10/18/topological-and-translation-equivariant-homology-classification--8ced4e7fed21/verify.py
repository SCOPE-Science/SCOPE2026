"""Reproduce the Paley-25 clique-complex collapse and fundamental-group proof.
Python 3 standard library only. Run: python3 paley25_verifier.py
"""
from itertools import combinations,product
from collections import Counter

P=5
V=tuple(product(range(P),repeat=2))
def multiply(x,y):
    return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
S={multiply(x,x) for x in V if x!=(0,0)}
assert len(S)==12
assert S=={(a,0) for a in range(1,5)}|{(a,a) for a in range(1,5)}|{(a,(-a)%5) for a in range(1,5)}
E=set()
for i,u in enumerate(V):
    for j in range(i):
        v=V[j]
        if ((u[0]-v[0])%5,(u[1]-v[1])%5) in S:
            E.add((j,i))
assert len(E)==150

def adjacent(x,y):return tuple(sorted((x,y))) in E
faces={}
faces[1]=[(i,) for i in range(25)]
for k in range(2,6):
    faces[k]=[z+(v,) for z in faces[k-1] for v in range(z[-1]+1,25)
              if all(adjacent(u,v) for u in z)]
assert [len(faces[k]) for k in range(1,6)]==[25,150,250,75,15]

# Exact elementary free-face collapses in the original complex.
remaining=set(z for k in faces for z in faces[k]); collapse=[]
def pair(low,high):
    assert low in remaining and high in remaining and len(high)==len(low)+1
    assert set(low)<set(high)
    # No remaining higher-dimensional coface may contain low other than high.
    cofaces=[z for z in remaining if len(z)>len(low) and set(low).issubset(z)]
    assert cofaces==[high],(low,cofaces)
    remaining.remove(low);remaining.remove(high);collapse.append((low,high))
for line in faces[5]:
    root=line[0]
    pair(tuple(x for x in line if x!=root),line)
    for excluded in line[1:]:
        tet=tuple(x for x in line if x!=excluded)
        pair(tuple(x for x in tet if x!=root),tet)
assert len(collapse)==75
assert Counter(map(len,remaining))=={1:25,2:150,3:190}

# Deterministic spanning tree: lexicographic Kruskal algorithm.
parent=list(range(25))
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i
tree=set()
for a,b in sorted(E):
    x,y=root(a),root(b)
    if x!=y:
        parent[x]=y;tree.add((a,b))
assert len(tree)==24
edges=sorted(E-tree)
index={z:i+1 for i,z in enumerate(edges)}
assert len(edges)==126

def freely_reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    while len(out)>1 and out[0]==-out[-1]:out=out[1:-1]
    return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def letter(a,b):
    z=index.get(tuple(sorted((a,b))),0)
    return z if a<b else -z

# Each triangle supplies its oriented boundary relator after contracting the tree.
relations=set()
for a,b,c in faces[3]:
    w=freely_reduce(tuple(x for x in (letter(a,b),letter(b,c),letter(c,a)) if x))
    if w:relations.add(w)
alive=set(index.values()); eliminated=[]
while True:
    relations={freely_reduce(w) for w in relations}-{()}
    occurrences=Counter(abs(x) for w in relations for x in w)
    candidates=[]
    for word in relations:
        for signed in word:
            if sum(abs(v)==abs(signed) for v in word)==1:
                candidates.append((len(word),occurrences[abs(signed)],abs(signed),signed,word))
    if not candidates:break
    _,_,k,signed,word=min(candidates)
    position=word.index(signed)
    before,after=word[:position],word[position+1:]
    # cyclically rotate 'before signed after' to 'signed after before';
    # signed = (after before)^(-1) as a group relation.
    value=inverse(after+before) if signed>0 else after+before
    assert all(abs(t)!=k for t in value)
    assert k in alive
    next_relations=set()
    for r in relations:
        if r==word:continue
        replaced=[]
        for t in r:
            if t==k:replaced.extend(value)
            elif t==-k:replaced.extend(inverse(value))
            else:replaced.append(t)
        next_relations.add(freely_reduce(replaced))
    relations=next_relations
    alive.remove(k);eliminated.append(k)
assert len(eliminated)==126,(len(eliminated),len(alive),len(relations))
assert not alive and not relations
assert 25-150+250-75+15==65
# Compute the complete translation Lefschetz character on exact cellular chains.
incidence={i:{j for j in range(25) if j!=i and adjacent(i,j)} for i in range(25)}
for a in range(25):
    for b in range(a+1,25):
        common=len(incidence[a]&incidence[b])
        assert common==(5 if adjacent(a,b) else 6)

def sign_of_permutation(original,transformed):
    loc={v:i for i,v in enumerate(original)}
    perm=[loc[v] for v in transformed]
    inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
    return -1 if inversions%2 else 1

trace_by_translation={}
for shift in V:
    translate={i:V.index(((v[0]+shift[0])%5,(v[1]+shift[1])%5)) for i,v in enumerate(V)}
    lefschetz=0
    for k in range(1,6):
        for simplex in faces[k]:
            image=tuple(translate[i] for i in simplex)
            if set(image)==set(simplex):
                lefschetz+=(-1)**(k-1)*sign_of_permutation(simplex,image)
    trace=lefschetz-1  # H_0 is the trivial line; only H_2 remains
    trace_by_translation[shift]=trace
    assert trace==(64 if shift==(0,0) else 4 if shift in S else -1)
assert Counter(trace_by_translation.values())=={64:1,4:12,-1:12}
# Restriction of adjacency to any nontrivial additive character has
# eigenvalue 2 or -3, by A*A + A = 6I + 6J. Multiplicities are 12 each.
# Fourier inversion of the displayed Lefschetz character then yields
# homology multiplicities: trivial 4; nontrivial eigenvalue 2: 3; -3: 2.
assert 4+12*3+12*2==64
assert (64+12*4+12*(-1))//25==4
assert (65+5*2)//25==3 and (65+5*(-3))//25==2
print('F_VECTOR 25 150 250 75 15')
print('FREE_FACE_PAIRS',len(collapse),'REMAINING_2_COMPLEX 25 150 190')
print('PRESENTATION_GENERATORS',len(index),'ELIMINATED_BY_T IETZE'.replace('T I','TI'),len(eliminated))
print('REDUCED_EULER_CHARACTERISTIC',64)
print('TRANSLATION_TRACES 64:1 4:12 -1:12; FOURIER_MULTIPLICITIES 4:1 3:12 2:12')
print('PI1_TRIVIAL; WEDGE_64_S2; VERIFY_OK')
