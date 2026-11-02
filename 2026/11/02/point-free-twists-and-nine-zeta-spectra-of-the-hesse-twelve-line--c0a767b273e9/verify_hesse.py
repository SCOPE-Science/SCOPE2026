#!/usr/bin/env python3
"""Exact standalone verification of Hesse-line Frobenius spectra and F_7 witnesses.

Run: python3 verify_hesse.py
Requires only the Python 3 standard library.
"""
from collections import Counter, defaultdict
from itertools import product

Q3 = range(3)
V = tuple(product(Q3, repeat=2))
VINDEX = {v: i for i, v in enumerate(V)}

# The four one-dimensional F_3-subspaces and their twelve cosets.
DIRECTIONS = tuple(sorted({frozenset({(0, 0), (x, y),
    ((2*x) % 3, (2*y) % 3)}) for x, y in V if (x, y) != (0, 0)},
    key=lambda s: tuple(sorted(s))))
LINES = tuple(sorted({frozenset(((a+x) % 3, (b+y) % 3) for x, y in H)
    for H in DIRECTIONS for a, b in V}, key=lambda s: tuple(sorted(s))))
LI = {L: i for i, L in enumerate(LINES)}
assert len(DIRECTIONS) == 4 and len(LINES) == 12
LINE_DIRECTION = tuple(DIRECTIONS.index(frozenset(((x-a)%3, (y-b)%3)
    for x,y in L)) for L in LINES for a,b in [min(L)])
FLEX_FLAGS = tuple((v, j) for j,L in enumerate(LINES) for v in sorted(L))
DOUBLE_BRANCHES = tuple((i,j) for i in range(12) for j in range(12)
    if i != j and LINE_DIRECTION[i] == LINE_DIRECTION[j])
FI = {flag:i for i,flag in enumerate(FLEX_FLAGS)}
DBI = {br:i for i,br in enumerate(DOUBLE_BRANCHES)}
assert len(FLEX_FLAGS) == 36 and len(DOUBLE_BRANCHES) == 24

def image(v,A,b):
    return ((A[0]*v[0]+A[1]*v[1]+b[0])%3,
            (A[2]*v[0]+A[3]*v[1]+b[1])%3)

def cycle_spectrum(perm):
    seen=set();c=Counter()
    for i in range(len(perm)):
        if i in seen: continue
        x=i;n=0
        while x not in seen:
            seen.add(x); n+=1; x=perm[x]
        c[n]+=1
    return tuple(sorted(c.items()))

def spectra(A,b):
    pperm=tuple(VINDEX[image(v,A,b)] for v in V)
    lperm=tuple(LI[frozenset(image(v,A,b) for v in L)] for L in LINES)
    fperm=tuple(FI[(image(v,A,b),lperm[j])] for v,j in FLEX_FLAGS)
    dperm=tuple(DBI[(lperm[i],lperm[j])] for i,j in DOUBLE_BRANCHES)
    return tuple(cycle_spectrum(p) for p in (pperm,lperm,fperm,dperm))

def fixed(spec,n=1):
    return sum(length*count for length,count in spec if n%length == 0)

def zeta_signature(spec):
    points,lines,flexflags,dbranches=map(dict,spec)
    exponents=tuple((d,flexflags.get(d,0)+dbranches.get(d,0)
        -2*lines.get(d,0)-points.get(d,0))
        for d in sorted(set(points)|set(lines)|set(flexflags)|set(dbranches))
        if flexflags.get(d,0)+dbranches.get(d,0)-2*lines.get(d,0)-points.get(d,0))
    return (exponents,tuple(sorted(lines.items())))

