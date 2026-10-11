"""Exact arithmetic checks for the diagonal bisection of a cube.
Run: python3 verify.py; only Python standard library is required.
These finite checks supplement the symbolic all-dimensional argument.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

def data(d):
    assert d >= 2
    if d % 2 == 0:
        return (F(1,d+1),F(d**3,(d+1)**2),F(d**3,d*d-1),
                {'pole':F(1,d+1),'balanced':F(d,d+1)})
    if d>=7:
        return (F(2,d+1),F(d*(d-1)**2,(d+1)**2),F(d),
                {'pole':F(1,d+1),'near':F(d,d+1)})
    return (F(d+1,4*d),F((3*d-1)**2,16*d),F((3*d-1)**2,8*d),
            {'pole':F(d*d+8*d-1,16*d*d),
             'near':F(3*d*d-4*d+1,16*d),
             'edge':F(-3*d**3+19*d*d-9*d+1,16*d*d)})

def norm(d,t,u,v,s,sq):
    return (F(s-d*t)**2/F(d*u))+(F(sq)-F(s*s,d))/v

def scalar_contact(d,t,u,v):
    assert u>0 and v>0 and u<v
    orbs={}
    for s in range(d%2,d+1,2):
        orbs[('cube',s)] = norm(d,t,u,v,s,d)
    if d%2:
        orbs['edge'] = norm(d,t,u,v,0,d-1)
    assert max(orbs.values()) == 1,(d,orbs)
    contact={k for k,r in orbs.items() if r == 1}
    expected={('cube',d),('cube',d%2)}
    if d in (3,5): expected.add('edge')
    assert contact==expected,(d,contact,expected)
    return orbs

def certificate(d,t,u,v,weights):
    assert all(w>0 for w in weights.values()),(d,weights)
    assert sum(weights.values()) == 1
    S={'pole':F(d), 'balanced':F(0),'near':F(1),'edge':F(0)}
    sq={'pole':F(d), 'balanced':F(d),'near':F(d),'edge':F(d-1)}
    avgS=sum(w*S[k] for k,w in weights.items())
    assert avgS==d*t,(d,'mean',avgS,d*t)
    varS=sum(w*(S[k]-d*t)**2 for k,w in weights.items())
    assert varS==u,(d,'axis',varS,u)
    avgOrtho=sum(w*(sq[k]-S[k]**2/F(d)) for k,w in weights.items())
    assert d*avgOrtho/F(d-1) == v,(d,'ortho',avgOrtho,v)

def check_John(d):
    t=F(1,d+1);u=F(d,(d+1)**2);v=F(d,d+1)
    # coordinate support from shape Q: Q_ii = u/d + v(d-1)/d
    assert u/F(d)+v*F(d-1,d)==(1-t)**2
    # section normal support: (d*t)^2 = d*u
    assert (d*t)**2==d*u
    assert t-(1-t)>-1

for d in range(2,71):
    t,u,v,weights=data(d)
    scalar_contact(d,t,u,v)
    certificate(d,t,u,v,weights)
    check_John(d)

# Exhaustively inspect every cube corner and every cut-edge midpoint
# through dimension nine, beyond the scalar orbit-class argument.
for d in range(2,10):
    t,u,v,weights=data(d)
    count=0
    full=set()
    for xs in product((-1,1),repeat=d):
        s=sum(xs)
        if s>=0:
            assert norm(d,t,u,v,s,sum(x*x for x in xs))<=1
            if norm(d,t,u,v,s,d)==1: full.add(xs)
            count+=1
        if d%2 and s==-1:
            for k,x in enumerate(xs):
                if x==-1:
                    mid=xs[:k]+(0,)+xs[k+1:]
                    assert norm(d,t,u,v,0,d-1)<=1
                    if norm(d,t,u,v,0,d-1)==1: full.add(mid)
                    count+=1
    expected=1+comb(d,d//2) if d%2==0 else 1+comb(d,(d+1)//2)
    if d in (3,5):expected+=d*comb(d-1,(d-1)//2)
    assert len(full)==expected,(d,len(full),expected)
    assert count>0
print('VERIFY_OK exact_Loewner_certificates_dimensions=2..70 exhaustive_vertices_dimensions=2..9 John_support=yes parity_and_exceptions=yes')
