"""Exact enumeration of tangent-filling plane cubics over F_3.

Python >=3.10 and SymPy >=1.12.  No random sampling or external data.
All coefficients and all point arithmetic are performed modulo three.
"""
from itertools import product
from collections import Counter
from sympy import symbols, groebner, diff, prod

Q = 3
POINTS = []
for vec in product(range(Q), repeat=3):
    if vec == (0, 0, 0):
        continue
    k = next(i for i in range(3) if vec[i])
    if vec[k] == 1:
        POINTS.append(vec)
assert len(POINTS) == 13


def mons(d):
    return [(a, b, d-a-b) for a in range(d, -1, -1)
            for b in range(d-a, -1, -1)]


def normalized_forms(n):
    # One representative for every point of P^{n-1}(F_3).
    for first in range(n):
        for tail in product(range(3), repeat=n-first-1):
            yield (0,)*first + (1,) + tail


def point_power(v, m):
    return (v[0]**m[0] * v[1]**m[1] * v[2]**m[2]) % 3


def matrices(monomials):
    values = []
    derivs = []
    for p in POINTS:
        values.append([point_power(p,m) for m in monomials])
        derivs.append([[ (m[j]*point_power(p, tuple(m[i]-(i==j) for i in range(3))))%3
                          if m[j] else 0 for m in monomials]
                       for j in range(3)])
    return values,derivs


LINES = {line: sum(1 << j for j,p in enumerate(POINTS)
                    if sum(line[i]*p[i] for i in range(3)) % 3 == 0)
         for line in POINTS}
FULL = (1 << len(POINTS)) - 1


def dot(a,b):
    return sum(x*y for x,y in zip(a,b)) % 3


def normalize(v):
    j = next(i for i,x in enumerate(v) if x%3)
    return tuple(int(x * (1 if v[j]%3==1 else 2))%3 for x in v)


def covering_data(c, values, derivs):
    tangent_lines = []
    n = 0
    coverage = 0
    for k in range(len(POINTS)):
        if dot(values[k],c):
            continue
        n += 1
        gradient = [dot(row,c) for row in derivs[k]]
        if not any(gradient):
            continue  # tangent defined only at smooth rational points
        tangent = normalize(gradient)
        tangent_lines.append(tangent)
        coverage |= LINES[tangent]
    return n, tuple(tangent_lines), coverage


def pol_mul(A,B):
    out={}
    for ma,ca in A.items():
        for mb,cb in B.items():
            m=tuple(ma[i]+mb[i] for i in range(3))
            out[m]=(out.get(m,0)+ca*cb)%3
    return {m:v for m,v in out.items() if v}


def substitution_matrix(monomials, linear_subs):
    zero=(0,0,0); unit={zero:1}
    polys=[{tuple(1 if k==j else 0 for k in range(3)): v%3
            for j,v in enumerate(linear_subs[i]) if v%3} for i in range(3)]
    ans=[]
    for exps in monomials:
        poly=unit
        for j,e in enumerate(exps):
            for _ in range(e):
                poly=pol_mul(poly,polys[j])
        ans.append(tuple(poly.get(m,0) for m in monomials))
    return ans


def transform(c,M):
    return normalize([sum(c[i]*M[i][j] for i in range(len(c)))%3
                      for j in range(len(c))])


def check_smooth(c,monomials):
    x,y,z=symbols('x y z')
    vs=(x,y,z)
    f=sum(a*prod(vs[i]**m[i] for i in range(3))
          for a,m in zip(c,monomials))
    deriv=[diff(f,v) for v in vs]
    for k,v in enumerate(vs):
        others=[vs[j] for j in range(3) if j!=k]
        ideal=[h.subs(v,1) for h in [f]+deriv]
        G=groebner(ideal,*others,modulus=3)
        assert len(G.polys)==1 and G.polys[0].is_one


# Degree 1/2 bound, using all normalized forms (including reducible curves).
for d,expected in ((1,13),(2,364)):
    ms=mons(d)
    V,G=matrices(ms)
    forms=list(normalized_forms(len(ms)))
    assert len(forms)==expected
    assert sum(covering_data(c,V,G)[2]==FULL for c in forms)==0
print('DEGREE_1_2: 13+364 forms checked, zero tangent-filling')

# Degree 3: all 29,524 projective ternary cubic forms, not only smooth forms.
ms=mons(3)
V,G=matrices(ms)
all_forms=normalized_forms(len(ms))
candidates={}
count=0
for c in all_forms:
    count += 1
    n,ts,covered=covering_data(c,V,G)
    if covered == FULL:
        candidates[c]=(n,len(set(ts)))
assert count==29524
assert len(candidates)==3744
assert Counter(candidates.values())==Counter({(4,4):936,(6,6):1872,(7,7):936})
print('DEGREE_3: 29524 forms, 3744 tangent-filling; (N,T) profile:',
      dict(sorted(Counter(candidates.values()).items())))

# Elementary transvections, coordinate swaps, and one diagonal scaling.
# Their substitutions generate GL_3(F_3), hence PGL_3(F_3).
generators=[
 ((1,1,0),(0,1,0),(0,0,1)),  # x -> x+y
 ((1,0,0),(1,1,0),(0,0,1)),  # y -> x+y
 ((1,0,0),(0,1,1),(0,0,1)),  # y -> y+z
 ((0,1,0),(1,0,0),(0,0,1)),  # swap x,y
 ((1,0,0),(0,0,1),(0,1,0)),  # swap y,z
 ((2,0,0),(0,1,0),(0,0,1)),  # x -> -x
]
actions=[substitution_matrix(ms,g) for g in generators]
reps={
 4:(0,0,1,0,0,0,1,0,2,0),
 6:(0,0,1,1,0,0,0,2,1,0),
 7:(0,0,1,0,0,0,1,0,2,2),
}
orbits={}
for N,seed in sorted(reps.items()):
    seen={seed}
    queue=[seed]
    for c in queue:
        for M in actions:
            cc=transform(c,M)
            if cc not in seen:
                seen.add(cc)
                queue.append(cc)
    expected_size={4:936,6:1872,7:936}[N]
    assert len(seen)==expected_size
    assert all(cc in candidates and candidates[cc]==(N,N) for cc in seen)
    orbits[N]=seen
    n,ts,covered=covering_data(seed,V,G)
    assert n==N and len(set(ts))==N and covered==FULL
    check_smooth(seed,ms)
    print('ORBIT: N=',N,'size=',len(seen),'rep=',seed,'geometrically_smooth=True')
assert len(set.union(*orbits.values()))==len(candidates)
assert all(orbits[a].isdisjoint(orbits[b]) for a in orbits for b in orbits if a<b)
print('PASS: three disjoint PGL3(F3) orbits cover all tangent-filling cubics')
