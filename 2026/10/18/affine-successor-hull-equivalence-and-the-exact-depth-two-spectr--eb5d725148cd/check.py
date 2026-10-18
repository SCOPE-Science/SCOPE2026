"""Independent finite semantic and affine-hull checks for bounded-depth modal parity."""
from collections import Counter
from itertools import product

def rank_vectors(vectors):
    b={}
    for v in vectors:
        x=v
        while x:
            j=x.bit_length()-1
            if j not in b:
                b[j]=x
                break
            x^=b[j]
    return len(b)

def affine_closure(S,n):
    if not S: return 0
    s0=min(S); basis=[]; cur={0}
    for p in S:
        x=p^s0
        if x not in cur:
            cur|={v^x for v in list(cur)}
    return sum(1<<x for x in (s0^v for v in cur))

def all_hulls_on(points,n):
    out={}
    for mask in range(1<<len(points)):
        S=[points[i] for i in range(len(points)) if mask>>i&1]
        out[affine_closure(S,n)]=1+rank_vectors([x^S[0] for x in S[1:]]) if S else 0
    return out

for n,expected in [(1,8),(2,48),(3,416)]:
    # Enumerate all affine flats including empty in n-dimensional binary space.
    hulls=all_hulls_on(list(range(1<<n)),n)
    assert (1<<n)*len(hulls)==expected, (n,len(hulls))
    print('DEPTH1',n,'affine_hulls',len(hulls),'pointed_types',(1<<n)*len(hulls))

# All eight depth-one pointed one-variable types are freely attainable.
# Bits (low to high): p, diamond_top, diamond_not_p, diamond_p.
points=[p | ((u or v)<<1) | (u<<2) | (v<<3)
        for p,u,v in product((0,1),repeat=3)]
assert len(set(points))==8,points
hulls=all_hulls_on(points,4)
distribution=Counter()
for mask in hulls:
    if mask == 0: distribution['empty']+=1
    else:
        vs=[x for x in range(16) if mask>>x&1]
        distribution[rank_vectors([x^vs[0] for x in vs[1:]])]+=1
print('DEPTH2_ONE_VARIABLE',len(hulls),'root_types',2*len(hulls),'hull_dimension_distribution',dict(distribution))
assert len(hulls)==96,(len(hulls),distribution)
assert distribution=={'empty':1,0:8,1:28,2:38,3:20,4:1}
assert rank_vectors([x^points[0] for x in points[1:]])==4

# Independent alternate computation: points share affine hull iff every
# affine linear test has the same existential truth on each set.
affine_tests={}
for subset in range(1<<len(points)):
    S=[points[i] for i in range(len(points)) if subset>>i&1]
    tests=0
    for coefficient in range(16):
        for intercept in range(2):
            true=any((((x&coefficient).bit_count()&1)^intercept) for x in S)
            tests|=int(true)<<(2*coefficient+intercept)
    aff=affine_closure(S,4)
    if aff in affine_tests: assert affine_tests[aff]==tests
    else: affine_tests[aff]=tests
assert len(set(affine_tests.values()))==len(hulls)==96

# Fully independent concrete Kripke model check, 3 labelled worlds,
# arbitrary directed relation and every binary valuation.
seen_by_hull={}
seen_by_tests={}
world_checks=0
for rel in range(1<<9):
    succ=[[j for j in range(3) if rel>>(3*i+j)&1] for i in range(3)]
    for val in range(8):
        p=[val>>i&1 for i in range(3)]
        types=[]
        for i in range(3):
            successors=succ[i]
            z=any(1 for j in successors if p[j]==0)
            o=any(1 for j in successors if p[j]==1)
            types.append(p[i] | (int(z or o)<<1) | (int(z)<<2) | (int(o)<<3))
        for i in range(3):
            S=[types[j] for j in succ[i]]
            inv=(p[i],affine_closure(S,4))
            truth=tuple(int(any((((x&mask).bit_count()&1)^c) for x in S))
                        for mask in range(16) for c in range(2))
            whole=(p[i],truth)
            if inv in seen_by_hull: assert seen_by_hull[inv]==whole
            else: seen_by_hull[inv]=whole
            if whole in seen_by_tests: assert seen_by_tests[whole]==inv
            else: seen_by_tests[whole]=inv
            world_checks+=1
print('CONCRETE_ROOT_CHECKS',world_checks,'realized_signatures',len(seen_by_hull))
assert world_checks==3*512*8
print('AFFINE_DEPTH_VERIFY_OK')
