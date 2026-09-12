"""Core projected-Verlet double-pendulum routines (no demo code on import)."""
import numpy as np
g = 9.81
def gradU(q): return np.array([0.0, g, 0.0, g])
def U(q): return g*(q[1]+q[3])
def H(q,p): return 0.5*np.dot(p,p)+U(q)
def constraints(q):
    x1,y1,x2,y2=q
    return np.array([x1**2+y1**2-1.0,(x2-x1)**2+(y2-y1)**2-1.0])
def jacobian(q):
    x1,y1,x2,y2=q
    G=np.zeros((2,4))
    G[0,0]=2*x1;G[0,1]=2*y1
    G[1,0]=-2*(x2-x1);G[1,1]=-2*(y2-y1);G[1,2]=2*(x2-x1);G[1,3]=2*(y2-y1)
    return G
def angles_to_qp(th1,th2,w1,w2):
    q1=np.array([np.sin(th1),-np.cos(th1)]); d2=np.array([np.sin(th2),-np.cos(th2)])
    q2=q1+d2; q=np.array([q1[0],q1[1],q2[0],q2[1]])
    dq1=np.array([np.cos(th1),np.sin(th1)])*w1; dd2=np.array([np.cos(th2),np.sin(th2)])*w2
    v1=dq1; v2=dq1+dd2
    return q,np.array([v1[0],v1[1],v2[0],v2[1]])
def project_position(qstar,tol=1e-14,maxit=20):
    q=qstar.copy(); mu=np.zeros(2)
    for it in range(maxit):
        G=jacobian(q); gc=constraints(q)
        r1=q-qstar+G.T@mu; r2=gc
        if np.linalg.norm(r1)<tol and np.linalg.norm(r2)<tol: break
        m1,m2=mu
        A=np.array([[2*m1+2*m2,0,-2*m2,0],[0,2*m1+2*m2,0,-2*m2],[-2*m2,0,2*m2,0],[0,-2*m2,0,2*m2]])
        J=np.zeros((6,6)); J[:4,:4]=np.eye(4)+A; J[:4,4:]=G.T; J[4:,:4]=G
        d=np.linalg.solve(J,-np.concatenate([r1,r2]))
        q=q+d[:4]; mu=mu+d[4:]
    return q,mu
def project_momentum(pstar,q):
    G=jacobian(q); A=G@G.T; rhs=G@pstar
    nu=np.linalg.solve(A,rhs)
    return pstar-G.T@nu,nu
def step(q,p,h):
    gr=gradU(q); ph=p-0.5*h*gr; qstar=q+h*ph
    ps=ph-0.5*h*gradU(qstar)
    qn,mu=project_position(qstar); pn,nu=project_momentum(ps,qn)
    return qn,pn,mu,nu
def wdens(q,p):
    GG=jacobian(q); Si=np.linalg.inv(GG@GG.T)
    v1=p[:2]; dv=p[2:]-p[:2]
    e=np.array([2*np.dot(v1,v1),2*np.dot(dv,dv)])
    Ga=GG@gradU(q)
    return float(-0.5*e@Si@(e-Ga))
