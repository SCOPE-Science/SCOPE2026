import math, cmath
import numpy as np

def blocks(N,r,s,theta,cut=180):
 out=[]
 for m in range(N):
  js=range(m,cut,N)
  aa=N*math.exp(-r*r)*sum(math.exp(2*j*math.log(r)-math.lgamma(j+1)) for j in js)
  bb=N*math.exp(-s*s)*sum(math.exp(2*j*math.log(s)-math.lgamma(j+1)) for j in js)
  cc=N*math.exp(-(r*r+s*s)/2)*sum(math.exp(j*math.log(r*s)-math.lgamma(j+1))*cmath.exp(1j*j*theta) for j in js)
  disc=math.hypot(aa-bb,2*abs(cc))
  out += [(aa+bb-disc)/2,(aa+bb+disc)/2]
 return sorted(out)

def direct(N,r,s,theta):
 omega=cmath.exp(2j*math.pi/N)
 nodes=[r*omega**k for k in range(N)]+[s*cmath.exp(1j*theta)*omega**k for k in range(N)]
 G=np.array([[cmath.exp(z.conjugate()*w-(abs(z)**2+abs(w)**2)/2) for w in nodes]for z in nodes],dtype=complex)
 return sorted(np.linalg.eigvalsh(G))

checks=0
for N in range(2,9):
 for r,s in [(0.45,1.1),(1.5,2.2),(2.5,2.5),(0.1,0.3)]:
  theta=math.pi/N
  opt=blocks(N,r,s,theta)
  assert abs(opt[0]-direct(N,r,s,theta)[0])<1e-10
  assert max(abs(a-b) for a,b in zip(opt,direct(N,r,s,theta)))<1e-10
  checks+=2
  for t in [0.0,0.07,0.25,0.5,0.9,1.6,2.0]:
   theta2=(t*math.pi/N)
   eig=blocks(N,r,s,theta2)
   if t!=1.0:
    assert eig[0]<opt[0]+5e-11,(N,r,s,t,eig[0],opt[0])
    assert eig[-1]>opt[-1]-5e-11
    checks+=2
print('passed checks',checks)
