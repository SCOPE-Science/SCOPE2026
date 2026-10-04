from itertools import product, combinations
from collections import deque, Counter

def add(a,b,mods):
    return tuple((x+y)%n for x,y,n in zip(a,b,mods))

def neg(a,mods):
    return tuple((-x)%n for x,n in zip(a,mods))

def kernel_elements(mods):
    return list(product(*[range(n) for n in mods]))

def build(mods):
    A=kernel_elements(mods)
    zero=tuple(0 for _ in mods)
    elems=[(a,e) for a in A for e in (0,1)]
    identity=(zero,0)
    def mul(x,y):
        a,e=x; b,f=y
        if e:
            b=neg(b,mods)
        return (add(a,b,mods),(e+f)%2)
    def inv(x):
        a,e=x
        if e==0:
            return (neg(a,mods),0)
        return x
    return A, elems, identity, mul, inv

def generated(gens, identity, mul, inv):
    gs=list(gens)+[inv(g) for g in gens]
    seen={identity}
    q=deque([identity])
    while q:
        x=q.popleft()
        for g in gs:
            y=mul(x,g)
            if y not in seen:
                seen.add(y); q.append(y)
    return seen

def cyclic_size(a,mods):
    zero=tuple(0 for _ in mods)
    x=zero
    seen={zero}
    while True:
        x=add(x,a,mods)
        if x in seen:
            return len(seen)
        seen.add(x)

def check(mods):
    A, elems, identity, mul, inv=build(mods)
    m=len(A)
    assert m%2==1 and m>1

    center=[]
    for x in elems:
        if all(mul(x,y)==mul(y,x) for y in elems):
            center.append(x)
    assert center==[identity]

    vertices=[x for x in elems if x!=identity]
    edges=set()
    for x,y in combinations(vertices,2):
        if mul(x,y)==mul(y,x):
            continue
        H=generated([x,y],identity,mul,inv)
        if len(H)<len(elems):
            edges.add(frozenset((x,y)))

    generators={a for a in A if a!=identity[0] and cyclic_size(a,mods)==m}
    nongens={a for a in A if a!=identity[0] and a not in generators}
    b=len(nongens)

    predicted=set()
    rotations=[(a,0) for a in A if a!=identity[0]]
    reflections=[(a,1) for a in A]

    # Mixed edges: exactly non-generator rotations to all reflections.
    for a in nongens:
        for r in reflections:
            predicted.add(frozenset(((a,0),r)))

    # Reflection edges: difference is a non-generator nonidentity kernel element.
    for x,y in combinations(reflections,2):
        a=x[0]; c=y[0]
        diff=add(a,neg(c,mods),mods)
        if diff in nongens:
            predicted.add(frozenset((x,y)))

    assert edges==predicted

    deg=Counter()
    for e in edges:
        x,y=tuple(e)
        deg[x]+=1; deg[y]+=1

    for a in generators:
        assert deg[(a,0)]==0
    for a in nongens:
        assert deg[(a,0)]==m
    for r in reflections:
        assert deg[r]==2*b

    assert 2*len(edges)==3*m*b

    # Noncyclic iff no element has cyclic subgroup of size m.
    if not generators:
        assert len(nongens)==m-1
        for x,y in combinations(reflections,2):
            assert frozenset((x,y)) in edges
        for x,y in combinations(rotations,2):
            assert frozenset((x,y)) not in edges
        for x in rotations:
            for y in reflections:
                assert frozenset((x,y)) in edges

    return {
        'kernel': 'x'.join(map(str,mods)),
        'm':m,
        'generators':len(generators),
        'b':b,
        'vertices':len(vertices),
        'edges':len(edges),
        'reflection_degree':2*b,
    }

rows=[check(mods) for mods in [
    (3,), (9,), (15,), (3,3), (9,3), (5,5)
]]

# Explicit sanity checks for representative formulas.
assert rows[0]['edges']==0
assert rows[1]['b']==2 and rows[1]['edges']==27
assert rows[2]['b']==6 and rows[2]['edges']==135
assert rows[3]['b']==8 and rows[3]['edges']==108
assert rows[4]['b']==26 and rows[4]['edges']==1053
assert rows[5]['b']==24 and rows[5]['edges']==900

print('VERIFY_OK')
for row in rows:
    print(row)
