#!/usr/bin/env python3
"""Exact chamber certificate for dual regular solids; Python 3 standard library.

All predicates and section counts are in Z[phi]. Floating point is used
only to order candidate tangent directions; each discovered open sign cell
is verified with exact signs, and Euler's independent cell count certifies
exhaustiveness.
"""
from itertools import product, combinations
from collections import Counter
from math import atan2, acos, pi, sqrt
Z=(0,0); ONE=(1,0); PHI=(0,1); INVPHI=(-1,1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return a*c+b*d,a*d+b*c+b*d
def sg(x):
    a,b=x;c=2*a+b
    if c==0:return (b>0)-(b<0)
    if b==0:return (c>0)-(c<0)
    if c*b>0:return (b>0)-(b<0)
    if c*c>5*b*b:return (c>0)-(c<0)
    return (b>0)-(b<0)
def scale(v,c):return tuple(mul(x,c) for x in v)
def vadd(u,v):return tuple(add(a,b) for a,b in zip(u,v))
def vneg(u):return tuple(neg(a) for a in u)
def dot(u,v):
    z=Z
    for a,b in zip(u,v):z=add(z,mul(a,b))
    return z
def cross(u,v):
    return (sub(mul(u[1],v[2]),mul(u[2],v[1])),
            sub(mul(u[2],v[0]),mul(u[0],v[2])),
            sub(mul(u[0],v[1]),mul(u[1],v[0])))
def zero(u):return all(a==Z for a in u)
def numeric(z):return z[0]+z[1]*(1+sqrt(5))/2

def vertices():
    D=[tuple((x,0) for x in t) for t in product((-1,1),repeat=3)]
    I=[]
    for a,b in product((-1,1),repeat=2):
        pa=scale((PHI,),(a,0))[0]
        pb=(b,0)
        ip=scale((INVPHI,),(a,0))[0]
        gp=scale((PHI,),(b,0))[0]
        D.extend(((Z,ip,gp),(ip,gp,Z),(gp,Z,ip)))
        I.extend(((Z,pa,pb),(pa,pb,Z),(pb,Z,pa)))
    assert len(D)==20 and len(I)==12
    return D,I

def edges(V, d2):
    E=[]
    for i,j in combinations(range(len(V)),2):
        dv=tuple(sub(a,b) for a,b in zip(V[i],V[j]))
        if dot(dv,dv)==d2:E.append((i,j))
    assert len(E)==30
    return E

def representatives(V):
    rep=[];maps=[]
    for x in V:
        if sg(next(z for z in x if sg(z)))>0:
            assert not any(x==y for y in rep)
            rep.append(x)
    for x in V:
        if x in rep: maps.append((rep.index(x),1))
        else:maps.append((rep.index(vneg(x)),-1))
    return rep,maps

def arrangement(axes):
    # Identical/projectively opposite pairwise circle intersections are merged.
    projective=[]
    for i,j in combinations(range(len(axes)),2):
        x=cross(axes[i],axes[j]);assert not zero(x)
        if not any(zero(cross(x,y)) for y in projective):projective.append(x)
    incidence=Counter()
    for x in projective:
        for i,a in enumerate(axes):
            if dot(x,a)==Z: incidence[i]+=2 # x and -x
    assert min(incidence.values())>=2
    V=2*len(projective); E=sum(incidence.values());F=E-V+2
    # Enumerate candidate open cells by the sectors at every arrangement vertex.
    masks=set()
    for xx in projective:
        for x in (xx,vneg(xx)):
            active=[i for i,a in enumerate(axes) if dot(x,a)==Z]
            assert len(active)>=2
            rays=[]
            for i in active:
                z=cross(x,axes[i]);assert not zero(z)
                rays.extend([z,vneg(z)])
            basis=rays[0]
            second=cross(x,basis)
            rays.sort(key=lambda z: atan2(numeric(dot(z,second)),numeric(dot(z,basis))))
            for j in range(len(rays)):
                y=vadd(rays[j],rays[(j+1)%len(rays)])
                if zero(y):continue
                mask=[]
                for a in axes:
                    t=dot(x,a)
                    q=sg(t) if t!=Z else sg(dot(y,a))
                    assert q!=0
                    mask.append(q)
                masks.add(tuple(mask))
    # The number F independently follows from the circle incidences and Euler.
    # Every recorded mask is realized by x+epsilon*y for small positive epsilon;
    # distinct masks are disjoint chambers of an intersection of hemispheres.
    assert len(masks)==F, (len(masks),F)
    return masks,(V,E,F),incidence

def mask_stats(masks,axes,D,DE,I,IE):
    key={x:i for i,x in enumerate(axes)}
    def member(x):
        if x in key:return key[x],1
        return key[vneg(x)],-1
    dm=[member(x) for x in D];im=[member(x) for x in I]
    out=Counter()
    for s in masks:
        def n_edges(E,which):
            return sum(s[which[i][0]]*which[i][1]*s[which[j][0]]*which[j][1]<0 for i,j in E)
        out[(n_edges(DE,dm),n_edges(IE,im))]+=1
    return out

def verify_turning_angles(masks, reps, section_count, expected):
    """Certify the complete polygon corner-turn multisets in Z[phi].

    The cosine of an exterior turn at two active hemispheres is
    sign_i sign_j <rep_i,rep_j> / (common squared axis norm).
    Each cell has no triple-concurrent vertex, checked exactly below.
    """
    pairxs=[]
    for i,j in combinations(range(len(reps)),2):
        x=cross(reps[i],reps[j])
        assert not zero(x)
        assert sum(dot(x,r)==Z for r in reps)==2 # no triple concurrence
        pairxs.append((i,j,x))
    for s in masks:
        turns=Counter()
        for i,j,x in pairxs:
            for v in (x,vneg(x)):
                if all(s[k]*sg(dot(v,r))>=0 for k,r in enumerate(reps)):
                    turns[mul((s[i]*s[j],0),dot(reps[i],reps[j]))]+=1
        # The exact raw dot products suffice: no floating point angles used.
        assert turns==expected[section_count(s)],(section_count(s),turns,expected[section_count(s)])

def main():
    D,I=vertices()
    DE=edges(D,(8,-4));IE=edges(I,(4,0))
    DR,dm=representatives(D);IR,im=representatives(I)
    assert len(DR)==10 and len(IR)==6
    assert all(dot(x,x)==(3,0) for x in DR)
    assert all(dot(x,x)==(2,1) for x in IR) # phi^2+1=2+phi
    axes=DR+IR
    assert len(set(axes))==16
    dmasks,dcells,dinc=arrangement(DR)
    imasks,icells,iinc=arrangement(IR)
    joint,jcells,jinc=arrangement(axes)
    assert dcells==(90,180,92),dcells
    assert icells==(30,60,32),icells
    assert jcells==(90,240,152),jcells
    def section_counter(E,rep,members):
        return lambda signs: sum(signs[members[i][0]]*members[i][1]*signs[members[j][0]]*members[j][1]<0 for i,j in E)
    # For dodecahedral axes, squared norm is 3, so raw cosine numerators
    # (1,0),(-1,2),(-1,0),(1,-2) encode respectively
    # beta,alpha, pi-beta,pi-alpha.
    d_expected={
       6: Counter({(1,0):3,(-1,2):3}),
       8: Counter({(-1,0):2,(1,-2):1}),
       10:Counter({(1,0):5})}
    verify_turning_angles(dmasks, DR, section_counter(DE,DR,dm), d_expected)
    # For icosahedron axes squared norm is 2+phi. Each twelve-gon
    # section cell has three exterior turns pi-theta, whose raw cosine
    # numerator is -phi; pentagon turns have numerator +phi.
    # Check sign and exact ratio using the common quadratic field.
    i_expected={12:Counter({(0,-1):3}),10:Counter({(0,1):5})}
    verify_turning_angles(imasks, IR, section_counter(IE,IR,im), i_expected)
    # Exact coordinates give disjoint dodecahedron/icosahedron section counts.
    actual=mask_stats(joint,axes,D,DE,I,IE)
    want=Counter({(6,10):60,(6,12):20,(8,10):60,(10,10):12})
    assert actual==want,(actual,want)
    # Recover the two marginals directly from each arrangement.
    assert mask_stats(dmasks,DR,D,DE,[],[])==Counter({(6,0):20,(8,0):60,(10,0):12})
    assert mask_stats(imasks,IR,[],[],I,IE)==Counter({(0,10):12,(0,12):20})
    A=acos(sqrt(5)/3)
    B=acos(1/3)
    T=acos(1/sqrt(5))
    p={(6,12):5*(3*T-pi)/pi,
       (6,10):15*(pi-A-B-T)/pi,
       (8,10):15*(2*B+A-pi)/pi,
       (10,10):3*(2*pi-5*B)/pi}
    assert abs(sum(p.values())-1)<1e-12
    assert all(v>0 for v in p.values())
    assert abs(p[(6,12)]+p[(6,10)]-5*(2*pi-3*(A+B))/pi)<1e-12
    print('EXACT_DUAL_CHAMBER_ENUMERATION_OK')
    print('dodecahedron(V,E,F)',dcells,'icosahedron',icells,'joint',jcells)
    print('joint_chamber_counts',sorted(actual.items()))
    for k in sorted(p):print('joint_probability',k,'%.15f'%p[k])
    print('SUM',sum(p.values()))
if __name__=='__main__':main()
