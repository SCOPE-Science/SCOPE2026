#!/usr/bin/env python3
"""Exact binary anticanonical-pencil census for the split sextic del Pezzo surface.
Run with Python 3 standard library only. No stochastic steps.
"""
import itertools, json
from collections import Counter

# Cubics passing through three coordinate points; monomial exponents (x,y,z).
MON = [(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,2,1),(0,1,2)]
MON_INDEX = {t:i for i,t in enumerate(MON)}
Q2 = [(a,b,2-a-b) for a in range(3) for b in range(3-a)]
Q4 = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
Q4_INDEX = {t:i for i,t in enumerate(Q4)}

def smooth_rank(mask):
    # A cubic is smooth over the algebraic closure iff its three quadratic
    # partial derivatives have no nonzero common zero. By regular sequences,
    # this is equivalent to surjectivity S_2^3 -> S_4.
    derivs=[set(),set(),set()]
    for i,e in enumerate(MON):
        if (mask>>i)&1:
            for j in range(3):
                if e[j]&1:
                    q=tuple(e[k]-(k==j) for k in range(3))
                    if q in derivs[j]:derivs[j].remove(q)
                    else:derivs[j].add(q)
    vectors=[]
    for support in derivs:
        for q in Q2:
            col=0
            for t in support:
                col^=1<<Q4_INDEX[tuple(t[k]+q[k] for k in range(3))]
            vectors.append(col)
    basis={}
    for col in vectors:
        w=col
        while w:
            lead=w.bit_length()-1
            if lead in basis:w^=basis[lead]
            else:basis[lead]=w;break
    return len(basis)==15

def field_mul(a,b,mod,k):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a & (1<<k):a^=mod
    return out

def point_singular(mask,pt,mod,k):
    a,b,c=pt
    sq=[field_mul(v,v,mod,k) for v in pt]
    e=lambda u,v:field_mul(u,v,mod,k)
    fvals=[e(sq[0],b),e(sq[0],c),e(a,sq[1]),e(e(a,b),c),e(a,sq[2]),e(sq[1],c),e(b,sq[2])]
    grads=[[0,sq[0],0],[0,0,sq[0]],[sq[1],0,0],[e(b,c),e(a,c),e(a,b)],[sq[2],0,0],[0,0,sq[1]],[0,sq[2],0]]
    f=0;diff=[0,0,0]
    for i in range(7):
        if mask>>i&1:
            f^=fvals[i]
            for j in range(3):diff[j]^=grads[i][j]
    return f==0 and diff==[0,0,0]

def smooth_extension(mask):
    # For cubics, a singular geometric point occurs over F2, F4 or F8:
    # a geometrically irreducible cubic has <=1 singular point; otherwise a
    # rational line meets a conic in degree 2, or three conjugate lines
    # meet in points of degrees <=3.
    for k,mod in [(1,0b11),(2,0b111),(3,0b1011)]:
        n=1<<k
        pts=[(1,a,b) for a in range(n) for b in range(n)]
        pts += [(0,1,b) for b in range(n)]+[(0,0,1)]
        for pt in pts:
            if point_singular(mask,pt,mod,k):return False
    return True

def action_perm(m,p):
    out=0
    for i,e in enumerate(MON):
        if m>>i&1:
            ee=[0]*3
            for j,t in enumerate(e):ee[p[j]]=t
            out^=1<<MON_INDEX[tuple(ee)]
    return out

def action_crem(m):
    # F(yz,xz,xy)/(xyz) permutes MON in reverse order.
    return sum(((m>>i)&1)<<(6-i) for i in range(7))

def norm_pencil(parts):return tuple(sorted(parts))

