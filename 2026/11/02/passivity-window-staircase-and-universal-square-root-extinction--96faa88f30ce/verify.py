#!/usr/bin/env python3
"""Numerical and exact-identity checks for lossy two-qubit-battery passivity windows.
Requires numpy and scipy. The universal result rests on the written proof.
"""
import math
import cmath
import numpy as np
from scipy.linalg import expm, eigvalsh
from scipy.optimize import brentq

CHECKS = 0

def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1

def close(a, b, atol=1e-10, rtol=3e-10):
    return abs(a-b) <= atol + rtol*max(abs(a),abs(b))

def transfer(t, J, gamma):
    z = J*J-(gamma/4)**2
    if abs(z)<1e-12*J*J:
        return J*t*math.exp(-gamma*t/4)
    if z>0:
        G=math.sqrt(z)
        return (J/G)*math.exp(-gamma*t/4)*math.sin(G*t)
    H=math.sqrt(-z)
    return (J/H)*math.exp(-gamma*t/4)*math.sinh(H*t)

def theoretical_ergotropy(t, J, gamma, p, omega):
    u = transfer(t,J,gamma)**2
    det = p*p*u*(1-u)
    return omega*(p*u-(1-math.sqrt(max(0,1-4*det)))/2)

def GKLS_ergotropy(t, J, gamma, p, omega):
    low=np.array([[0,1],[0,0]],dtype=complex)
    Id=np.eye(2,dtype=complex)
    a=np.kron(low,Id)
    b=np.kron(Id,low)
    na=a.conj().T@a
    nb=b.conj().T@b
    H=omega*(na+nb)+J*(a.conj().T@b+b.conj().T@a)
    Id4=np.eye(4,dtype=complex)
    L=-1j*(np.kron(Id4,H)-np.kron(H.T,Id4))
    L+=gamma*(np.kron(a.conj(),a)-.5*np.kron(Id4,na)-.5*np.kron(na.T,Id4))
    psi_a=np.array([math.sqrt(1-p),cmath.exp(.27j)*math.sqrt(p)])
    psi=np.kron(psi_a,np.array([1,0]))
    R=np.outer(psi,psi.conj())
    rt=(expm(t*L)@R.reshape(-1,order='F')).reshape((4,4),order='F')
    rb=np.array([[rt[0,0]+rt[2,2],rt[0,1]+rt[2,3]],
                 [rt[1,0]+rt[3,2],rt[1,1]+rt[3,3]]])
    check(close(np.trace(rt),1,1e-10),"trace")
    check(np.min(eigvalsh(rb))>=-1e-10,"positivity")
    computed=omega*(rb[1,1].real-eigvalsh(rb)[0])
    return computed,rb

def F(k,x):
    return 2*x/math.sqrt(1-x*x)*(math.acos(x)+k*math.pi)

def critical(k):
    lo,hi=0.0,.999999999
    for _ in range(100):
        mid=(lo+hi)/2
        if F(k,mid)<math.log(2): lo=mid
        else: hi=mid
    return (lo+hi)/2

def count(x):
    if x==0: return math.inf
    if x>=1: return 0
    A=2*math.pi*x/math.sqrt(1-x*x)
    return max(0,math.ceil((math.log(2)-F(0,x))/A))

def peak(k,x,J):
    G=J*math.sqrt(1-x*x)
    a=math.acos(x)
    t=(a+k*math.pi)/G
    return t,math.exp(-F(k,x))

