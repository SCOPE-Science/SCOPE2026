from itertools import product
from collections import Counter
import sympy as sp

a,b,c,d=sp.symbols("a b c d")
M=sp.Matrix([[a,c],[b,d]])
basis=(sp.Matrix([1,0]),sp.Matrix([0,1]))

def smul(x,y):
    return sp.Matrix([sp.expand(x[0]*y[0]),
                      sp.expand(x[0]*y[1]+x[1]*y[0])])

eqs=[]
for x in basis:
    for y in basis:
        Tx=M*x
        Ty=M*y
        eqs.extend(list(sp.expand(z) for z in (M*smul(Tx,y)-smul(Tx,Ty))))
        eqs.extend(list(sp.expand(z) for z in (M*smul(x,Ty)-smul(Tx,Ty))))

gens={sp.factor(z) for z in eqs if z!=0}
canonical={sp.factor(z) for z in gens}
for expected in (b*c, b*(a-d), c*d, d*(a-d)):
    assert expected in canonical or -expected in canonical
assert all(any(sp.expand(g-e)==0 or sp.expand(g+e)==0
               for e in (b*c,b*(a-d),c*d,d*(a-d))) for g in canonical)

u,v=sp.symbols("u v")
families=[
    sp.Matrix([[u,v],[0,0]]),
    sp.Matrix([[u,0],[v,u]]),
]
for N in families:
    for x in basis:
        for y in basis:
            Nx=N*x
            Ny=N*y
            assert sp.simplify(N*smul(Nx,y)-smul(Nx,Ny))==sp.zeros(2,1)
            assert sp.simplify(N*smul(x,Ny)-smul(Nx,Ny))==sp.zeros(2,1)

def mul(x,y,p):
    return (x[0]*y[0]%p,(x[0]*y[1]+x[1]*y[0])%p)

def mv(T,x,p):
    return ((T[0][0]*x[0]+T[0][1]*x[1])%p,
            (T[1][0]*x[0]+T[1][1]*x[1])%p)

def avg(T,p):
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            Tx=mv(T,x,p); Ty=mv(T,y,p)
            common=mul(Tx,Ty,p)
            if mv(T,mul(Tx,y,p),p)!=common: return False
            if mv(T,mul(x,Ty,p),p)!=common: return False
    return True

def conj(T,s,p):
    si=pow(s,-1,p)
    return ((T[0][0]%p,T[0][1]*si%p),
            (s*T[1][0]%p,T[1][1]%p))

for p in (2,3,5,7):
    mats=[((aa,cc),(bb,dd)) for aa,bb,cc,dd in product(range(p),repeat=4)]
    ops=[T for T in mats if avg(T,p)]
    expected=[
        T for T in mats
        if (
            (T[1][0]==0 and T[1][1]==0)
            or
            (T[0][1]==0 and T[1][1]==T[0][0])
        )
    ]
    assert set(ops)==set(expected)
    assert len(ops)==2*p*p-1

    rem=set(ops); orbits=[]
    while rem:
        T=next(iter(rem))
        orb={conj(T,s,p) for s in range(1,p)}
        orbits.append(orb)
        rem-=orb

    assert len(orbits)==4*p-1
    sizes=Counter(map(len,orbits))
    expected_sizes=Counter()
    expected_sizes[1]+=2*p-1
    expected_sizes[p-1]+=2*p
    assert sizes==expected_sizes, (p,sizes,expected_sizes)
    print({"q":p,"operators":len(ops),"orbits":len(orbits),
           "orbit_sizes":dict(sorted(sizes.items()))})

print("VERIFY_OK")
