import math

def probability(t):
 z=math.hypot(1.0,t)
 A=math.atan(t/z)
 B=math.atan(1.0/(math.sqrt(2.0)*t))
 L=2.0+t+2*z+math.sqrt(2.0)
 D=2*z*A+math.sqrt(2.0)*B
 return 4.0/(1+2*D/(math.pi*L))-3.0

def integral_section_probability(t,N=30000):
 vertices=((0.,0.,0.),(1.,0.,0.),(0.,1.,0.),(0.,0.,t))
 golden=math.pi*(3.-math.sqrt(5.))
 width_integral=edge_integral=0.
 for i in range(N):
  zz=1-2*(i+.5)/N; theta=golden*i
  rr=math.sqrt(max(0,1-zz*zz));ux=rr*math.cos(theta);uy=rr*math.sin(theta)
  d=(0.,ux,uy,zz*t)
  width_integral+=max(d)-min(d)
  edge_integral+=sum(abs(d[j]-d[k]) for j in range(4) for k in range(j+1,4))
 return edge_integral/width_integral-3.

for t in (0.1,0.5,1.0,2.0,7.0):
 analytical=probability(t)
 numerical=integral_section_probability(t)
 print(f't={t:g} analytical={analytical:.12f} numeric={numerical:.12f} error={abs(analytical-numerical):.2g}')
 assert abs(analytical-numerical)<0.0005
for k in range(-80,80):
 t=math.exp(k/20)
 h=0.000005*t
 dp=(probability(t+h)-probability(t-h))/(2*h)
 assert (dp>0 if t<1 else dp<0) if t!=1 else True
expected=4.0/(1.0+(2.0/math.pi)*(2-math.sqrt(2))*math.atan(1/math.sqrt(2)))-3
assert abs(probability(1)-expected)<1e-13
assert abs(probability(1e-9)-(3-2*math.sqrt(2)))<1e-7
assert 0<probability(1e9)<1e-7
print('TETRA_CROFTON_PROFILE_CHECK_OK')
