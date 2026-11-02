import numpy as np,math

def width(t,R,r,h):
 s=np.sqrt(np.maximum(0,1-np.asarray(t)**2));return np.maximum(2*R*s,(R+r)*s+h*np.asarray(t))
def cdf(z,R,r,h):
 D=R-r; S=R+r; theta0=math.atan2(D,h);t0=math.sin(theta0);L=math.hypot(S,h);alpha=math.atan2(h,S)
 w0=2*R*math.cos(theta0)
 if z<w0:A=0
 elif z>=2*R:A=t0
 else:A=t0-math.sqrt(max(0,1-(z/(2*R))**2))
 if z>=L:B=1-t0
 elif z<=0:B=0
 else:
  delta=math.acos(z/L)
  left=max(0,math.sin(alpha-delta)-t0)
  right=0 if alpha+delta>=math.pi/2 else max(0,1-math.sin(max(theta0,alpha+delta)))
  B=left+right
 return A+B

if __name__=='__main__':
 rng=np.random.default_rng(93251)
 maxerr=0
 for R,r,h in [(3.,1.,2.),(3.,1.,2.9),(3.,1.,3.4),(3.,1.,4.7),(3.,1.,6),(1.1,1.,.02),(1.1,1.,4),(2,0.1,3),(2,1.999,1)]:
  t=np.linspace(0,1,300001);v=width(t,R,r,h)
  z0=min(v);z1=max(v)
  errs=[]
  for z in np.linspace(z0-0.0001,z1+0.0001,150):
   a=cdf(z,R,r,h); b=np.mean(v<=z)
   errs.append(abs(a-b))
  e=max(errs);maxerr=max(maxerr,e)
  D=R-r;h2=h*h
  print('params',R,r,h,'three thresholds',D*(R+r),D*(3*R+r),(R+r)*(3*R-r),'min,max',z0,z1,'err',e)
  assert e<0.00002
  expected_min=min(h,2*R*h/math.hypot(h,D))
  expected_max=max(2*R,math.hypot(h,R+r))
  expected_mean=math.pi*(R+r)/4+h/2+D*math.atan(D/h)/2
  assert abs(min(v)-expected_min)<2e-5
  assert abs(max(v)-expected_max)<2e-5
  assert abs(float(np.trapz(v,t))-expected_mean)<2e-5
 print('max error',maxerr)
