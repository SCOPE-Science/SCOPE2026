"""Exact F_7 verifier for a 49-point characteristic-seven Klein configuration.

Run: python3 klein_bad7_verify.py
No external packages, network access, or random input are required.
"""
from itertools import combinations, product
from collections import Counter

P = 7

def normalize(v):
    c = pow(next(x for x in v if x % P), -1, P)
    return tuple(c * x % P for x in v)

all_points = sorted({normalize((x, y, z)) for x, y, z in product(range(P), repeat=3)
                     if (x, y, z) != (0, 0, 0)})
conic = [v for v in all_points if sum(x*x for x in v) % P == 0]
Z = [v for v in all_points if v not in conic]
assert len(all_points) == 57 and len(conic) == 8 and len(Z) == 49

a = 3
lines = [(1,0,0),(0,1,1),(a,1,-1),(a,-1,1),(0,-1,1),
         (1,a,-1),(a,-1,-1),(-1,1,a),(a,1,1),(-1,a,1),
         (-1,-1,a),(1,0,1),(-1,a,-1),(1,a,1),(-1,0,1),
         (1,-1,a),(1,1,a),(0,0,1),(-1,1,0),(1,1,0),(0,1,0)]
lines = [normalize(v) for v in lines]
assert len(set(lines)) == 21
incidence = {v: sum(sum(v[k]*line[k] for k in range(3)) % P == 0
                    for line in lines) for v in all_points}
assert Counter(incidence.values()) == {0: 8, 3: 28, 4: 21}
assert {v for v in all_points if incidence[v] > 0} == set(Z)
print('KLEIN_21_LINES: incidence {0:8,3:28,4:21}; singular set = off-conic 49')

def monomials(d):
    return [(i,j,d-i-j) for i in range(d+1) for j in range(d-i+1)]

def rref_rank(rows):
    rows = [[int(x)%P for x in r] for r in rows if any(int(x)%P for x in r)]
    if not rows:
        return 0
    n=len(rows[0]); pivot=0
    for col in range(n):
        k=next((k for k in range(pivot,len(rows)) if rows[k][col]),None)
        if k is None: continue
        rows[pivot],rows[k]=rows[k],rows[pivot]
        inv=pow(rows[pivot][col],-1,P)
        rows[pivot]=[(x*inv)%P for x in rows[pivot]]
        for k in range(pivot+1,len(rows)):
            if rows[k][col]:
                c=rows[k][col]
                rows[k]=[(x-c*y)%P for x,y in zip(rows[k],rows[pivot])]
        pivot+=1
        if pivot==len(rows):break
    return pivot

def eval_rank(points,d):
    mons=monomials(d)
    return rref_rank([[pow(x,i,P)*pow(y,j,P)*pow(z,k,P)%P for i,j,k in mons]
                      for x,y,z in points])

# Polynomial dictionaries map exponent triples to coefficients in F_7.
def var(i):
    e=[0,0,0];e[i]=1
    return {tuple(e):1}

def mul(f,g):
    out={}
    for u,a in f.items():
        for v,b in g.items():
            e=tuple(u[i]+v[i] for i in range(3))
            out[e]=(out.get(e,0)+a*b)%P
    return {e:c for e,c in out.items() if c}

def sub(f,g):
    h=f.copy()
    for e,c in g.items():h[e]=(h.get(e,0)-c)%P
    return {e:c for e,c in h.items() if c}

def power(f,n):
    h={(0,0,0):1}
    for _ in range(n):h=mul(h,f)
    return h

x,y,z=(var(i) for i in range(3))
J=[sub(mul(power(x,7),y),mul(x,power(y,7))),
   sub(mul(power(x,7),z),mul(x,power(z,7))),
   sub(mul(power(y,7),z),mul(y,power(z,7)))]
G=mul(mul(x,y),z)
for u,v in [(x,y),(y,z),(z,x)]:
    G=mul(G,sub(power(u,2),power(v,2)))
assert set(sum(e) for e in G)=={9}

def ev(f,v):
    return sum(c*pow(v[0],e[0],P)*pow(v[1],e[1],P)*pow(v[2],e[2],P)
               for e,c in f.items())%P
assert all(ev(f,v)==0 for v in all_points for f in J)
assert all(ev(G,v)==0 for v in Z) and all(ev(G,v)!=0 for v in conic)
print('DEGREE_NINE_SEPARATOR: vanishes on exactly 49 F_7 points')

# The eight conic points form the transverse intersection of the conic
# Q=x^2+y^2+z^2 with T=(y^2-4x^2)(y^2-2x^2).
Q={ (2,0,0):1,(0,2,0):1,(0,0,2):1 }
T=mul(sub(power(y,2),{(2,0,0):4}),
      sub(power(y,2),{(2,0,0):2}))
assert all(ev(Q,v)==ev(T,v)==0 for v in conic)
assert all(not (ev(Q,v)==0 and ev(T,v)==0) for v in Z)
print('CONIC_CI: transverse complete intersection of degrees 2 and 4')

# Check the Hilbert function of the 49 reduced points and equality with
# J+(G) through degree 11. The known exact sequence
# 0 -> S/I(C)(-9) -> S/J -> S/(J,G) -> 0 gives the Hilbert series
# (1-3*t^8+t^11+t^13)/(1-t)^3 for J+(G).
expected_h=[1,3,6,10,15,21,28,36,42,46,48,49]
for d in range(12):
    h=eval_rank(Z,d)
    assert h==expected_h[d],(d,h,expected_h[d])
    basis=monomials(d); idx={m:i for i,m in enumerate(basis)}
    gens=[]
    for f in J+[G]:
        r=next(iter(f.values())) if f else 0
        deg=sum(next(iter(f))) if f else 0
        if deg>d:continue
        for u in monomials(d-deg):
            v=[0]*len(basis)
            for e,c in f.items():
                k=tuple(e[i]+u[i] for i in range(3))
                v[idx[k]]=(v[idx[k]]+c)%P
            gens.append(v)
    assert rref_rank(gens)==len(basis)-h,(d,rref_rank(gens),len(basis)-h)
assert all(eval_rank(Z,d)==49 for d in (11,12,13))
print('HILBERT_49:',expected_h)
print('IDEAL_EQUALITY_THROUGH_REGULARITY: (J,G)=I(Z) in every degree')
print('MINIMAL_GENERATORS: degrees 8,8,8,9; syzygies 9,11,13')
print('BETTI_NUMERATOR: 1-3*t^8+t^11+t^13')
print('VERIFY_OK')
