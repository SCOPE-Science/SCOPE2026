#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter, defaultdict

F = [tuple(sorted(x)) for x in [
(1,2,4),(1,2,5),(1,3,8),(1,3,9),(1,4,9),(1,5,6),(1,6,7),(1,7,8),
(2,3,7),(2,3,9),(2,4,6),(2,5,9),(2,6,8),(2,7,8),(3,4,6),(3,4,7),
(3,5,6),(3,5,8),(4,5,7),(4,5,8),(4,8,9),(5,7,9),(6,7,9),(6,8,9)]]
V = tuple(range(1,10))
E = sorted({tuple(sorted(e)) for t in F for e in combinations(t,2)})
Ei = {e:i for i,e in enumerate(E)}
Fset = set(F)

def evec(edges):
    x=0
    for e in edges:
        x ^= 1 << Ei[tuple(sorted(e))]
    return x

def rref_basis(rows):
    basis={}
    for x in rows:
        while x:
            p=(x & -x).bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                for q in list(basis):
                    if (basis[q] >> p) & 1:
                        basis[q] ^= x
                basis[p]=x
                break
    return dict(sorted(basis.items()))

B = rref_basis([evec(combinations(t,2)) for t in F])
def red(x):
    for p,row in B.items():
        if (x >> p) & 1:
            x ^= row
    return x

def cyc_edges(c):
    return [(c[i],c[(i+1)%len(c)]) for i in range(len(c))]

def cycles(k):
    out=[]
    for S in combinations(V,k):
        root=min(S)
        rest=[v for v in S if v != root]
        for p in permutations(rest):
            c=(root,)+p
            if c[1] < c[-1]:
                out.append(c)
    return out

assert len(F)==24 and len(E)==36
assert set(E)==set(combinations(V,2))
edge_deg=Counter(e for t in F for e in combinations(t,2))
assert set(edge_deg.values())=={2}
assert len(B)==23
assert 36-8-len(B)==5

mins={}
mult=Counter()
rep={}
cycle_counts={}
for k in range(3,7):
    C=cycles(k)
    cycle_counts[k]=len(C)
    for c in C:
        s=red(evec(cyc_edges(c)))
        if not s:
            continue
        if s not in mins:
            mins[s]=k
            mult[s]=1
            rep[s]=c
        elif mins[s]==k:
            mult[s]+=1

assert len(mins)==31
assert Counter(mins.values())==Counter({3:24,4:3,5:3,6:1})
profile={k:Counter(mult[s] for s in mins if mins[s]==k) for k in range(3,7)}
assert profile[3]==Counter({1:3,2:9,3:9,4:3})
assert profile[4]==Counter({6:3})
assert profile[5]==Counter({18:3})
assert profile[6]==Counter({66:1})
assert cycle_counts=={3:84,4:378,5:1512,6:5040}

faces=set(F)
missing=[c for c in combinations(V,3) if tuple(sorted(c)) not in faces]
assert len(missing)==60
assert all(red(evec(combinations(c,2))) != 0 for c in missing)
assert all(red(evec(combinations(c,2))) == 0 for c in faces)

autos=[]
for p in permutations(V):
    mp={i:p[i-1] for i in V}
    if {tuple(sorted(mp[x] for x in t)) for t in F}==Fset:
        autos.append(p)
assert len(autos)==18

def action(s,p):
    c=rep[s]
    mp={i:p[i-1] for i in V}
    cc=tuple(mp[x] for x in c)
    return red(evec(cyc_edges(cc)))

unseen=set(mins)
orbits=[]
while unseen:
    s=next(iter(unseen))
    orb={action(s,p) for p in autos}
    orbits.append(orb)
    unseen -= orb
orbprof=sorted((len(o),mins[next(iter(o))],mult[next(iter(o))]) for o in orbits)
assert orbprof==[(1,6,66),(3,3,1),(3,3,4),(3,4,6),(3,5,18),(9,3,2),(9,3,3)]

# Integral Bockstein representative: orient every facet increasingly, sum them,
# and divide the integral boundary by 2.
coeff={e:0 for e in E}
for a,b,c in F:
    coeff[(b,c)] += 1
    coeff[(a,c)] -= 1
    coeff[(a,b)] += 1
assert Counter(coeff.values())==Counter({2:18,0:12,-2:6})
assert all(v%2==0 for v in coeff.values())
half={e:v//2 for e,v in coeff.items()}
vbd={v:0 for v in V}
for (a,b),q in half.items():
    vbd[a]-=q
    vbd[b]+=q
assert all(q==0 for q in vbd.values())
half_mod2=0
for e,q in half.items():
    if q&1:
        half_mod2 ^= 1 << Ei[e]
tors=red(half_mod2)
assert tors in mins and mins[tors]==6 and mult[tors]==66
assert len(next(o for o in orbits if tors in o))==1

print(
 "VERIFY_OK f=9,36,24 H1_F2_dim=5 nonzero_classes=31 "
 "min_lengths=3:24,4:3,5:3,6:1 "
 "triangular_multiplicities=1:3,2:9,3:9,4:3 "
 "length4_multiplicity=6x3 length5_multiplicity=18x3 "
 "length6_multiplicity=66x1 missing3=60 essential3=60 "
 "aut=18 class_orbits=1:6:66|3:3:1|3:3:4|3:4:6|3:5:18|9:3:2|9:3:3 "
 "bockstein_length=6 bockstein_minimizers=66 bockstein_fixed=yes"
)
