from itertools import product
from collections import Counter
import sympy as sp

# Symbolic multiplication for e1*e1=2e1, e1*e2=e2, e2*e2=0.
a,b,c,d=sp.symbols("a b c d")
M=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1]); basis=(e1,e2)

def mul(x,y):
    return sp.Matrix([2*x[0]*y[0], x[0]*y[1]+x[1]*y[0]])

# Jordan identity.
x0,x1,y0,y1=sp.symbols("x0 x1 y0 y1")
x=sp.Matrix([x0,x1]); y=sp.Matrix([y0,y1])
assert sp.simplify(mul(mul(mul(x,x),y),x)-mul(mul(x,x),mul(y,x)))==sp.zeros(2,1)

# Rota-Baxter defects.
eqs=[]
for x in basis:
    for y in basis:
        Rx=M*x; Ry=M*y
        eqs.extend(list(sp.expand(z) for z in (mul(Rx,Ry)-M*(mul(Rx,y)+mul(x,Ry)))))
nonzero=[sp.factor(z) for z in eqs if z!=0]
expected=[-2*(a*a+b*c),-2*c*(a+d),-b*(a+d),-(b*c+d*d),-b*(a+d),-(b*c+d*d)]
assert len(nonzero)==len(expected) and all(sp.expand(x-y)==0 for x,y in zip(nonzero,expected)), nonzero

# General conjugation formula.
t,s=sp.symbols("t s", nonzero=True)
P=sp.Matrix([[1,0],[t,s]])
C=sp.simplify(P*M*P.inv())
assert C==sp.Matrix([[a-b*t/s,b/s],[a*t-b*t*t/s+c*s-d*t,b*t/s+d]])

# Finite field direct replay for prime fields.
def vmul(x,y,p):
    return (2*x[0]*y[0]%p,(x[0]*y[1]+x[1]*y[0])%p)

def mv(A,x,p):
    return ((A[0][0]*x[0]+A[0][1]*x[1])%p,
            (A[1][0]*x[0]+A[1][1]*x[1])%p)

def rb(A,p):
    E=((1,0),(0,1))
    for x in E:
        for y in E:
            Rx=mv(A,x,p); Ry=mv(A,y,p)
            lhs=vmul(Rx,Ry,p)
            inside=tuple((u+v)%p for u,v in zip(vmul(Rx,y,p),vmul(x,Ry,p)))
            if lhs!=mv(A,inside,p): return False
    return True

def det(A,p):
    return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%p

def mm(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))

def inv(A,p):
    z=pow(det(A,p),-1,p)
    return ((A[1][1]*z%p,-A[0][1]*z%p),(-A[1][0]*z%p,A[0][0]*z%p))

def auto(A,p):
    if det(A,p)==0: return False
    E=((1,0),(0,1))
    return all(mv(A,vmul(x,y,p),p)==vmul(mv(A,x,p),mv(A,y,p),p) for x in E for y in E)

def conj(P,A,p):
    return mm(mm(P,A,p),inv(P,p),p)

for p in (2,3,5,7):
    mats=[((aa,bb),(cc,dd)) for aa,bb,cc,dd in product(range(p),repeat=4)]
    ops=[A for A in mats if rb(A,p)]
    autos=[A for A in mats if auto(A,p)]
    expected_aut=[((1,0),(tt,ss)) for tt in range(p) for ss in range(1,p)]
    assert set(autos)==set(expected_aut)

    if p==2:
        predicted=[A for A in mats if (A[0][1]*(A[0][0]+A[1][1]))%p==0 and (A[0][1]*A[1][0]+A[1][1]**2)%p==0]
        assert len(ops)==2*p*p-p
        expected_count=p+2
    else:
        predicted=[A for A in mats if A[1][1]%p==(-A[0][0])%p and (A[0][0]**2+A[0][1]*A[1][0])%p==0]
        assert len(ops)==p*p
        expected_count=3
    assert set(ops)==set(predicted)

    rem=set(ops); orbits=[]
    while rem:
        A=next(iter(rem))
        orb={conj(P,A,p) for P in autos}
        orbits.append(orb); rem-=orb
    assert len(orbits)==expected_count

    sizes=Counter(map(len,orbits))
    if p==2:
        exp=Counter(); exp[1]+=1; exp[p-1]+=1; exp[p*(p-1)]+=1; exp[p]+=p-1
    else:
        exp=Counter(); exp[1]+=1; exp[p-1]+=1; exp[p*(p-1)]+=1
    assert sizes==exp,(p,sizes,exp)
    print({"q":p,"operators":len(ops),"orbits":len(orbits),"orbit_sizes":dict(sorted(sizes.items()))})

print("VERIFY_OK")
