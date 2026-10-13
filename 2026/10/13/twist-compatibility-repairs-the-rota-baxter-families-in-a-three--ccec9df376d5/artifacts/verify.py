import sympy as sp
from itertools import product

a,b,c,d,f,gam,lam=sp.symbols("a b c d f gam lam")
R=sp.Matrix([[a,c,0],[b,d,0],[0,0,f]])
Alpha=sp.diag(gam,1,lam)
Beta=sp.diag(gam,1,-lam)
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
basis=(e1,e2,e3)

def br(x,y):
    return sp.Matrix([sp.expand(x[0]*y[1]-x[1]*y[0]),0,0])

CA=sp.simplify(R*Alpha-Alpha*R)
CB=sp.simplify(R*Beta-Beta*R)
expected=sp.Matrix([[0,(1-gam)*c,0],[(gam-1)*b,0,0],[0,0,0]])
assert sp.simplify(CA-expected)==sp.zeros(3,3)
assert sp.simplify(CB-expected)==sp.zeros(3,3)

def defect(x,y):
    Rx=R*x; Ry=R*y
    return sp.simplify(br(Rx,Ry)-R*(br(Rx,y)+br(x,Ry)))

nonzero=[]
for x in basis:
    for y in basis:
        z=defect(x,y)
        for t in z:
            t=sp.factor(t)
            if t!=0: nonzero.append(t)

target=[a*a+b*c,b*(a+d)]
G=sp.groebner(target,a,b,c,d,f,order="grevlex")
for z in nonzero:
    assert G.reduce(z)[1]==0
G2=sp.groebner(nonzero,a,b,c,d,f,order="grevlex")
for z in target:
    assert G2.reduce(z)[1]==0

# Source first family: a=b=0, c=a1, d=a2.
a1,a2,c1=sp.symbols("a1 a2 c1")
R1=R.subs({a:0,b:0,c:a1,d:a2,f:c1})
assert sp.simplify(R1*Alpha-Alpha*R1)==sp.Matrix([[0,(1-gam)*a1,0],[0,0,0],[0,0,0]])

# Source second family: b=b2 !=0, a=b1, c=-b1^2/b2, d=-b1.
b1,b2,c2=sp.symbols("b1 b2 c2", nonzero=True)
R2=R.subs({a:b1,b:b2,c:-b1**2/b2,d:-b1,f:c2})
assert sp.simplify(defect(e1,e2).subs({a:b1,b:b2,c:-b1**2/b2,d:-b1,f:c2}))==sp.zeros(3,1)
C2=sp.simplify(R2*Alpha-Alpha*R2)
assert sp.factor(C2[1,0])==(gam-1)*b2

def count(q,g):
    n=0
    for aa,bb,cc,dd,ff in product(range(q),repeat=5):
        if (aa*aa+bb*cc)%q: continue
        if bb*(aa+dd)%q: continue
        if (g-1)*bb%q: continue
        if (g-1)*cc%q: continue
        n+=1
    return n

for q in (3,5,7):
    counts={g:count(q,g) for g in range(1,q)}
    assert counts[1]==2*q**3-q**2
    for g in range(2,q):
        assert counts[g]==q**2
    total=(q-1)*sum(counts.values())
    assert total==3*q**2*(q-1)**2
    print({"q":q,"fixed_lambda_counts_by_gamma":counts,"all_nonzero_gamma_lambda_total":total})

print("VERIFY_OK")
