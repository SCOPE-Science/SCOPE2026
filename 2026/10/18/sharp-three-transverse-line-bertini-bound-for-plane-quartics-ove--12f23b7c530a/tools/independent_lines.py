"""Independent direct-substitution and finite rational-point validation."""
import json
from itertools import product
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parent.parent
DATA=json.loads((ROOT/'data/quartic_tab.json').read_text())
monos=DATA['monos']
u,v,X,Y,Z=sp.symbols('u v X Y Z')
R=(X,Y,Z)

def normalized_triples():
    out=set()
    for a in product(range(3),repeat=3):
        if a!=(0,0,0):
            fst=next(c for c in a if c)
            out.add(tuple(c*fst%3 if fst==1 else c*2%3 for c in a))
    return sorted(out)

def form(n):
    d=[n//3**i%3 for i in range(15)]
    return sp.expand(sum(c*X**a*Y**b*Z**c3 for c,(a,b,c3) in zip(d,monos)))

def is_good(n,L):
    pivot=next(i for i,c in enumerate(L) if c)
    inds=[i for i in range(3) if i!=pivot]
    q=[0,0,0]
    q[inds[0]]=u;q[inds[1]]=v
    q[pivot]=-(L[inds[0]]*u+L[inds[1]]*v)*pow(L[pivot],-1,3)
    p=sp.Poly(sp.expand(form(n).subs({X:q[0],Y:q[1],Z:q[2]}, simultaneous=True)),u,v,modulus=3)
    coeff=[int(p.coeff_monomial(u**(4-j)*v**j))%3 for j in range(5)]
    if not any(coeff):return False
    if next(i for i,c in enumerate(coeff) if c)>1:return False
    t=sp.symbols('t')
    p1=sp.Poly(sum(coeff[j]*t**(4-j) for j in range(5)),t,modulus=3)
    return sp.gcd(p1,p1.diff()).degree()==0

def count_points(n):
    f=sp.Poly(form(n),X,Y,Z,modulus=3)
    return sum(int(f.eval({X:a,Y:b,Z:c}))%3==0 for a,b,c in normalized_triples())

LS=normalized_triples();assert len(LS)==13
orbits=[]
for s in (ROOT/'out/plane_qorbits.txt').read_text().splitlines():
    if s.startswith('ORBIT'):
        _,t,i,n,size=s.split()
        orbits.append((int(t),int(i),int(n),int(size)))
assert len(orbits)==92
for t,idx,n,size in orbits:
    actual=sum(is_good(n,L) for L in LS)
    assert actual==t,(n,t,actual)
print('All 92 low-transversality orbit representatives independently validated by direct symbolic substitution.')
for n in [78805,80265]:
    good=[L for L in LS if is_good(n,L)]
    assert len(good)==3
    count=count_points(n)
    print('Extremal representative',n,'rational_points',count,'transverse_lines',good)
assert sorted((count_points(i) for i in [78805,80265]))==[1,10]
print('PASS independent line and rational-point checks')
