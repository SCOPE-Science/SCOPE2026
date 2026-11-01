"""Exact rational verification for electrical-gradient projections on parallel-path networks.

Run: python3 verify_theta.py. Requires only the Python 3 standard library.
A finite test is corroborative; the accompanying proof treats every valid path profile.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
from math import isqrt


def invert(a):
    n=len(a)
    z=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if z[i][j])
        z[j],z[k]=z[k],z[j]
        pivot=z[j][j]
        z[j]=[v/pivot for v in z[j]]
        for i in range(n):
            if i!=j and z[i][j]:
                p=z[i][j]
                z[i]=[a-p*b for a,b in zip(z[i],z[j])]
    return [row[n:] for row in z]


def build_incidence(lengths):
    assert len(lengths)>=2 and min(lengths)>=1 and lengths.count(1)<=1
    # Shared end vertices s=0, t=1. Other vertices private to their path.
    edges=[]
    nxt=2
    for length in lengths:
        if length==1:
            path=[0,1]
        else:
            path=[0]+list(range(nxt,nxt+length-1))+[1]
            nxt+=length-1
        edges.extend([(path[j],path[j+1]) for j in range(length)])
    # Ground the common terminal t=1 and use a full column-rank incidence.
    B=[]
    kept=[0]+list(range(2,nxt))
    for a,b in edges:
        B.append([F(int(v==b)-int(v==a)) for v in kept])
    return B


def independent_projection(lengths):
    B=build_incidence(lengths)
    e=len(B); v=len(B[0])
    gram=[[sum(B[k][i]*B[k][j] for k in range(e)) for j in range(v)] for i in range(v)]
    gi=invert(gram)
    C=[[sum(B[i][k]*gi[k][j] for k in range(v)) for j in range(v)] for i in range(e)]
    return [[sum(C[i][k]*B[j][k] for k in range(v)) for j in range(e)] for i in range(e)]


def closed_form_projection(lengths):
    G=sum((F(1,L) for L in lengths),F(0))
    idx=[i for i,L in enumerate(lengths) for _ in range(L)]
    return [[(F(int(e==f))-F(int(idx[e]==idx[f]),lengths[idx[e]])+
              F(1,lengths[idx[e]]*lengths[idx[f]])/G)
            for f in range(len(idx))] for e in range(len(idx))]


def predicted_norm(lengths):
    G=sum((F(1,L) for L in lengths),F(0))
    r=len(lengths)
    return max(F(2)-F(2,L)+(F(2)+F(r-2)*L)/(L*L*G) for L in lengths)


def run():
    tests=0
    # Diverse deterministic small simple graph configurations.
    profiles=[]
    for r in range(2,6):
        for ls in product(range(1,5),repeat=r):
            if ls.count(1)<=1 and sum(ls)<=14 and tuple(sorted(ls))==ls:
                profiles.append(ls)
    rng=Random(650913)
    for _ in range(60):
        r=rng.randint(2,5)
        ls=sorted(rng.randint(2,6) for _ in range(r))
        if rng.randint(0,1):ls[0]=1
        if sum(ls)<=21: profiles.append(tuple(ls))
    for lengths in profiles:
        actual=independent_projection(lengths)
        expected=closed_form_projection(lengths)
        assert actual==expected, lengths
        tests+=len(actual)**2
        rows=[sum(map(abs,row),F(0)) for row in actual]
        assert max(rows)==predicted_norm(lengths),lengths
        tests+=len(rows)
        # Verify both its Hilbert projection properties independently.
        assert all(actual[i][j]==actual[j][i] for i in range(len(actual)) for j in range(len(actual)))
        tests+=1
        if len(actual)<=15:
            assert all(sum(actual[i][k]*actual[k][j] for k in range(len(actual)))==actual[i][j]
                   for i in range(len(actual)) for j in range(len(actual)))
            tests+=1
    # The sharp minimum-length hierarchy includes the one-edge shortcut regime.
    for s in range(1,9):
        for q in range(2,45):
            lengths=[s]+[s*q]*q
            G=sum((F(1,L) for L in lengths),F(0))
            assert G==F(2,s)
            short_row=F(2)-F(2,s)+(F(2)+F(q-1)*s)/(s*s*G)
            assert short_row==F(q,2)+F(3,2)-F(1,s)
            assert predicted_norm(lengths)>=short_row
            tests+=3
    print('PASS: %d exact-rational checks across %d finite network profiles and 344 scaling witnesses' % (tests,len(profiles)))

if __name__=='__main__':run()
