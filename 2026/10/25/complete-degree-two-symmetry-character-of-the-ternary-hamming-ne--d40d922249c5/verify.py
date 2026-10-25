#!/usr/bin/env python3
"""Exact rational cohomology and symmetry-character verification for N(H(3,3)).
Requires Python 3.10+ and SymPy 1.14. No external files are required.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from sympy import Matrix, eye

V=list(product(range(3),repeat=3))
VID={v:i for i,v in enumerate(V)}
N=[tuple(sorted(VID[w] for w in V if sum(a!=b for a,b in zip(v,w))==1)) for v in V]
F=[set() for _ in range(6)]
for nb in N:
    for size in range(1,7):
        F[size-1].update(combinations(nb,size))
assert tuple(map(len,F))==(27,243,540,405,162,27)
face_set=set().union(*F)
assert len(face_set)==1404

# Elementary collapse with a face whose unique cofacet is maximal.
C=[set(f) for f in F]
collapses=0
while True:
    found=None
    for dim in range(4,-1,-1):
        counter=Counter(sub for upper in C[dim+1] for sub in combinations(upper,dim+1))
        for lower in sorted(C[dim]):
            if counter[lower]!=1:
                continue
            upper=next(up for up in sorted(C[dim+1]) if set(lower)<=set(up))
            if any(set(lower)<=set(up) for j in range(dim+2,6) for up in C[j]):
                continue
            found=(dim,lower,upper)
            break
        if found is not None:
            break
    if found is None:
        break
    dim,lower,upper=found
    C[dim].remove(lower)
    C[dim+1].remove(upper)
    collapses+=1
assert collapses==486,(collapses,tuple(map(len,C)))
assert tuple(map(len,C))==(27,189,216,0,0,0)
print('F_VECTOR',tuple(map(len,F)))
print('COLLAPSE_PAIRS',collapses,'CORE_VECTOR',tuple(map(len,C)))

# Exact cohomology: gauge by a lexicographically chosen spanning tree.
E=sorted(F[1]);T=sorted(F[2])
parent=list(range(27));tree=[]
def root(x):
    while x!=parent[x]:
        x=parent[x]
    return x
for a,b in E:
    ra,rb=root(a),root(b)
    if ra!=rb:
        parent[rb]=ra
        tree.append((a,b))
assert len(tree)==26
S=set(tree)
ct=[e for e in E if e not in S]
idx={e:i for i,e in enumerate(ct)}
D=Matrix.zeros(len(ct),len(T))
for j,(a,b,c) in enumerate(T):
    for e,s in (((b,c),1),((a,c),-1),((a,b),1)):
        if e in idx:
            D[idx[e],j]=s
Bcols=D.T.nullspace()
assert len(Bcols)==3
B=Matrix.hstack(*Bcols)
rows=[]
for j in range(len(ct)):
    if Matrix([list(B[i,:]) for i in rows+[j]]).rank()>len(rows):
        rows.append(j)
    if len(rows)==3:
        break
assert len(rows)==3
invert=B[rows,:].inv()
assert D.T*B==Matrix.zeros(len(T),3)
print('TREE_COTREE_RANKS',len(tree),len(ct),len(T),'H1_DIM',len(Bcols))

adj=defaultdict(list)
for a,b in tree:
    adj[a].append(b);adj[b].append(a)
P=list(permutations(range(3)))
id3=(0,1,2)
def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def on_vertices(rho,syms):
    return [VID[tuple(syms[j][v[rho[j]]] for j in range(3))] for v in V]

def cohomology_action(rho,syms):
    vertexperm=on_vertices(rho,syms)
    outputs=[]
    for z in Bcols:
        def cochain(a,b):
            aa,bb=vertexperm[a],vertexperm[b]
            sign=1 if aa<bb else -1
            e=(min(aa,bb),max(aa,bb))
            return sign*z[idx[e]] if e in idx else 0
        phi={0:0};stack=[0]
        while stack:
            a=stack.pop()
            for b in adj[a]:
                if b not in phi:
                    phi[b]=phi[a]+cochain(a,b)
                    stack.append(b)
        assert len(phi)==27
        transformed=Matrix([cochain(a,b)-phi[b]+phi[a] for a,b in ct])
        coeff=invert*transformed[rows,:]
        assert B*coeff==transformed
        outputs.append(coeff)
    return Matrix.hstack(*outputs)

# An explicit signed-coordinate basis for H^1, with generators checked exactly.
trans=[]
for j in range(3):
    syms=[id3]*3;syms[j]=(1,0,2)
    trans.append(cohomology_action(id3,syms))
lines=[]
for t in trans:
    diff=t-eye(3)
    lines.append(next(diff[:,i] for i in range(3) if diff[:,i]!=Matrix.zeros(3,1)))
L=Matrix.hstack(lines[0],lines[1],-2*lines[2])
assert L.det()!=0
for j,t in enumerate(trans):
    expected=eye(3);expected[j,j]=-1
    assert L.inv()*t*L==expected
for j in range(3):
    syms=[id3]*3;syms[j]=(1,2,0)
    assert cohomology_action(id3,syms)==eye(3)
for rho in ((1,0,2),(0,2,1)):
    assert L.inv()*cohomology_action(rho,[id3]*3)*L == Matrix(3,3,lambda i,j:int(rho[i]==j))
print('SIGNED_COORDINATE_H1_GENERATORS_OK')

# Conjugacy class notation: a rho-cycle of length h colored I,T,C by
# the S3 conjugacy class of the product of the symbol permutations along it.
def color(sigma):
    if sigma==id3:return 'I'
    return 'T' if parity(sigma)<0 else 'C'
def class_key(rho,syms):
    seen=set();value=[]
    for i in range(3):
        if i in seen:continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=rho[j]
        sigma=id3
        for j in cyc:
            sigma=tuple(sigma[syms[j][h]] for h in range(3))
        value.append((len(cyc),color(sigma)))
    return tuple(sorted(value))

def chain_lefschetz(vertexperm):
    result=0
    for k,faces in enumerate(F):
        for f in faces:
            im=tuple(vertexperm[i] for i in f)
            if set(im)!=set(f):continue
            places={v:j for j,v in enumerate(f)}
            result+=(-1)**k*parity(tuple(places[i] for i in im))
    return result

records=defaultdict(list)
for rho in P:
    for syms in product(P,repeat=3):
        vp=on_vertices(rho,syms)
        assert all(tuple(sorted(vp[i] for i in f)) in F[len(f)-1] for f in N)
        first=sum(parity(syms[j]) for j in range(3) if rho[j]==j)
        Lf=chain_lefschetz(vp)
        second=Lf-1+first
        records[class_key(rho,syms)].append((first,second))
assert len(records)==22 and sum(map(len,records.values()))==1296
for key,values in records.items():
    assert len(set(values))==1,(key,set(values))
expected={
 '1C 1C 1C':(8,3,2), '1C 1C 1I':(12,3,2),
 '1C 1C 1T':(36,1,0),'1C 1I 1I':(6,3,2),
 '1C 1I 1T':(36,1,0),'1C 1T 1T':(54,-1,-2),
 '1C 2C':(72,1,0),'1C 2I':(36,1,0),'1C 2T':(108,1,0),
 '1I 1I 1I':(1,3,56),'1I 1I 1T':(9,1,0),
 '1I 1T 1T':(27,-1,4),'1I 2C':(36,1,0),
 '1I 2I':(18,1,-18),'1I 2T':(54,1,0),
 '1T 1T 1T':(27,-3,4),'1T 2C':(108,-1,-2),
 '1T 2I':(54,-1,-2),'1T 2T':(162,-1,0),
 '3C':(144,0,-1),'3I':(72,0,5),'3T':(216,0,1)
}
assert len(expected)==22
for key,vals in records.items():
    name=' '.join(str(n)+c for n,c in key)
    assert expected[name]==(len(vals),*vals[0]),(name,len(vals),vals[0])
assert sum(len(v)*v[0][1] for v in records.values())==0
assert sum(len(v)*v[0][0] for v in records.values())==0
print('FULL_AUTOMORPHISM_GROUP',1296,'CONJUGACY_CLASSES',len(records))
for key,values in sorted(records.items()):
    print('CLASS',' '.join(str(n)+c for n,c in key),'SIZE',len(values),'H1',values[0][0],'H2',values[0][1])

# Translation subgroup, fixed-simplicial-cell test, and Fourier decomposition.
for t in product(range(3),repeat=3):
    syms=[tuple((i+t[j])%3 for i in range(3)) for j in range(3)]
    p=on_vertices(id3,syms)
    fixed=sum(set(p[v] for v in face)==set(face) for face in face_set)
    if t==(0,0,0):
        assert fixed==1404
    else:
        assert fixed==0
    first=3
    second=chain_lefschetz(p)-1+first
    assert second==(56 if t==(0,0,0) else 2)
print('TRANSLATION_CHARACTER',56,2,'MODULE_QA_TWICE_PLUS_TWO_TRIVIAL')
print('TRANSLATION_INVARIANTS_H1_3_H2_4')
print('FULL_INVARIANTS_H1_0_H2_0')
print('VERIFY_OK_TERNARY_NEIGHBORHOOD_FULL_SYMMETRY_CHARACTER')
