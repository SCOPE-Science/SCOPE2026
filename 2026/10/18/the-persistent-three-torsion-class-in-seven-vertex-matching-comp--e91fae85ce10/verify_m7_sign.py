"""Exact integral and mod-three homology and symmetry certificate for M(K_7).

Run with Python 3 (standard library only). All faces, matrices, and permutations
are generated from the mathematical definitions; no external files are needed.
"""
from collections import deque
from itertools import combinations, permutations

N = 7
P = 3
labels = list(combinations(range(N), 2))
label_index = {e: i for i, e in enumerate(labels)}
faces1 = [(i,j) for i,j in combinations(range(len(labels)), 2)
          if set(labels[i]).isdisjoint(labels[j])]
faces2 = [(i,j,k) for i,j,k in combinations(range(len(labels)), 3)
          if len(set(labels[i] + labels[j] + labels[k])) == 6]
face1_index = {f:i for i,f in enumerate(faces1)}
assert (len(labels), len(faces1), len(faces2)) == (21, 105, 105)
adj = [[] for _ in labels]
for e,(i,j) in enumerate(faces1):
    adj[i].append((j,e,1))
    adj[j].append((i,e,-1))
parent={0:None}
parent_edge={}
tree=set()
q=deque([0])
while q:
    v=q.popleft()
    for u,e,direction in adj[v]:
        if u not in parent:
            parent[u]=v
            parent_edge[u]=(e,direction)
            tree.add(e)
            q.append(u)
assert len(parent)==len(labels)==21 and len(tree)==20
non_tree=[e for e in range(len(faces1)) if e not in tree]
non_tree_index={e:i for i,e in enumerate(non_tree)}
assert len(non_tree)==85

def toward_root(v):
    while v!=0:
        e,d=parent_edge[v]
        yield e,-d
        v=parent[v]

# A Z-basis of ker(d_1), with one fundamental cycle per non-tree edge.
cycles=[]
for e in non_tree:
    i,j=faces1[e]
    cycle=[0]*len(faces1)
    cycle[e]=1
    for f,d in toward_root(j): cycle[f]+=d
    for f,d in toward_root(i): cycle[f]-=d
    cycles.append(cycle)

def d1(chain):
    out=[0]*21
    for e,c in enumerate(chain):
        if c:
            i,j=faces1[e]
            out[i]-=c
            out[j]+=c
    return out
assert all(not any(d1(c)) for c in cycles)

# Coordinate matrix of d_2, in the integer basis of ker(d_1).
columns=[]
for i,j,k in faces2:
    col=[0]*len(non_tree)
    for face,s in (((j,k),1),((i,k),-1),((i,j),1)):
        e=face1_index[face]
        if e in non_tree_index:col[non_tree_index[e]]+=s
    columns.append(col)
assert all(sum(abs(x) for x in col)>0 for col in columns)

def row_echelon(cols,p,record_independent=False):
    basis={}
    independent=[]
    for idx,col in enumerate(cols):
        vec=[x%p for x in col]
        for pivot,row in sorted(basis.items()):
            if vec[pivot]:
                fac=vec[pivot]
                for j in range(pivot,len(vec)):
                    vec[j]=(vec[j]-fac*row[j])%p
        pivot=next((i for i,x in enumerate(vec) if x),None)
        if pivot is not None:
            inverse=pow(vec[pivot],-1,p)
            vec=[x*inverse%p for x in vec]
            basis[pivot]=vec
            independent.append(idx)
    return basis,independent

basis3,_=row_echelon(columns,3)
assert len(basis3)==84
free=list(set(range(85))-set(basis3))
assert len(free)==1

def quotient_coordinate(vec):
    vec=[x%3 for x in vec]
    for pivot,row in sorted(basis3.items()):
        if vec[pivot]:
            fac=vec[pivot]
            for j in range(pivot,len(vec)):
                vec[j]=(vec[j]-fac*row[j])%3
    return vec[free[0]]

# Independent modulo 5 => full rational rank. The unit-free determinant
# of 3 proves the entire integer cokernel has order exactly 3.
basis5, independent5 = row_echelon(columns,5)
assert len(basis5)==len(independent5)==85

def bareiss_determinant(rows):
    A=[r[:] for r in rows]
    n=len(A)
    prev=1
    sign=1
    for k in range(n-1):
        if not A[k][k]:
            swap=next((i for i in range(k+1,n) if A[i][k]),None)
            if swap is None:return 0
            A[k],A[swap]=A[swap],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            a=A[i][k]
            for j in range(k+1,n):
                numerator=A[i][j]*pivot - a*A[k][j]
                assert numerator%prev==0
                A[i][j]=numerator//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

minor=[[columns[c][r] for c in independent5] for r in range(85)]
determinant=bareiss_determinant(minor)
assert abs(determinant)==3,determinant
# A 3-divisible cokernel and a maximal minor of absolute value 3
# imply Smith invariants (1,...,1,3) without needing a full SNF.

nonzero_generator_index = next(j for j in range(85)
    if quotient_coordinate([int(i==j) for i in range(85)]))
gen=cycles[nonzero_generator_index]
assert not any(d1(gen))
gen_value=quotient_coordinate([gen[e] for e in non_tree])
assert gen_value in (1,2)

phi=[0]*len(faces1)
for j,e in enumerate(non_tree):
    phi[e]=quotient_coordinate([int(i==j) for i in range(85)])
assert all(sum(phi[e]*columns[k][j] for j,e in enumerate(non_tree))%3==0
           for k in range(len(columns)))
assert sum(phi[e]*gen[e] for e in range(len(faces1)))%3==gen_value

def induced_action(g,chain):
    out=[0]*len(faces1)
    for e,val in enumerate(chain):
        if not val:continue
        a,b=faces1[e]
        aa=label_index[tuple(sorted((g[labels[a][0]],g[labels[a][1]])))]
        bb=label_index[tuple(sorted((g[labels[b][0]],g[labels[b][1]])))]
        f=face1_index[(min(aa,bb),max(aa,bb))]
        out[f]+=val*(1 if aa<bb else -1)
    return out

def pairing_phi(chain):
    return sum(phi[e]*v for e,v in enumerate(chain))%3

transposition=list(range(7))
transposition[0],transposition[1]=transposition[1],transposition[0]
assert pairing_phi(induced_action(transposition,gen)) == -gen_value%3
checked=0
for g in permutations(range(7)):
    sign=-1 if sum(g[i]>g[j] for i in range(7) for j in range(i+1,7))%2 else 1
    assert pairing_phi(induced_action(g,gen)) == sign*gen_value%3
    checked+=1
assert checked==5040
print('f-vector:',len(labels),len(faces1),len(faces2))
print('cycle-lattice rank:',len(non_tree),'mod-3 second-boundary rank:',len(basis3))
print('mod-5 maximal rank:',len(basis5),'integer maximal minor:',determinant)
print('integral reduced homology H1 = Z/3, H2 = Z^20')
print('generator fundamental index:',nonzero_generator_index,'phi pairing:',gen_value)
print('nonzero phi coefficients:',sum(bool(v) for v in phi))
print('all 5040 vertex permutations act by their sign on H1')
print('PASS')
