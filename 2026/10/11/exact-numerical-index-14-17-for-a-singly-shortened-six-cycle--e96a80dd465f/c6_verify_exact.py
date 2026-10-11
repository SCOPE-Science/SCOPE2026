"""Exact rational verification of the six-cycle numerical index certificate."""
import itertools
import json
import sys
from fractions import Fraction as F

def vec(t):
    return tuple(F(*x) if isinstance(x,list) else F(x) for x in t)

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))

def check(data):
    w=data['weights']; assert w==[1,2,2,2,2,2] and data['dimension']==5
    # The dual ball is the zero-sum intersection of six weighted strips.
    D=set()
    for free in range(6):
        others=[i for i in range(6) if i!=free]
        for signs in itertools.product([-1,1],repeat=5):
            increments=[0]*6
            for j,s in zip(others,signs): increments[j]=s*w[j]
            increments[free]=-sum(increments)
            if abs(increments[free])<=w[free]:
                D.add(tuple(sum(increments[:i]) for i in range(1,6)))
    assert len(D)==60 and D=={tuple(p) for p in data['dual_vertices']}
    # Vertex molecules of the real Arens-Eells unit ball.
    P=set()
    for i,weight in enumerate(w):
        a,b=i,(i+1)%6
        p=[F(0)]*5
        if a!=0:p[a-1]+=F(1,weight)
        if b!=0:p[b-1]-=F(1,weight)
        P.add(tuple(p));P.add(tuple(-z for z in p))
    assert len(P)==12 and P=={vec(t) for t in data['primal_vertices']}
    # Polyhedral numerical radius: all norming extreme pairs.
    B={tuple(f*x for f in d for x in p) for p in P for d in D if dot(d,p)==1}
    C={tuple(f*x for f in d for x in p) for p in P for d in D}
    BB=[vec(x) for x in data['contact_tensors']]
    CC=[vec(x) for x in data['norm_tensors']]
    assert len(B)==150 and len(C)==360 and set(BB)==B and set(CC)==C
    rho=F(*data['target_ratio']);assert rho==F(17,14)
    assert len(data['upper_certificates'])==len(CC)
    for c,cert in zip(CC,data['upper_certificates']):
        target=[F(0)]*25;total=F(0)
        for j,p,q in cert:
            assert 0<=j<len(BB) and q>0
            z=F(p,q);total+=abs(z)
            for k,v in enumerate(BB[j]):target[k]+=z*v
        assert tuple(target)==c and total<=rho,(total,rho)
    T=vec(data['lower_witness']['matrix'])
    assert len(T)==25
    assert max(abs(dot(b,T)) for b in BB)==1
    assert max(abs(dot(c,T)) for c in CC)==rho
    assert abs(dot(CC[data['lower_witness']['norm_tensor_index']],T))==rho
    assert F(*data['target_index'])==1/rho
    print('PASS: 60 dual extreme points, 12 primal extreme points, 150 norming contacts, 360 exact upper certificates, sharp matrix witness; numerical index 14/17')

if __name__=='__main__':
    with open(sys.argv[1],encoding='utf-8') as fh: check(json.load(fh))
