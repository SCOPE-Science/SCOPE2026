import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
R=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def prod_sym(x,y):
    return sp.Matrix([0,2*x[0]*y[0]])

def defect_sym(x,y):
    Rx=R*x; Ry=R*y
    return sp.simplify(prod_sym(Rx,Ry)-R*(prod_sym(Rx,y)+prod_sym(x,Ry)))

actual=[]
for x in basis:
    for y in basis:
        actual.extend(sp.factor(z) for z in defect_sym(x,y) if z!=0)

targets=[-4*a*b,2*a*(a-2*d),-2*b*b,2*b*(a-d),2*b*b]
G=sp.groebner(targets,a,b,c,d,order="grevlex")
for z in actual:
    assert G.reduce(z)[1]==0
G2=sp.groebner(actual,a,b,c,d,order="grevlex")
for z in targets:
    assert G2.reduce(z)[1]==0

def pmul(x,y,p):
    return (0,2*x[0]*y[0]%p)

def mv(M,x,p):
    return ((M[0]*x[0]+M[1]*x[1])%p,
            (M[2]*x[0]+M[3]*x[1])%p)

def is_rb(M,p):
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            Rx=mv(M,x,p); Ry=mv(M,y,p)
            lhs=pmul(Rx,Ry,p)
            q1=pmul(Rx,y,p); q2=pmul(x,Ry,p)
            inside=((q1[0]+q2[0])%p,(q1[1]+q2[1])%p)
            if lhs!=mv(M,inside,p):
                return False
    return True

def rank2(M,p):
    aa,bb,cc,dd=M
    if all(v%p==0 for v in M): return 0
    return 2 if (aa*dd-bb*cc)%p else 1

def inv2(M,p):
    aa,bb,cc,dd=M
    det=(aa*dd-bb*cc)%p
    if det==0: return None
    inv=pow(det,-1,p)
    return (dd*inv%p,-bb*inv%p,-cc*inv%p,aa*inv%p)

def mm(A,B,p):
    return tuple(
        sum(A[2*i+k]*B[2*k+j] for k in range(2))%p
        for i in range(2) for j in range(2)
    )

def auts_odd(p):
    return [(s,0,t,s*s%p) for s in range(1,p) for t in range(p)]

def conj(M,P,p):
    Pinv=inv2(P,p); assert Pinv is not None
    return mm(mm(P,M,p),Pinv,p)

for p in (2,3,5,7):
    sols=[M for M in product(range(p),repeat=4) if is_rb(M,p)]
    if p==2:
        assert len(sols)==p**4
        ranks=Counter(rank2(M,p) for M in sols)
        assert tuple(ranks[i] for i in range(3)) == (
            1,(p-1)*(p+1)**2,p*(p-1)**2*(p+1)
        )
        G2s=[M for M in product(range(p),repeat=4) if inv2(M,p) is not None]
        pool=set(sols); orbits=[]
        while pool:
            M=next(iter(pool))
            O={conj(M,P,p) for P in G2s}
            orbits.append(O); pool-=O
        assert len(orbits)==p*p+p
        print({"q":p,"operators":len(sols),"ranks":tuple(ranks[i] for i in range(3)),
               "similarity_classes":len(orbits)})
    else:
        expected={(0,0,c0,d0) for c0 in range(p) for d0 in range(p)}
        expected |= {(2*d0%p,0,c0,d0) for c0 in range(p) for d0 in range(1,p)}
        assert set(sols)==expected
        assert len(sols)==2*p*p-p
        ranks=Counter(rank2(M,p) for M in sols)
        assert tuple(ranks[i] for i in range(3))==(1,p*p-1,p*(p-1))
        auts=auts_odd(p)
        pool=set(sols); orbits=[]
        while pool:
            M=next(iter(pool))
            O={conj(M,P,p) for P in auts}
            assert O<=set(sols)
            orbits.append(O); pool-=O
        sizes=Counter(len(O) for O in orbits)
        expected_sizes=Counter({1:1,p-1:1,p:2*(p-1)})
        # At p=2 sizes collide, but this branch is odd only.
        assert sizes==expected_sizes,(p,sizes,expected_sizes)
        assert len(orbits)==2*p
        print({"q":p,"operators":len(sols),"ranks":tuple(ranks[i] for i in range(3)),
               "orbits":len(orbits),"orbit_sizes":dict(sorted(sizes.items()))})

print("VERIFY_OK")
