import numpy as np
from scipy.linalg import sqrtm
from math import sqrt
I=np.eye(2,dtype=complex)
P=np.array([[1,0],[0,0]],complex)
Q=np.ones((2,2),dtype=complex)/2
H=np.array(sqrtm(I-(P+Q)/2),complex)
sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
K={-2:Q/2,-1:P/2,0:H,1:P/2,2:Q/2}
lam=.25+1/(2*sqrt(2))
a=.75
B=.5*P+2*Q
rho0=I/2

def ch(z):return sum(L@z@L.conj().T for L in K.values())
def chq(z):return sum(j*j*L@z@L.conj().T for j,L in K.items())
def tr(z):return float(np.trace(z).real)
def U(n,r):return (1-r**n)/(1-r)
def pred_x(n,x,z):return 1.25*n+1.25*(x+z)/2*U(n,a)+.75*(x-z)/2*U(n,lam)
def G(n,r):return ((n-1)-n*r+r**n)/(1-r)**2
def pred_Qvar(n):return 43*n/16+25*G(n,a)/16+9*G(n,lam)/16

# Channel eigenmodes, and exact Markov-instrument enumeration
for S,v in [(sx+sz,a),(sx-sz,lam),(sy,1/(2*sqrt(2)))]:
 assert np.allclose(ch(S),v*S,atol=1e-13)
assert np.allclose(ch(rho0),rho0,atol=1e-13)
for n in range(1,7):
 for x,z in [(0.,0.),(1.,0.),(0.,1.),(1/sqrt(2),1/sqrt(2)),(-.6,.8)]:
  state=(I+x*sx+z*sz)/2
  nodes=[(state,0,0)]
  for j in range(n):
   nodes=[(L@v@L.conj().T,X+s,V+s*s) for v,X,V in nodes for s,L in K.items()]
  mass=sum(tr(v) for v,X,V in nodes)
  ex=sum(tr(v)*X for v,X,V in nodes)
  ex2=sum(tr(v)*X*X for v,X,V in nodes)
  assert abs(mass-1)<2e-11,(n,x,z,mass)
  assert abs(ex)<2e-11,(n,x,z,ex)
  assert abs(ex2-pred_x(n,x,z))<2e-10,(n,x,z,ex2,pred_x(n,x,z))
  if x==z==0:
   eq=sum(tr(v)*V for v,X,V in nodes)
   eq2=sum(tr(v)*V*V for v,X,V in nodes)
   assert abs(eq-1.25*n)<2e-11,(n,eq)
   assert abs(eq2-eq*eq-pred_Qvar(n))<2e-10,(n,eq2-eq*eq,pred_Qvar(n))
 print('Enumerated n=',n,'paths=',5**n,'all moments pass')

for k in range(1,30):
 z=chq(rho0)
 for i in range(k-1):z=ch(z)
 co=tr(B@z)-(1.25)**2
 expect=25/32*a**(k-1)+9/32*lam**(k-1)
 assert abs(co-expect)<2e-13,(k,co,expect)
print('29 lag covariances pass')
for n in range(1,51):
 U1=U(n,a);U2=U(n,lam)
 A=np.sqrt((1.25*U1)**2+(.75*U2)**2)/sqrt(2)
 vx=np.array([(1.25*U1+.75*U2)/2,(1.25*U1-.75*U2)/2])/A
 assert abs(np.linalg.norm(vx)-1)<1e-14
 assert abs(pred_x(n,*vx)-(1.25*n+A))<5e-14
print('50 exact envelope identities pass')
asym=43/16+25/(16*(1-a))+9/(16*(1-lam))
print('theta=',lam,'quadratic variation asymptotic variance=',asym,'iid variance=',43/16,'factor=',asym/(43/16))
