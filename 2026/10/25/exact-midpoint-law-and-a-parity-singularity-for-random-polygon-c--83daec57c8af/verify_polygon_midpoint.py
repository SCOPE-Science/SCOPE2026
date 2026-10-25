"""Reproduce finite checks for the polygonal random-chord midpoint law.

Only standard-library dependencies. The theorem is proved analytically; these
finite checks are non-exhaustive diagnostics of the formulas and sampling model.
"""
from math import sin,cos,pi,hypot,isclose
from random import Random
from itertools import combinations

def polygon_edges(vertices):
    n=len(vertices)
    assert n>=3
    starts=vertices
    vecs=[(vertices[(i+1)%n][0]-vertices[i][0], vertices[(i+1)%n][1]-vertices[i][1]) for i in range(n)]
    lens=[hypot(*e) for e in vecs]
    return starts, vecs, lens

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def parallel(e,f,tol=1e-10):
    return abs(cross(e,f)) <= tol*hypot(*e)*hypot(*f)

def components(vertices):
    _,edges,lengths=polygon_edges(vertices)
    P=sum(lengths)
    boundary=sum(x*x for x in lengths)/P**2
    interior=sum(2*lengths[i]*lengths[j]/P**2 for i,j in combinations(range(len(edges)),2) if parallel(edges[i],edges[j]))
    bulk=1-boundary-interior
    bulk_integral=sum(2*lengths[i]*lengths[j]/P**2 for i,j in combinations(range(len(edges)),2) if not parallel(edges[i],edges[j]))
    assert isclose(bulk,bulk_integral,abs_tol=1e-12)
    return boundary,interior,bulk

def regular(n):
    return [(cos(2*pi*k/n),sin(2*pi*k/n)) for k in range(n)]

def sample_edges(vertices,N=180000,seed=44):
    _,edges,lengths=polygon_edges(vertices)
    P=sum(lengths)
    cum=[];s=0
    for t in lengths:
        s+=t;cum.append(s)
    rng=Random(seed)
    counts=[0,0,0]
    for _ in range(N):
        indices=[]
        for z in range(2):
            u=rng.random()*P
            j=next(i for i,b in enumerate(cum) if u<b)
            indices.append(j)
        i,j=indices
        if i==j: counts[0]+=1
        elif parallel(edges[i],edges[j]): counts[1]+=1
        else: counts[2]+=1
    return [v/N for v in counts]

def triangular_medial_test(N=180000,seed=86):
    vertices=[(0.,0.),(2.0,0.),(0.8,1.7)]
    starts,edges,lengths=polygon_edges(vertices)
    P=sum(lengths)
    cum=[];s=0
    for L in lengths:
        s+=L;cum.append(s)
    rng=Random(seed)
    singular=central=0
    def sample():
        u=rng.random()*P
        i=next(j for j,v in enumerate(cum) if u<v)
        t=rng.random()
        return i,(starts[i][0]+t*edges[i][0], starts[i][1]+t*edges[i][1])
    A=vertices[0]; E=(vertices[1][0]-A[0], vertices[1][1]-A[1]); F=(vertices[2][0]-A[0],vertices[2][1]-A[1]);det=cross(E,F)
    for _ in range(N):
        i,p=sample();j,q=sample()
        if i==j:singular+=1;continue
        m=((p[0]+q[0])/2,(p[1]+q[1])/2)
        w=(m[0]-A[0],m[1]-A[1])
        lam_b=cross(w,F)/det;lam_c=cross(E,w)/det;lam_a=1-lam_b-lam_c
        if max(lam_a,lam_b,lam_c)<0.5:central+=1
    exact_sing=sum(x*x for x in lengths)/P**2
    exact_central=(1-exact_sing)/2
    return (singular/N,exact_sing,central/N,exact_central)

def trapezoid_component_integral(length1,length2,perimeter,steps=30000):
    # Pair of parallel sides, project both uniformly to [0,length_i].
    lo=0.0;hi=(length1+length2)/2
    dx=(hi-lo)/steps
    total=0.0
    for k in range(steps+1):
        z=lo+dx*k
        overlap=max(0.,min(length1,2*z)-max(0.,2*z-length2))
        density=4*overlap/perimeter**2
        total += (0.5 if k in (0,steps) else 1.)*density*dx
    exact=2*length1*length2/perimeter**2
    assert abs(total-exact)<1e-8
    return total,exact

def same_edge_component_integral(length,perimeter):
    # Arc-length density 4 l/P^2 min(t,1-t) along edge.
    return 4*length*length/perimeter**2*(.5*.5*.5*2) # integral min(t,1-t)=1/4

if __name__=='__main__':
    tests=[('triangle',regular(3)),('square',regular(4)),('pentagon',regular(5)),('hexagon',regular(6)),('octagon',regular(8)),('2-by-1 rectangle',[(0,0),(2,0),(2,1),(0,1)])]
    for label,verts in tests:
        formula=components(verts)
        sample=sample_edges(verts)
        assert max(abs(a-b) for a,b in zip(formula,sample))<0.009
        print(label, 'boundary/interior/bulk predicted=',tuple(round(x,9) for x in formula),'observed=',tuple(round(x,6) for x in sample))
    for l1,l2 in [(2.,2.),(1.,1.),(2.,1.),(1.,.3)]:
        numeric,exact=trapezoid_component_integral(l1,l2,2*(l1+l2))
        assert abs(numeric-exact)<1e-8
    for n in range(3,21):
        boundary,interior,bulk=components(regular(n))
        assert isclose(boundary,1/n,abs_tol=1e-12)
        assert isclose(interior,0 if n%2 else 1/n,abs_tol=1e-12)
        assert isclose(bulk,1-1/n-(0 if n%2 else 1/n),abs_tol=1e-12)
    assert abs(same_edge_component_integral(2.,6.) - 4./36.)<1e-12
    q=triangular_medial_test()
    assert abs(q[0]-q[1])<.008 and abs(q[2]-q[3])<.008
    print('non-equilateral triangle: same-edge mass (empirical,exact), medial core (empirical,exact):',tuple(round(x,8) for x in q))
    print('PASS: 6 empirical mixtures, 18 regular-parity identities, four trapezoid-density integrals, triangular medial probability.')
