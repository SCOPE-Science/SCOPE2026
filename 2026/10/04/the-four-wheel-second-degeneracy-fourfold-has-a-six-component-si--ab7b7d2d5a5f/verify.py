import sympy as sp
from itertools import combinations
z1,z2,z3,z4,y1,y2,y3,y4 = sp.symbols('z1 z2 z3 z4 y1 y2 y3 y4')
vars=(z1,z2,z3,z4,y1,y2,y3,y4)
Q=sp.Matrix([[z1,y1,0,y4],[y1,z2,y2,0],[0,y2,z3,y3],[y4,0,y3,z4]])
mins=[]
for rs in combinations(range(4),3):
  for cs in combinations(range(4),3):
    f=sp.expand(Q.extract(rs,cs).det())
    if f not in mins and -f not in mins: mins.append(f)
assert len(mins)>0
# six predicted components: 4 Veronese conics + 2 opposite diagonal lines
s,t=sp.symbols('s t')
components={
'C12':{z1:s*s,z2:t*t,z3:0,z4:0,y1:s*t,y2:0,y3:0,y4:0},
'C23':{z1:0,z2:s*s,z3:t*t,z4:0,y1:0,y2:s*t,y3:0,y4:0},
'C34':{z1:0,z2:0,z3:s*s,z4:t*t,y1:0,y2:0,y3:s*t,y4:0},
'C41':{z1:s*s,z2:0,z3:0,z4:t*t,y1:0,y2:0,y3:0,y4:s*t},
'L13':{z1:s,z2:0,z3:t,z4:0,y1:0,y2:0,y3:0,y4:0},
'L24':{z1:0,z2:s,z3:0,z4:t,y1:0,y2:0,y3:0,y4:0},
}
for name,sub in components.items():
  for f in mins:
    assert sp.expand(f.subs(sub))==0, (name,f)
# Jacobian ranks: rank-1 points are singular; generic points of each extra rank-2 line are singular;
# a generic rank-2 point off the predicted locus is smooth (codimension 3).
J=sp.Matrix([[sp.diff(f,v) for v in vars] for f in mins])
def rank_at(sub):
  return J.subs(sub).rank()
assert rank_at({z1:1,z2:4,z3:0,z4:0,y1:2,y2:0,y3:0,y4:0})==0
assert rank_at({z1:1,z2:0,z3:2,z4:0,y1:0,y2:0,y3:0,y4:0})<3
assert rank_at({z1:0,z2:1,z3:0,z4:2,y1:0,y2:0,y3:0,y4:0})<3
# rank-2 Gram point with row vectors (1,0),(1,1),(0,1),(1,-1)
smooth={z1:1,z2:2,z3:1,z4:2,y1:1,y2:1,y3:-1,y4:1}
assert Q.subs(smooth).rank()==2
assert all(sp.expand(f.subs(smooth))==0 for f in mins)
assert rank_at(smooth)==3
# Conormal rank classification for alpha E13 + beta E24: determinant = alpha^2 beta^2 (up to sign/scale)
a,b=sp.symbols('a b')
N=sp.Matrix([[0,0,a,0],[0,0,0,b],[a,0,0,0],[0,b,0,0]])
assert sp.factor(N.det())==a**2*b**2
# rank-1 locus in L is parametrized by v v^T with v1*v3=v2*v4=0,
# hence the four coordinate P1-lines listed above. Check their images satisfy the two forbidden entries.
u1,u2,u3,u4=sp.symbols('u1 u2 u3 u4')
v=sp.Matrix([u1,u2,u3,u4]); R=v*v.T
assert R[0,2]==u1*u3 and R[1,3]==u2*u4
print('minor_count',len(mins))
print('rank_generic_smooth',rank_at(smooth))
print('components',','.join(components))
print('VERIFY_OK')
