#!/usr/bin/env python3
"""Exact, standard-library certificate for five-site cyclic two-distance transportation balls.
Run with: python3 pentagon_verify.py
"""
from fractions import Fraction as Q
from itertools import product, permutations
from collections import Counter
from dataclasses import dataclass

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]

def ell(i,j):
    return (1,0) if (i-j)%N in (1,N-1) else (0,1)

def prufer(seq):
    deg=[1+seq.count(i) for i in range(N)]
    edges=[]
    for j in seq:
        i=min(i for i in range(N) if deg[i]==1)
        edges.append(tuple(sorted((i,j))))
        deg[i]-=1;deg[j]-=1
    i,j=[i for i in range(N) if deg[i]==1]
    return tuple(sorted(edges+[tuple(sorted((i,j)))]))

def tree_potential(tree,signs):
    adj=[[] for _ in range(N)]
    for (i,j),sign in zip(tree,signs):
        a,b=ell(i,j)
        adj[i].append((j,sign*a,sign*b))
        adj[j].append((i,-sign*a,-sign*b))
    f=[None]*N;f[0]=(0,0);stack=[0]
    while stack:
        i=stack.pop()
        for j,a,b in adj[i]:
            if f[j] is None:
                f[j]=(f[i][0]+a,f[i][1]+b)
                stack.append(j)
    assert all(z is not None for z in f)
    return tuple(f)

def feasible_interval(f):
    lo,hi=Q(1),Q(2)
    for i,j in EDGES:
        d0,d1=ell(i,j)
        for sign in (-1,1):
            a=sign*(f[i][0]-f[j][0])-d0
            b=sign*(f[i][1]-f[j][1])-d1
            if b==0:
                if a>0:return None
            elif b>0:hi=min(hi,Q(-a,b))
            else:lo=max(lo,Q(-a,b))
            if lo>hi:return None
    return lo,hi

def shift_orbit(v):
    O=set()
    for k in range(N):
        for reflect in (-1,1):
            for sign in (-1,1):
                w=[(sign*v[(k+reflect*j)%N][0], sign*v[(k+reflect*j)%N][1]) for j in range(N)]
                O.add(tuple((a-w[0][0],b-w[0][1]) for a,b in w))
    return O

def value(f,t):
    return tuple(Q(a)+Q(b)*t for a,b in f)

def orbit_lengths(vs):
    remaining=set(vs);sizes=[]
    while remaining:
        f=next(iter(remaining))
        # Orbit on numeric potentials (all already normalized at site zero).
        orbit=set()
        for k in range(N):
            for flip in (-1,1):
                for sign in (-1,1):
                    a=[sign*f[(k+flip*j)%N] for j in range(N)]
                    orbit.add(tuple(x-a[0] for x in a))
        assert orbit<=remaining
        remaining-=orbit
        sizes.append(len(orbit))
    return sorted(sizes)

def centered_norm2(v):
    return sum(x*x for x in v)-sum(v)**2/Q(N)

