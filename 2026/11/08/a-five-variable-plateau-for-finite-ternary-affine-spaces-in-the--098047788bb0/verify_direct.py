"""Direct small-dimension checks for the ternary affine parallelogram relation."""
from itertools import combinations, product

def pts(d):
    return list(product(range(3), repeat=d))

def P(a,b,c,e):
    return all((x-y+z-w)%3 == 0 for x,y,z,w in zip(a,b,c,e))

def collinear(a,b,c):
    return P(a,b,c,b)

def four_independent(q):
    if any(collinear(*t) for t in combinations(q,3)):
        return False
    a,b,c,d=q
    return not (P(a,b,c,d) or P(a,c,b,d) or P(a,b,d,c))

counts=[]
for d in (0,1,2,3):
    vs=pts(d)
    independent3=sum(not collinear(*t) for t in combinations(vs,3))
    independent4=sum(four_independent(q) for q in combinations(vs,4))
    counts.append((d,len(vs),independent3,independent4))
    assert bool(independent3)==(d>=2)
    assert bool(independent4)==(d>=3)
    print(f'd={d}: points={len(vs)} independent_triples={independent3} independent_quadruples={independent4}')
assert counts[2][2]==72 and counts[3][3]==12636
print('DIRECT_WITNESSES=PASS')
