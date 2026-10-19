"""Exact, dependency-free finite-field checks of parabolic triple-fiber phases.

For F_25 represent a+b*z with z*z=2 in F_5. The kernel rank computation
uses *only noncritical fibers*, which is the condition required by the proof.
"""
from itertools import combinations_with_replacement

P = 5
Q = 25

def plus(a,b):
    return (a%P+b%P)%P + P*((a//P+b//P)%P)

def times(a,b):
    a0,a1=a%P,a//P
    b0,b1=b%P,b//P
    return (a0*b0+2*a1*b1)%P + P*((a0*b1+a1*b0)%P)

def square(x):
    return times(x,x)

def trace(x):
    return (2*(x%P))%P  # conjugation sends z to -z

def rank_mod_p(rows):
    pivots={}
    for row in rows:
        v=row[:]
        while True:
            k=next((i for i,x in enumerate(v) if x%P),None)
            if k is None:
                break
            if k not in pivots:
                inv=pow(v[k],-1,P)
                pivots[k]=[(x*inv)%P for x in v]
                break
            v=[(x-v[k]*w)%P for x,w in zip(v,pivots[k])]
    return len(pivots)

fibers={}
for a,b,c in combinations_with_replacement(range(Q),3):
    key=(plus(plus(a,b),c),plus(plus(square(a),square(b)),square(c)))
    fibers.setdefault(key,[]).append((a,b,c))
assert len(fibers)==Q*Q
rows=[]
noncritical=0
for (s,e),triples in fibers.items():
    is_critical=(times(3,e)==square(s))
    assert len(triples)>=1
    if is_critical:
        continue
    noncritical+=1
    first=triples[0]
    for triple in triples[1:]:
        row=[0]*Q
        for x in first:row[x]=(row[x]-1)%P
        for x in triple:row[x]=(row[x]+1)%P
        rows.append(row)
assert noncritical==600
assert len(rows)==2100
rank=rank_mod_p(rows)
assert rank==20 and Q-rank==5

# For each of the 25 quadratic-trace parameters, the 25 coefficient vectors
# have constant triple products on every noncritical fiber. The remaining
# 25 linear characters are automatic because all triples have equal sum.
for b in range(Q):
    phase=[trace(times(b,square(x))) for x in range(Q)]
    for triples in fibers.values():
        ex=sum(phase[x] for x in triples[0])%P
        assert all(sum(phase[x] for x in t)%P==ex for t in triples)

# Independently count ordered triple fibers and the normalized constant moment.
ordered={}
for a in range(Q):
    for b in range(Q):
        for c in range(Q):
            key=(plus(plus(a,b),c),plus(plus(square(a),square(b)),square(c)))
            ordered[key]=ordered.get(key,0)+1
assert sorted(set(ordered.values()))==[24,49]
assert sum(n==49 for n in ordered.values())==25
assert sum(n==24 for n in ordered.values())==600
moment_numerator=sum(n*n for n in ordered.values())
assert moment_numerator==405625
assert moment_numerator*625==Q**4*(Q*Q+Q-1)  # 1+1/q-1/q^2
print('F_25: 600 noncritical fibers; 2100 relations; rank 20 over F_5, nullity 5.')
print('F_25: 25 critical fibers of 49 triples and 600 fibers of 24 triples.')
print('F_25: all trace-quadratic phase products constant on fibers; moment 405625/25^4 = 649/625.')
