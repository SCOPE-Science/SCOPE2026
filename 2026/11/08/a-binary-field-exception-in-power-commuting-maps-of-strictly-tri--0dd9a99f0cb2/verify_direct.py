#!/usr/bin/env python3
"""Independent original-equation enumeration at q=2; no coefficient interpolation."""
from verify import POS, ID, PSI, EXTRA, D, gf2_rank

def mul(a,b):
    z=0
    for u,(i,j) in enumerate(POS):
        if not a>>u&1:continue
        for v,(k,l) in enumerate(POS):
            if j==k and b>>v&1:z^=1<<ID[(i,l)]
    return z

def evalmap(cols,x):
    z=0
    for u in range(D):
        if (cols[u]&x).bit_count()%2:z|=1<<u
    return z

def addmap(output, inputs):
    a=[0]*D
    for inp in inputs:a[ID[output]]^=1<<ID[inp]
    return a

standard=[addmap(out,[inp]) for out in sorted(PSI) for inp in POS]
standard.append([1<<i for i in range(D)])
exotic=[addmap(p,inputs) for p,inputs in EXTRA]
assert len(standard)==41 and len(exotic)==4
# Independently establish 45 independent binary maps using vectors of
# all output coefficients, rather than coefficient-polynomial rows.
assert gf2_rank([[int(cols[u]>>v&1) for u in range(D) for v in range(D)] for cols in standard+exotic],D*D)==45
constraints=[]
for x in range(1<<D):
    sq=mul(x,x)
    # Commutator of f(x) with x^2, as a linear function of the 100 entries.
    left=[mul(1<<u,sq)^mul(sq,1<<u) for u in range(D)]
    for out in range(D):
        row=[0]*(D*D)
        for u in range(D):
            if left[u]>>out&1:
                for v in range(D):
                    if x>>v&1:row[u*D+v]=1
        constraints.append(row)
    for mat in standard+exotic:
        fx=evalmap(mat,x)
        assert mul(fx,sq)==mul(sq,fx)
assert gf2_rank(constraints,D*D)==55
print('VERIFY_OK_DIRECT all 1024 elements, all 45 explicit maps, functional constraint rank 55')
