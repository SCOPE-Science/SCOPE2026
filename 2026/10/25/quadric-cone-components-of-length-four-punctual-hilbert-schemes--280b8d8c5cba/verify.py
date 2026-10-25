"""Exact finite-field and Pluecker-chart checks for length-four punctual Hilbert schemes.

Only verifies finite examples and the explicit Grassmannian chart identities;
the all-germs classification is proved independently in RESULT.md.
"""
from itertools import product,combinations
from sympy import symbols,expand,Matrix

x,y,b,c=symbols('x y b c')
monomials=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]

def vec(poly,p):
    P=__import__('sympy').Poly(expand(poly),x,y)
    return tuple(int(P.coeff_monomial(x**i*y**j))%p for i,j in monomials)

def rref(rows,p):
    a=[list(map(lambda v:v%p,r)) for r in rows]
    rank=0
    for col in range(len(monomials)):
        piv=next((j for j in range(rank,len(a)) if a[j][col]),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[(v*inv)%p for v in a[rank]]
        for j in range(len(a)):
            if j!=rank and a[j][col]:
                k=a[j][col]
                a[j]=[(u-k*v)%p for u,v in zip(a[j],a[rank])]
        rank+=1
        if rank==len(a): break
    return tuple(tuple(r) for r in a[:rank])

def normalized_projective(n,p):
    return [v for v in product(range(p),repeat=n) if any(v) and v[next(i for i,z in enumerate(v) if z)]==1]

def ideal_curv(l,u,B,C,p):
    v=l-B*u**2-C*u**3
    rows=[vec(v,p),vec(u*v,p),vec(l*v,p),vec(x*x*v,p),vec(x*y*v,p),vec(y*y*v,p),vec(x**4,p)]
    # easier: span of v multiplied by monomials of degree 0,1,2, plus all m^4 (already truncated)
    # the v itself has a linear term; multiplying up to degree2 spans six generators
    rows=[vec(v,p),vec(x*v,p),vec(y*v,p),vec(x*x*v,p),vec(x*y*v,p),vec(y*y*v,p)]
    return rref(rows,p)

def ideal_noncurv(lam,p):
    # kernel in degree 2, plus all degree-3 monomials
    quad=[]
    for i,xi in enumerate([x*x,x*y,y*y]):
        for j,xj in enumerate([x*x,x*y,y*y]):
            if j>i: continue
            if lam[i]==0 and lam[j]==0: continue
            row=lam[j]*xi-lam[i]*xj
            if row!=0:quad.append(vec(row,p))
    # alternate robust kernel from rank condition: v with lambda dot v=0
    quad=[]
    piv=next(i for i,a in enumerate(lam) if a)
    for i in range(3):
        if i!=piv:
            coeff=[0]*3;coeff[i]=lam[piv];coeff[piv]=-lam[i]
            quad.append(vec(sum(k*t for k,t in zip(coeff,[x*x,x*y,y*y])),p))
    return rref(quad+[vec(t,p) for t in [x**3,x*x*y,x*y*y,y**3]],p)

# Explicit 2-plane wedge in the 4D span (y,x^2,x^3,xy)
r1=Matrix([1,-b,-c,0]);r2=Matrix([0,0,-b,1])
minor={(i,j):expand(r1[i]*r2[j]-r1[j]*r2[i]) for i,j in combinations(range(4),2)}
assert minor[(0,3)]==1 and minor[(1,2)]==b*b and minor[(2,3)]==-c
assert minor[(0,2)]==-b and minor[(1,3)]==-b
print('PLUCKER_QUADRIC_OK',minor)

for p in [3,5,7]:
    # f=xy(y-x), with three distinct rational tangents
    f=x*y*(y-x)
    tangents=[(y,x),(x,y),(y-x,x)]
    ideals=set();counts=[]
    for l,u in tangents:
        local=[]
        for B,C in product(range(p),repeat=2):
            I=ideal_curv(l,u,B,C,p)
            assert len(I)==6 and rref(list(I)+[vec(f,p)],p)==I
            local.append(I)
        assert len(set(local))==p*p
        ideals.update(local);counts.append(len(local))
    non=[]
    for lam in normalized_projective(3,p):
        I=ideal_noncurv(lam,p)
        assert len(I)==6 and rref(list(I)+[vec(f,p)],p)==I
        non.append(I)
    assert len(set(non))==p*p+p+1
    assert not set(non).intersection(ideals)
    ideals.update(non)
    assert len(ideals)==4*p*p+p+1
    print('FINITE_FIELD_OK',p, 'curvilinear',counts, 'noncurvilinear',len(non),'total',len(ideals))
print('VERIFY_OK')