def run():
    for J in [.72,1.,1.63]:
      for gammaJ in [0.,.04,.2,.45,.85,1.01,1.3,2.8,4.,4.8,7.5]:
       for p in [0.,.13,.5,.92,1.]:
        for tJ in [.03,.34,1.1,2.0,3.2]:
          t=tJ/J
          erg,rb=GKLS_ergotropy(t,J,gammaJ*J,p,2.1)
          ana=theoretical_ergotropy(t,J,gammaJ*J,p,2.1)
          check(close(erg,ana,1.8e-10,8e-10),f'GKLS analytic mismatch J={J}, gamma/J={gammaJ},p={p},tJ={tJ}: {erg}, {ana}')
          u=transfer(t,J,gammaJ*J)**2
          check(close(rb[1,1].real,p*u,3e-10),'battery occupation')
          check(close(abs(rb[0,1])**2,p*(1-p)*u,3e-10),'battery coherence')
    for k in range(15):
      x=critical(k)
      check(close(F(k,x),math.log(2),5e-14),'root')
      if k: check(x<critical(k-1),'ordered threshold')
      for frac in [.92,.985,.999]:
        y=x*frac
        t,u=peak(k,y,1.0)
        check(u>.5,'active peak')
        check(theoretical_ergotropy(t,1.,4*y,1.,1.)>.0,'ergotropy peak')
        z=x+(1-x)*(1-frac)
        tz,uz=peak(k,z,1.0)
        check(uz<.5,'passive peak beyond root')
    for x in [.005,.015,.04,.055,.075,.095,.16,.24,.255,.257,.3,.8,.999]:
      N=count(x)
      peaks=[peak(k,x,1)[1] for k in range(max(8,N+4))]
      check(sum(u>0.5 for u in peaks)==N,'exact window count')
      check(all(F(k,x)<F(k+1,x) for k in range(len(peaks)-1)),'peak decay in log coordinates')
    for k in [0,1,3,8]:
      xk=critical(k)
      # Symmetric local curvature and onset-width asymptotics.
      for delta in [1e-4,1e-5,1e-6]:
        x=xk-delta
        J=1.0
        t,u=peak(k,x,J)
        A=2*u
        width_left, width_right=0.,1.0
        def h(z): return math.log(2*transfer(t+z,J,4*x*J)**2)
        while h(width_right)>0: width_right*=2
        for _ in range(80):
          mid=(width_left+width_right)/2
          if h(mid)>0: width_left=mid
          else: width_right=mid
        rp=(width_left+width_right)/2
        width_left,width_right=0.,1.0
        while h(-width_right)>0: width_right*=2
        for _ in range(80):
          mid=(width_left+width_right)/2
          if h(-mid)>0: width_left=mid
          else: width_right=mid
        rm=(width_left+width_right)/2
        # log-transmission curvature exactly -2 J^2 at a lobe top.
        hh=1e-4
        curv=(math.log(transfer(t+hh,J,4*x*J)**2)+math.log(transfer(t-hh,J,4*x*J)**2)-2*math.log(u))/(hh*hh)
        check(close(curv,-2*J*J,3e-7),'universal peak curvature')
        der=(F(k,xk+1e-7)-F(k,xk-1e-7))/2e-7
        asym=2*math.sqrt(der*delta)/J
        check(abs((rm+rp)/asym-1)<.042,'square root width ratio')
    for k in [20,50,100,250]:
      x=critical(k)
      asym=math.log(2)/(math.pi*(2*k+1))
      check(abs(x/asym-1)<.003,'large lobe threshold law')
    # The global positive-ergotropy time budget: integrate actual threshold-root intervals.
    C=4*0.91596559417721901505460351493238411/math.pi-math.log(2)
    for x in [.008,.004,.002,.001,.0005]:
      gamma=4*x
      G=math.sqrt(1-x*x)
      duration=0.
      k=0
      while F(k,x)<math.log(2):
        a=k*math.pi/G
        b=(k+1)*math.pi/G
        top=(math.acos(x)+k*math.pi)/G
        fun=lambda t: (math.exp(-gamma*t/2)*math.sin(G*t)**2/G**2)-.5
        left=brentq(fun,a,top)
        right=brentq(fun,top,b)
        duration+=right-left
        k+=1
      check(abs(gamma*duration-C)<.002, 'universal Catalan total active-time budget')
    print(f'PASS: {CHECKS} exact-identity/numerical checks, independent GKLS comparison and threshold tests')
    for k in [0,1,2,3]:
      print('critical k,x,gamma/J:',k,'%.12f'%critical(k),'%.12f'%(4*critical(k)))

if __name__=='__main__': run()
