#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, combinations

# Exact verification on finite atomic L1 models.  The theorem itself is
# proved analytically in RESULT.md; this script stress-tests the polyhedral
# finite-atomic cases without floating point arithmetic.

def l1(v):
    return sum(abs(z) for z in v)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def vertices(n):
    ans=[]
    for i in range(n):
        for s in (-1,1):
            v=[F(0)]*n; v[i]=F(s); ans.append(tuple(v))
    return ans

def edge_pairs(V):
    # In an n-dimensional crosspolytope, every non-antipodal pair is an edge.
    for u,v in combinations(V,2):
        if all(u[i] == -v[i] for i in range(len(u))):
            continue
        yield u,v

def slice_closure_vertices(phi,t):
    V=vertices(len(phi)); out=[]
    for v in V:
        if dot(phi,v) >= t:
            out.append(v)
    for u,v in edge_pairs(V):
        a=dot(phi,u); b=dot(phi,v)
        if (a-t)*(b-t) < 0:
            lam=(t-a)/(b-a)
            w=tuple((F(1)-lam)*u[i]+lam*v[i] for i in range(len(u)))
            out.append(w)
    return out

def slice_sup_distance(x,phi,t):
    W=slice_closure_vertices(phi,t)
    assert W
    return max(l1(tuple(x[i]-w[i] for i in range(len(x)))) for w in W)

def comps(total,n,prefix=()):
    if n==1:
        yield prefix+(total,); return
    for k in range(1,total-n+2):
        yield from comps(total-k,n-1,prefix+(k,))

checks=0
phis_cache={}
for n in (2,3,4):
    vals=(F(-1),F(-1,2),F(0),F(1,2),F(1))
    phis=[p for p in product(vals, repeat=n) if max(abs(z) for z in p)==1]
    phis_cache[n]=phis
    for den in range(n,7):
        for c in comps(den,n):
            x=tuple(F(k,den) for k in c)
            m=max(x)
            expected=2*(1-m)
            # The canonical avoiding coordinate slice has threshold m and exact supremum.
            k=x.index(m)
            phi=tuple(F(1) if i==k else F(0) for i in range(n))
            got=slice_sup_distance(x,phi,m)
            assert got==expected, (x,got,expected)
            checks+=1
            # Test many arbitrary avoiding slices. Their supremum must be at least expected.
            for phi in phis:
                px=dot(phi,x)
                for t in (F(-1,2),F(0),F(1,2),F(3,4)):
                    if t>=1 or px>t: # x belongs to the strict slice when px>t
                        continue
                    got=slice_sup_distance(x,phi,t)
                    assert got>=expected, (x,phi,t,got,expected)
                    checks+=1

# Endpoint: signed basis vectors are nabla points, so every avoiding slice has supremum 2.
for n in (2,3,4):
    for j in range(n):
        x=tuple(F(1) if i==j else F(0) for i in range(n))
        for phi in phis_cache[n]:
            px=dot(phi,x)
            for t in (F(-1,2),F(0),F(1,2),F(3,4)):
                if t>=1 or px>t:
                    continue
                got=slice_sup_distance(x,phi,t)
                assert got==2, (x,phi,t,got)
                checks+=1

print('VERIFY_OK', checks)
