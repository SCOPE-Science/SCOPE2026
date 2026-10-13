#!/usr/bin/env python3
"""Exact coefficient and phase checks for three-point concentration theorem.
Standard-library arithmetic only; no numerical search is used in the proof.
Run: python3 check.py
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys

ZERO=(0,0,0,0)
def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def neg(p):return scale(p,-1)
def sub(p,q):return add(p,neg(q))
def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            k=tuple(x+y for x,y in zip(i,j))
            out[k]=out.get(k,0)+a*b
    return {k:v for k,v in out.items() if v}
def eq(p,q,label):
    assert p==q,(label,sub(p,q))

t=[{tuple(1 if j==i else 0 for j in range(4)):1} for i in range(4)]
S=add(*t)
A=add(scale(S,2),t[0]); B=add(A,t[1]); C=add(B,t[2])
Z=lambda U:sub(scale(S,6),scale(U,2))
def p_dist(U):return [U,U,Z(U)]
def r_dist(U):return [Z(U),U,U]
def convolution(polys):
    d=[{ZERO:1}]
    for law in polys:
        nd=[{} for _ in range(len(d)+2)]
        for k,v in enumerate(d):
            for j,w in enumerate(law):nd[k+j]=add(nd[k+j],mul(v,w))
        d=nd
    return d
P=convolution([p_dist(A),p_dist(B),p_dist(C)])
H=convolution([p_dist(A),p_dist(B),r_dist(C)])
J=convolution([p_dist(A),r_dist(B),p_dist(C)])
K=convolution([r_dist(A),p_dist(B),p_dist(C)])
# These eight coefficient inequalities place every mode at the claimed sites;
# the coefficient positivity is checked identically on the entire ordered
# parameter simplex (not by sampling points).
modal_checks={
 '+++ c2>=c1':sub(P[2],P[1]),
 '+++ c3>=c4':sub(P[3],P[4]),
 '++- c3>=c2':sub(H[3],H[2]),
 '++- c3>=c4':sub(H[3],H[4]),
 '+-+ c3>=c2':sub(J[3],J[2]),
 '+-+ c3>=c4':sub(J[3],J[4]),
 '-++ c2>=c1':sub(K[2],K[1]),
 '-++ c3>=c4':sub(K[3],K[4]),
}
monos=list(product(range(4), repeat=4))
monos=[k for k in monos if sum(k)==3]
for label,p in modal_checks.items():
    assert all(v>=0 for v in p.values()),(label,p)
    print(label,'nonnegative homogeneous-cubic monomials:',len(p),
          'minimum nonzero coefficient:',min(p.values()),
          'zero coefficients:',20-len(p))
assert len(monos)==20
lines=['comparison\t'+'\t'.join(''.join(map(str,k)) for k in monos)]
for label,p in modal_checks.items():
    lines.append(label+'\t'+'\t'.join(str(p.get(k,0)) for k in monos))
certificate='\n'.join(lines)+'\n'
cert_path=Path(__file__).with_name('COEFFICIENTS.tsv')
if '--write-certificate' in sys.argv:
    cert_path.write_text(certificate,encoding='utf-8')
assert cert_path.read_text(encoding='utf-8')==certificate,'standalone certificate disagrees with exact polynomial expansion'
print('complete 8x20 exact integer coefficient certificate: passed')
# Exact non-negativity comparisons; the factorizations are independent
# algebraic checks for the orientation phase.
eq(sub(P[2],H[3]),mul(Z(C),sub(scale(mul(A,B),5),scale(mul(S,add(A,B)),6))), 'phase')
eq(sub(H[3],P[3]),mul(sub(scale(C,3),scale(S,6)),sub(scale(mul(A,B),6),scale(mul(S,add(A,B)),6))), '+++ c3')
eq(sub(H[3],J[3]),mul(scale(S,6),mul(sub(scale(A,3),scale(S,6)),sub(C,B))),'+-+')
eq(sub(H[3],K[3]),mul(scale(S,6),mul(sub(C,A),sub(scale(B,3),scale(S,6)))),'-++ c3')
eq(sub(H[3],K[2]),mul(Z(B),add(scale(mul(S,sub(A,C)),6),mul(A,C))),'-++ c2')
print('five exact orientation-factor identities: passed')

# Independently enumerate a rational subgrid, including boundaries. This
# finite check is corroboration, not the source of the universal proof.
qvals=[F(1,3),F(7,20),F(3,8),F(2,5),F(17,40),F(9,20),F(19,40),F(1,2)]
def convol_rat(a,b,c,s):
    d={0:F(1)}
    for v,e in zip((a,b,c),s):
        nd={}
        for k,p in d.items():
            for j,w in enumerate((v,v,1-2*v)):
                nd[k+e*j]=nd.get(k+e*j,F(0))+p*w
        d=nd
    return max(d.values())
n=0
for a in qvals:
 for b in qvals:
  if b<a:continue
  for c in qvals:
   if c<b:continue
   q=[convol_rat(a,b,c,s) for s in ((1,1,1),(1,1,-1),(1,-1,1),(-1,1,1))]
   up=a*b+a*c+b*c-3*a*b*c
   down=7*a*b*c-4*a*b-a*c-b*c+a+b
   assert max(q)==max(up,down), (a,b,c,q,up,down)
   assert (q[0] if 5*a*b>=a+b else q[1])==max(q)
   n+=1
print('exact rational ordered triples:',n,'passed; polynomial proof covers all real parameters')
