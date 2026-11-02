#!/usr/bin/env python3
"""Exact finite congruence and small-difference enumeration for Z[omega]."""
from itertools import combinations
from collections import Counter, defaultdict

LIMIT = {1,3,4,12}

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def conj(x):
    a,b=x
    return (a-b,-b)
UNITS = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
assert sorted({norm(u) for u in UNITS})==[1]

# A six-point set satisfying the requisite residue balance must have every
# pairwise norm in LIMIT. Its translation to include zero is thus contained
# in this complete 25-point candidate set (coordinate bound |a|,|b| <= 4 suffices).
V = sorted({(0,0)} | {(a,b) for a in range(-5,6) for b in range(-5,6)
                      if norm((a,b)) in LIMIT})
assert len(V) == 25, len(V)
NEIGH = [v for v in V if v != (0,0)]

def profile(S):
    c3 = Counter((a+b)%3 for a,b in S)  # modulo 1-omega
    c4 = Counter((a%2,b%2) for a,b in S)  # modulo 2 (inert)
    return tuple(sorted(c3.get(r,0) for r in range(3))), tuple(sorted(c4.get(r,0) for r in [(0,0),(0,1),(1,0),(1,1)]))

def almost_even(xs): return max(xs)-min(xs)<=1

def small_difference(S):
    return all(norm(sub(x,y)) in LIMIT for x,y in combinations(S,2))

def is_balanced(S):
    a,b=profile(S)
    return small_difference(S) and almost_even(a) and almost_even(b)

def canonical(S):
    vals=[]
    for base in S:
        shifted=[sub(z,base) for z in S]
        for reflect in (False,True):
            for u in UNITS:
                vals.append(tuple(sorted(mul(u,conj(z) if reflect else z) for z in shifted)))
    return min(vals)

# Graph-clique search, with indices increasing: every rooted 6-set is visited once.
allcliques=[]
for sub5 in combinations(NEIGH,5):
    S=((0,0),)+sub5
    if small_difference(S): allcliques.append(S)
assert len(allcliques)==54,len(allcliques)
orbits=defaultdict(list)
for S in allcliques: orbits[canonical(S)].append(S)
assert len(orbits)==3,len(orbits)
assert sorted(map(len,orbits.values())) == [6,12,36]
assert not any(is_balanced(S) for S in allcliques)
for C,members in sorted(orbits.items(),key=lambda kv:kv[0]):
    print('ORBIT',len(members),'REP',C,'RESIDUES',profile(C))

witnesses={
    1:[(0,0),(1,0)],
    2:[(0,0),(0,1),(1,1)],
    3:[(0,0),(0,1),(1,2),(1,1)],
    4:[(0,0),(0,2),(0,1),(1,2),(1,1)],
}
for n,S in witnesses.items():
    assert len(S)==n+1 and len(set(S))==len(S)
    assert is_balanced(S),(n,S,profile(S))
    print('EXISTS',n,'WITNESS',S,'RESIDUES',profile(S))
print('VERIFY_OK disk=25 rooted_six_cliques=54 symmetry_orbits=3 balanced_six=0 witnesses=1..4')
