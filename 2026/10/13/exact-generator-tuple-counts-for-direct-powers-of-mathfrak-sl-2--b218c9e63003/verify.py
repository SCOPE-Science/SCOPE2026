"""Finite-field checks for the exact direct-power generation formulas.
Pure Python; enumerates generated Lie subalgebras independently of formula.
"""
from itertools import product
from math import prod

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
        self.p=2 if q==4 else q
    def add(self,x,y): return (x^y) if self.q==4 else (x+y)%self.q
    def neg(self,x): return x if self.q==4 else (-x)%self.q
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.q!=4:return (x*y)%self.q
        z=0
        for i in range(2):
            if (y>>i)&1:z^=x<<i
        for j in (2,):
            if z & (1<<j):z^=7<<(j-2)
        return z
    def inv(self,x):
        assert x
        return next(y for y in range(1,self.q) if self.mul(x,y)==1)
    def scalar(self,s,v):return tuple(self.mul(s,t) for t in v)
    def addv(self,a,b):return tuple(self.add(x,y) for x,y in zip(a,b))
    def subvec(self,a,b):return tuple(self.sub(x,y) for x,y in zip(a,b))

def basis(vectors,F):
    pivots=[]; rows=[]
    for v in vectors:
        w=list(v)
        for i,row in zip(pivots,rows):
            if w[i]:
                t=w[i]
                w=[F.sub(x,F.mul(t,y)) for x,y in zip(w,row)]
        p=next((i for i,x in enumerate(w) if x),None)
        if p is None:continue
        inv=F.inv(w[p]);w=[F.mul(inv,x) for x in w]
        at=next((j for j,k in enumerate(pivots) if k>p),len(pivots))
        pivots.insert(at,p);rows.insert(at,w)
    return rows

def canon_rows(vectors,F):
    rows=[list(x) for x in basis(vectors,F)]
    piv=[next(i for i,z in enumerate(row) if z) for row in rows]
    for j in range(len(rows)-1,-1,-1):
        for i in range(j):
            t=rows[i][piv[j]]
            rows[i]=[F.sub(x,F.mul(t,y)) for x,y in zip(rows[i],rows[j])]
    return tuple(tuple(row) for row in rows)

def bracket(a,b,F):
    a0,a1,a2=a; b0,b1,b2=b
    d=F.sub(F.mul(a1,b2),F.mul(a2,b1))
    u=F.add(F.sub(F.mul(a0,b1),F.mul(a1,b0)),F.sub(F.mul(a0,b1),F.mul(a1,b0)))
    v=F.add(F.sub(F.mul(a2,b0),F.mul(a0,b2)),F.sub(F.mul(a2,b0),F.mul(a0,b2)))
    return(d,u,v)

def lie_generated_dimension(generators,F,k=1):
    dim=3*k
    def joint_bracket(x,y):
        z=[]
        for j in range(k):z.extend(bracket(x[3*j:3*j+3],y[3*j:3*j+3],F))
        return tuple(z)
    rows=basis(generators,F)
    while True:
        # Binary span is a Lie algebra iff brackets of its basis lie in span.
        new=basis(rows+[joint_bracket(a,b) for a in rows for b in rows],F)
        if len(new)==len(rows):return len(rows)
        rows=new

def expected_base(q,r):
    Q=q**r
    return Q*(Q-1)*(Q-q)

def expected_direct(q,r,k):
    if q%2==0:
        if r<2*k:return 0
        return q**(k*r)*prod(q**r-q**i for i in range(2*k))
    g=expected_base(q,r)
    a=q*(q*q-1)
    return prod(g-i*a for i in range(k)) if k<=g//a else 0

def all_vectors(F,k=1):return list(product(range(F.q),repeat=3*k))

def check_single(q,r):
    F=Field(q); elems=all_vectors(F)
    actual=sum(lie_generated_dimension(T,F)==3 for T in product(elems,repeat=r))
    expect=expected_base(q,r)
    assert actual==expect,(q,r,actual,expect)
    print('BASE_OK',q,r,actual)

