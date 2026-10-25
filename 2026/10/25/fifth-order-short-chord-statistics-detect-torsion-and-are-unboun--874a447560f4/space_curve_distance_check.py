"""Independent numerical checks for the short-chord expansion of smooth embedded loops.
Scientific computation only. Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.optimize import brentq


def clifford_loop(a=1.0,b=0.6,m=2,n=3):
    speed=math.sqrt(a*a*m*m+b*b*n*n)
    L=2*math.pi*speed
    k2=(a*a*m**4+b*b*n**4)/speed**4
    norm_T2_sq=(a*a*m**6+b*b*n**6)/speed**6
    c3=k2/(12*L)
    c5=(35*k2*k2-8*norm_T2_sq)/(2880*L)
    def chord(u):
        return math.sqrt(4*a*a*math.sin(m*u/(2*speed))**2+
                         4*b*b*math.sin(n*u/(2*speed))**2)
    print('CLlFFORD', 'L',L,'kappa2',k2,'normal_twist_sq',norm_T2_sq-k2*k2,
          'c3',c3,'c5',c5)
    for radius in [0.5,0.3,0.2,0.12]:
        root=brentq(lambda u:chord(u)-radius, 0.,1.)
        F=2*root/L
        rem=(F-2*radius/L-c3*radius**3)/radius**5
        print(f'  r={radius:.3f}, r^5 quotient={rem:.12g}, expected={c5:.12g}, error={rem-c5:+.3g}')


def wavy_loop(k,N=65536):
    # Gamma=(cos t,sin t,k^{-5/2}sin(kt)), 0<=t<2pi.
    t=2*math.pi*np.arange(N)/N
    a=k**(-2.5)
    s,c=np.sin(t),np.cos(t)
    sk,ck=np.sin(k*t),np.cos(k*t)
    P=np.column_stack([-s,c,a*k*ck])
    Q=np.column_stack([-c,-s,-a*k*k*sk])
    R=np.column_stack([s,-c,-a*k**3*ck])
    v=np.linalg.norm(P,axis=1)
    pv=np.einsum('ij,ij->i',P,Q)
    vt=pv/v
    vtt=(np.einsum('ij,ij->i',Q,Q)+np.einsum('ij,ij->i',P,R)-vt**2)/v
    T1=Q/v[:,None]**2-P*(vt/v**3)[:,None]
    T2=R/v[:,None]**3 -3*Q*(vt/v**4)[:,None]+P*((3*vt**2/v**5-vtt/v**4))[:,None]
    L=2*math.pi*v.mean()
    I4=2*math.pi*np.mean(np.sum(T1*T1,axis=1)**2*v)
    I2=2*math.pi*np.mean(np.sum(T2*T2,axis=1)*v)
    c5=(35*I4-8*I2)/(2880*L*L)
    return L,I4,I2,c5

if __name__=='__main__':
    clifford_loop()
    for m in [8,16,32,64,128,256]:
        L,I4,I2,c5=wavy_loop(m)
        print(f'WAVY m={m:3d} L={L:.10f}, int_k4={I4:.9f}, int_T2_sq={I2:.7f}, int_T2_sq/(pi*m)={I2/(math.pi*m):.8f}, c5={c5:.9f}, c5/m={c5/m:.10f}, expected_limit={-1/(1440*math.pi):.10f}')