by=defaultdict(list)
for A in product(Q3, repeat=4):
    determinant=(A[0]*A[3]-A[1]*A[2])%3
    if determinant == 0: continue
    for b in V:
        sp=spectra(A,b)
        assert tuple(sum(d*m for d,m in kind) for kind in sp)==(9,12,36,24)
        for n in range(1,25):
            # Normalization minus branches plus nodes.
            P,L,F,B=(fixed(kind,n) for kind in sp)
            q=7**n
            point_count=(q+1)*L-F-B+P+L
            assert point_count==(q+2)*L+P-F-B
            assert point_count>=0
        by[sp].append((A,b,determinant))
assert sum(map(len,by.values()))==432 and len(by)==10
assert len({zeta_signature(sp) for sp in by})==9

# Full abstract signatures, sorted deterministically by point and line cycles.
ordered=sorted(by,key=lambda sp:(sp[0],sp[1],sp[2],sp[3]))
assert sorted(len(by[s]) for s in ordered)==sorted([72,9,54,108,36,24,1,72,8,48])
empty=[]
for idx,sp in enumerate(ordered,1):
    determinant=by[sp][0][2]
    assert all(t[2]==determinant for t in by[sp])
    P,L,F,B=(fixed(s) for s in sp)
    coeff=L; const=2*L+P-F-B
    print('TYPE',idx,'count',len(by[sp]),'det',determinant,
          'P',sp[0],'L',sp[1],'F',sp[2],'B',sp[3],
          'N(q)=',str(coeff)+'q+'+str(const))
    if coeff==const==0:
        empty.append((sp,by[sp]))
assert len(empty)==1 and len(empty[0][1])==48
assert all(det==1 for _,_,det in empty[0][1])
# In the point-free type the linear part is nontrivially unipotent,
# and the translation is outside the image of A-I.
for A,b,_ in empty[0][1]:
    assert (A[0]+A[3])%3==2 and (A[0]*A[3]-A[1]*A[2])%3==1
    assert A!=(1,0,0,1)
    image_diff={( (image(v,A,(0,0))[0]-v[0])%3,
                  (image(v,A,(0,0))[1]-v[1])%3 ) for v in V}
    assert b not in image_diff
print('POINT_FREE_TYPE_CERTIFIED',len(empty[0][1]))

# Integer Eisenstein determinant certificate for all twelve geometric lines.
# A coefficient a+b*w has w^2+w+1=0 and norm a*a-a*b+b*b.
from itertools import combinations
w=((1,0),(0,1),(-1,-1))
def wadd(a,b): return (a[0]+b[0],a[1]+b[1])
def wneg(a): return (-a[0],-a[1])
def wmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def triple_det(abc):
    a,b,c=abc
    positive=wadd(wadd(wmul(a[0],wmul(b[1],c[2])),
                        wmul(a[1],wmul(b[2],c[0]))),
                   wmul(a[2],wmul(b[0],c[1])))
    negative=wadd(wadd(wmul(a[2],wmul(b[1],c[0])),
                        wmul(a[0],wmul(b[2],c[1]))),
                   wmul(a[1],wmul(b[0],c[2])))
    return wadd(positive,wneg(negative))
WONE=(1,0);WZERO=(0,0)
lines_eisenstein=[(WONE,WZERO,WZERO),(WZERO,WONE,WZERO),
                  (WZERO,WZERO,WONE)]+[(WONE,w[a],w[b])
                      for a,b in product(range(3),repeat=2)]
det_norms=Counter()
for triple in combinations(lines_eisenstein,3):
    a,b=triple_det(triple)
    det_norms[a*a-a*b+b*b]+=1
assert det_norms==Counter({0:36,1:28,3:81,9:72,27:3})
print('EISENSTEIN_TRIPLE_DETERMINANT_NORMS',dict(sorted(det_norms.items())))

# Independent geometric sanity check using the explicit Hesse lines over F_7.
p=7; cube_root=2
projective=[(1,y,z) for y in range(p) for z in range(p)]\
    +[(0,1,z) for z in range(p)]+[(0,0,1)]
assert len(projective)==p*p+p+1
geometric_lines=[(1,0,0),(0,1,0),(0,0,1)] + [
    (1,pow(cube_root,a,p),pow(cube_root,b,p)) for a,b in product(range(3),repeat=2)]