@dataclass(frozen=True)
class Radical:
    """Exact a+b sqrt(5), with rational a,b."""
    a:Q=Q(0)
    b:Q=Q(0)
    def __post_init__(self):
        object.__setattr__(self,'a',Q(self.a))
        object.__setattr__(self,'b',Q(self.b))
    @staticmethod
    def coerce(v):
        return v if isinstance(v,Radical) else Radical(Q(v))
    def __add__(self,v):
        v=self.coerce(v);return Radical(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return Radical(-self.a,-self.b)
    def __sub__(self,v):return self+-self.coerce(v)
    def __rsub__(self,v):return self.coerce(v)+-self
    def __mul__(self,v):
        v=self.coerce(v)
        return Radical(self.a*v.a+5*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=self.coerce(v);det=v.a*v.a-5*v.b*v.b
        assert det
        return self*Radical(v.a/det,-v.b/det)

SQ5=Radical(0,1)
PHI=(1+SQ5)/2

def project_W(v):
    """Projection to the rotation-frequency-two plane in the zero-sum space."""
    w=[]
    for i in range(N):
        z=Radical()
        for j in range(N):
            d=min((i-j)%N,(j-i)%N)
            pij=Radical(Q(2,5)) if d==0 else -PHI/5 if d==1 else (PHI-1)/5
            z+=pij*v[j]
        w.append(z)
    return tuple(w)

def norm2_rad(v):
    return sum((x*x for x in v),Radical())-(sum(v,Radical())*sum(v,Radical()))/5

def det_polynomial_linear(rows):
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    out=[0]*5
    for p in permutations(range(4)):
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        coeff=[sign]
        for i,j in enumerate(p):coeff=mul(coeff,list(rows[i][j]))
        for k,x in enumerate(coeff):out[k]+=x
    return tuple(out)

def proof_checks():
    trees={prufer(seq) for seq in product(range(N),repeat=N-2)}
    assert len(trees)==125
    intervals={}
    for T in trees:
        for signs in product((-1,1),repeat=4):
            f=tree_potential(T,signs)
            rng=feasible_interval(f)
            if rng is not None:intervals[f]=rng
    assert len(intervals)==310
    assert Counter(intervals.values())=={
        (Q(1),Q(1)):180,(Q(1),Q(2)):70,(Q(2),Q(2)):60}
    open_aff={v for v,I in intervals.items() if I==(Q(1),Q(2))}
    assert len(open_aff)==70
    reps=[
      ((0,0),(-1,0),(0,-1),(0,-1),(-1,0)),  # A
      ((0,0),(-1,0),(0,-1),(-1,0),(0,0)),   # B
      ((0,0),(-1,0),(-1,0),(0,0),(-1,0)),  # C
      ((0,0),(-1,0),(0,-1),(0,-1),(1,-1)),  # D
      ((0,0),(-1,0),(0,-1),(1,-1),(-1,0)),  # E
    ]
    orbits=[shift_orbit(v) for v in reps]
    assert [len(o) for o in orbits]==[10,10,10,20,20]
    assert len(set.union(*orbits))==70
    assert set.union(*orbits)==open_aff
    # No two different affine normals coalesce inside (1,2).
    critical=set()
    for f in open_aff:
        for g in open_aff:
            if f>=g:continue
            roots=set()
            for (a,b),(c,d) in zip(f,g):
                if b!=d:roots.add(Q(c-a,b-d))
                elif a!=c:roots.add('impossible')
            if len(roots)==1:
                x=next(iter(roots))
                if isinstance(x,Q) and 1<x<2:critical.add(x)
    assert not critical,critical
    for t,cnt,osizes in [(Q(1),30,[10,10,10]),(Q(5,4),70,[10,10,10,20,20]),(Q(3,2),70,[10,10,10,20,20]),(Q(7,4),70,[10,10,10,20,20]),(Q(2),30,[10,10,10])]:
        vertices={value(f,t) for f,(a,b) in intervals.items() if a<=t<=b}
        assert len(vertices)==cnt and orbit_lengths(vertices)==osizes
    # The center inball's squared facet-normal lengths for all five orbits.
    expected=[
      lambda t: Q(2,5)*(3*t*t-4*t+3),
      lambda t: Q(2,5)*(2*t*t-2*t+3),
      lambda t: Q(6,5),
      lambda t: Q(2,5)*(3*t*t-5*t+5),
      lambda t: Q(2,5)*(3*t*t-7*t+7),
    ]
    for t in (Q(1),Q(5,4),Q(3,2),Q(7,4),Q(2)):
        for v,formula in zip(reps,expected):
            assert centered_norm2(value(v,t))==formula(t)
    # Polynomial determinant for cyclic shifts of B, coordinates site 0 normalized.
    b=reps[1];M=[]
    for k in range(4):
        v=[b[(k+j)%N] for j in range(N)]
        M.append([tuple(v[j][c]-v[0][c] for c in (0,1)) for j in range(1,N)])
    assert det_polynomial_linear(M)==(1,2,-1,-2,1)
    # Exact golden-ratio Fourier projections.
    V=[tuple(Radical(a)+Radical(b)*PHI for a,b in rep) for rep in reps]
    exV=[Radical(Q(11,5),Q(-1,5)),Radical(2),Radical(Q(6,5)),Radical(Q(14,5),Q(-2,5)),Radical(Q(16,5),Q(-4,5))]
    exQ=[Radical(Q(3,5),Q(-1,5)),Radical(0),Radical(Q(3,5),Q(1,5)),Radical(Q(7,5),Q(-3,5)),Radical(Q(8,5),Q(-2,5))]
    for v,Vexpect,Qexpect in zip(V,exV,exQ):
        assert norm2_rad(v)==Vexpect
        assert sum((w*w for w in project_W(v)),Radical())==Qexpect
    assert all(u==Radical() for u in project_W(V[1]))
    # The first two cyclic shifts of B have a nonzero two-by-two minor
    # in normalized site-zero coordinates, proving rank at least two.
    b0=V[1]
    b1=tuple(b0[(1+j)%N] for j in range(N))
    u=[b0[j]-b0[0] for j in (1,2)]
    w=[b1[j]-b1[0] for j in (1,2)]
    assert u[0]*w[1]-u[1]*w[0] == Radical(-1)
    # The five-by-five Fourier-frequency-two matrix is an orthogonal projector.
    for i in range(N):
        e=[Radical(int(j==i)) for j in range(N)]
        pe=project_W(e)
        assert project_W(pe)==pe
        assert sum(pe,Radical())==Radical()
    # The twenty D-family facets induce ten distinct supporting directions.
    D=set()
    for k in range(5):
        for flip in (-1,1):
            for sign in (-1,1):
                f=tuple(sign*V[3][(k+flip*j)%N] for j in range(N))
                D.add(project_W(f))
    assert len(D)==10
    # Rigorous rational bounds controlling noncontact facets on the exceptional plane.
    # Comparisons in Q(sqrt(5)) avoid floating point.
    def positive(z):
        z=Radical.coerce(z)
        a,b=z.a,z.b
        if a==0:return b>0
        if b==0:return a>0
        if a>0 and b>0:return True
        if a<0 and b<0:return False
        return (a*a>5*b*b) if a>0 else (5*b*b>a*a)
    assert positive(SQ5-Q(2236,1000)) and positive(Q(2237,1000)-SQ5)
    # h_D / cos(pi/10) < 0.106 follows from delta_D<0.024,
    # ||P_W D||>0.24 and cos(pi/10)>0.95.
    assert positive(exQ[3]-Q(24,100)**2)
    assert positive((7-SQ5)/5-Q(976,1000)**2)
    assert positive((5+SQ5)/8-Q(95,100)**2)
    assert Q(24,1000)/(Q(24,100)*Q(95,100)) < Q(106,1000)
    # Other facet families have more slack than a 0.106-radius disk requires.
    assert positive(Q(94,100)**2-exV[0]/2)
    assert positive(Q(391,1000)**2-exQ[0])
    assert positive(Q(78,100)**2-exV[2]/2)
    assert positive(Q(1024,1000)**2-exQ[2])
    assert positive(Q(841,1000)**2-exV[4]/2)
    assert positive(Q(841,1000)**2-exQ[4])
    assert Q(106,1000)*Q(391,1000)<Q(6,100)
    assert Q(106,1000)*Q(1024,1000)<Q(22,100)
    assert Q(106,1000)*Q(841,1000)<Q(159,1000)
    print('125 labeled trees, 16 orientations each: 310 feasible affine assignments')
    print('Parameter intervals: 180 endpoint-one, 70 entire interior, 60 endpoint-two')
    print('Interior orbits: 10, 10, 10, 20, 20; endpoint facets: 30 each')
    print('Normal lengths, golden projections, and determinant polynomial exact')
    print('Golden exceptional-center polygon has 10 supporting directions')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':proof_checks()
