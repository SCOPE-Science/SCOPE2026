"""Exact checks for period-two dyadic three-cylinder survivors.
Run: python verify.py. Standard library only.
"""
from itertools import permutations, product, combinations
from fractions import Fraction
from collections import defaultdict

WORDS=list(product((0,1),repeat=3))
STATES=list(product((0,1),repeat=2))
INDEX={s:i for i,s in enumerate(STATES)}

def transition(w):
    a=[[0]*4 for _ in range(4)]
    for state in STATES:
        for bit in (0,1):
            if state+(bit,)!=w:
                a[INDEX[state]][INDEX[(state[1],bit)]]+=1
    return a

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def det(a):
    d=0
    for p in permutations(range(len(a))):
        s=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        t=s
        for i,j in enumerate(p):t*=a[i][j]
        d+=t
    return d

def reciprocal_char(a):
    # Coefficients of det(I-zA) from principal minors.
    ans=[1]
    for k in range(1,5):
        ans.append((-1)**k*sum(det([[a[i][j] for j in S] for i in S]) for S in combinations(range(4),k)))
    return tuple(ans)

def apply(op,pair):
    u,v=pair
    if op==0:return (tuple(1-x for x in u),tuple(1-x for x in v))
    if op==1:return v,u
    return u[::-1],v[::-1]

def orbit(pair):
    seen={pair}; front=[pair]
    while front:
        p=front.pop()
        for op in (0,1,2):
            q=apply(op,p)
            if q not in seen: seen.add(q);front.append(q)
    return seen

matrix={w:transition(w) for w in WORDS}
pair_poly={(u,v):reciprocal_char(multiply(matrix[u],matrix[v])) for u in WORDS for v in WORDS}
assert len(pair_poly)==64
seen=set(); representatives=[]
for pair in pair_poly:
    if pair in seen:continue
    o=orbit(pair);seen.update(o)
    assert len({pair_poly[x] for x in o})==1
    representatives.append((pair,len(o),pair_poly[pair]))
assert len(seen)==64 and len(representatives)==14
classes=defaultdict(list)
for pair,poly in pair_poly.items():classes[poly].append(pair)
expected={
 (1,-4,4,-1,0):8,
 (1,-3,0,1,0):16,
 (1,-2,-3,-1,0):12,
 (1,-4,3,-1,0):8,
 (1,-3,-1,1,0):16,
 (1,-3,-1,-1,0):4,
}
assert {poly:len(pairs) for poly,pairs in classes.items()}==expected

def direct_survivor(u,v,n):
    return sum(all(tuple(bits[i:i+3])!=(u if i%2==0 else v) for i in range(n)) for bits in product((0,1),repeat=n+2))

def transfer_survivor(u,v,n):
    vals=[1]*4
    for i in reversed(range(n)):
        a=matrix[u if i%2==0 else v]
        vals=[sum(a[j][k]*vals[k] for k in range(4)) for j in range(4)]
    return sum(vals)

def direct_periodic(u,v,n):
    # Time-2 return: period 2n sequence, tested on circular length-three words.
    return sum(all(tuple(bits[(i+j)%(2*n)] for j in range(3))!=(u if i%2==0 else v) for i in range(2*n)) for bits in product((0,1),repeat=2*n))

def trace_power(u,v,n):
    p=multiply(matrix[u],matrix[v]); q=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(n):q=multiply(q,p)
    return sum(q[i][i] for i in range(4))

surv_tests=0;period_tests=0
for u in WORDS:
    for v in WORDS:
        for n in range(0,9):
            assert direct_survivor(u,v,n)==transfer_survivor(u,v,n),(u,v,n)
            surv_tests+=1
        for n in range(1,6):
            assert direct_periodic(u,v,n)==trace_power(u,v,n),(u,v,n)
            period_tests+=1
# Exact rational brackets around largest Perron roots of the six cubic factors.
intervals={
 (1,-4,4,-1,0):('2.61','2.63'),
 (1,-3,0,1,0):('2.87','2.89'),
 (1,-2,-3,-1,0):('3.07','3.09'),
 (1,-4,3,-1,0):('3.14','3.15'),
 (1,-3,-1,1,0):('3.21','3.22'),
 (1,-3,-1,-1,0):('3.38','3.39'),
}
for poly,(lo,hi) in intervals.items():
    q=lambda x:sum(poly[j]*x**(4-j) for j in range(4))
    a,b=Fraction(lo),Fraction(hi)
    assert q(a)<0<q(b),(poly,a,b,q(a),q(b))
print('VERIFY_OK pairs',len(pair_poly),'symmetry_orbits',len(representatives),'spectral_classes',len(classes),'survivor_tests',surv_tests,'periodic_tests',period_tests)
for (u,v),size,poly in representatives:
    print('REP', ''.join(map(str,u)), ''.join(map(str,v)),size,','.join(map(str,poly)))
