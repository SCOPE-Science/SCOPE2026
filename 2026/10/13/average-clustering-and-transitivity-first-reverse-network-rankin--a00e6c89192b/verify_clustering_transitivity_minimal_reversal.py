#!/usr/bin/env python3
from itertools import combinations, permutations
from fractions import Fraction

def pairs(n):
    return list(combinations(range(n), 2))

def connected(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

def canonical_code(n, edges):
    E={tuple(sorted(e)) for e in edges}
    ps=pairs(n)
    best=None
    for p in permutations(range(n)):
        F={tuple(sorted((p[u],p[v]))) for u,v in E}
        code=''.join('1' if e in F else '0' for e in ps)
        if best is None or code < best:
            best=code
    return best

def metrics(n, edges, leaf_convention="exclude"):
    E={tuple(sorted(e)) for e in edges}
    adj=[set() for _ in range(n)]
    for u,v in E:
        adj[u].add(v); adj[v].add(u)

    triangles=0
    for a,b,c in combinations(range(n),3):
        if (a,b) in E and (a,c) in E and (b,c) in E:
            triangles += 1

    triples=sum(len(adj[v])*(len(adj[v])-1)//2 for v in range(n))
    T=Fraction(3*triangles, triples) if triples else Fraction(0)

    locals_=[]
    for v in range(n):
        d=len(adj[v])
        if d < 2:
            if leaf_convention == "zero":
                locals_.append(Fraction(0))
            continue
        closed=sum(
            1 for x,y in combinations(adj[v],2)
            if tuple(sorted((x,y))) in E
        )
        locals_.append(Fraction(closed, d*(d-1)//2))
    C=sum(locals_, Fraction(0))/len(locals_) if locals_ else Fraction(0)
    return T,C

def unlabeled_connected(n):
    ps=pairs(n)
    reps={}
    for mask in range(1 << len(ps)):
        E=[ps[i] for i in range(len(ps)) if (mask >> i) & 1]
        if connected(n,E):
            reps.setdefault(canonical_code(n,E), E)
    return reps

expected_classes={2:1,3:2,4:6,5:21}
expected_reversals_exclude={2:0,3:0,4:0,5:13}
expected_reversals_zero={2:0,3:0,4:0,5:12}

for convention, expected in [
    ("exclude", expected_reversals_exclude),
    ("zero", expected_reversals_zero),
]:
    for n in range(2,6):
        reps=unlabeled_connected(n)
        assert len(reps)==expected_classes[n]
        values=[metrics(n,E,convention) for E in reps.values()]
        rev=0
        for (T1,C1),(T2,C2) in combinations(values,2):
            if (T1-T2)*(C1-C2) < 0:
                rev += 1
        assert rev==expected[n], (convention,n,rev)

# Under the Schank-Wagner convention, n=4 has pointwise disagreement but
# still no strict cross-graph ranking reversal.
vals4=set(metrics(4,E,"exclude") for E in unlabeled_connected(4).values())
assert vals4 == {
    (Fraction(0),Fraction(0)),
    (Fraction(3,5),Fraction(7,9)),
    (Fraction(3,4),Fraction(5,6)),
    (Fraction(1),Fraction(1)),
}

# Matched five-vertex witness: both graphs have five edges and one triangle.
A=[(0,4),(1,4),(2,3),(2,4),(3,4)] # two leaves on one triangle vertex
B=[(0,1),(0,2),(0,4),(1,2),(2,3)] # leaves on two triangle vertices
assert len(A)==len(B)==5

assert metrics(5,A,"exclude") == (Fraction(3,8),Fraction(13,18))
assert metrics(5,B,"exclude") == (Fraction(3,7),Fraction(5,9))
TA,CA=metrics(5,A,"exclude")
TB,CB=metrics(5,B,"exclude")
assert TA < TB and CA > CB

# Same witness and same sharp order threshold if degree-0/1 local clustering
# is defined as zero and averaged over all vertices.
assert metrics(5,A,"zero") == (Fraction(3,8),Fraction(13,30))
assert metrics(5,B,"zero") == (Fraction(3,7),Fraction(1,3))
TA0,CA0=metrics(5,A,"zero")
TB0,CB0=metrics(5,B,"zero")
assert TA0 < TB0 and CA0 > CB0

# Independent hand-count checks for the witness.
# A: one triangle; wedge count C(4,2)+C(2,2)+C(2,2)=8.
#    local coefficients on degree>=2 vertices are 1/6,1,1.
# B: one triangle; wedge count C(3,2)+C(3,2)+C(2,2)=7.
#    local coefficients on degree>=2 vertices are 1/3,1/3,1.
assert Fraction(3,8)==TA
assert (Fraction(1,6)+1+1)/3==CA
assert Fraction(3,7)==TB
assert (Fraction(1,3)+Fraction(1,3)+1)/3==CB

print("VERIFY_OK")
print("connected_unlabeled_counts", expected_classes)
print("strict_reversal_counts_exclude", expected_reversals_exclude)
print("strict_reversal_counts_zero", expected_reversals_zero)
print("n4_metric_pairs_exclude", sorted(map(str, vals4)))
print("witness_A_exclude", TA, CA)
print("witness_B_exclude", TB, CB)
print("witness_A_zero", TA0, CA0)
print("witness_B_zero", TB0, CB0)
