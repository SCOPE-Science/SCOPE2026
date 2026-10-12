import sympy as sp

l,m,n = sp.symbols("l m n")
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])
B=[e1,e2]

# TH_2^7 from the source.
D={(0,1):e1,(1,1):e2}
V={(1,0):e1,(1,1):e2}
P={(0,0):e1,(0,1):e1,(1,0):e1,(1,1):e2}

def mul(T,x,y):
    z=sp.zeros(2,1)
    for i in range(2):
        for j in range(2):
            if (i,j) in T:
                z += x[i]*y[j]*T[(i,j)]
    return sp.simplify(z)

# The eleven Hom-trialgebra identities for alpha=id.
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
    for x in B:
        for y in B:
            for z in B:
                assert sp.simplify(ax(x,y,z)) == sp.zeros(2,1)

def star(x,y):
    return l*mul(D,x,y)+m*mul(V,x,y)+n*mul(P,x,y)

def assoc(x,y,z):
    return sp.simplify(star(star(x,y),z)-star(x,star(y,z)))

assert sp.simplify(assoc(e2,e2,e1)-sp.Matrix([l*(m+n),0])) == sp.zeros(2,1)
assert sp.simplify(assoc(e1,e2,e2)-sp.Matrix([-m*(l+n),0])) == sp.zeros(2,1)
assert sp.simplify(assoc(e1,e2,e1)-sp.Matrix([n*(l-m),0])) == sp.zeros(2,1)

# All-plus failure.
assert assoc(e1,e2,e2).subs({l:1,m:1,n:1}) == sp.Matrix([-2,0])

# Signed direction works on every witness triple.
for x in B:
    for y in B:
        for z in B:
            assert sp.simplify(assoc(x,y,z).subs({l:1,m:1,n:-1})) == sp.zeros(2,1)

# Formal universal reduction. Tags encode normal-form classes under the
# nine displayed relation groups in Definition 2.1. Each key is
# (outer operation, inner operation).
ops=("D","V","P")
L={
 ("D","D"):"A", ("D","V"):"B", ("D","P"):"D0",
 ("V","D"):"C", ("V","V"):"C", ("V","P"):"C",
 ("P","D"):"E", ("P","V"):"F", ("P","P"):"G",
}
R={
 ("D","D"):"A", ("D","V"):"A", ("D","P"):"A",
 ("V","D"):"B", ("V","V"):"C", ("V","P"):"F",
 ("P","D"):"D0", ("P","V"):"E", ("P","P"):"G",
}
coef={"D":l,"V":m,"P":n}
tags=("A","B","C","D0","E","F","G")
tot={t:0 for t in tags}
for outer in ops:
    for inner in ops:
        tot[L[(outer,inner)]] += coef[outer]*coef[inner]
        tot[R[(outer,inner)]] -= coef[outer]*coef[inner]
tot={k:sp.factor(v) for k,v in tot.items()}
assert tot["A"] == -l*(m+n)
assert tot["B"] == 0
assert tot["C"] == m*(l+n)
assert tot["D0"] == 0
assert tot["E"] == n*(l-m)
assert tot["F"] == 0
assert tot["G"] == 0

print("VERIFY_OK")