def check_planes(q):
    F=Field(q); elems=all_vectors(F)
    planes={canon_rows([u,v],F) for u in elems for v in elems if len(basis([u,v],F))==2}
    sub=sum(lie_generated_dimension(P,F)==2 for P in planes)
    assert sub==q+1,(q,len(planes),sub)
    assert len(planes)==q*q+q+1
    print('PLANES_OK',q,len(planes),sub)

def rank(vectors,F):return len(basis(vectors,F))

def check_binary_direct(q,k,r):
    F=Field(q)
    # Independent rank census in the 2k-dimensional abelianization.
    V=list(product(range(q),repeat=2*k))
    actual=sum(rank(T,F)==2*k for T in product(V,repeat=r))*q**(k*r)
    expect=expected_direct(q,r,k)
    assert actual==expect,(q,k,r,actual,expect)
    print('BINARY_DIRECT_OK',q,k,r,actual)

def check_odd_automorphism_orbits(q):
    F=Field(q)
    vecs=all_vectors(F)
    pairs=[(x,y) for x in vecs for y in vecs if lie_generated_dimension((x,y),F)==3]
    gl=[]
    for a,b,c,d in product(range(q),repeat=4):
        det=F.sub(F.mul(a,d),F.mul(b,c))
        if det:
            v=(a,b,c,d)
            lead=next(t for t in v if t)
            rep=tuple(F.mul(F.inv(lead),t) for t in v)
            if rep==v:gl.append((a,b,c,d))
    assert len(gl)==q*(q*q-1)
    def action(g,x):
        u,v,w,t=g
        de=F.sub(F.mul(u,t),F.mul(v,w)); ide=F.inv(de)
        z0,z1,z2=x
        M=((z0,z1),(z2,F.neg(z0)))
        H=((u,v),(w,t))
        I=((F.mul(t,ide),F.neg(F.mul(v,ide))), (F.neg(F.mul(w,ide)),F.mul(u,ide)))
        def mm(A,B):
            return tuple(tuple(F.add(F.mul(A[i][0],B[0][j]),F.mul(A[i][1],B[1][j])) for j in range(2)) for i in range(2))
        Z=mm(mm(H,M),I)
        assert Z[1][1]==F.neg(Z[0][0])
        return (Z[0][0],Z[0][1],Z[1][0])
    pairset=set(pairs); unseen=set(pairs);orbits=[]
    while unseen:
        p=next(iter(unseen))
        orbit={(action(g,p[0]),action(g,p[1])) for g in gl}
        assert len(orbit)==len(gl)
        assert orbit<=pairset
        unseen.difference_update(orbit)
        orbits.append(orbit)
    g=expected_base(q,2);a=q*(q*q-1)
    assert len(orbits)==g//a
    assert sum(len(x)*(g-len(x)) for x in orbits)==expected_direct(q,2,2)
    print('ODD_ORBITS_OK',q,'generating pairs',g,'automorphisms',a,'orbits',len(orbits),'two-factor tuples',expected_direct(q,2,2))

if __name__=='__main__':
    for q in (2,3,4,5):
        check_planes(q)
        check_single(q,2)
    for q in (2,3):check_single(q,3)
    for q in (3,5):check_odd_automorphism_orbits(q)
    for (q,k,r) in ((2,2,4),(2,2,3),(2,2,2),(4,1,2)):
        check_binary_direct(q,k,r)
    F=Field(3)
    samples=[tuple((i//(3**j))%3 for j in range(6)) for i in range(150)]
    import random
    rand=random.Random(20261009)
    for _ in range(300):
        vecs=[tuple(rand.randrange(3) for j in range(6)) for i in range(2)]
        dimension=lie_generated_dimension(vecs,F,2)
        assert dimension<=6
    print('DIRECT_SUBALGEBRA_SPOT_CHECK_OK')
    print('VERIFY_OK')
