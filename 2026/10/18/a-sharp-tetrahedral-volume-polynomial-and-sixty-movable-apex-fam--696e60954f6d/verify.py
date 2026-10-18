"""Exact arithmetic certificate for tetrahedra in edge-truncated icosahedra.

Run with Python 3.10+ (standard library only).  All comparisons use Z[phi],
phi=(1+sqrt(5))/2; no floating-point computations or sampling.
"""
from itertools import combinations
from collections import defaultdict
from time import perf_counter

ZERO=(0,0)
ONE=(1,0)
PHI=(0,1)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def scale(k,x): return (k*x[0],k*x[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d,a*d+b*c+b*d)

def sg(x):
    """Exact sign of a+b*phi, with phi=(1+sqrt(5))/2."""
    a,b=x; A=2*a+b
    if b==0:return (A>0)-(A<0)
    if A==0:return (b>0)-(b<0)
    if A>0 and b>0:return 1
    if A<0 and b<0:return -1
    if A>0:return (A*A>5*b*b)*2-1
    return (5*b*b>A*A)*2-1

def vsub(x,y):return tuple(sub(x[i],y[i]) for i in range(3))
def vscale(k,x):return tuple(scale(k,z) for z in x)
def vadd(x,y):return tuple(add(x[i],y[i]) for i in range(3))
def determinant(x,y,z):
    c0=sub(mul(y[1],z[2]),mul(y[2],z[1]))
    c1=sub(mul(y[2],z[0]),mul(y[0],z[2]))
    c2=sub(mul(y[0],z[1]),mul(y[1],z[0]))
    return add(add(mul(x[0],c0),mul(x[1],c1)),mul(x[2],c2))

def vertices_and_edges():
    X=[]
    for a in (-1,1):
        for b in (-1,1):
            X.extend([(ZERO,(a,0),(0,b)), ((a,0),(0,b),ZERO), ((0,b),ZERO,(a,0))])
    assert len(X)==12 and len(set(X))==12
    edges=[]
    for i,j in combinations(range(12),2):
        d=vsub(X[i],X[j]); norm=add(add(mul(d[0],d[0]),mul(d[1],d[1])),mul(d[2],d[2]))
        if norm==(4,0):edges.append((i,j))
    assert len(edges)==30
    directed=edges+[(j,i) for i,j in edges]
    A=[X[i] for i,j in directed]
    B=[vsub(X[j],X[i]) for i,j in directed]
    return X,directed,A,B

def poly_coeff(A,B,quad):
    i,j,k,l=quad
    a=vsub(A[j],A[i]);b=vsub(A[k],A[i]);c=vsub(A[l],A[i])
    d=vsub(B[j],B[i]);e=vsub(B[k],B[i]);f=vsub(B[l],B[i])
    return (
        determinant(a,b,c),
        add(add(determinant(d,b,c),determinant(a,e,c)),determinant(a,b,f)),
        add(add(determinant(d,e,c),determinant(d,b,f)),determinant(a,e,f)),
        determinant(d,e,f),
    )

def bernstein24(p):
    """24 times degree-3 Bernstein coefficients on [0,1/2]."""
    a,b,c,d=p
    return (scale(24,a),add(scale(24,a),scale(4,b)),
            add(add(scale(24,a),scale(8,b)),scale(2,c)),
            add(add(add(scale(24,a),scale(12,b)),scale(6,c)),scale(3,d)))

def main():
    start=perf_counter()
    X,directed,A,B=vertices_and_edges()
    # This polynomial equals six times the maximal tetrahedron volume.
    Q=((4,8),(0,-8),(-4,8),(4,-4))
    test=poly_coeff(A,B,(0,13,16,53))
    assert test==tuple(neg(t) for t in Q)
    QB=bernstein24(Q)
    assert all(sg(x)>0 for x in QB)
    fixed_winners=[]
    nchecked=0
    coeff_nonnegative=0
    for a,b,c in combinations(range(1,60),3):
        p=poly_coeff(A,B,(0,a,b,c))
        pb=bernstein24(p)
        signs=[]
        for eps in (1,-1):
            diff=tuple(add(QB[i],scale(eps,pb[i])) for i in range(4))
            assert all(sg(w)>=0 for w in diff), (a,b,c,eps,diff)
            signs.append(all(w==ZERO for w in diff))
            coeff_nonnegative+=4
        if any(signs):fixed_winners.append((0,a,b,c))
        nchecked+=1
    assert nchecked==32509 and coeff_nonnegative==260072
    assert len(fixed_winners)==8
    print('BERNSTEIN exact nonnegative certificates:',coeff_nonnegative)
    print('With first directed vertex fixed:',nchecked,'triples,',len(fixed_winners),'strict-interior maximizing triples')

    # Independent all-vertex exact check at s=1/4.  Multiplying
    # all coordinates by four removes denominators: 4*x_i=3*u_i+w_i.
    W=[vadd(vscale(4,A[i]),B[i]) for i in range(60)]
    target=(244,412) # 64*Q(1/4)
    winners=[]
    for i in range(57):
        wi=W[i]
        for j,k,l in combinations(range(i+1,60),3):
            det=determinant(vsub(W[j],wi),vsub(W[k],wi),vsub(W[l],wi))
            assert sg(sub(target,det))>=0 and sg(add(target,det))>=0
            if det==target or det==neg(target):
                winners.append((i,j,k,l))
    assert len(winners)==120, len(winners)
    assert [q for q in winners if q[0]==0]==fixed_winners
    print('Full vertex check at s=1/4: 487635 combinations,',len(winners),'extremizers')

    # No branching among maximum-vertex tetrahedra: each one has
    # exactly one neighbor sharing three vertices. The differing pair
    # is the two endpoints of a remaining edge of the truncated solid.
    shared=defaultdict(list)
    for q in winners:
        for tri in combinations(q,3):
            shared[tri].append(q)
    families=[]
    for tri,neighbors in shared.items():
        assert len(neighbors)<=2
        if len(neighbors)==2:
            a=next(iter(set(neighbors[0])-set(tri)))
            b=next(iter(set(neighbors[1])-set(tri)))
            assert directed[a]==directed[b][::-1]
            # With the same fixed ordered base, both endpoint
            # determinants must have identical extremal orientation.
            # Otherwise their connecting edge would not be a family.
            base0,base1,base2=tri
            def oriented_apex(z):
                return determinant(vsub(W[base1],W[base0]),
                                   vsub(W[base2],W[base0]),
                                   vsub(W[z],W[base0]))
            assert oriented_apex(a)==oriented_apex(b)
            assert oriented_apex(a) in (target,neg(target))
            families.append((tri,a,b))
    assert len(families)==60
    incidence={q:0 for q in winners}
    for tri,a,b in families:
        for z in (a,b):
            q=tuple(sorted((*tri,z)))
            incidence[q]+=1
    assert set(incidence.values())=={1}
    print('Equality classification:',len(families),'maximizing segments; each of 120 vertex tetrahedra is in exactly one segment')
    print('Q power coefficients:',Q)
    print('Q Bernstein *24:',QB)
    print('PASS; elapsed seconds:',round(perf_counter()-start,2))

if __name__=='__main__':main()
