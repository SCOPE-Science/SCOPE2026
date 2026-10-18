"""Independent parametrization and orbit/tangent verification for (4,3) filling curves.

Run: python verify_orbits.py
The 11 parameters come from the homogeneous-ideal representation
F = A(X,Y)*(X0^2*X1+X0*X1^2)+B(X)*(Y0^2*Y1+Y0*Y1^2),
with B having only the X0^4, X0^2*X1^2, X1^4 coefficients.
No input census file is required.
"""
from collections import Counter
from itertools import product
import json
import sympy as sy
X0, X1, Y0, Y1, u, v = sy.symbols('X0 X1 Y0 Y1 u v')
mon = [(i,j) for i in range(5) for j in range(4)]
T_X = X0**2*X1 + X0*X1**2
T_Y = Y0**2*Y1 + Y0*Y1**2
term = [X0**(1-i)*X1**i*Y0**(3-j)*Y1**j*T_X
        for i in range(2) for j in range(4)]
term += [X0**(4-i)*X1**i*T_Y for i in (0,2,4)]
assert len(term)==11
pairs = [(1,0),(0,1),(1,1)]
chart_subs = [(dict(zip((X0,X1,Y0,Y1),(1,u,1,v))),0,0),
              (dict(zip((X0,X1,Y0,Y1),(1,u,v,1))),0,1),
              (dict(zip((X0,X1,Y0,Y1),(u,1,1,v))),1,0),
              (dict(zip((X0,X1,Y0,Y1),(u,1,v,1))),1,1)]

def smooth(F):
    for sub,_,_ in chart_subs:
        f=sy.Poly(F.subs(sub),u,v,modulus=2).as_expr()
        if list(sy.groebner([sy.diff(f,u),sy.diff(f,v),f],
                            u,v,modulus=2,order='grevlex').exprs)!=[sy.Integer(1)]:
            return False
    return True

def tangent_pattern(F):
    fs=[]
    for point_x,point_y in product(pairs,repeat=2):
        a,b=point_x;c,d=point_y
        subs={X0:a,X1:b,Y0:c,Y1:d}
        fx=sy.diff(F,X1 if a else X0)
        fy=sy.diff(F,Y1 if c else Y0)
        v1=int(fx.subs(subs))&1
        v2=int(fy.subs(subs))&1
        fs.append(2*v1+v2)
    return tuple(fs)

def mask(F):
    # Decode a bihomogeneous form directly, rather than inverting the
    # rational-point evaluation matrix.
    pp=sy.Poly(F,X0,X1,Y0,Y1, modulus=2)
    return sum((int(pp.coeff_monomial(X0**(4-i)*X1**i*Y0**(3-j)*Y1**j))&1)
               << (4*i+j) for i,j in mon)

smooth_forms={};tangent_forms={}
for k in range(1,2048):
    F=sy.Add(*(term[i] for i in range(11) if k>>i&1))
    if smooth(F):
        m=mask(F)
        assert m not in smooth_forms
        smooth_forms[m]=F
        tangent_forms[m]=tangent_pattern(F)
assert len(smooth_forms)==66

shared=Counter()
keys=sorted(smooth_forms)
for idx,a in enumerate(keys):
    for b in keys[idx+1:]:
        shared[sum(x==y for x,y in zip(tangent_forms[a],tangent_forms[b]))]+=1
assert shared=={3:642,5:981,7:468,9:54}

# Enumerate the action of PGL_2(F2) x PGL_2(F2) on all 20 monomials
# using binomial expansions in characteristic two.
GL=[(a,b,c,d) for a,b,c,d in product((0,1),repeat=4) if (a*d+b*c)%2]
assert len(GL)==6

def mul(P,Q):
    R={}
    for (i,j) in P:
        for (k,l) in Q:
            ind=(i+k,j+l)
            if ind in R:del R[ind]
            else:R[ind]=1
    return R

def transformed_binary_monomial(idx,degree,M):
    a,b,c,d=M
    first={k:1 for k,w in [((1,0),a),((0,1),b)] if w}
    second={k:1 for k,w in [((1,0),c),((0,1),d)] if w}
    ans={(0,0):1}
    for _ in range(degree-idx):ans=mul(ans,first)
    for _ in range(idx):ans=mul(ans,second)
    return ans

actions=[]
for gx,gy in product(GL,repeat=2):
    generator=[]
    for i,j in mon:
        a=transformed_binary_monomial(i,4,gx)
        b=transformed_binary_monomial(j,3,gy)
        m=0
        for p,q in product(a,b):m^=1<<(p[1]*4+q[1])
        generator.append(m)
    actions.append(generator)

def transform(m,act):
    out=0
    for bit in range(20):
        if m>>bit&1:out ^= act[bit]
    return out

remaining=set(keys);orbit_sizes=[];orbit_representatives=[]
while remaining:
    m=min(remaining)
    orbit={transform(m,act) for act in actions}
    assert orbit <=remaining
    orbit_sizes.append(len(orbit))
    orbit_representatives.append(m)
    remaining -= orbit
assert sorted(orbit_sizes)==[6,6,18,36]
print(json.dumps({
    'smooth_forms':len(smooth_forms),
    'smooth_orbit_sizes':sorted(orbit_sizes),
    'orbit_representatives_coefficient_masks':orbit_representatives,
    'pair_shared_tangents':dict(sorted(shared.items())),
    'distinct_tangent_patterns':len(set(tangent_forms.values())),
    'pairs_with_no_shared_rational_tangent':shared.get(0,0)
},sort_keys=True))
