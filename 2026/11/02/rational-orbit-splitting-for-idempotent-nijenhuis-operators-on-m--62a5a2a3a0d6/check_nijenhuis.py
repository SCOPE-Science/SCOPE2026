#!/usr/bin/env python3
"""Finite-field checks of idempotent Nijenhuis projections on sl_2."""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (3,5,7,9)
        self.q=q
        if q != 9:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
            self.neg=lambda a:(-a)%q
        else:
            self.add=lambda a,b:((a%3+b%3)%3)+3*((a//3+b//3)%3)
            self.neg=lambda a:(-a%3)+3*((-(a//3))%3)
            self.mul=lambda a,b:((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        self.inv={a:next(x for x in range(1,q) if self.mul(a,x)==1) for a in range(1,q)}
    def sub(self,a,b):return self.add(a,self.neg(b))
    def div(self,a,b):return self.mul(a,self.inv[b])

def vecs(F): return product(range(F.q),repeat=3)
def dot(F,a,b):
    z=0
    for x,y in zip(a,b): z=F.add(z,F.mul(x,y))
    return z

def lines(F):
    out=[]
    for v in vecs(F):
        lead=next((i for i,x in enumerate(v) if x),None)
        if lead is not None and v[lead]==1 and all(x==0 for x in v[:lead]): out.append(v)
    return out

def bracket(F,x,y):
    # Coordinates (f,h,e), with [h,e]=2e, [h,f]=-2f, [e,f]=h.
    two=F.add(1,1)
    return (F.mul(two,F.sub(F.mul(x[0],y[1]),F.mul(x[1],y[0]))),
            F.sub(F.mul(x[2],y[0]),F.mul(x[0],y[2])),
            F.mul(two,F.sub(F.mul(x[1],y[2]),F.mul(x[2],y[1]))))

def matrix_mul(F,A,B):
    return tuple(tuple(dot(F,A[i],tuple(B[k][j] for k in range(3))) for j in range(3)) for i in range(3))

def mv(F,A,v): return tuple(dot(F,row,v) for row in A)

def rank_one(F,v,w):
    d=dot(F,v,w)
    assert d
    return tuple(tuple(F.div(F.mul(vi,wj),d) for wj in w) for vi in v)

def complement(F,P):
    return tuple(tuple(F.sub((1 if i==j else 0),P[i][j]) for j in range(3)) for i in range(3))

def is_nijenhuis(F,P):
    basis=((1,0,0),(0,1,0),(0,0,1))
    for x in basis:
        for y in basis:
            px,py=mv(F,P,x),mv(F,P,y)
            lhs=bracket(F,px,py)
            t1,t2,t3=bracket(F,px,y),bracket(F,x,py),mv(F,P,bracket(F,x,y))
            inner=tuple(F.sub(F.add(a,b),c) for a,b,c in zip(t1,t2,t3))
            if lhs!=mv(F,P,inner):return False
    return True

def is_plane_subalgebra(F,lambda_):
    basis=[]
    for v in vecs(F):
        if v==(0,0,0) or dot(F,lambda_,v): continue
        if not basis: basis=[v]
        elif not any(v==tuple(F.mul(k,basis[0][i]) for i in range(3)) for k in range(F.q)):
            basis.append(v);break
    return dot(F,lambda_,bracket(F,basis[0],basis[1]))==0


def exact_group_orbits(F,projections):
    # Independent conjugation by all projective 2-by-2 invertible matrices.
    q=F.q
    basis=(((0,0),(1,0)),((1,0),(0,F.neg(1))),((0,1),(0,0)))
    def mm2(A,B):
        return tuple(tuple(F.add(F.mul(A[i][0],B[0][j]),F.mul(A[i][1],B[1][j])) for j in range(2)) for i in range(2))
    def normalize(G):
        z=next(x for row in G for x in row if x)
        return tuple(tuple(F.div(x,z) for x in row) for row in G)
    actions={}
    for entries in product(range(q),repeat=4):
        a,b,c,d=entries
        det=F.sub(F.mul(a,d),F.mul(b,c))
        if not det:continue
        G=normalize(((a,b),(c,d)))
        a,b=G[0];c,d=G[1]
        det=F.sub(F.mul(a,d),F.mul(b,c))
        Gi=((F.div(d,det),F.div(F.neg(b),det)),(F.div(F.neg(c),det),F.div(a,det)))
        def adj(H):
            cols=[]
            for e in basis:
                x=mm2(mm2(H,e),Gi if H==G else G)
                cols.append((x[1][0],x[0][0],x[0][1]))
            return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
        T=adj(G)
        Tin=tuple(tuple((lambda x:(x[1][0],x[0][0],x[0][1]))(mm2(mm2(Gi,basis[j]),G))[i] for j in range(3)) for i in range(3))
        actions[G]=(T,Tin)
    assert len(actions)==q*(q*q-1)
    remain=set(projections);orbits=[]
    while remain:
        P=next(iter(remain)); orb={matrix_mul(F,matrix_mul(F,T,P),Tin) for T,Tin in actions.values()}
        assert orb<=remain
        remain-=orb;orbits.append(len(orb))
    expected=sorted([1,1, q*(q+1), q*(q+1)]+[q*(q*q-1)//2]*4)
    assert sorted(orbits)==expected,(q,sorted(orbits),expected)
    return sorted(orbits)

def count_check(q,ambient=False):
    F=Field(q); all_lines=lines(F)
    borels=[w for w in all_lines if is_plane_subalgebra(F,w)]
    assert len(borels)==q+1, (q,len(borels))
    projections=set()
    for w in borels:
        for v in all_lines:
            if not dot(F,w,v): continue
            P=rank_one(F,v,w)
            assert matrix_mul(F,P,P)==P and is_nijenhuis(F,P)
            projections.add(P)
            Q=complement(F,P)
            assert matrix_mul(F,Q,Q)==Q and is_nijenhuis(F,Q)
            projections.add(Q)
    I=tuple(tuple(1 if i==j else 0 for j in range(3)) for i in range(3))
    O=tuple(tuple(0 for j in range(3)) for i in range(3))
    projections.update((O,I))
    assert len(projections)==2*q*q*(q+1)+2,(q,len(projections))
    # The Borel stabilizer acts on its affine complement by (a,b)->(s+ta,-s^2-2sta+t^2b).
    points=set(product(range(q),repeat=2))
    orbits=[]
    while points:
        a,b=next(iter(points)); orbit=set()
        for s in range(q):
            for t in range(1,q):
                ap=F.add(s,F.mul(t,a))
                bp=F.add(F.neg(F.mul(s,s)),F.add(F.neg(F.mul(F.add(1,1),F.mul(F.mul(s,t),a))),F.mul(F.mul(t,t),b)))
                orbit.add((ap,bp))
        assert orbit<=points
        points-=orbit;orbits.append(len(orbit))
    assert sorted(orbits)==sorted([q,q*(q-1)//2,q*(q-1)//2]),(q,orbits)
    if ambient:
        assert q==3
        all_valid=set()
        for entries in product(range(q), repeat=9):
            X=tuple(tuple(entries[3*i+j] for j in range(3)) for i in range(3))
            if matrix_mul(F,X,X)==X and is_nijenhuis(F,X):all_valid.add(X)
        assert all_valid==projections,(len(all_valid),len(projections))
    group_orbits=exact_group_orbits(F,projections) if q in (3,5) else None
    print(f'FIELD={q} BORELS={len(borels)} NIJENHUIS_IDEMPOTENTS={len(projections)} RANK1_RANK2_EACH={q*q*(q+1)} BOREL_COMPLEMENT_ORBITS={sorted(orbits)} AMBIENT_CHECK={ambient} FULL_GROUP_ORBITS={group_orbits}')

if __name__=='__main__':
    for q in (3,5,7,9):count_check(q,ambient=(q==3))
    print('SL2_NIJENHUIS_PROJECTION_CHECKS_OK 4_FIELDS 1_AMBIENT_EXHAUSTIVE 2_FULL_GROUP_ORBIT_CHECKS')
