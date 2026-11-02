"""Exact checks for numerical cases, node support parity and conic-grid lemma."""
from itertools import combinations_with_replacement, product
from fractions import Fraction
import sympy as S

# Nearly-free degree 9 has r=4, tau=47, two conics and five lines.
profiles=[]
for n3 in range(35):
 for t in range(35):
  n2=34-2*t-3*n3
  if n2<0 or n2+3*t+4*n3!=47: continue
  if 16+n2+Fraction(3*n3,4)<5+Fraction(5*t,2):continue
  profiles.append((n2,t,n3))
assert profiles == [(2,7,6),(1,6,7),(0,5,8)] or sorted(profiles)==sorted([(2,7,6),(1,6,7),(0,5,8)])

# Nodes may involve two lines, one line and one conic, or two conics.
L=range(5)
node_types=[('LL',i,j) for i in L for j in L if i<j]
node_types += [('LQ',i,q) for i in L for q in range(2)]
node_types += [('QQ',0,1)]
for n in (1,2):
 allowed=[]
 for multi in combinations_with_replacement(node_types,n):
  if any(multi.count(e)>1 and e[0]=='LL' for e in multi):continue
  parity=[0]*5
  for typ,a,b in multi:
   if typ=='LL':parity[a]^=1;parity[b]^=1
   elif typ=='LQ':parity[a]^=1
  if not any(parity):allowed.append(multi)
 assert all(all(e[0]!='LL' for e in m) for m in allowed)
 if n==1:assert all(m[0][0]=='QQ' for m in allowed)
 if n==2:assert all((all(e[0]=='QQ' for e in m) or
  (all(e[0]=='LQ' for e in m) and m[0][1]==m[1][1])) for m in allowed)

# When all four remaining line-line pairs are LLQ triples, they form K_2,2.
edges=((1,3),(1,4),(2,3),(2,4))
valid=[]
for colors in product((0,1),repeat=4):
 if all(sum(colors[j]==color for j,e in enumerate(edges) if i in e)%2==0
        for color in (0,1) for i in (1,2,3,4)):
  valid.append(colors)
assert valid==[(0,0,0,0),(1,1,1,1)]

# Four corners force any conic to be A*X*(X-Z)+B*Y*(Y-Z).
X,Y,Z,A,B,C,D,E,F=S.symbols('X Y Z A B C D E F')
conic=A*X**2+B*Y**2+C*Z**2+D*X*Y+E*X*Z+F*Y*Z
corners=[(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
conditions=[conic.subs({X:x,Y:y,Z:z}) for x,y,z in corners]
sol=S.solve(conditions,[C,D,E,F],dict=True)
assert sol==[{C:0,D:0,E:-A,F:-B}]
assert S.expand(conic.subs(sol[0])-(A*X*(X-Z)+B*Y*(Y-Z))) == 0
# Restriction to infinity has discriminant -4*A*B for the univariate Y/X.
assert S.discriminant(A+B*Y**2,Y)==-4*A*B
print('DEGREE9_TWO_CONIC_FIVE_LINE_NUMERICS_PARITY_GRID_OK')
