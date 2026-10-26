"""Exact arithmetic certificate for three quadratic-residue translates of F_25.
Run: python3 paley25_verifier.py (no external libraries).
An element a+b*u is encoded as a+5*b, with u*u=2 mod 5.
"""
from collections import Counter
from itertools import combinations

P=5
N=25

def add(x,y):
    return ((x%P+y%P)%P)+P*((x//P+y//P)%P)

def neg(x):
    return (-(x%P))%P+P*((-(x//P))%P)

def sub(x,y):
    return add(x,neg(y))

def mul(x,y):
    a,b=x%P,x//P
    c,d=y%P,y//P
    return ((a*c+2*b*d)%P)+P*((a*d+b*c)%P)

assert all(mul(x,1)==x for x in range(N))
assert all(mul(x,add(y,z))==add(mul(x,y),mul(x,z))
           for x in range(N) for y in range(N) for z in range(N))
S={mul(x,x) for x in range(N)}
SQ=S-{0}
NS=set(range(N))-S
assert len(S)==13 and len(SQ)==12 and len(NS)==12
assert S=={0,1,2,3,4,6,9,12,13,17,18,21,24}
chi=lambda x:0 if x==0 else (1 if x in SQ else -1)

def cover(a):
    return len({add(t,h) for t in a for h in S})==N

def cubic_sum(lam):
    return sum(chi(mul(mul(x,sub(x,1)),sub(x,lam))) for x in range(N))

vals={lam:cubic_sum(lam) for lam in range(2,25)}
assert {k:len([x for x in vals if vals[x]==k]) for k in set(vals.values())} == {
    -10:2,-6:2,-2:8,2:4,6:7}
assert {lam for lam in vals if vals[lam]==-10}=={13,18}
assert all(lam in SQ and sub(lam,1) in SQ for lam in (13,18))

covers={frozenset(a) for a in combinations(range(N),3) if cover(a)}
assert len(covers)==100
assert all(not cover(a) for a in combinations(range(N),2))
assert cover((0,5,16))

# Classification deduced from Hasse-sharp cubic sums and verified directly:
classified={frozenset((a,add(a,t),add(a,mul(t,lam))))
            for a in range(N) for t in NS for lam in (13,18)}
assert len(classified)==100 and classified==covers

# Independent orbit construction under translations and square scalings.
witness=(0,5,16)
orbit={frozenset(add(v,mul(s,x)) for x in witness)
       for v in range(N) for s in SQ}
assert len(orbit)==100 and orbit==covers
stabilizers=sum(frozenset(add(v,mul(s,x)) for x in witness)==frozenset(witness)
                for v in range(N) for s in SQ)
assert stabilizers==3

# Check character-sum identity for every triple; equality forces the two properties.
for a,b,c in combinations(range(N),3):
    T=sum(chi(mul(mul(sub(x,a),sub(x,b)),sub(x,c))) for x in range(N))
    R=sum(all(chi(sub(z,w))==-1 for w in (a,b,c) if w!=z)
          for z in (a,b,c))
    missed=sum(all(chi(sub(x,z))==-1 for z in (a,b,c)) for x in range(N))
    assert 22-T == 8*missed+4*R
    assert (-10<=T<=10)
    assert (missed==0)==(T==10 and R==3)

print('CERTIFICATE_OK squares=13 triple_subsets=2300 covers=100')
print('CUBIC_SUM_CLASSES',dict(sorted(Counter(vals.values()).items())))
print('AFFINE_SQUARE_ORBIT',len(orbit),'STABILIZER',stabilizers)
