"""Exact cube 1-factorization and octahedral triangle-face incidence certificate.
No third-party dependencies; execute with Python 3.
"""
import itertools
V=list(itertools.product((0,1),repeat=3))
E=tuple((u,v) for u in V for v in V if sum(x!=y for x,y in zip(u,v))==1 and u<v)
assert len(V)==8 and len(E)==12
perfect=[]
for idx in itertools.combinations(range(12),4):
    touched=[v for k in idx for v in E[k]]
    if len(set(touched))==8:perfect.append(frozenset(idx))
assert len(perfect)==9
fac=set()
for a,b in itertools.combinations(perfect,2):
    if a.isdisjoint(b):
        c=frozenset(set(range(12))-a-b)
        if c in perfect:fac.add(frozenset((a,b,c)))
assert len(fac)==4
is_axis=lambda block:len({next(j for j in range(3) if u[j]!=v[j]) for i in block for u,v in (E[i],)})==1
counts=sorted(sum(is_axis(block) for block in F) for F in fac)
assert counts==[1,1,1,3]
for j in range(3):
    axis=frozenset(i for i,(u,v) in enumerate(E) if u[j]!=v[j])
    assert sum(axis in F for F in fac)==2
# Gram exact face-edge-square dispersion for 3 synthetic vectors:
from fractions import Fraction as Q
u=(Q(1),Q(0),Q(0)); v=(Q(1,3),Q(2),Q(0));w=(Q(-1,2),Q(1,7),Q(3))
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
T=[]
for s1,s2,s3 in itertools.product((1,-1),repeat=3):
    U=tuple(s1*x for x in u);W=tuple(s2*x for x in v);Z=tuple(s3*x for x in w)
    T.append(dot(sub(U,W),sub(U,W))+dot(sub(U,Z),sub(U,Z))+dot(sub(W,Z),sub(W,Z)))
bar=sum(T)/8
assert sum((t-bar)**2 for t in T)==32*(dot(u,v)**2+dot(u,w)**2+dot(v,w)**2)
# Strictly acute (3,4,5.1) and nonacute (3,4,5) give 4 and 2 permitted orbits:
for sides,expected in [((3,4,4.5),4),((3,4,5),2),((3,4,5.1),2)]:
    mixed=sum(sides[j]**2<sides[(j+1)%3]**2+sides[(j+2)%3]**2 for j in range(3))
    all_axis=int(all(sides[j]**2<sides[(j+1)%3]**2+sides[(j+2)%3]**2 for j in range(3)))
    assert mixed+all_axis==expected,(sides,mixed,all_axis)
print('EXACT_OCTAHEDRAL_COLORINGS_OK: nine perfect matchings, four factorizations, axis counts [1,1,1,3]; Gram certificate and acute/nonacute class counts.')
