import numpy as np

X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)

def kronpow(A,n):
    R=np.array([[1]],dtype=complex)
    for _ in range(n):
        R=np.kron(R,A)
    return R

def dist_l1_ball(c):
    a=np.abs(np.asarray(c,dtype=float))
    if a.sum()<=1+1e-14:
        return 0.0
    lo,hi=0.0,float(a.max())
    for _ in range(100):
        tau=(lo+hi)/2
        s=np.maximum(a-tau,0).sum()
        if s>1:
            lo=tau
        else:
            hi=tau
    tau=(lo+hi)/2
    return float(np.linalg.norm(np.minimum(a,tau)))

for n in (3,5,7):
    P=[kronpow(A,n) for A in (X,Y,Z)]
    for i in range(3):
        for j in range(i+1,3):
            assert np.linalg.norm(P[i]@P[j]+P[j]@P[i])<1e-9
    for w in ([1.0,2.0,-0.5],[0.3,-0.9,0.7],[-1.0,-1.0,-1.0]):
        B=sum(wi*Pi for wi,Pi in zip(w,P))
        op=max(abs(np.linalg.eigvalsh(B)))
        assert abs(op-np.linalg.norm(w))<1e-9

for a in (0.55,0.60,1/np.sqrt(2)):
    c=np.array([a,a,0.0])
    d=dist_l1_ball(c)
    expected=(2*a-1)/np.sqrt(2)
    assert abs(d-expected)<1e-10
    optimized=0.5*d*d
    equal=(2*a-1)**2/6
    assert abs(optimized-(2*a-1)**2/4)<1e-10
    assert optimized>equal

# Representative soft-threshold checks.
assert dist_l1_ball([0.2,0.3,0.4])==0.0
c=np.array([0.7,0.6,0.2])
d=dist_l1_ball(c)
# Projection threshold is 1/6, so all three residual coordinates equal 1/6.
assert abs(d-np.sqrt(3)/6)<1e-10
print('VERIFY_OK')
