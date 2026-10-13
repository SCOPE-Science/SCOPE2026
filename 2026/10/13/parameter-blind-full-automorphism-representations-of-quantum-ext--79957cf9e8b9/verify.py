#!/usr/bin/env python3
"""Finite-field corroboration for a two-generator quantum complete intersection.

Run with Python 3: python verify.py . Independent enumeration is only a
finite check; the proof for arbitrary finite fields is in RESULT.md.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        self.q=q
        if q in (4,8):
            self.p=2; self.degree={4:2,8:3}[q]; self.mod={4:0b111,8:0b1011}[q]
        elif q==9:
            self.p=3; self.degree=2; self.mod=(1,0,1)
        else:
            self.p=q; self.degree=1; self.mod=None
    def add(self,a,b):
        if self.p==2:return a^b
        if self.degree==1:return (a+b)%self.p
        return (a%3+b%3)%3+3*((a//3+b//3)%3)
    def neg(self,a):
        if self.p==2:return a
        if self.degree==1:return (-a)%self.p
        return (-a%3)+3*(-(a//3)%3)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.degree==1:return a*b%self.p
        if self.p==2:
            acc=0;u=a;v=b
            while v:
                if v&1:acc^=u
                u<<=1
                if u & (1<<self.degree):u^=self.mod
                v>>=1
            return acc
        # (a0+a1 t)(b0+b1 t), t^2=-1 in F_9
        a0,a1=a%3,a//3;b0,b1=b%3,b//3
        return (a0*b0-a1*b1)%3 + 3*((a0*b1+a1*b0)%3)
    def inv(self,a):
        assert a
        for i in range(1,self.q):
            if self.mul(a,i)==1:return i
        raise AssertionError('nonfield')
    def pow(self,a,n):
        out=1
        for _ in range(n):out=self.mul(out,a)
        return out


def rank(F, rows):
    if not rows:return 0
    z=[list(row) for row in rows];j=0
    ncols=len(z[0]);r=0
    while j<ncols and r<len(z):
        h=next((k for k in range(r,len(z)) if z[k][j]),None)
        if h is None:j+=1;continue
        z[r],z[h]=z[h],z[r]
        inv=F.inv(z[r][j]);z[r]=[F.mul(inv,x) for x in z[r]]
        for k in range(len(z)):
            if k!=r and z[k][j]:
                m=z[k][j]
                z[k]=[F.sub(x,F.mul(m,y)) for x,y in zip(z[k],z[r])]
        r+=1;j+=1
    return r


def mul_alg(F,lam,U,V):
    r,u,v,t=U;s,a,b,c=V
    M=F.mul;A=F.add
    return (M(r,s), A(M(r,a),M(u,s)), A(M(r,b),M(v,s)),
            A(A(M(r,c),M(s,t)),A(M(u,b),M(lam,M(v,a)))))


def candidate_automorphisms(F,lam):
    """Independently enumerate every pair of candidate generator images."""
    q=F.q;M=F.mul;A=F.add;Z=(0,0,0,0)
    for ax,bx,cx,ay,by,cy in product(range(q),repeat=6):
        if not F.sub(M(ax,by),M(bx,ay)):continue
        X=(0,ax,bx,cx);Y=(0,ay,by,cy)
        if mul_alg(F,lam,X,X)!=Z or mul_alg(F,lam,Y,Y)!=Z:continue
        if mul_alg(F,lam,Y,X)!=tuple(M(lam,v) for v in mul_alg(F,lam,X,Y)):continue
        yield (ax,bx,cx,ay,by,cy)


def fixed_dim(F,a,b,c,d):
    ab=F.mul(a,b)
    m=[[F.sub(a,1),0,0], [0,F.sub(b,1),0], [c,d,F.sub(ab,1)]]
    return 4-rank(F,m)


def group(F):
    for a,b in product(range(1,F.q),repeat=2):
        for c,d in product(range(F.q),repeat=2):
            yield (a,b,c,d)


def act(F,g,vector):
    a,b,c,d=g;r,u,v,t=vector;M=F.mul;A=F.add
    return (r,M(a,u),M(b,v),A(A(M(c,u),M(d,v)), M(M(a,b),t)))


def element_orbits(F):
    q=F.q
    group_elements=list(group(F));unseen=set(product(range(q),repeat=4));sizes=[]
    while unseen:
        v=next(iter(unseen));orb={act(F,g,v) for g in group_elements}
        assert orb <= unseen, (q,v)
        unseen-=orb;sizes.append(len(orb))
    return Counter(sizes)


def all_radical_subspaces(F):
    """Enumerate all RREF bases of subspaces of the three-dimensional radical."""
    q=F.q
    yield ()
    for a,b in product(range(q),repeat=2):yield ((1,a,b),)
    for a in range(q):yield ((0,1,a),)
    yield ((0,0,1),)
    for a,b in product(range(q),repeat=2):yield ((1,0,a),(0,1,b))
    for a in range(q):yield ((1,a,0),(0,0,1))
    yield ((0,1,0),(0,0,1))
    yield ((1,0,0),(0,1,0),(0,0,1))


def independently_enumerate_ideals(F):
    """Test two-sided closure for every radical subspace, not just modeled ideals."""
    out=[]
    for basis in all_radical_subspaces(F):
        dim=len(basis)
        if all(v[0]==v[1]==0 for v in basis):
            out.append(basis)
        elif rank(F,list(basis)+[(0,0,1)])==dim:
            out.append(basis)
    # The entire algebra is an additional ideal.
    return out


def ideal_orbits(F):
    q=F.q
    # 0, kz, J, A; and one 2-dimensional ideal I_[u:v]
    # for every projective line [u:v].
    slopes=[(1,s) for s in range(q)]+[(0,1)]
    def canonical(u,v):
        if u:return (1,F.mul(F.inv(u),v))
        return (0,1)
    G=list(group(F));unseen=set(slopes);sizes=[]
    while unseen:
        v=next(iter(unseen))
        orb={canonical(F.mul(g[0],v[0]),F.mul(g[1],v[1])) for g in G}
        assert orb<=unseen
        unseen-=orb;sizes.append(len(orb))
    return Counter([1,1,1,1]+sizes)


def test_q(q):
    F=Field(q);assert all(F.mul(x,F.inv(x))==1 for x in range(1,q))
    generic=[lam for lam in range(1,q) if lam not in {1,F.neg(1)}]
    assert len(generic)==(q-3 if q%2 else q-2)
    expected=Counter({1:q*q*(q-2)*(q-3),2:3*(q-2)*q*q,3:q*q-1,4:1})
    assert sum(expected.values())==q*q*(q-1)**2
    assert sum(q**d*n for d,n in expected.items())//sum(expected.values())==5*q
    assert sum(q**d*n for d,n in expected.items())%sum(expected.values())==0
    seen_matrices=None
    for lam in generic:
        actual=list(candidate_automorphisms(F,lam))
        expected_matrices={(a,0,c,0,b,d) for a,b,c,d in group(F)}
        assert set(actual)==expected_matrices,('automorphisms',q,lam,len(actual))
        if seen_matrices is None:seen_matrices=set(actual)
        assert set(actual)==seen_matrices
    observed=Counter(fixed_dim(F,*g) for g in group(F))
    assert observed==expected,(q,expected,observed)
    assert element_orbits(F)==Counter({1:q,q-1:q,q*(q-1):2*q,q*(q-1)**2:q}),(q,'orbit')
    ideals=independently_enumerate_ideals(F)
    assert len(ideals)+1==q+5, (q,len(ideals))
    assert ideal_orbits(F)==Counter({1:6,q-1:1})
    # Two parameter values induce isomorphic algebras iff lambda=mu^{+/-1}.
    classes=set()
    for lam in generic:classes.add(tuple(sorted((lam,F.inv(lam)))))
    assert len(classes)==len(generic)//2
    print('q=%d, generic_parameters=%d, nonisomorphic_classes=%d, autos=%d, fixed=%s, element_orbits=%d, ideal_orbits=7'
          %(q,len(generic),len(classes),sum(expected.values()),dict(sorted(observed.items())),5*q))

if __name__=='__main__':
    for q in (4,5,7,8,9):test_q(q)
    print('VERIFY_OK')
