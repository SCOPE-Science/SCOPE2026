#!/usr/bin/env python3
import itertools
import collections
import sympy as sp
import networkx as nx

I = sp.I
phi = (1 + sp.sqrt(5))/2

A = [
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(1,I,0),(1,1+I,0),
    (1,0,1),(2,0,1+I),(1,0,I),
    (0,1,-1),(0,-2,1+I),
    (1,I,1),(1,-1+I,1),
]
B = [
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(1,-phi,0),(1,1-phi,0),
    (1,0,1),(1,0,-phi),(1,0,1+phi),
    (0,1,-1),(0,1,-(1+phi)),
    (1,-1,1),(1,1-phi,phi),
]

def vec(v):
    return sp.Matrix(v)

def cross(a,b):
    return (
        sp.simplify(a[1]*b[2]-a[2]*b[1]),
        sp.simplify(a[2]*b[0]-a[0]*b[2]),
        sp.simplify(a[0]*b[1]-a[1]*b[0]),
    )

def proportional(v,w):
    return all(sp.simplify(v[i]*w[j]-v[j]*w[i]) == 0
               for i in range(3) for j in range(i+1,3))

def incidence_points(lines):
    reps=[]
    for i,j in itertools.combinations(range(len(lines)),2):
        p=cross(lines[i],lines[j])
        for q in reps:
            if proportional(p,q):
                break
        else:
            reps.append(p)
    out=[]
    for p in reps:
        S=tuple(i for i,l in enumerate(lines)
                if sp.simplify(l[0]*p[0]+l[1]*p[1]+l[2]*p[2]) == 0)
        if S not in [T for _,T in out]:
            out.append((p,S))
    return out

def lattice_automorphisms(lines):
    pts=incidence_points(lines)
    high=[S for _,S in pts if len(S)>=3]
    G=nx.Graph()
    for i in range(len(lines)):
        G.add_node(('L',i), color=('L',))
    for j,S in enumerate(high):
        G.add_node(('P',j), color=('P',len(S)))
        for i in S:
            G.add_edge(('L',i),('P',j))
    gm=nx.algorithms.isomorphism.GraphMatcher(
        G,G,node_match=lambda a,b:a['color']==b['color'])
    perms=[]
    for m in gm.isomorphisms_iter():
        perms.append(tuple(m[('L',i)][1] for i in range(len(lines))))
    return pts, sorted(set(perms))

def permutation_order(p):
    seen=[False]*len(p)
    ans=1
    for i in range(len(p)):
        if not seen[i]:
            j=i; c=0
            while not seen[j]:
                seen[j]=True; c+=1; j=p[j]
            if c:
                ans=int(sp.ilcm(ans,c))
    return ans

def det3(lines,inds):
    return sp.simplify(sp.Matrix.hstack(*[vec(lines[i]) for i in inds]).det())

def frame(lines):
    for q in itertools.combinations(range(len(lines)),4):
        if all(det3(lines,t)!=0 for t in itertools.combinations(q,3)):
            return q
    raise AssertionError('no projective frame')

def homography_for_perm(lines,p,q):
    a,b,c,d=q
    X=sp.Matrix.hstack(*[vec(lines[i]) for i in (a,b,c)])
    Y=sp.Matrix.hstack(*[vec(lines[p[i]]) for i in (a,b,c)])
    cv=list(X.inv()*vec(lines[d]))
    dv=list(Y.inv()*vec(lines[p[d]]))
    assert all(sp.simplify(z)!=0 for z in cv+dv)
    lam=[sp.simplify(dv[k]/cv[k]) for k in range(3)]
    return sp.simplify(Y*sp.diag(*lam)*X.inv())

def realizes(M,lines,p):
    for i,l in enumerate(lines):
        v=M*vec(l); w=vec(lines[p[i]])
        if not proportional(tuple(v),tuple(w)):
            return False
    return True

def analyze(lines):
    pts,auts=lattice_automorphisms(lines)
    q=frame(lines)
    proj=[]
    for p in auts:
        M=homography_for_perm(lines,p,q)
        if realizes(M,lines,p):
            proj.append((p,M))
    return pts,auts,proj

def weak_profile(pts):
    c=collections.Counter(len(S) for _,S in pts)
    return (13,c[2],c[3],c[4],c[5])

pa,aa,ga=analyze(A)
pb,ab,gb=analyze(B)
assert weak_profile(pa)==(13,16,6,4,2)
assert weak_profile(pb)==(13,16,6,4,2)
assert len(aa)==2 and collections.Counter(map(permutation_order,aa))=={1:1,2:1}
assert len(ga)==1 and permutation_order(ga[0][0])==1
assert len(ab)==8 and collections.Counter(map(permutation_order,ab))=={1:1,2:5,4:2}
assert len(gb)==4 and collections.Counter(permutation_order(p) for p,_ in gb)=={1:1,2:3}

# The two order profiles identify C2 and D8 among these explicitly enumerated groups;
# the projective subgroup of B is V4 because all three nonidentity elements are involutions.
print('VERIFY_OK sympy=%s networkx=%s weak=(13;16,6,4,2) A:lattice=C2,projective=1 B:lattice=D8(order8),projective=V4' % (sp.__version__, nx.__version__))
