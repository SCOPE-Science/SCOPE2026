import sympy as s
from itertools import product

phi=(1+s.sqrt(5))/2
m=s.symbols('m', integer=True, positive=True)

def dist(i,j):
    if i==j:
        return s.Integer(0)
    d=abs(i-j)%5
    d=min(d,5-d)
    return s.Integer(1) if d==1 else phi

def value(t, mm):
    a,b,c=t
    ds=[dist(a,b),dist(b,c),dist(c,a)]
    return s.simplify(sum(ds)+(mm-3)*max(ds, key=lambda x: float(x.evalf())))

# Exact classification of all unordered side multisets for distinct triples.
types=set()
for a,b,c in product(range(5), repeat=3):
    if len({a,b,c})==3:
        ds=tuple(sorted([dist(a,b),dist(b,c),dist(c,a)], key=lambda x: float(x.evalf())))
        types.add(tuple(map(s.simplify,ds)))
assert len(types)==2
assert any(ds==(s.Integer(1),s.Integer(1),phi) for ds in types)
assert any(ds==(s.Integer(1),phi,phi) for ds in types)

A=s.simplify(2+(m-2)*phi)
B=s.simplify(1+(m-1)*phi)
assert s.simplify(B-A-(phi-1))==0
assert s.simplify(B-(m-1)*phi-1)==0
assert bool((phi-1)>0)

# Representative exact enumeration; the symbolic comparison above proves all m.
for mm in range(3,32,2):
    vals=[]
    for t in product(range(5), repeat=3):
        vals.append((s.simplify(value(t,mm)),t))
    best=max(vals,key=lambda z:float(z[0].evalf()))[0]
    target=s.simplify(1+(mm-1)*phi)
    assert s.simplify(best-target)==0
    best_distinct=[t for v,t in vals if s.simplify(v-target)==0 and len(set(t))==3]
    assert best_distinct
    for t in best_distinct:
        ds=sorted([dist(t[0],t[1]),dist(t[1],t[2]),dist(t[2],t[0])],key=lambda x:float(x.evalf()))
        assert ds[0]==1 and s.simplify(ds[1]-phi)==0 and s.simplify(ds[2]-phi)==0

print('VERIFY_OK')
print('pentagon_formula =', s.simplify(B))
print('type_gap =', s.simplify(B-A))
