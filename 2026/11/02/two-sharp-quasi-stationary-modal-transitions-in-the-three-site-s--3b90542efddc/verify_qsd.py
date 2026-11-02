#!/usr/bin/env python3
"""Exact symbolic checks for the three-site absorbing SIS modal classification.
Run: python verify_qsd.py; requires SymPy and NumPy."""
import sympy as S
import numpy as np
l, z = S.symbols('l z', real=True)
M = S.Matrix([
 [z-1-2*l,0,2,0,0],
 [0,z-1-l,1,1,0],
 [l,l,z-2-l,0,1],
 [0,0,0,z-2-2*l,1],
 [0,0,2*l,2*l,z-3]])
P = S.expand(M.det())
V = M.adjugate()[:,0]
F = 18*l**5-140*l**4+77*l**3+92*l**2-50*l+4
assert all(S.expand(x)==0 for x in (M*V-S.Matrix([P,0,0,0,0])))
assert S.expand(P.subs(z,2*l-1) - 8*(l-3)*(l-2)*(4*l-3))==0
for i,j,expected in [
 (0,1,8*l**9*(l-2)**2*(l+1)*(4*l-3)),
 (1,2,-16*l**8*(l-2)**3*(l+1)**3*(4*l-3)),
 (2,4,8*l**10*(l-2)*(l+1)*F)]:
 assert S.simplify(S.resultant(P,V[i]-V[j],z)-expected)==0
 assert S.factor(S.gcd(P.subs(l,2),(V[i]-V[j]).subs(l,2))) == z-3
q={l:S.Rational(3,4),z:S.Rational(1,2)}
assert P.subs(q)==0
v=list(V.subs(q)); norm=v[0]+2*v[1]+2*v[2]+v[3]+v[4]
assert [S.factor(x/norm) for x in v] == [S.Rational(1,6)]*3+[S.Rational(1,24),S.Rational(1,8)]
theta_prime = -S.diff(P,l).subs(q)/S.diff(P,z).subs(q)
assert theta_prime==-S.Rational(6,17)
for i,j,expected in [(0,1,-S.Rational(75,68)),(1,2,-S.Rational(375,68))]:
 assert S.factor((S.diff(V[i]-V[j],l)+theta_prime*S.diff(V[i]-V[j],z)).subs(q)) == expected

def variations(q):
 signs=[S.sign(f.subs(l,q)) for f in S.sturm(F,l)]
 signs=[a for a in signs if a]
 return sum(a!=b for a,b in zip(signs,signs[1:]))
assert (variations(S.Rational(7,10)),variations(S.Rational(3,4)),variations(S.Rational(5,4)))==(2,2,1)
assert F.subs(l,S.Rational(3,4))>0 and F.subs(l,S.Rational(5,4))<0
r=float(S.nroots(F)[3]);assert 1<r<1.02
# Q computed independently from the seven infectious subset states.
states=list(range(1,8));groups=[[2],[1,4],[3,6],[5],[7]]
for lam, expected_modes in [(.01,[2]),(.74,[2]),(.75,[1,2,3,4,6]),(.76,[3,6]),(.95,[3,6]),(r-1e-4,[3,6]),(r+1e-4,[7]),(1.2,[7]),(3.,[7])]:
 Q=np.zeros((7,7))
 for k,m in enumerate(states):
  for j in range(3):
   if m&(1<<j):
    n=m&~(1<<j)
    Q[k,k]-=1
    if n:Q[k,states.index(n)]+=1
   else:
    neighbors=(1,) if j!=1 else (0,2)
    rate=lam*sum(bool(m&(1<<h)) for h in neighbors)
    Q[k,k]-=rate
    if rate:Q[k,states.index(m|(1<<j))]+=rate
 ev, evec=np.linalg.eig(Q.T)
 h=int(np.argmax(ev.real));theta=-ev[h].real
 a=evec[:,h].real; a=a/np.sum(a)
 assert a.min()>0
 assert max(abs(a@Q+theta*a))<1e-10
 assert 0<theta<1
 v_num=np.array([float(x.subs({l:lam,z:theta})) for x in V],float)
 v_num/=v_num[0]+2*v_num[1]+2*v_num[2]+v_num[3]+v_num[4]
 for group,x in zip(groups,v_num):
  for s in group: assert abs(x-a[states.index(s)])<1e-8
 if abs(lam-.75)<1e-12:
  modes=[s for s in states if abs(a[states.index(s)]-max(a))<1e-8]
 else:
  modes=[s for s in states if abs(a[states.index(s)]-max(a))<1e-9]
 assert set(modes)==set(expected_modes),(lam,modes,expected_modes)
print('PASS: exact adjugate, eliminants, spurious-root exclusions, Sturm root count, crossing signs, and independent 7-state Markov-chain replay; threshold =',r)
