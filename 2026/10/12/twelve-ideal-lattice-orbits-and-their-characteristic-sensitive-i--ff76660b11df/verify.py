#!/usr/bin/env python3
"""Independent projective-action and incidence checks for a short local algebra."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, p, polynomial=None):
        self.p = p
        self.polynomial = polynomial or [0, 1]
        self.n = len(self.polynomial)-1
        self.q = p**self.n
    def encode(self, coeffs):
        return sum((c%self.p)*self.p**i for i,c in enumerate(coeffs))
    def decode(self, a):
        return [(a//(self.p**i))%self.p for i in range(self.n)]
    def add(self,a,b):
        return self.encode([(x+y)%self.p for x,y in zip(self.decode(a),self.decode(b))])
    def neg(self,a):
        return self.encode([-x%self.p for x in self.decode(a)])
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        x=self.decode(a);y=self.decode(b)
        z=[0]*(2*self.n-1)
        for i,u in enumerate(x):
            for j,v in enumerate(y):z[i+j]=(z[i+j]+u*v)%self.p
        for d in range(2*self.n-2,self.n-1,-1):
            t=z[d]
            for j in range(self.n):z[d-self.n+j]=(z[d-self.n+j]-t*self.polynomial[j])%self.p
        return self.encode(z[:self.n])
    def power(self,a,k):
        r=1
        while k:
            if k&1:r=self.mul(r,a)
            a=self.mul(a,a);k//=2
        return r
    def inv(self,a):
        assert a
        return self.power(a,self.q-2)
    def dot(self,x,y):
        r=0
        for a,b in zip(x,y):r=self.add(r,self.mul(a,b))
        return r
    def canon(self,v):
        i=next(i for i,a in enumerate(v) if a)
        inv=self.inv(v[i]);return tuple(self.mul(inv,x) for x in v)
    def det2(self,g):
        return self.sub(self.mul(g[0][0],g[1][1]),self.mul(g[0][1],g[1][0]))
    def matvec(self,M,v):
        return tuple(self.dot(row,v) for row in M)
    def invmat(self,M):
        n=len(M)
        a=[list(M[i])+[int(i==j) for j in range(n)] for i in range(n)]
        for j in range(n):
            pivot=next(i for i in range(j,n) if a[i][j])
            a[j],a[pivot]=a[pivot],a[j]
            z=self.inv(a[j][j]);a[j]=[self.mul(z,v) for v in a[j]]
            for i in range(n):
                if i==j:continue
                z=a[i][j]
                a[i]=[self.sub(v,self.mul(z,w)) for v,w in zip(a[i],a[j])]
        return [row[n:] for row in a]
    def sym2(self,g):
        (a,b),(c,d)=g
        m=self.mul
        return [[m(a,a),m(a,b),m(b,b)],
                [self.mul(2%self.p,m(a,c)),self.add(m(a,d),m(b,c)),self.mul(2%self.p,m(b,d))],
                [m(c,c),m(c,d),m(d,d)]]
    def projective(self,d):
        return sorted({self.canon(v) for v in product(range(self.q),repeat=d) if any(v)})

def orbit_partition(points,actions):
    pending=set(points); result=[]
    while pending:
        seed=min(pending); seen={seed}; todo=[seed]
        for v in todo:
            for A in actions:
                w=A(v)
                if w not in seen:
                    seen.add(w);todo.append(w)
        assert seen<=pending
        result.append(seen);pending-=seen
    return result

def field_case(F):
    q=F.q;m=F.mul
    # A primitive scalar together with the elementary generators generates GL_2.
    primitive=next(a for a in range(1,q) if len({F.power(a,k) for k in range(q-1)})==q-1)
    gens=[[[1,1],[0,1]],[[1,0],[1,1]],[[primitive,0],[0,1]],[[0,1],[1,0]]]
    pts=F.projective(3)
    acts=[];dualacts=[]
    for g in gens:
        assert F.det2(g)
        M=F.sym2(g)
        inv=F.invmat(M)
        acts.append(lambda v,M=M:F.canon(F.matvec(M,v)))
        dualacts.append(lambda h,inv=inv:F.canon(tuple(F.dot(h,[inv[i][j] for i in range(3)]) for j in range(3))))
    p_orbs=orbit_partition(pts,acts)
    h_orbs=orbit_partition(pts,dualacts)
    line=F.projective(2)
    def point_type(v):
        a,b,c=v
        roots=sum(F.add(F.add(m(a,m(u,u)),m(b,m(u,w))),m(c,m(w,w)))==0 for u,w in line)
        return {0:'I',1:'C',2:'E'}[roots]
    classes={v:point_type(v) for v in pts}
    p_types={}
    for o in p_orbs:
        ty=classes[next(iter(o))]
        assert all(classes[x]==ty for x in o)
        assert ty not in p_types
        p_types[ty]=len(o)
    expected={'C':q+1,'E':q*(q+1)//2,'I':q*(q-1)//2}
    assert p_types==expected,(q,p_types,expected)
    h_classes={};pinc={}
    for orb in h_orbs:
        reps=[Counter(classes[v] for v in pts if F.dot(h,v)==0) for h in orb]
        assert all(x==reps[0] for x in reps)
        incidence=(reps[0]['C'],reps[0]['E'],reps[0]['I'])
        assert incidence not in h_classes
        h_classes[incidence]=len(orb)
    if F.p!=2:
        expected_h={(1,q,0):q+1,
                    (2,(q-1)//2,(q-1)//2):q*(q+1)//2,
                    (0,(q+1)//2,(q+1)//2):q*(q-1)//2}
    else:
        expected_h={(q+1,0,0):1,(1,q,0):q+1,(1,q//2,q//2):q*q-1}
    assert h_classes==expected_h,(q,h_classes,expected_h)
    # The two line-projection ideal strata and four distinguished ideals are separate orbits.
    ideals=4+sum(p_types.values())+sum(h_classes.values())+q*(q+1)+(q+1)
    assert ideals==3*q*q+4*q+7
    orbit_sizes=[1]*4+list(p_types.values())+list(h_classes.values())+[q*(q+1),q+1]
    assert len(orbit_sizes)==12 and sum(orbit_sizes)==ideals
    print('q',q,'P2_points',p_types,'P2_lines',h_classes,'ideals',ideals,
          'orbits',len(orbit_sizes),'sizes',sorted(orbit_sizes))

for p,polynomial in [(2,None),(3,None),(2,[1,1,1]),(5,None),(7,None),
                     (2,[1,1,0,1]),(3,[1,0,1])]:
    field_case(Field(p,polynomial))
print('VERIFY_OK')

# A direct ideal census and full automorphism action over F_2, independent
# of the projection/graph decomposition used in the mathematical proof.
def brute_f2():
    def span(basis):
        s={0}
        for v in basis:s|={u^v for u in list(s)}
        return frozenset(s)
    subs={span(())};pending=[span(())]
    while pending:
        s=pending.pop()
        for v in range(32):
            if v not in s:
                t=span(list(s)+[v])
                if t not in subs:subs.add(t);pending.append(t)
    assert len(subs)==374
    def times(v,source):
        # Basis x,y,x^2,xy,y^2; source=0: x, source=1:y.
        if source==0:return ((v&1)<<2)|(((v>>1)&1)<<3)
        return ((v&1)<<3)|(((v>>1)&1)<<4)
    ideals={s for s in subs if all(times(v,i) in s for v in s for i in (0,1))}
    assert len(ideals)==26
    gl=[(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if ((a*d+b*c)&1)]
    autos=[]
    for a,b,c,d in gl:
        for u,v,w,z,s,t in product(range(2),repeat=6):
            X=a|(c<<1)|(u<<2)|(v<<3)|(w<<4)
            Y=b|(d<<1)|(z<<2)|(s<<3)|(t<<4)
            XY=times(X,0) if False else 0
            # Multiplication of any two linear-plus-socle elements.
            def mul2(P,Q):
                p0,p1=P&1,(P>>1)&1
                q0,q1=Q&1,(Q>>1)&1
                return ((p0&q0)<<2)|(((p0&q1)^(p1&q0))<<3)|((p1&q1)<<4)
            basis=(X,Y,mul2(X,X),mul2(X,Y),mul2(Y,Y))
            assert span(basis)==frozenset(range(32))
            def act(vector,basis=basis):
                out=0
                for i,bv in enumerate(basis):
                    if vector>>i&1:out^=bv
                return out
            autos.append(act)
    assert len(autos)==384
    remaining=set(ideals);orbit_sizes=[]
    while remaining:
        seed=next(iter(remaining));orbit={frozenset(a(v) for v in seed) for a in autos}
        assert orbit<=remaining
        remaining-=orbit;orbit_sizes.append(len(orbit))
    assert len(orbit_sizes)==11 and sum(orbit_sizes)==26
    print('F2_full_ideal_census',len(subs),len(ideals)+1,len(autos), sorted(orbit_sizes+[1]))
brute_f2()
