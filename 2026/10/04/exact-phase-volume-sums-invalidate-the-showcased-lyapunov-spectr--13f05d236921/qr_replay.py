import numpy as np

a=40.0; b=2.0; c=22.0; e=0.5

def f(x):
    X,Y,Z,P=x
    return np.array([a*(Y-X), c*Y-X*Z+P, -b*Z+Y*Y, -e*(X+Y)], dtype=float)

def jac(x):
    X,Y,Z,P=x
    return np.array([[-a,a,0.0,0.0],[-Z,c,-X,1.0],[0.0,2.0*Y,-b,0.0],[-e,-e,0.0,0.0]], dtype=float)

def step(x,Q,h):
    def d(xx,QQ): return f(xx), jac(xx)@QQ
    k1x,k1q=d(x,Q)
    k2x,k2q=d(x+h*k1x/2,Q+h*k1q/2)
    k3x,k3q=d(x+h*k2x/2,Q+h*k2q/2)
    k4x,k4q=d(x+h*k3x,Q+h*k3q)
    return x+h*(k1x+2*k2x+2*k3x+k4x)/6, Q+h*(k1q+2*k2q+2*k3q+k4q)/6

h=0.002
qr_every=10
burn_steps=int(80/h)
main_steps=int(100/h)
x=np.array([1.0,1.0,1.0,1.0])
Q=np.eye(4)
for i in range(burn_steps):
    x,Q=step(x,Q,h)
    if (i+1)%qr_every==0:
        Q,_=np.linalg.qr(Q)
Q=np.eye(4)
s=np.zeros(4)
for i in range(main_steps):
    x,Q=step(x,Q,h)
    if (i+1)%qr_every==0:
        Q,R=np.linalg.qr(Q)
        s += np.log(np.abs(np.diag(R)))
le=s/100.0
print('finite_time_qr=', ' '.join(f'{v:.10f}' for v in le))
print('sum=', f'{le.sum():.10f}')
print('exact_required_sum=', c-a-b)
assert abs(le.sum()-(c-a-b)) < 5e-5
print('QR_REPLAY_OK')
