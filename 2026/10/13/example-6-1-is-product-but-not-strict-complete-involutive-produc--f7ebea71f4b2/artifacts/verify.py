from itertools import product

# degrees in Z2^2
deg=[(0,0),(0,0),(0,1),(1,0),(1,1)]
def eps(g,h):
    return -1 if ((g[0]*h[1]-g[1]*h[0])%2) else 1

# vectors are tuples length 5 over integers (sign arithmetic suffices)
E=[tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]
def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(5))
def smul(a,v):
    return tuple(a*x for x in v)
def alpha(v):
    return (v[1],v[0],v[2],v[3],v[4])

# Independent source brackets in increasing basis order.
# [e1,e3,e4,e5]=e1; [e2,e3,e4,e5]=e2; [e1,e2,e4,e5]=e3.
base={
    (0,2,3,4): E[0],
    (1,2,3,4): E[1],
    (0,1,3,4): E[2],
}

def bracket_basis(indices):
    # color skew-sort with adjacent transpositions
    inds=list(indices); coeff=1
    if len(set(inds))<4:
        return (0,)*5
    for i in range(4):
        for j in range(3-i):
            if inds[j]>inds[j+1]:
                g,h=deg[inds[j]],deg[inds[j+1]]
                coeff *= -eps(g,h)
                inds[j],inds[j+1]=inds[j+1],inds[j]
    v=base.get(tuple(inds),(0,)*5)
    return smul(coeff,v)

def bracket(vs):
    out=(0,)*5
    supports=[]
    for v in vs:
        supports.append([(i,a) for i,a in enumerate(v) if a])
    for terms in product(*supports):
        idx=tuple(t[0] for t in terms)
        coeff=1
        for _,a in terms: coeff*=a
        out=add(out,smul(coeff,bracket_basis(idx)))
    return out

def mat_apply(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(5)) for i in range(5))
def mat_mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
def ident():
    return [[1 if i==j else 0 for j in range(5)] for i in range(5)]
def sign_map(kind,ep,s3,s4,s5):
    M=[[0]*5 for _ in range(5)]
    if kind=="D":
        M[0][0]=ep; M[1][1]=ep
    else:
        M[1][0]=ep; M[0][1]=ep
    M[2][2]=s3; M[3][3]=s4; M[4][4]=s5
    return M

# Nijenhuis identity, Definition 6.2 specialized to n=4:
# [Px1,...,Px4] = P(sum over one un-P input of bracket of 3 P inputs)
#                  - P^2(sum over two un-P inputs)
#                  + P^3(sum over three un-P inputs)
#                  - P^4([x1,x2,x3,x4]).
# This is the standard inclusion-exclusion form in the source.
def nij_defect(M, xs):
    powers=[ident()]
    for _ in range(4):
        powers.append(mat_mul(powers[-1],M))
    Pxs=[mat_apply(M,x) for x in xs]
    lhs=bracket(Pxs)
    rhs=(0,)*5
    n=4
    # r = number of untransformed inputs; coefficient (-1)^(r-1), outer P^r
    for r in range(1,n+1):
        subtotal=(0,)*5
        for un in __import__('itertools').combinations(range(n),r):
            un=set(un)
            args=[xs[i] if i in un else Pxs[i] for i in range(n)]
            subtotal=add(subtotal,bracket(args))
        term=mat_apply(powers[r],subtotal)
        rhs=add(rhs,smul(1 if r%2==1 else -1,term))
    return add(lhs,smul(-1,rhs))

def centroid(M):
    for inds in product(range(5), repeat=4):
        xs=[E[i] for i in inds]
        lhs=mat_apply(M,bracket(xs))
        for slot in range(4):
            args=xs[:]
            args[slot]=mat_apply(M,args[slot])
            if lhs!=bracket(args):
                return False
    return True

maps=[]
for kind in ("D","S"):
    for ep,s3,s4,s5 in product((1,-1),repeat=4):
        M=sign_map(kind,ep,s3,s4,s5)
        assert mat_mul(M,M)==ident()
        # commutes with alpha
        for e in E:
            assert mat_apply(M,alpha(e))==alpha(mat_apply(M,e))
        maps.append((kind,ep,s3,s4,s5,M))
assert len(maps)==32

nij=[]
strict=[]
for rec in maps:
    M=rec[-1]
    ok=True
    for inds in product(range(5),repeat=4):
        if nij_defect(M,[E[i] for i in inds])!=(0,)*5:
            ok=False; break
    if ok: nij.append(rec)
    if ok and centroid(M): strict.append(rec)

assert len(nij)==30
# failures exactly D with s3=-ep, s4=s5=ep
fail={(k,e,s3,s4,s5) for k,e,s3,s4,s5,M in maps if (k,e,s3,s4,s5,M) not in nij}
expect={("D",1,-1,1,1),("D",-1,1,-1,-1)}
assert fail==expect,(fail,expect)

# product structures exclude +/- identity
def is_pmI(M):
    I=ident()
    return M==I or M==[[-x for x in row] for row in I]
products=[r for r in nij if not is_pmI(r[-1])]
assert len(products)==28
strict_products=[r for r in products if centroid(r[-1])]
assert len(strict_products)==0

P0=sign_map("D",1,-1,-1,-1)
assert any(r[-1]==P0 for r in products)
assert not centroid(P0)
# explicit witness
lhs=mat_apply(P0,bracket([E[1],E[2],E[3],E[4]]))
rhs=bracket([E[1],mat_apply(P0,E[2]),E[3],E[4]])
assert lhs==E[1] and rhs==smul(-1,E[1])

print({"commuting_involutions":len(maps),
       "nijenhuis_involutions":len(nij),
       "product_structures":len(products),
       "strict_product_structures":len(strict_products)})
print("VERIFY_OK")
