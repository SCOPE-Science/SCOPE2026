#!/usr/bin/env python3
"""Independent exact identities and bounded checks for height-restricted Dyck arch enumeration.
Requires Python 3 and sympy; no external data. All indices are zero-based.
"""
from collections import Counter
import itertools
import sympy as S

t,u=S.symbols('t u')
I=S.eye(3)
M0=S.Matrix([[0,1,0],[0,1,0],[u,0,0]])
M1=S.Matrix([[0,0,1],[u,0,0],[0,0,1]])
E=I
formulas={
  1:1/(1-u*t),
  2:(1-2*u*t+u*t**2)/((1-u*t)*(1-2*u*t)),
  3:(1-4*u*t+(u+4*u**2)*t**2+(u-3*u**2)*t**3)/
     ((1-u*t)*((1-2*u*t)**2-u**2*t**3))
}
for H in (1,2,3):
    E=(I-t*M0*E*M1).inv().applyfunc(S.cancel)
    gf=S.cancel((S.Matrix([[1,0,0]])*E*S.ones(3,1))[0])
    assert S.cancel(gf-formulas[H])==0, (H,gf)

# Separately construct the finite words, with no matrix method.
def dyck_words(n,h):
    def rec(w,level,ups):
        if len(w)==2*n:
            if level==0: yield w
        else:
            if ups<n and level<h: yield from rec(w+'0',level+1,ups+1)
            if level: yield from rec(w+'1',level-1,ups)
    yield from rec('',0,0)

def arch_index(w):
    state=None
    arches=0
    for ch in w:
        if state is None: state=ch
        elif state!=ch:
            arches+=1
            state=None
    return arches

# Independent direct universal-subsequence definition.
def explicit_universal_index(w):
    for k in range(len(w)//2+2):
        for tup in itertools.product('01',repeat=k):
            pos=0
            for a in tup:
                z=w.find(a,pos)
                if z<0: return k-1
                pos=z+1
    raise AssertionError('unexpected')

for H in (1,2,3):
    for n in range(0,11):
        observed=Counter(arch_index(w) for w in dyck_words(n,H))
        # Extract [t^n] of predicted rational GF via a 1D coefficient recurrence,
        # expanding u exactly (without substituting numeric values).
        gf=formulas[H]
        poly=S.Poly(S.cancel(S.together(gf)).as_numer_denom()[0],t)
        den=S.Poly(S.cancel(S.together(gf)).as_numer_denom()[1],t)
        if n==0: known=[S.Integer(1)]
        else: known=[S.Integer(1)]
        for j in range(1,n+1):
            numerator=poly.nth(j)
            coeff=S.cancel((numerator-sum(den.nth(a)*known[j-a] for a in range(1,j+1)))/den.nth(0))
            known.append(coeff)
        predicted={k:int(S.expand(known[n]).coeff(u,k)) for k in range(n+1)}
        predicted={k:v for k,v in predicted.items() if v}
        assert predicted==dict(observed), (H,n,observed,predicted)
        if n<=6:
            for word in dyck_words(n,H):
                assert arch_index(word)==explicit_universal_index(word),(n,H,word)
        if H==2 and n>=1:
            assert observed[n]==1
            if n>=2: assert observed[n-1]==2**(n-1)-1

root=(S.Integer(3)-S.sqrt(5))/2
Q=(1-2*u*t)**2-u**2*t**3
q_t=S.diff(Q,t).subs({t:root,u:1})
q_u=S.diff(Q,u).subs({t:root,u:1})
dr=S.simplify(-q_u/q_t)
ddr=S.simplify(-(S.diff(Q,u,2)+2*S.diff(Q,t,u)*dr+S.diff(Q,t,2)*dr**2).subs({t:root,u:1})/q_t)
mu=S.simplify(-dr/root)
sig2=S.simplify(mu+mu**2-ddr/root)
assert S.simplify(mu-2/S.sqrt(5))==0,(mu,dr)
assert S.simplify(sig2-(2-22*S.sqrt(5)/25))==0,(sig2,ddr)
assert sig2.evalf()>0
assert S.cancel(formulas[3].subs(u,1)-(1-2*t)/(1-3*t+t*t))==0
print('VERIFY_OK: 3 exact transfer identities; exhaustive depth 1..3 through n=10;')
print('direct subsequence definition through n=6; poles, mean and variance identities.')
print('mu=',mu,'sigma2=',sig2)