def point_count(mask):
    # Plane smooth cubic has same number of rational points as its strict
    # transform at the three rational blow-up centers.
    pts=[(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
    c=3
    for X,Y,Z in pts:
        f=0
        for i,(a,b,d) in enumerate(MON):
            if mask>>i&1:f^=(X**a*Y**b*Z**d)&1
        c+=(f==0)
    return c

# binary polynomial arithmetic, integer coefficients as bit masks.
def rem(a,b):
    while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
    return a

def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def pmod_pow2(x,n,mod):
    for i in range(n):x=rem(pmul(x,x),mod)
    return x

def irreducible_degree6(g):
    assert g.bit_length()==7 and (g&1)==1
    x=0b10
    return pmod_pow2(x,6,g)==x and all(gcd(g,pmod_pow2(x,k,g)^x)==1 for k in (2,3))

def f_substitution_mod(mask,X,Y,g):
    xx=rem(pmul(X,X),g);yy=rem(pmul(Y,Y),g)
    expr=[pmul(xx,Y),xx,pmul(X,yy),pmul(X,Y),X,yy,Y]
    out=0
    for i,t in enumerate(expr):
        if mask>>i&1:out^=t
    return rem(out,g)

S={n for n in range(1,128) if smooth_rank(n)}
SS={n for n in range(1,128) if smooth_extension(n)}
assert S==SS, (sorted(S^SS))
assert len(S)==23, sorted(S)
P=sorted({norm_pencil((u,v,u^v)) for u,v in itertools.combinations(S,2) if u^v in S})
assert len(P)==12
assert len({tuple(u for u in Q if u in S) for Q in P})==12
# All 12 preserve the three fixed points and are genuine anticanonical pencils.
perms=list(itertools.permutations((0,1,2)))
G=[]
for p in perms:
    for b in (0,1):
        G.append(lambda m,p=p,b=b: action_crem(action_perm(m,p)) if b else action_perm(m,p))
assert len({tuple(g(1<<i) for i in range(7)) for g in G})==12
Pset=set(P)
for g in G:
    assert {norm_pencil(map(g,Q)) for Q in P}==Pset
orbits=[];remaining=Pset.copy()
while remaining:
    Q=min(remaining)
    orbit={norm_pencil(map(g,Q)) for g in G}
    orbits.append((Q,orbit))
    remaining-=orbit
assert len(orbits)==2 and sorted(len(o) for q,o in orbits)==[6,6]
# Base certificates: a single irreducible degree-six point of the complement
# of the three exceptional divisors. x=X(y), z=1.
basecerts={
 (49,71,118):{'g':(1<<6)|(1<<5)|(1<<4)|(1<<1)|1, 'x':(1<<6)|(1<<4)|(1<<2)},
 (51,93,110):{'g':(1<<6)|(1<<1)|1, 'x':(1<<5)|(1<<3)|(1<<2)|(1<<1)},
}
for Q,orbit in orbits:
    assert Q in basecerts, Q
    cert=basecerts[Q];g=cert['g'];X=cert['x'];Y=0b10
    assert irreducible_degree6(g)
    assert gcd(X,g)==1
    for m in Q:assert f_substitution_mod(m,X,Y,g)==0,(Q,m)
    # Six distinct geometric points, each with x,y,z nonzero.
    # Since (-K_S)^2=6, they exhaust the base scheme with multiplicity 1.
    spectra={tuple(sorted(point_count(m) for m in T)) for T in orbit}
    assert len(spectra)==1, spectra
assert {tuple(sorted(point_count(m) for m in Q)) for Q,_ in orbits}=={(3,5,5),(4,4,5)}
# Explicit rational-base check independent of the sextic certificates.
rational_pts=[(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
for Q in P:
    a,b,_=Q
    # No common point among the four plane rational points outside centers:
    for X,Y,Z in rational_pts:
        def e(m):return sum((m>>i&1)*(X**q[0]*Y**q[1]*Z**q[2]) for i,q in enumerate(MON))&1
        assert e(a) or e(b)
    # No common rational point on the three exceptional divisors: different tangent directions.
    for i,j in [(0,1),(2,5),(4,6)]:
        assert ((a>>i)&1,(a>>j)&1)!=((b>>i)&1,(b>>j)&1)
# Maximality proof: any all-smooth 3-space has an all-smooth pencil in
# the kernel of evaluation at any rational point of the surface; impossible.
output={
 'smooth_masks':sorted(S), 'smooth_count':len(S), 'pencil_count':len(P),
 'pencils':[list(Q) for Q in P],
 'automorphism_order':len(G),
 'orbit_classes':[
  {'representative':list(q),'orbit_size':len(o),'stabilizer_order':len(G)//len(o),
   'point_count_spectrum':sorted(point_count(m) for m in q),
   'sextic_base_polynomial':basecerts[q]['g'],
   'coordinate_x_polynomial':basecerts[q]['x']}
  for q,o in orbits],
 'base_frobenius_partition':[6],
 'common_rational_base_points':0,
 'all_smooth_projective_dimension_max':1,
}
print(json.dumps(output,sort_keys=True,indent=2))
