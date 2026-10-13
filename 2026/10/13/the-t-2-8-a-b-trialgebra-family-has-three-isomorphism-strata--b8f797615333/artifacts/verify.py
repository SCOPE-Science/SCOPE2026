import sympy as sp

a,b=sp.symbols("a b")
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])
basis=[e1,e2]

def table(av,bv):
    dash={(0,0):sp.Matrix([av,0]),(1,0):sp.Matrix([0,av])}
    vdash={(0,0):sp.Matrix([av,0]),(0,1):sp.Matrix([0,av])}
    perp={(0,0):sp.Matrix([av,bv])}
    return dash,vdash,perp

def mul(T,x,y):
    z=sp.zeros(2,1)
    for i in range(2):
        for j in range(2):
            if (i,j) in T:
                z += x[i]*y[j]*T[(i,j)]
    return sp.simplify(z)

D,V,P=table(a,b)

axioms=[
 lambda x,y,z: mul(D,mul(D,x,y),z)-mul(D,x,mul(D,y,z)),
 lambda x,y,z: mul(D,mul(D,x,y),z)-mul(D,x,mul(V,y,z)),
 lambda x,y,z: mul(D,mul(V,x,y),z)-mul(V,x,mul(D,y,z)),
 lambda x,y,z: mul(V,mul(D,x,y),z)-mul(V,x,mul(V,y,z)),
 lambda x,y,z: mul(V,mul(V,x,y),z)-mul(V,x,mul(V,y,z)),
 lambda x,y,z: mul(D,mul(D,x,y),z)-mul(D,x,mul(P,y,z)),
 lambda x,y,z: mul(D,mul(P,x,y),z)-mul(P,x,mul(D,y,z)),
 lambda x,y,z: mul(P,mul(D,x,y),z)-mul(P,x,mul(V,y,z)),
 lambda x,y,z: mul(P,mul(V,x,y),z)-mul(V,x,mul(P,y,z)),
 lambda x,y,z: mul(V,mul(P,x,y),z)-mul(V,x,mul(V,y,z)),
 lambda x,y,z: mul(P,mul(P,x,y),z)-mul(P,x,mul(P,y,z)),
]
for ax in axioms:
    for x in basis:
        for y in basis:
            for z in basis:
                assert sp.simplify(ax(x,y,z)) == sp.zeros(2,1)

# Basis normalization for a != 0.
f1=sp.Matrix([1/a,b/a**2])
f2=e2
Q=sp.Matrix.hstack(f1,f2)
assert sp.simplify(Q.det()-1/a)==0
for T, expected in [
    (D,{(0,0):f1,(1,0):f2}),
    (V,{(0,0):f1,(0,1):f2}),
    (P,{(0,0):f1}),
]:
    for i,x in enumerate([f1,f2]):
        for j,y in enumerate([f1,f2]):
            want=expected.get((i,j),sp.zeros(2,1))
            assert sp.simplify(mul(T,x,y)-want)==sp.zeros(2,1)

# Basis normalization for a=0,b!=0.
D0,V0,P0=table(0,b)
g1=e1
g2=sp.Matrix([0,b])
assert sp.simplify(sp.Matrix.hstack(g1,g2).det()-b)==0
for T, expected in [
    (D0,{}),(V0,{}),(P0,{(0,0):g2})
]:
    for i,x in enumerate([g1,g2]):
        for j,y in enumerate([g1,g2]):
            want=expected.get((i,j),sp.zeros(2,1))
            assert sp.simplify(mul(T,x,y)-want)==sp.zeros(2,1)

x0,x1,x2,x3=sp.symbols("x0 x1 x2 x3")
vars_=[x0,x1,x2,x3]
M=sp.Matrix([[x0,x2],[x1,x3]])

def derivation_matrix(av,bv):
    eqs=[]
    for T in table(av,bv):
        for x in basis:
            for y in basis:
                eqs.extend(list(M*mul(T,x,y)-mul(T,M*x,y)-mul(T,x,M*y)))
    A,_=sp.linear_eq_to_matrix(eqs,vars_)
    return A

def centroid_matrix(av,bv):
    eqs=[]
    for T in table(av,bv):
        for x in basis:
            for y in basis:
                lhs=M*mul(T,x,y)
                eqs.extend(list(lhs-mul(T,M*x,y)))
                eqs.extend(list(lhs-mul(T,x,M*y)))
    A,_=sp.linear_eq_to_matrix(eqs,vars_)
    return A

def image_dims(av,bv):
    dims=[]
    for T in table(av,bv):
        cols=[]
        for x in basis:
            for y in basis:
                cols.append(mul(T,x,y))
        dims.append(sp.Matrix.hstack(*cols).rank())
    return tuple(dims)

expected_der={
    (1,0):[sp.Matrix([0,0,0,1])],
    (0,1):[sp.Matrix([0,1,0,0]),sp.Matrix([sp.Rational(1,2),0,0,1])],
}
expected_cent={
    (1,0):[sp.Matrix([1,0,0,1])],
    (0,1):[sp.Matrix([0,1,0,0]),sp.Matrix([1,0,0,1])],
}

for key,dim in [((1,0),1),((0,1),2),((0,0),4)]:
    A=derivation_matrix(*key)
    assert 4-A.rank()==dim
    C=centroid_matrix(*key)
    assert 4-C.rank()==dim

for key,vecs in expected_der.items():
    A=derivation_matrix(*key)
    E=sp.Matrix.hstack(*vecs)
    assert all(A*E[:,j]==sp.zeros(A.rows,1) for j in range(E.cols))
    N=sp.Matrix.hstack(*A.nullspace())
    assert sp.Matrix.hstack(N,E).rank()==N.rank()==E.rank()

for key,vecs in expected_cent.items():
    A=centroid_matrix(*key)
    E=sp.Matrix.hstack(*vecs)
    assert all(A*E[:,j]==sp.zeros(A.rows,1) for j in range(E.cols))
    N=sp.Matrix.hstack(*A.nullspace())
    assert sp.Matrix.hstack(N,E).rank()==N.rank()==E.rank()

assert image_dims(1,0)==(2,2,1)
assert image_dims(0,1)==(0,0,1)
assert image_dims(0,0)==(0,0,0)

print("VERIFY_OK")
