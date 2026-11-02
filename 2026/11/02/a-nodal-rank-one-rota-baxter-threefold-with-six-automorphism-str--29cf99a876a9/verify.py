#!/usr/bin/env python3
"""Exact rank-one weight-zero Rota--Baxter classification checks."""
from itertools import product

def projective_vectors(q):
    for vals in product(range(q),repeat=3):
        for a in vals:
            if a:
                if a==1:
                    yield vals
                break

def multiply(a,b,q):
    a0,ax,ay,az=a
    b0,bx,by,bz=b
    return ((a0*b0)%q,(a0*bx+ax*b0)%q,(a0*by+ay*b0)%q,
            (a0*bz+az*b0+ax*by-ay*bx)%q)

def apply_R(u,phi,v,q):
    coefficient=sum(s*t for s,t in zip(phi,v))%q
    return tuple(coefficient*w%q for w in u)

def identity_holds(u,phi,q):
    basis=[(int(i==j) for i in range(4)) for j in range(4)]
    basis=[tuple(v) for v in basis]
    for a in basis:
        for b in basis:
            Ra=apply_R(u,phi,a,q);Rb=apply_R(u,phi,b,q)
            lhs=multiply(Ra,Rb,q)
            m1=multiply(Ra,b,q);m2=multiply(a,Rb,q)
            rhs=apply_R(u,phi,tuple((x+y)%q for x,y in zip(m1,m2)),q)
            if lhs!=rhs:return False
    return True

def rank_one_operators(q):
    for a,b,c in projective_vectors(q):
        u=(0,a,b,c)
        for alpha,beta,gamma in product(range(q),repeat=3):
            if alpha==beta==gamma==0:continue
            if (a*beta+b*gamma)%q:continue
            yield (u,(alpha,beta,gamma,0))

def matrix_of(u,phi,q):
    return tuple(u[i]*phi[j]%q for i in range(4) for j in range(4))

def conjugate(u,phi,q,A,sh):
    # Columns of invertible 2x2 matrix A=(a,b,d,e).
    a,b,d,e=A
    det=(a*e-b*d)%q
    invdet=pow(det,-1,q)
    ua,ub,uc=u[1:]
    cu,cv=sh
    new_u=(0,(a*ua+d*ub)%q,(b*ua+e*ub)%q,(cu*ua+cv*ub+det*uc)%q)
    alpha,beta,gamma,_=phi
    # A^{-1} on column (x,y): det^{-1} [[e,-d],[-b,a]].
    new_phi=(alpha,(beta*e-gamma*b)*invdet%q,(-beta*d+gamma*a)*invdet%q,0)
    return matrix_of(new_u,new_phi,q)

def automorphisms(q):
    for a,b,d,e in product(range(q),repeat=4):
        if (a*e-b*d)%q==0:continue
        for sh in product(range(q),repeat=2):
            yield (a,b,d,e),sh

def run(q,orbits):
    candidates=list(rank_one_operators(q))
    rs={matrix_of(u,p,q) for u,p in candidates}
    assert len(rs)==len(candidates)
    expected=q**4+2*q**3-q*q-q-1
    assert len(rs)==expected, (q,len(rs),expected)
    assert all(identity_holds(u,p,q) for u,p in candidates)
    # 6 canonical families: socle image z vs nonsocle image x;
    # within each, constant/linear functional support both/one.
    z=(0,0,0,1);x=(0,1,0,0)
    reps=[(z,(0,1,0,0)),(z,(1,0,0,0)),(z,(1,1,0,0)),
          (x,(0,0,1,0)),(x,(1,0,0,0)),(x,(1,0,1,0))]
    if orbits:
        aut=list(automorphisms(q))
        assert len(aut)==q*q*(q*q-1)*(q*q-q)
        computed=[{conjugate(u,p,q,A,sh) for A,sh in aut} for u,p in reps]
        sizes=[len(s) for s in computed]
        predicted=[q*q-1,q-1,(q-1)*(q*q-1),
                   q*(q+1)*(q-1),q*(q+1)*(q-1),q*(q+1)*(q-1)**2]
        assert sizes==predicted,(q,sizes,predicted)
        assert len(set.union(*computed))==len(rs)
        assert len(set.union(*computed))==sum(sizes)
        assert set.union(*computed)==rs
        print('orbit_decomposition:',q,sizes,'aut',len(aut))
    else:
        print('rank_one_points:',q,len(rs))

def verify_geometry():
    import sympy as sp
    a,b,beta,gamma=sp.symbols('a b beta gamma')
    F=a*beta+b*gamma
    partials=[sp.diff(F,t) for t in (a,b,beta,gamma)]
    assert partials==[beta,gamma,a,b]
    H=sp.hessian(F,(a,b,beta,gamma))
    assert H.det()==1
    print('node_gradient_and_quadratic_rank: PASS')

if __name__=='__main__':
    verify_geometry()
    for q in [2,3,5]:run(q,True)
    run(7,False)
    print('VERIFY_OK')
