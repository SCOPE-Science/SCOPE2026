#!/usr/bin/env python3
"""Exact projector and time-domain tests of capture on balanced block designs."""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import expm


def cyclic_design(v, base):
    return sp.Matrix([[int((j-i)%v in base) for j in range(v)] for i in range(v)])


def projective_hyperplanes():
    return sp.Matrix([[int(((i+1)&(j+1)).bit_count()%2==0) for j in range(15)] for i in range(15)])


def affine_plane_three():
    points=[(x,y) for x in range(3) for y in range(3)]
    blocks=[]
    for slope in range(3):
        for c in range(3): blocks.append({(x,(slope*x+c)%3) for x in range(3)})
    for c in range(3): blocks.append({(c,y) for y in range(3)})
    return sp.Matrix([[int(pt in line) for line in blocks] for pt in points])


def projective_lines_15():
    lines=sorted({tuple(sorted({a,b,a^b})) for a in range(1,16) for b in range(a+1,16)})
    assert len(lines)==35
    return sp.Matrix([[int(i in line) for line in lines] for i in range(1,16)])


def all_triples_seven():
    blocks=list(itertools.combinations(range(7),3))
    return sp.Matrix([[int(i in line) for line in blocks] for i in range(7)])


def examples():
    return [('Fano projective plane',cyclic_design(7,{0,1,3}),3,1),
            ('projective plane of order three',cyclic_design(13,{0,1,3,9}),4,1),
            ('symmetric biplane',cyclic_design(11,{1,3,4,5,9}),5,2),
            ('PG(3,2) hyperplanes',projective_hyperplanes(),7,3),
            ('affine plane of order three',affine_plane_three(),3,1),
            ('PG(3,2) projective lines',projective_lines_15(),3,1),
            ('complete triple design of seven points',all_triples_seven(),3,5)]


def projection(X):
    return X*(X.T*X).inv()*X.T


def run():
    cases=sites=exact=dynamic=0
    worst=0.
    for name,B,k,lam in examples():
        v,b=B.shape
        replication=int(sum(B[0,j] for j in range(b)))
        delta=replication-lam
        assert delta>0
        assert B*B.T == delta*sp.eye(v)+lam*sp.ones(v,v)
        assert all(sum(B[i,j] for j in range(b))==replication for i in range(v))
        assert all(sum(B[i,j] for i in range(v))==k for j in range(b))
        A=sp.zeros(v+b,v+b)
        A[:v,v:]=B; A[v:,:v]=B.T
        subset_sizes=sorted(set([3,4,v//2,v-2,v-1]))
        subsets=[]
        for t in subset_sizes:
            if not (3<=t<v): continue
            subsets += [tuple(range(t)),tuple(range(v-t,v))]
        if v==7:
            subsets=list(itertools.chain.from_iterable(itertools.combinations(range(v),t) for t in range(3,v)))
        subsets=sorted(set(subsets))
        Bfloat=np.asarray(B,dtype=float)
        for S in subsets:
            t=len(S);s=v-t
            W=sp.zeros(v,t+1)
            for j,p in enumerate(S):W[p,j]=1
            W[:,t]=sp.ones(v,1)
            G=B.T*W
            assert W.rank()==t+1 and G.rank()==t+1
            assert B*G == delta*W+lam*sp.ones(v,1)*(sp.ones(1,v)*W)
            if t<=3 or (v==7 and t<=4):
                P=projection(W);Q=projection(G)
                for x in range(v):
                    want=sp.Integer(1) if x in S else sp.Rational(1,s)
                    assert P[x,x]==want,(name,S,x)
                for ell in range(b):
                    u=sum(1-int(B[p,ell]) for p in range(v) if p not in S)
                    want=sp.Rational(v,b)-sp.Rational(u*(s-u),s*delta)
                    assert Q[ell,ell]==want,(name,S,ell,Q[ell,ell],want)
                exact+=1
            p=np.linalg.qr(np.asarray(W,dtype=float))[0]
            q=np.linalg.qr(np.asarray(G,dtype=float))[0]
            pd=np.sum(p*p,axis=1);qd=np.sum(q*q,axis=1)
            for x in range(v):
                target=1 if x in S else 1/s
                worst=max(worst,abs(pd[x]-target));sites+=1
            for ell in range(b):
                u=sum(1-int(B[p,ell]) for p in range(v) if p not in S)
                target=v/b-u*(s-u)/(s*delta)
                worst=max(worst,abs(qd[ell]-target));sites+=1
            assert abs(float(pd.sum()+qd.sum())-2*(t+1))<1.e-9
            cases+=1
        # independent non-Hermitian propagation with several sink geometries
        if name in ['Fano projective plane','affine plane of order three']:
            Af=np.asarray(A,dtype=float)
            for S in [(0,1,2),(0,2,4)]:
                s=v-len(S);mask=np.zeros(v+b);mask[list(S)]=1
                U=expm((-1j*Af-0.5*np.diag(mask))*500)
                for j in [0,v-1,v,v+b//2,v+b-1]:
                    surv=float(np.linalg.norm(U[:,j])**2)
                    if j<v: eta=1 if j in S else 1/s
                    else:
                        u=sum(1-int(B[p,j-v]) for p in range(v) if p not in S)
                        eta=v/b-u*(s-u)/(s*delta)
                    assert abs(1-surv-eta)<5.e-5,(name,S,j,surv,eta)
                    dynamic+=1
        print(f'{name}: v={v}, b={b}, k={k}, replication={replication}, lambda={lam}, subsets={len(subsets)}')
    assert worst<1.e-11
    print(f'PASS subsets={cases} site_probabilities={sites} exact_projector_subsets={exact} dissipative_site_tests={dynamic} maximum_error={worst:.3e}')

if __name__=='__main__': run()
