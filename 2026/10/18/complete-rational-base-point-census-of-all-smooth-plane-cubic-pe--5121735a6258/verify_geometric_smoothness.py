#!/usr/bin/env python3
"""Independent exact Groebner verification for all cubic projective orbit representatives."""
import re, pathlib
from sympy import symbols, groebner, S
X,Y,Z=symbols('X Y Z')
M=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
p=pathlib.Path(__file__).with_name('smooth_cubic_pencils_f3_v2.err')
reps=[(int(a),int(b),int(c)) for a,b,c in re.findall(r'all_orbit \d+ rep=(\d+) size=(\d+) smooth=(\d+)',p.read_text())]
assert len(reps)==25
counts={0:0,1:0}
for rep,size,expected in reps:
 digs=[];t=rep
 for k in range(10):digs.append(t%3);t//=3
 F=sum(c*X**i*Y**j*Z**k for c,(i,j,k) in zip(digs,M))
 got=True
 for sub,vs in [({X:1},[Y,Z]),({Y:1},[X,Z]),({Z:1},[X,Y])]:
  f=F.subs(sub)
  g=groebner([f,f.diff(vs[0]),f.diff(vs[1])],*vs,modulus=3)
  unit=(g.reduce(S.One)[1]==0)
  if not unit:got=False
 assert got==bool(expected), (rep,expected,got)
 counts[expected]+=size
print('verified_orbits',len(reps),'smooth_forms',counts[1],'singular_forms',counts[0])
print('projective_forms_total',sum(counts.values()))
