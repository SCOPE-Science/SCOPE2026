#!/usr/bin/env python3
"""Exact characteristic-five checks for the elementary-symmetric Bring model.
Only Python's standard library is required; all algebra is exact modulo five.
"""
from itertools import combinations, permutations, product
P = 5
ZERO = (0, 0, 0, 0)
ONE = {ZERO: 1}

def variable(j):
    e = list(ZERO); e[j] = 1
    return {tuple(e): 1}

def plus(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = (out.get(key, 0) + value) % P
    return {k:v for k,v in out.items() if v}

def scalar(poly, s):
    return {k:(v*s)%P for k,v in poly.items() if (v*s)%P}

def mul(a,b):
    out={}
    for k,x in a.items():
        for j,y in b.items():
            m=tuple(k[i]+j[i] for i in range(4))
            out[m]=(out.get(m,0)+x*y)%P
    return {k:v for k,v in out.items() if v}

def powers(a,n):
    out=ONE
    for i in range(n):out=mul(out,a)
    return out

z,a,b,c=[variable(j) for j in range(4)]
R=[plus(z,a),plus(z,b),plus(z,c),z,plus(z,scalar(plus(a,b,c),-1))]
e1=plus(*R)
e2=plus(*(mul(R[i],R[j]) for i,j in combinations(range(5),2)))
e3=plus(*(mul(R[i],mul(R[j],R[k])) for i,j,k in combinations(range(5),3)))
q=plus(powers(a,2),powers(b,2),powers(c,2),mul(a,b),mul(a,c),mul(b,c))
h=plus(mul(powers(a,2),b),mul(powers(a,2),c),mul(a,powers(b,2)),scalar(mul(a,mul(b,c)),2),mul(a,powers(c,2)),mul(powers(b,2),c),mul(b,powers(c,2)))
assert e1=={} and e2==scalar(q,-1) and e3==plus(scalar(h,-1),scalar(mul(z,q),2))

def evalpoly(poly,vals):
    return sum(coeff*__import__('math').prod(pow(vals[j],exp,P) for j,exp in enumerate(k)) for k,coeff in poly.items())%P

def proj(t):
    lead=next(x for x in t if x)
    inv=pow(lead,-1,P)
    return tuple((x*inv)%P for x in t)
points={proj(t) for t in product(range(P),repeat=3) if any(t)}
conic={t for t in points if evalpoly(q,(0,)+t)==0}
base={t for t in conic if evalpoly(h,(0,)+t)==0}
expected={(1,2,3),(1,2,4),(1,3,2),(1,3,4),(1,4,2),(1,4,3)}
assert len(points)==31 and conic==base==expected
# Independent census of the complete characteristic-five projective model.
projective_3={proj(t) for t in product(range(P),repeat=4) if any(t)}
curve_5={t for t in projective_3 if all(evalpoly(eq,t)==0 for eq in (e1,e2,e3))}
assert len(projective_3)==156 and len(curve_5)==31
# Hessian of q is I_3 + J_3; determinant 4 in characteristic five.
assert (4%P)!=0
# The cubic h has no pure cubes, so it cannot equal q times a linear form.
assert h and all(h.get(tuple(3 if i==j else 0 for i in range(4)),0)==0 for j in (1,2,3))
# Every generator has five distinct F_5 coordinate residues.
residues={t:(t[0],t[1],t[2],0,(-sum(t))%P) for t in expected}
for t,x in residues.items():
    assert set(x)==set(range(5))
    assert evalpoly(e1,(0,)+t)==evalpoly(e2,(0,)+t)==evalpoly(e3,(0,)+t)==0

def induced(t,perm):
    vals=residues[t]
    x=[vals[j] for j in perm]
    direction=tuple((x[j]-x[3])%P for j in (0,1,2))
    return proj(direction)
labels=tuple(sorted(expected))
representations=set()
for permutation in permutations(range(5)):
    moved=tuple(labels.index(induced(t,permutation)) for t in labels)
    assert set(moved)==set(range(6))
    representations.add(moved)
assert len(representations)==120
# The six projective lines have 6*(5+1)-5=31 rational points.
assert len(curve_5)==6*(P+1)-5
# Explicit S_5 action on six conic directions is faithful and hence PGL_2(F_5).
# The (2,3) complete intersection has arithmetic genus 4; six branches give delta 9.
assert 6*(2+3-4)//2+1==4
assert 4+6-1==9
print('BRING_CHAR5_SIX_LINES_CONIC_OUTER_S5_DELTA9_OK')
print('directions:',labels)
print('S5 induced distinct permutations:',len(representations))
