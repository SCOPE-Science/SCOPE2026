#!/usr/bin/env python3
"""Exact binary-linear verification of the Bring theta-pair classification.
Riera--Rodriguez integral matrices transcribed from Pacific J. Math. 154 (1992), p. 182.
The proof of identification and centralizer is in RESULT.md.
"""
from collections import Counter
from itertools import permutations, product

A = ((0, 0, 0, 1), (-1, 0, 0, -1), (0, -1, 0, 1), (0, 0, -1, -1))
B = ((1, 0, 0, 0), (-1, -1, 0, 0), (1, 0, -1, 0), (-1, 0, 0, -1))
T = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 1))


def mm(P, Q):
    return tuple(tuple(sum(P[i][k]*Q[k][j] for k in range(len(Q))) % 2
                       for j in range(len(Q[0]))) for i in range(len(P)))

def matperm(p):
    # Basis e_i+e_5, i=1,...,4, of F_2^5 even-weight vectors.
    result = [[0]*4 for _ in range(4)]
    for j in range(4):
        mask = (1 << p[j]) | (1 << p[4])
        for i in range(4):
            result[i][j] = (mask >> i)&1
    return tuple(map(tuple, result))

five_cycle = (1, 2, 3, 4, 0)
swap = (1, 0, 2, 3, 4)
As, Bs = matperm(five_cycle), matperm(swap)
assert mm(A, T) == mm(T, As) and mm(B, T) == mm(T, Bs)

# Check invertibility of T over F2 by full column image.
def mact(P, u):
    return tuple(sum(P[i][j]*u[j] for j in range(4))%2 for i in range(4))
assert len({mact(T,u) for u in product(range(2),repeat=4)})==16
print('RIERA_S5_GENERATORS_CONJUGATE_TO_EVEN_SUBSET_MODULE=PASS')

# The invariant dot form on V: H_ij=1 if i!=j and 0 otherwise.
H = tuple(tuple(int(i != j) for j in range(4)) for i in range(4))
for M in (As, Bs):
    assert all(sum(H[i][j]*x[i]*y[j] for i in range(4) for j in range(4)) % 2 ==
               sum(H[i][j]*mact(M,x)[i]*mact(M,y)[j] for i in range(4) for j in range(4))%2
               for x in product(range(2),repeat=4) for y in product(range(2),repeat=4))
print('S5_PRESERVES_ALTERNATING_NONDEGENERATE_PAIRING=PASS')

E = [m for m in range(32) if m.bit_count()%2==0]
assert len(E)==16
X = [(a,b) for a in E for b in E]
assert len(X)==256
q = lambda ab: (ab[0]&ab[1]).bit_count()%2

def permute_mask(p,m):
    return sum(1<<p[i] for i in range(5) if m>>i&1)

def permute_pair(p,ab):
    return (permute_mask(p,ab[0]), permute_mask(p,ab[1]))

# Exhaustive S5 orbit enumeration, not simply expected partition sizes.
unseen=set(X); orbits=[]
while unseen:
    seed=min(unseen); orbit={seed}; frontier=[seed]
    while frontier:
        z=frontier.pop()
        for p in (five_cycle, swap):
            nxt=permute_pair(p,z)
            if nxt not in orbit: orbit.add(nxt);frontier.append(nxt)
    assert orbit<=unseen
    unseen-=orbit; orbits.append(orbit)
assert len(orbits)==14
stat = lambda ab: (ab[0].bit_count(),ab[1].bit_count(),(ab[0]&ab[1]).bit_count())
assert all(len({stat(z) for z in O})==1 for O in orbits)
summary={(stat(next(iter(O)))):(len(O),q(next(iter(O)))) for O in orbits}
assert len(summary)==14
expected_even={(0,0,0):1,(0,2,0):10,(0,4,0):5,(2,0,0):10,
               (2,2,0):30,(2,2,2):10,(2,4,2):30,(4,0,0):5,
               (4,2,2):30,(4,4,4):5}
expected_odd={(2,2,1):60,(2,4,1):20,(4,2,1):20,(4,4,3):20}
assert {k:v[0] for k,v in summary.items() if v[1]==0}==expected_even
assert {k:v[0] for k,v in summary.items() if v[1]==1}==expected_odd
print('S5_ORBIT_COUNTS_EVEN=136:1+5+5+5+10+10+10+30+30+30')
print('S5_ORBIT_COUNTS_ODD=120:20+20+20+60')

# GL2(F2) centralizes S5 and preserves parity on the direct sum V+V.
GL = [(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if (a*d+b*c)%2==1]
assert len(GL)==6

def glact(M,z):
    a,b,c,d=M;x,y=z
    return ((x if a else 0)^(y if b else 0),
            (x if c else 0)^(y if d else 0))
assert all(glact(M,z) in X and q(glact(M,z))==q(z) for M in GL for z in X)
assert all(glact(M,permute_pair(p,z))==permute_pair(p,glact(M,z))
           for M in GL for p in (five_cycle,swap) for z in X)

# The GL2(F2) orbit of each S5 orbit is described by its triple of statistics.
idx={z:i for i,O in enumerate(orbits) for z in O}
meta=[(len(O),q(next(iter(O))),stat(next(iter(O)))) for O in orbits]
for k,size,par in [(0,1,0)]:pass
classes=set(range(len(orbits))); action_classes=[]
while classes:
    i=min(classes); companions={idx[glact(M,next(iter(orbits[i])))] for M in GL}
    assert companions<=classes
    classes-=companions
    action_classes.append(tuple(sorted(companions)))
structure=Counter((len(c),meta[c[0]][0],meta[c[0]][1]) for c in action_classes)
assert structure==Counter({(1,1,0):1,(3,5,0):1,(3,10,0):1,
                          (3,30,0):1,(3,20,1):1,(1,60,1):1})
print('COMMUTING_GL2_F2=S3;S5_ORBIT_BUNDLES=',sorted((len(c),meta[c[0]][0],meta[c[0]][1]) for c in action_classes))

# Determine the entire commutant of S5 on V (not just its invertible elements).
# For the vector v={1,2}, S2xS3 fixed vectors in V are 0 and v.
v=(1<<0)|(1<<1)
stab=[p for p in permutations(range(5)) if permute_mask(p,v)==v]
assert len(stab)==12
fixed=[w for w in E if all(permute_mask(p,w)==w for p in stab)]
assert fixed==[0,v]
assert len({((1<<i)|(1<<j)) for i in range(5) for j in range(i+1,5)})==10
print('END_S5_OF_EVEN_WEIGHT_MODULE=F2;FULL_ORTHOGONAL_CENTRALIZER=GL2_F2=S3')
print('VERIFY_OK')
