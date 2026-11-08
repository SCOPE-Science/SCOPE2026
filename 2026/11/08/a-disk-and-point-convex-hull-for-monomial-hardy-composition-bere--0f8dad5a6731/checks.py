import math
from fractions import Fraction
for m in range(2,31):
 R=1/(m+1)
 theta=math.acos(1/m)
 t=complex(1/m, math.sqrt(m*m-1)/(m*(m+1)))
 assert abs(abs(t-R)-R)<1e-12
 assert abs((t.real-1)*(t.real-R)+t.imag*t.imag)<1e-12
 area=(math.pi-theta+math.sqrt(m*m-1))/(m+1)**2
 perim=2*math.sqrt((m-1)/(m+1))+2*(math.pi-theta)/(m+1)
 # formula via disk+triangle-circular-segment
 area2=math.pi*R*R+(1-t.real)*t.imag-R*R*(theta-math.sin(theta)*math.cos(theta))
 assert abs(area-area2)<1e-12
 for k in range(1,30):
  r=k/30
  c=(1-r*r)/(1-r**(2*m+2)); small=c*r**(m+1)
  alpha=c-small
  big=(1-alpha)*R
  assert 0<alpha<1 and 0<small<big and abs(c-(alpha+small))<1e-10
  assert sum(r**(2*j) for j in range(m))>=m*r**(m-1)-1e-12
  for s in [j*math.pi/31 for j in range(62)]:
   support_small=c*math.cos(s)+small
   support_outer=max(math.cos(s),R*(1+math.cos(s)))
   assert support_small<support_outer+1e-12
 print('m',m,'area',round(area,8),'perim',round(perim,8)) if m in (2,3,4,10,30) else None
print('monomial geometry diagnostics passed')
