"""Exact identities for a four-step itinerary of a piecewise-affine planar map.
Requires Python 3 and sympy. Run: python verify_left_triplet.py
"""
import sympy as S
u,v,a,b,r,p=S.symbols('u v a b r p', real=True)
L=S.Matrix([[u,1],[-a,0]])
R=S.Matrix([[v,1],[-b,0]])
e=S.Matrix([1,0]);I=S.eye(2)
M=R*L**3
D=S.factor((I-M).det()); E=S.factor((I+M).det())
K=u*v+(a-1)*(b-1)
U=u*u-(a+1)**2
assert S.expand(E-(u*u-2*a)*K+(1+a*b)*U+2*a*a+2*a*b)==0
q=I; t=S.zeros(2,1)
for A in [L,L,L,R]:
    t=A*t+e
    q=A*q
z=(I-q).inv()*t
assert S.simplify((L*z+e)[0]-(u+a+1)*K/D)==0
# Restrict to a=-r<0, b>0, v=-(1+b).
u0=(r+1)*(1-b)/(1+b)
Eb=S.expand(E.subs({a:-r,v:-(1+b)}))
Kb=S.expand(K.subs({a:-r,v:-(1+b)}))
assert S.expand(Kb-((r+1)*(1-b)-u*(1+b)))==0
assert S.expand(S.diff(Eb,u)-(-3*(1+b)*u*u-2*b*u+2*r*(u-1-b)))==0
assert S.simplify(Eb.subs(u,1-r)-2*(r-b)*(r*r-r+1))==0
assert S.simplify(Eb.subs(u,r-1)+2*(b*r**3-1))==0
pos=2*b*b*r*r+r*(1-b)**2+2
assert S.simplify(Eb.subs(u,u0)+2*(r-b)*pos/(1+b)**2)==0
# At K=0, the Schur necessary quantity E is negative in its admissible range.
Ez=S.simplify(E.subs({a:-r,v:-(r+1)*(1-b)/u}))
assert S.simplify(Ez-(-(1-r*b)*(u*u-(1-r)**2)+2*r*(b-r)))==0
print('SYMBOLIC_IDENTITIES_OK')

def example(params,word):
    uu,aa,vv,bb=map(S.Rational,params)
    matrices={'L':L.subs({u:uu,a:aa}), 'R':R.subs({v:vv,b:bb})}
    assert uu>abs(1+aa) and vv<-abs(1+bb)
    P=I;c=S.zeros(2,1)
    for w in word:
        c=matrices[w]*c+e;P=matrices[w]*P
    z=(I-P).inv()*c
    xx=[]
    for w in word:
        xx.append(z[0]);z=matrices[w]*z+e
    assert z==(I-P).inv()*c
    assert all((x<0 if w=='L' else x>0) for x,w in zip(xx,word))
    return xx,P
xs,M4=example(['9/5','-2','-7/5','1/5'],'LRRR')
assert all(abs(complex(t).real)<1 for t in M4.eigenvals())
assert all((t<0 if i<3 else t>0) for i,t in enumerate(example(['9/2','-5','-10/3','2'],'LLLR')[0]))
print('RATIONAL_ORBIT_CHECK_OK', xs)
