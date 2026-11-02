"""Verify exact extension multiplicities against independent tuple counting.

The predicted counts are calculated from a coordinate-mask formula, whereas
observed counts enumerate all ordered vertex pairs and witness vertices.
"""
from itertools import product, combinations
import json

def formula(q, same):
    N=1; A=1; I=1
    for x,is_same in zip(q,same):
        N*=x
        A*=x-1
        I*=x-1 if is_same else x-2
    adjacent = not any(same)
    return [N-2*A+I-2*(not adjacent),
            A-I-adjacent, A-I-adjacent, I]

def count(q):
    vertices=list(product(*(range(x) for x in q)))
    profiles={}
    for a,b in combinations(vertices,2):
        same=tuple(x==y for x,y in zip(a,b))
        observed=[0,0,0,0]
        for w in vertices:
            if w==a or w==b:
                continue
            aw=all(x!=y for x,y in zip(a,w))
            bw=all(x!=y for x,y in zip(b,w))
            observed[2*aw+bw]+=1
        expected=formula(q,same)
        assert observed==expected,(q,a,b,observed,expected)
        profiles[tuple(same)]=expected
    return len(vertices),len(profiles),sum(1 for a,b in combinations(vertices,2))

qs=[(3,3),(3,4),(4,4),(3,5),(3,3,3),(3,3,4),(3,4,4),(3,3,3,3)]
results=[]
for q in qs:
    results.append([list(q),*count(q)])

# Prove that no product of >=2 complete factors is 3-e.c.
# A pair (a,b) differing in all coordinates, with a hybrid third anchor,
# forbids the (+,+,-) pattern exactly.
hybrid=[]
for q in qs:
    a=tuple(0 for _ in q)
    b=tuple(1 for _ in q)
    c=tuple([0]+[1]*(len(q)-1))
    V=list(product(*(range(x) for x in q)))
    witness=[w for w in V if w not in (a,b,c)
             and all(x!=y for x,y in zip(w,a))
             and all(x!=y for x,y in zip(w,b))
             and any(x==y for x,y in zip(w,c))]
    assert not witness,(q,witness)
    hybrid.append([list(q),list(a),list(b),list(c)])
print(json.dumps({"independent_pair_checks":sum(r[3] for r in results),
                  "size_profile_pair_checks":results,
                  "3ec_hybrid_obstruction_checks":len(hybrid),
                  "hybrid_examples":hybrid,
                  "status":"PASS"},sort_keys=True,separators=(',',':')))
