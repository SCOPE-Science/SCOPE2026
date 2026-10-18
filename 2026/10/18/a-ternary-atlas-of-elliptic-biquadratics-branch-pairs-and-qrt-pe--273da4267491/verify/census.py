"""Exact F_3 census of smooth (2,2) curves and their two deck maps.
No external packages; run as python verify/census.py from package root.
A coefficient is indexed 3*i+j at U^(2-i)V^i S^(2-j)T^j.
"""
import collections
import json
from pathlib import Path

Q = 3
POWERS = tuple(Q**i for i in range(9))
POINTS = ((1,0), (0,1), (1,1), (1,2))
MATRICES = (((0,1),(1,0)), ((1,1),(0,1)), ((2,0),(0,1)))

def digits(number):
    return tuple((number // p) % Q for p in POWERS)

def encode(c):
    return sum(ci * p for ci, p in zip(c, POWERS))

def canonical(c):
    for x in c:
        if x:
            return encode(c if x == 1 else tuple((2*v) % Q for v in c))
    return 0

def sym2(matrix):
    (a,b),(c,d) = matrix
    def product(x,y):
        return ((x[0]*y[0])%Q,
                (x[0]*y[1]+x[1]*y[0])%Q,
                (x[1]*y[1])%Q)
    return (product((a,b),(a,b)), product((a,b),(c,d)),
            product((c,d),(c,d)))

SYMMETRIC_GENERATORS = tuple(sym2(m) for m in MATRICES)

def act(c, symmetric_matrix=None, axis=0):
    out = [0]*9
    if axis == 2:
        for i in range(3):
            for j in range(3):
                out[3*j+i] = c[3*i+j]
    else:
        for i in range(3):
            for j in range(3):
                x = c[3*i+j]
                if x == 0: continue
                for k in range(3):
                    idx = 3*k+j if axis == 0 else 3*i+k
                    factor = symmetric_matrix[i][k] if axis == 0 else symmetric_matrix[j][k]
                    out[idx] = (out[idx] + x*factor)%Q
    return canonical(tuple(out))

def generators(number):
    c = digits(number)
    return tuple(act(c, m, axis) for axis in (0,1)
                 for m in SYMMETRIC_GENERATORS) + (act(c, axis=2),)

def convolve(a,b):
    out = [0]*5
    for i in range(3):
        for j in range(3):
            out[i+j] = (out[i+j]+a[i]*b[j])%Q
    return tuple(out)

def discriminant(c, axis=0):
    if axis == 1:
        c = tuple(c[3*j+i] for i in range(3) for j in range(3))
    a = tuple(c[3*i] for i in range(3))
    b = tuple(c[3*i+1] for i in range(3))
    d = tuple(c[3*i+2] for i in range(3))
    bb, ad = convolve(b,b), convolve(a,d)
    return tuple((x-y)%Q for x,y in zip(bb,ad))

def remainder(a,b):
    a,b = list(a),list(b)
    while a and a[0] == 0: a.pop(0)
    while b and b[0] == 0: b.pop(0)
    while a and len(a) >= len(b):
        factor = a[0] * pow(b[0],-1,Q)%Q
        for k in range(len(b)):
            a[k] = (a[k] - factor*b[k])%Q
        while a and a[0] == 0: a.pop(0)
    return a

def projectively_squarefree(d):
    # d is a degree-4 homogeneous binary form, descending coefficients.
    d = list(d)
    while d and d[0] == 0: d.pop(0)
    if len(d) < 4: # root at infinity has multiplicity >=2
        return False
    degree = len(d)-1
    deriv = [(degree-i)*d[i]%Q for i in range(degree)]
    while deriv and deriv[0] == 0: deriv.pop(0)
    if not deriv: return False
    while deriv: d,deriv = deriv,remainder(d,deriv)
    return len(d)==1

def smooth(c):
    a = projectively_squarefree(discriminant(c,0))
    assert a == projectively_squarefree(discriminant(c,1))
    return a

def eval_form(c,x,y):
    u,v = x; s,t = y
    bx = (u*u,u*v,v*v); by = (s*s,s*t,t*t)
    return sum(c[3*i+j]*bx[i]*by[j]
               for i in range(3) for j in range(3))%Q

def quartic_value(d,x):
    u,v=x
    return sum(d[i]*u**(4-i)*v**i for i in range(5))%Q

def orbit_invariants(number):
    c=digits(number)
    n=sum(eval_form(c,x,y)==0 for x in POINTS for y in POINTS)
    ram=tuple(sum(quartic_value(discriminant(c,axis), x)==0
                  for x in POINTS) for axis in (0,1))
    geometric_points={(i,j) for i,x in enumerate(POINTS)
                              for j,y in enumerate(POINTS)
                              if eval_form(c,x,y)==0}
    assert n==len(geometric_points)
    def flip(pt, axis):
        same=[q for q in geometric_points if q[axis]==pt[axis]]
        assert len(same) in (1,2)
        return next((q for q in same if q!=pt),pt)
    def step(pt):return flip(flip(pt,0),1)
    def iterate(pt,k):
        for _ in range(k): pt=step(pt)
        return pt
    order=next(k for k in range(1,9)
               if all(iterate(pt,k)==pt for pt in geometric_points))
    return n,tuple(sorted(ram)),order

def compute():
    forms = {canonical(digits(i)) for i in range(1,Q**9)}
    assert len(forms)==(Q**9-1)//(Q-1)==9841
    visited=set(); orbits=[]
    for root in sorted(forms):
        if root in visited: continue
        seen={root}; pending=[root]
        while pending:
            for image in generators(pending.pop()):
                if image not in seen: seen.add(image);pending.append(image)
        assert not (seen & visited)
        visited.update(seen)
        c=digits(root)
        row={'representative':root, 'size':len(seen), 'smooth':smooth(c)}
        if row['smooth']:
            N,r,T=orbit_invariants(root)
            row.update({'points':N,'ramification':list(r),'qrt_order':T})
        orbits.append(row)
    assert visited==forms
    tally=collections.Counter()
    orbit_counts=collections.Counter()
    for o in orbits:
        if o['smooth']:
            key=(o['points'],*o['ramification'],o['qrt_order'])
            tally[key]+=o['size'];orbit_counts[key]+=1
    assert len(orbits)==41
    assert len([o for o in orbits if o['smooth']])==14
    assert sum(v for v in tally.values())==5184
    assert sum(orbit_counts.values())==14
    return orbits,[{'points':k[0], 'branch_pair':[k[1],k[2]],
                    'qrt_order':k[3], 'equations':tally[k],
                    'projective_orbits':orbit_counts[k]} for k in sorted(tally)]

if __name__=='__main__':
    orbits, table=compute()
    summary={'total_projective_equations':9841,
             'smooth_equations':5184,'all_orbits':41,'smooth_orbits':14,
             'strata':table,'orbits':orbits}
    print(json.dumps(summary,sort_keys=True,indent=2))
    p=Path(__file__).resolve().parent.parent/'data'/'orbits.json'
    assert json.loads(p.read_text())==summary, 'Replayed result differs from expected census'
