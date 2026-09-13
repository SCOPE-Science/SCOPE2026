"""Molien certification: 2I has no invariant polynomials in degrees 1..11.
Group = 120 icosian unit quaternions; character of Sym^k(C^2) averaged.
Certifies first nonzero link eigenvalue >= 12*14 = 168, so indicial gap (-2,0) free."""
import json
from math import sqrt, sin, cos, acos, pi

phi = (1 + sqrt(5)) / 2
elts = []
# vertices (±1,0,0,0) and permutations (8 total)
elts += [(s,0,0,0) for s in (1,-1)] + [(0,s,0,0) for s in (1,-1)] + \
        [(0,0,s,0) for s in (1,-1)] + [(0,0,0,s) for s in (1,-1)]
# (±1/2,±1/2,±1/2,±1/2) (16)
for a in (1,-1):
    for b in (1,-1):
        for c in (1,-1):
            for d in (1,-1):
                elts.append((a/2,b/2,c/2,d/2))
# even permutations of (±phi/2, ±1/(2phi), ±1/2, 0) with ... : 96 elements.
# Standard: even permutations of coordinates of (0, ±1/2, ±1/(2phi), ±phi/2)? Use
# cyclic-shift construction: base patterns, all sign combos, even coordinate perms.
import itertools
def even_perms(t):
    out = set()
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j])
        if inv % 2 == 0:
            out.add(tuple(t[p[i]] for i in range(4)))
    return out
base = (0.0, 0.5, 1/(2*phi), phi/2)
perms = even_perms(base)
count = 0
for q in perms:
    nz = [i for i in range(4) if q[i] != 0]
    for signs in itertools.product((1,-1), repeat=3):
        v = list(q)
        for i,s in zip(nz,signs):
            v[i] *= s
        elts.append(tuple(v)); count += 1
assert len(elts) == 8 + 16 + 96, len(elts)

def molien_dim(k):
    tot = 0.0
    for (a,b,c,d) in elts:
        n = sqrt(a*a+b*b+c*c+d*d)
        ct = max(-1.0, min(1.0, a/n))
        th = acos(ct)
        if abs(sin(th)) < 1e-12:
            chi = float(k+1) * (1.0 if ct > 0 else (-1.0)**k)
        else:
            chi = sin((k+1)*th)/sin(th)
        tot += chi
    return tot/len(elts)

dims = {k: round(molien_dim(k), 6) for k in range(0, 13)}
cert = all(abs(dims[k]) < 1e-6 for k in range(1, 12))
out = {"group_order": len(elts), "molien_dims_0_to_12": dims,
       "no_invariants_deg_1_to_11": bool(cert),
       "dim_deg_12": dims[12],
       "conclusion": "No 2I-invariant homogeneous polynomial in degrees 1..11; first nonzero "
                     "S^3/2I link eigenvalue >= 168; scalar indicial roots avoid (-2,0)."}
with open("molien_2I.json","w") as f:
    json.dump(out,f,indent=1)
print("order:",len(elts),"| dims:",dims,"| certified:",cert)
