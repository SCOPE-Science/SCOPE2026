import sys; sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1321/output/artifacts')
import numpy as np
from core import angles_to_qp,wdens
def exact_rhs(s):
    th1,th2,w1,w2=s; g=9.81; d=th1-th2; c=np.cos(d); sd=np.sin(d)
    M=np.array([[2.0,c],[c,1.0]])
    rhs=np.array([-2*g*np.sin(th1)-sd*w2*w2,-g*np.sin(th2)+sd*w1*w1])
    return np.array([w1,w2,*np.linalg.solve(M,rhs)])
def rk4(s,dt):
    k1=exact_rhs(s);k2=exact_rhs(s+0.5*dt*k1);k3=exact_rhs(s+0.5*dt*k2);k4=exact_rhs(s+dt*k3)
    return s+dt/6*(k1+2*k2+2*k3+k4)
def mean_w(pt,T=10.0,dt=0.002):
    s=np.array(pt,float); n=int(round(T/dt)); acc=0.0
    for i in range(n):
        q,p=angles_to_qp(s[0],s[1],s[2],s[3]); acc+=wdens(q,p); s=rk4(s,dt)
    return acc/n
A=(0.840,0.842,1.918,1.782)
pts=[A,(A[0]+0.03,A[1],A[2],A[3]),(A[0],A[1]-0.03,A[2],A[3]),(A[0],A[1],A[2]+0.06,A[3]),(A[0],A[1],A[2],A[3]-0.06)]
for dt in [0.004,0.002]:
    for pt in pts:
        m=mean_w(pt,dt=dt)
        print("dt=%.3f pt=(%.3f,%.3f,%.3f,%.3f) mean=%.1f I=%.0f"%(dt,pt[0],pt[1],pt[2],pt[3],m,10*m))