mult=Counter(sum((a*X+b*Y+c*Z)%p==0 for a,b,c in geometric_lines)
             for X,Y,Z in projective)
assert mult[4]==9 and mult[2]==12 and sum(k*(k-1)//2*v for k,v in mult.items())==66
print('SPLIT_HESSE_INTERSECTIONS',dict(sorted(mult.items())))

# Symbolic integer-polynomial routines, for exact F_7 Hessian checks without CAS.
def add(P,Q,sign=1):
    r=dict(P)
    for e,c in Q.items():r[e]=r.get(e,0)+sign*c
    return {e:c for e,c in r.items() if c}
def mul(P,Q):
    r={}
    for e,c in P.items():
        for f,d in Q.items():
            g=tuple(e[k]+f[k] for k in range(3))
            r[g]=r.get(g,0)+c*d
    return {e:c for e,c in r.items() if c}
def diff(P,i):
    r={}
    for e,c in P.items():
        if e[i]:
            f=list(e);f[i]-=1;r[tuple(f)]=c*e[i]
    return r
def ev(P,v):
    return sum(c*math_prod(v[i]**e[i] for i in range(3)) for e,c in P.items())%p
def math_prod(vals):
    a=1
    for x in vals:a*=x
    return a
def hessian(F):
    M=[[diff(diff(F,i),j) for j in range(3)] for i in range(3)]
    ans={}
    for perm,sgn in [((0,1,2),1),((1,2,0),1),((2,0,1),1),
                     ((2,1,0),-1),((1,0,2),-1),((0,2,1),-1)]:
        term=mul(mul(M[0][perm[0]],M[1][perm[1]]),M[2][perm[2]])
        ans=add(ans,term,sgn)
    return ans

def check_plane_cubic(F,name,expected_flex,expected_lines,expected_curve):
    H=hessian(F)
    flex=[v for v in projective if ev(F,v)==ev(H,v)==0]
    on_cubic=[v for v in projective if ev(F,v)==0]
    grads=[diff(F,i) for i in range(3)]
    assert all(any(ev(g,v) for g in grads) for v in on_cubic)
    rational_lines=[]
    for a,b,c in projective:
        if a: v1=(-b,1,0);v2=(-c,0,1)
        elif b: v1=(1,0,0);v2=(0,-c,1)
        else: v1=(1,0,0);v2=(0,1,0)
        param=[(1,0),(0,1),(1,1),(1,2)]
        evals=[]
        for polynomial in (F,H):
            evals.append([ev(polynomial,tuple((s*v1[i]+t*v2[i])%p
                                         for i in range(3))) for s,t in param])
        u,w=evals
        if all((u[i]*w[j]-u[j]*w[i])%p==0
               for i in range(4) for j in range(4)):
            rational_lines.append((a,b,c))
    assert (len(flex),len(rational_lines),len(on_cubic))==(
        expected_flex,expected_lines,expected_curve)
    print('F7_EXAMPLE',name,'flex',len(flex),'inflection_lines',len(rational_lines),
          'cubic_points',len(on_cubic))

# Maps E -> P^2 associated with |2O+P|, and the |3O| Weierstrass embedding.
# Coordinates (X:Y:Z) and coefficients over F_7.
check_plane_cubic({(1,2,0):1,(0,2,1):1,(0,1,2):-2,
                   (2,0,1):-1,(1,0,2):1,(0,0,3):-2},
                  'point_free',0,0,6)
check_plane_cubic({(1,2,0):1,(0,1,2):1,(2,0,1):-1},
                  'same_zeta_no_rational_flex',0,3,9)
check_plane_cubic({(0,2,1):1,(3,0,0):-1,(1,0,2):-1,(0,0,3):-3},
                  'same_zeta_three_rational_flexes',3,3,6)
print('VERIFY_OK')
