"""Direct finite-dimensional and algebraic checks for the qubit battery comparison.
Run: python verify.py; requires numpy, sympy.
"""
import math
import numpy as np
import sympy as sp

Z=np.diag([1.,-1.]).astype(complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
SM=np.array([[0,0],[1,0]],complex)
SP=SM.conj().T
I=np.eye(2,dtype=complex)

def lindblad_rho(f1,f2,omega,N,p,boson):
    k=N/p if boson else N
    Lm=f1*Z+f2*SM
    Lp=f1*Z+f2*SP
    H=omega*Z/2
    def generator(R):
        o=-1j*(H@R-R@H)
        for rate,L in ((k*(1+p)/2,Lm),(k*(1-p)/2,Lp)):
            a=L.conj().T@L
            o+=rate*(L@R@L.conj().T-(a@R+R@a)/2)
        return o
    basis=[I/2,X/2,Y/2,Z/2]
    c=generator(basis[0]); B=np.empty((3,3),float); d=np.empty(3)
    for i,S in enumerate((X,Y,Z)):
        d[i]=float(np.trace(S@c).real)
        for j in range(3):B[i,j]=float(np.trace(S@generator(basis[j+1])).real)
    r=np.linalg.solve(B,-d)
    R=(I+r[0]*X+r[1]*Y+r[2]*Z)/2
    assert np.linalg.norm(generator(R)) < 2e-10
    assert min(np.linalg.eigvalsh(R)) > -2e-12
    return r,R

def exact_bloch(f1,f2,omega,N,p,boson):
    u,v=f1*f1,f2*f2
    A=2*u+v/2; B=u+v/2
    q=(omega/N)**2*(p*p if boson else 1)
    h=A*B+q
    return np.array([p*f1*f2*A/h,p*f1*f2*math.sqrt(q)/h,-p*(A*v/2+q)/h])

def erg(r,omega):return omega*(r[2]+np.linalg.norm(r))/2

def purity(r):return (1+sum(r*r))/2

def exact_qc(f1,f2,p):
    u,v=f1*f1,f2*f2
    A=2*u+v/2; B=u+v/2
    return 2*B*v/((1+p*p)+math.sqrt((1+p*p)**2+16*p*p*B*v/A**2))

checks=0
for f1 in (0.13,0.6,1.5):
 for f2 in (0.23,0.8):
  for omega in (0.05,0.8,3.3):
   for N in (1,2,4,10):
    for p in (0.05,0.42,0.85):
     bos=[]
     for is_boson in (False,True):
      r,R=lindblad_rho(f1,f2,omega,N,p,is_boson)
      b=exact_bloch(f1,f2,omega,N,p,is_boson)
      assert np.max(np.abs(r-b)) < 5e-11, (f1,f2,omega,N,p,r,b)
      bos.append(r)
      checks+=1
     f,b=bos
     assert erg(b,omega)>erg(f,omega)+1e-13
     qc=exact_qc(f1,f2,p)
     q=(omega/N)**2
     delta=purity(b)-purity(f)
     assert delta*(qc-q)>-2e-12,(q,qc,delta)
     checks+=2

u,v,q,t=sp.symbols('u v q t', positive=True)
A=2*u+v/sp.Integer(2); B=u+v/sp.Integer(2);K=A*B;L=A*(A+v);a=A*v/2
rsq=((a+q)**2+u*v*(A*A+q))/(K+q)**2
assert sp.simplify(rsq-(1-4*u*u/(K+q)+u*u*L/(K+q)**2))==0
assert sp.simplify((4*(K+q)*(K+t*q)-L*(2*K+(1+t)*q))/(4*(K+q)*(K+t*q))-( (4*t/A**2*q*q+(1+t)*q-B*v)*A*A/(4*(K+q)*(K+t*q)) ))==0
checks+=2

# Same parameters, choose two integer cluster sizes on opposite sides.
f1=f2=1.0; omega=3.0; p=0.5
qc=exact_qc(f1,f2,p)
assert (omega/1)**2>qc and (omega/10)**2<qc
for N in (1,10):
 rf,_=lindblad_rho(f1,f2,omega,N,p,False)
 rb,_=lindblad_rho(f1,f2,omega,N,p,True)
 print(f'N={N}: critical_q={qc:.12g}, q={(omega/N)**2:.12g}, '
       f'P_bose-P_qubit={purity(rb)-purity(rf):+.12g}, '
       f'W_bose-W_qubit={erg(rb,omega)-erg(rf,omega):+.12g}')
 checks+=1
print(f'PASS {checks} checks')

# Independent symbolic certificates for the response signs and sharp thresholds.
h=K+q
R=1-4*u*u/h+u*u*L/h**2
q0=A*v/4
assert sp.simplify(sp.diff(R,q)-4*u*u*(q-q0)/h**3)==0
q2=sp.symbols('q2',positive=True)
R2=R.subs(q,q2)
step_diff=sp.factor(R2-R)
step_fact=u*u*(1/(K+q2)-1/(K+q))*(L*(1/(K+q2)+1/(K+q))-4)
assert sp.simplify(step_diff-step_fact)==0
c=sp.simplify(u*u*A*v/(K**3))
assert sp.simplify(sp.diff(R,q).subs(q,0)+c)==0
assert sp.simplify(sp.diff(R,q,2).subs(q,0))!=0
checks+=4

# Verify that the exact integer-step rule predicts one U-shaped sequence.
for f1 in (0.3,0.75,1.4):
 for f2 in (0.4,1.1):
  for p in (0.13,0.55):
   for omega in (1.2,3.1):
    u0,v0=f1*f1,f2*f2
    A0=2*u0+v0/2; B0=u0+v0/2; K0=A0*B0; L0=A0*(A0+v0)
    for boson in (False,True):
     c0=p*p if boson else 1.0
     signs=[]
     for n in range(1,20):
      qn=c0*omega*omega/n**2
      qn1=c0*omega*omega/(n+1)**2
      rho1=exact_bloch(f1,f2,omega,n,p,boson)
      rho2=exact_bloch(f1,f2,omega,n+1,p,boson)
      diff=purity(rho2)-purity(rho1)
      marker=L0/(K0+qn1)+L0/(K0+qn)-4
      assert diff*marker>=-3e-15
      signs.append(marker)
      checks+=1
     assert all(signs[j+1]>signs[j] for j in range(len(signs)-1))
     checks+=1
print('PASS all checks including symbolic response and integer-step certificates', checks)
