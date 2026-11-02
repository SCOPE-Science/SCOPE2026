"""Independent finite-matrix tests for weighted-dark two-charger collision identities."""
import math
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
Z = np.diag([0, 1]).astype(complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SP = np.array([[0, 0], [1, 0]], dtype=complex)
SM = SP.conj().T
P = [X, Y, np.diag([1, -1]).astype(complex)]
checks = 0
rng = np.random.default_rng(20261025)

def test(g1, g2, delta, tau, c, phase, e, phi):
    global checks
    G = np.hypot(g1,g2)
    h = delta * np.kron(np.kron(I, I), Z)
    for g,k in [(g1,0),(g2,1)]:
        ops=[I,I,I]
        ops[k]=SP
        ops[2]=SM
        op=np.kron(np.kron(*ops[:2]),ops[2]);h+=g*(op+op.conj().T)
    U=expm(-1j*tau*h)
    d2=np.array([0,-g2/G,g1/G,0],complex)
    b2=np.array([0,g1/G,g2/G,0],complex)
    charger=np.sqrt(1-c)*np.array([0,0,0,1],complex)+np.exp(1j*phase)*np.sqrt(c)*d2
    battery=np.array([np.sqrt(1-e),np.exp(1j*phi)*np.sqrt(e)])
    v=U@np.kron(charger,battery)
    v=v.reshape((4,2))
    p=float(np.vdot(v[:,1],v[:,1]).real)
    Omega=np.sqrt(delta**2+4*G**2)
    q=(4*G**2/Omega**2)*np.sin(Omega*tau/2)**2
    contrast=(g1**2-g2**2)/(G*G)
    rate=q*(1-c+c*contrast**2)
    assert abs(p-(e+(1-e)*rate))<1e-10
    checks+=1
    # Exact leakage criterion tested with independent random pure charger.
    a=rng.normal(size=4)+1j*rng.normal(size=4);a/=np.linalg.norm(a)
    wa=(U@np.kron(a,np.array([0,1],complex))).reshape(4,2)
    leak=float(np.vdot(wa[:,0],wa[:,0]).real)
    assert abs(leak-q*(abs(a[0])**2+abs(np.vdot(b2,a))**2))<1e-10
    checks+=1
    # Product eigenbasis in which both charger-conditionals have equal diagonal.
    A,B=v[:,0],v[:,1]
    na=np.linalg.norm(A);nb=np.linalg.norm(B)
    if na<1e-11 or nb<1e-11: return
    da=np.outer(A/na,(A/na).conj())-np.outer(B/nb,(B/nb).conj())
    av=np.array([np.trace(da@np.kron(z,I)).real for z in P])
    bv=np.array([np.trace(da@np.kron(I,z)).real for z in P])
    T=np.array([[np.trace(da@np.kron(z,w)).real for w in P] for z in P])
    n=np.array([av[2],0,-av[0]])
    if np.linalg.norm(n)<1e-10: n=np.array([1.,0.,0.])
    n/=np.linalg.norm(n)
    assert abs(np.dot(n,av))<1e-10
    m=np.cross(bv,T.T@n)
    if np.linalg.norm(m)<1e-10:
        u=bv if np.linalg.norm(bv)>1e-10 else T.T@n
        if np.linalg.norm(u)>1e-10:
            m=np.cross(u,[1.,0.,0.])
            if np.linalg.norm(m)<1e-10:m=np.cross(u,[0.,1.,0.])
        else:m=np.array([0.,0.,1.])
    m/=np.linalg.norm(m)
    for s in [-1,1]:
        proj1=(I+s*sum(n[j]*P[j] for j in range(3)))/2
        for t in [-1,1]:
            proj2=(I+t*sum(m[j]*P[j] for j in range(3)))/2
            PP=np.kron(proj1,proj2)
            prob=(np.vdot(A,PP@A)+np.vdot(B,PP@B)).real
            if prob>1e-11:
                conditional=np.vdot(B,PP@B).real/prob
                assert abs(conditional-p)<1e-9
                checks+=1
for i in range(300):
    g1,g2=rng.uniform(0.2,2.0,2)
    if i%10==0:g2=g1
    delta=rng.uniform(-2,2)
    tau=rng.uniform(0.1,3)
    c=float(rng.uniform(0.01,.99) if i%9 else (i%2))
    e=float(rng.uniform(.01,.99))
    test(g1,g2,delta,tau,c,rng.uniform(0,2*np.pi),e,rng.uniform(0,2*np.pi))
print(f'PASS: {checks} independent numeric matrix, leakage and local-product readout assertions')
