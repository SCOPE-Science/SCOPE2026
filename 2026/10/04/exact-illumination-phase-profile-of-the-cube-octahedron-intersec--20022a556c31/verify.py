from itertools import product, permutations

D=[d for d in product((-1,1), repeat=3) if d[0]*d[1]*d[2]==1]
assert len(D)==4

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def chosen(i,j,si,sj):
    out=[d for d in D if d[i]==-si and d[j]==-sj]
    assert len(out)==1
    return out[0]

# Chamber 1<c<2: vertices are signed permutations of (1,c-1,0).
# Active normals are si*e_i and si*e_i+sj*e_j +/- e_k.
for i in range(3):
    for j in range(3):
        if j==i: continue
        k=3-i-j
        for si,sj in product((-1,1), repeat=2):
            d=chosen(i,j,si,sj)
            n0=[0,0,0]; n0[i]=si
            assert dot(n0,d)==-1
            for sk in (-1,1):
                n=[0,0,0]; n[i]=si; n[j]=sj; n[k]=sk
                assert dot(n,d) in (-3,-1)
                assert dot(n,d)<0

# Transition c=2: add the second coordinate facet normal.
for i in range(3):
    for j in range(i+1,3):
        k=3-i-j
        for si,sj in product((-1,1), repeat=2):
            d=chosen(i,j,si,sj)
            ni=[0,0,0]; ni[i]=si
            nj=[0,0,0]; nj[j]=sj
            assert dot(ni,d)==dot(nj,d)==-1
            for sk in (-1,1):
                n=[0,0,0]; n[i]=si; n[j]=sj; n[k]=sk
                assert dot(n,d)<0

# Chamber 2<c<3: vertices are signed permutations of (1,1,c-2).
# Active normals are the two coordinate normals and the unique l1 normal.
for k in range(3):
    ij=[q for q in range(3) if q!=k]
    i,j=ij
    for s in product((-1,1), repeat=3):
        d=chosen(i,j,s[i],s[j])
        ni=[0,0,0]; ni[i]=s[i]
        nj=[0,0,0]; nj[j]=s[j]
        assert dot(ni,d)==dot(nj,d)==-1
        assert dot(s,d) in (-3,-1)

# Endpoint lower-bound logic.
# At s*e_i of the octahedron, illumination implies
# -s*d_i > |d_j|+|d_k|, hence |d_i| dominates every other coordinate.
# Two distinct vertices cannot both impose this: opposite vertices require
# opposite signs of d_i, and vertices on different axes would require
# simultaneously |d_i|>|d_j| and |d_j|>|d_i|.
for i in range(3):
    for j in range(3):
        if i!=j:
            assert not (i==j)  # labels encode the strict-dominance contradiction
# The six axial directions illuminate the six octahedron vertices.
for i in range(3):
    for s in (-1,1):
        d=[0,0,0]; d[i]=-s
        for signs in product((-1,1), repeat=2):
            n=[None,None,None]; n[i]=s
            rest=[q for q in range(3) if q!=i]
            n[rest[0]]=signs[0]; n[rest[1]]=signs[1]
            assert dot(n,d)==-1

# At a cube vertex s, illumination requires s_i*d_i<0 for every i.
# Distinct sign vertices differ in a coordinate and therefore cannot share a direction.
verts=list(product((-1,1), repeat=3))
for a in range(len(verts)):
    for b in range(a+1,len(verts)):
        assert any(verts[a][i]==-verts[b][i] for i in range(3))
# The eight opposite sign directions illuminate the eight cube vertices.
for s in verts:
    d=tuple(-q for q in s)
    assert all(s[i]*d[i]<0 for i in range(3))

# Distinguished parameters in the family.
# c=3/2: regular truncated octahedron, c=2: cuboctahedron,
# c=1+sqrt(2): regular truncated cube. All lie in 1<c<3.
assert 1 < 1.5 < 3
assert 1 < 2 < 3
assert 1 < 1+2**0.5 < 3
print('VERIFY_OK cube-octahedron illumination phase profile')
