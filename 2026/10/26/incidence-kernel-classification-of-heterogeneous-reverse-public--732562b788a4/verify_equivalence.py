"""Exact finite checks for heterogeneous reverse/ordinary public-goods equivalence.
Run with Python 3 (standard library only): python verify_equivalence.py
These finite tests corroborate but do not replace the analytical theorem.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import exp

checks=0

def test(assertion, description):
    global checks
    if not assertion:
        raise AssertionError(description)
    checks+=1

def payoffs(n,groups,lam,y,m=F(1)):
    r=[F(0) for _ in range(n)]; p=[F(0) for _ in range(n)]
    for group in groups:
        g=len(group)
        weighted_claim=sum((lam[j]*y[j] for j in group),F(0))
        weighted_give=sum((lam[j]*(1-y[j]) for j in group),F(0))
        for i in group:
            r[i]+=m*y[i]-m*weighted_claim/g
            p[i]+=-m*(1-y[i])+m*weighted_give/g
    return r,p

def incidence_offset(n,groups,lam,m=F(1)):
    g=len(groups[0]); degrees=[sum(i in e for e in groups) for i in range(n)]
    return [m*degrees[i]-m*sum((sum(lam[j] for j in e) for e in groups if i in e),F(0))/g for i in range(n)]

# Bipartite connected 2-regular graph, heterogeneous waste factors.
C4=[(0,1),(1,2),(2,3),(3,0)]
l4=[F(6,5),F(9,5),F(6,5),F(9,5)]
ref4=incidence_offset(4,C4,l4)
test(ref4==[-F(1)]*4,'C4 group offsets')
for y in product((0,1),repeat=4):
    R,P=payoffs(4,C4,l4,y)
    test(all(R[i]-P[i]==ref4[i] for i in range(4)),'C4 exact profile offset')
    for i,j in C4:
        test((R[j]-R[i])==(P[j]-P[i]),'C4 exact pairwise difference')
        if y[i]!=y[j]:
            for omega in (0.25,1.0,3.0):
                u=lambda z:1/(1+exp(-omega*float(z)))
                test(abs(u(R[j]-R[i])-u(P[j]-P[i]))<1e-14,'C4 logistic transition')

# Nonbipartite connected 2-regular graph, nonconstant factor obstruction.
C3=[(0,1),(1,2),(2,0)]
l3=[F(6,5),F(3,2),F(9,5)]
ref3=incidence_offset(3,C3,l3)
test(ref3==[-F(17,20),-F(1),-F(23,20)],'triangle offset vector')
non_equiv=0
for y in product((0,1),repeat=3):
    R,P=payoffs(3,C3,l3,y)
    test(all(R[i]-P[i]==ref3[i] for i in range(3)),'C3 exact profile offset')
    for i,j in C3:
        if y[i]!=y[j] and R[j]-R[i]!=P[j]-P[i]:
            non_equiv+=1
            u=lambda z:1/(1+exp(-float(z)))
            test(abs(u(R[j]-R[i])-u(P[j]-P[i]))>1e-7,'C3 strict logistic difference')
test(non_equiv>0,'C3 detectable disparity')

# Regular complete tripartite 3-uniform hypergraph with 2 vertices in each part:
# a genuinely two-dimensional family of exact heterogeneous profiles.
parts=((0,1),(2,3),(4,5))
triples=list(product(*parts)); lambdas=[F(6,5)]*2+[F(9,5)]*2+[F(3,2)]*2
ref6=incidence_offset(6,triples,lambdas)
test(len(triples)==8 and all(sum(i in e for e in triples)==4 for i in range(6)),'3-uniform regularity')
test(ref6==[-F(2)]*6,'3-uniform payoff offset')
for y in product((0,1),repeat=6):
    R,P=payoffs(6,triples,lambdas,y)
    test(all(R[i]-P[i]==-F(2) for i in range(6)),'3-uniform exact profile offset')
    for i,j in combinations(range(6),2):
        test((R[j]-R[i])==(P[j]-P[i]),'3-uniform pairwise difference')

# Exact equality for triangle quantitative signless/Laplacian certificate.
avg=sum(l3,F(0))/3
v=[z-avg for z in l3]
Qv=[2*v[i]+sum(v[j] for a,b in C3 for j in ((b,) if a==i else (a,) if b==i else ())) for i in range(3)]
test(Qv==v,'triangle Q smallest eigenspace')
sumsq=sum(((Qv[i]-Qv[j])**2 for i,j in C3),F(0))
vnorm=sum((z*z for z in v),F(0))
test(sumsq==3*vnorm==F(27,50),'triangle exact spectral lower-bound equality')
print(f'PASS {checks} exact/numeric checks; nonzero mismatch cases={non_equiv}; triangle spectral equality={sumsq}')
