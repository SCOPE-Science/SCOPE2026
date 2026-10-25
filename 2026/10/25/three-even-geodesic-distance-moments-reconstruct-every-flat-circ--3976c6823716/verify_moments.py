from fractions import Fraction as F
from math import comb

def moment(x,y,j):
  return sum(F(comb(j,i))*x**i*y**(j-i)/F((2*i+1)*(j-i+1)*(2*(j-i)+1)) for i in range(j+1))

def q4(t): return (F(324)-48*t+11*t*t)/180

def q6(t): return (F(1620)-432*t+93*t*t+4*t**3)/420

def brute(x,y):
 s=moment(x,y,1);t=y/s
 assert moment(x,y,2)==s*s*q4(t)
 assert moment(x,y,3)==s**3*q6(t)
 return s,t,moment(x,y,2),moment(x,y,3)

for i in range(1,45):
 for j in range(1,45): brute(F(i,11),F(j,13))

x1,y1=F(2),F(2)
x2,y2=F(20,11),F(26,11)
a=brute(x1,y1);b=brute(x2,y2)
print('alias:',a,b)
assert a[0]==b[0]==1 and a[2]==b[2]==F(68,45)
assert a[3]==F(58,21)
assert b[3]==F(77950,27951)
assert b[3]-a[3]==F(752,27951)

for t_num in range(1,66):
 t=F(t_num,11)
 if not 0<t<6:continue
 other=F(48,11)-t
 actual=q6(t)-q6(other)
 formula=F(2)*(11*t-24)*(121*t*t-528*t+1512)/139755
 assert actual==formula,(t,actual,formula)

# Exact-rational exhaustive tests of inverse uniqueness on a nontrivial grid
shape_moments={}
for x in range(1,34):
 for y in range(1,34):
  shape=(F(x,13),F(y,17))
  triple=tuple(moment(*shape,k) for k in (1,2,3))
  assert triple not in shape_moments or shape==shape_moments[triple]
  shape_moments[triple]=shape
print('all 1089 shape triples unique; exact symbolic identities checked')
print('vertex Q4:',q4(F(24,11)),q4(F(0)),q4(F(48,11)),q4(F(6)))
