"""Exact finite checks for complete-bipartite stable-set normal fans.
Runs using only the Python standard library; no numerical tolerance.
The symbolic all-parameter proof is in RESULT.md.
"""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    i = 0
    for j in range(nc):
        k = next((k for k in range(i, nr) if a[k][j]), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        d = a[i][j]
        a[i] = [v / d for v in a[i]]
        for k in range(nr):
            if k != i and a[k][j]:
                d = a[k][j]
                a[k] = [u - d*v for u,v in zip(a[k], a[i])]
        i += 1
        if i == nr:
            break
    return i


def face_test(p, q):
    n = p+q
    verts = [tuple((m>>i)&1 for i in range(p))+(0,)*q for m in range(1<<p)]
    verts += [(0,)*p+tuple((m>>j)&1 for j in range(q)) for m in range(1, 1<<q)]
    facet_masks=[]; normals=[]
    def add(fn, normal):
        facet_masks.append(sum(1<<t for t,v in enumerate(verts) if fn(v)))
        normals.append(tuple(normal))
    for i in range(p):
        e=[0]*n; e[i]=-1
        add(lambda v,i=i: v[i]==0,e)
    for j in range(q):
        e=[0]*n; e[p+j]=-1
        add(lambda v,j=j: v[p+j]==0,e)
    for i in range(p):
        for j in range(q):
            e=[0]*n; e[i]=1; e[p+j]=1
            add(lambda v,i=i,j=j: v[i]+v[p+j]==1,e)
    full=(1<<len(verts))-1
    faces={full}
    for fm in facet_masks:
        faces |= {x&fm for x in list(faces) if x&fm}
    singular=set()
    for f in faces:
        active=[i for i,mask in enumerate(facet_masks) if f&mask==f]
        r=rank([normals[i] for i in active])
        # The rank of the active facet normals equals the cone dimension.
        vv=[v for t,v in enumerate(verts) if (f>>t)&1]
        dim=rank([tuple(a-b for a,b in zip(v,vv[0])) for v in vv[1:]])
        assert r==n-dim, (p,q,dim,r)
        if len(active)>r:
            singular.add(f)
    maximal={f for f in singular if not any(f!=g and f&g==f for g in singular)}
    predicted=set()
    for i in range(p):
        predicted.add(sum(1<<k for k,v in enumerate(verts) if v[i]==1))
    for j in range(q):
        predicted.add(sum(1<<k for k,v in enumerate(verts) if v[p+j]==1))
    for ii in combinations(range(p),2):
        for jj in combinations(range(q),2):
            predicted.add(sum(1<<k for k,v in enumerate(verts) if all(v[i]+v[p+j]==1 for i in ii for j in jj)))
    assert maximal == predicted, (p,q,maximal-predicted,predicted-maximal)
    assert len(maximal)==p+q+comb(p,2)*comb(q,2)
    return len(verts), len(faces), len(singular),len(maximal)


def segre_test(q):
    # Character-semigroup S={(a,c):0<=c_j<=a}: check cube generators
    # and Hilbert function up to a=5, proving neither claim for all a.
    from itertools import product
    gens=[(1,)+z for z in product((0,1),repeat=q)]
    current={(0,)+(0,)*q}
    for a in range(1,6):
        current={tuple(x+y for x,y in zip(u,g)) for u in current for g in gens}
        expected={(a,)+z for z in product(range(a+1),repeat=q)}
        assert current==expected
        assert len(current)==(a+1)**q
    assert factorial(q)>=2


def bridge_test():
    # Four primitive rays span a saturated rank-three lattice and obey the square relation.
    rays=[(1,0,0),(0,1,0),(0,0,1),(-1,1,1)]
    assert rank(rays)==3
    assert tuple(rays[0][j]+rays[3][j] for j in range(3))==tuple(rays[1][j]+rays[2][j] for j in range(3))

for p,q in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    print('FACES',p,q,*face_test(p,q))
for q in (2,3,4): segre_test(q)
bridge_test()
print('VERIFY_OK')
