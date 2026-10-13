import math
import numpy as np

def imtlg_weights(grads):
    G=np.asarray(grads,dtype=float)
    T,d=G.shape
    norms=np.linalg.norm(G,axis=1)
    assert np.all(norms>0)
    Udir=G/norms[:,None]
    D=np.vstack([G[0]-G[j] for j in range(1,T)])
    Ud=np.vstack([Udir[0]-Udir[j] for j in range(1,T)])
    M=D@Ud.T
    rhs=G[0]@Ud.T
    rest=rhs@np.linalg.inv(M)
    a=np.empty(T)
    a[1:]=rest
    a[0]=1.0-rest.sum()
    return a,M,Udir

r=1.0/math.sqrt(2.0)
U=np.array([
    [r,0.0,r],
    [0.0,r,r],
    [0.5,0.5,r],
])
assert abs(np.linalg.det(U))>1e-4
a,M,dirs=imtlg_weights(U)
expected=np.array([1.0+r,1.0+r,-1.0-math.sqrt(2.0)])
assert np.max(np.abs(a-expected))<2e-12
assert abs(a.sum()-1.0)<2e-12
g=a@U
target=np.array([0.0,0.0,r])
assert np.max(np.abs(g-target))<2e-12
proj=dirs@g
assert np.max(np.abs(proj-0.5))<2e-12

kstar=1.0/math.sqrt(2.0)
# Full row rank survives at the critical scaling.
Gcrit=U.copy()
Gcrit[2]*=kstar
assert abs(np.linalg.det(Gcrit))>1e-4
norms=np.linalg.norm(Gcrit,axis=1)
Ucrit=Gcrit/norms[:,None]
Dcrit=np.vstack([Gcrit[0]-Gcrit[j] for j in range(1,3)])
Udcrit=np.vstack([Ucrit[0]-Ucrit[j] for j in range(1,3)])
Mcrit=Dcrit@Udcrit.T
assert abs(np.linalg.det(Mcrit))<2e-12

def lambda_formula(k):
    return 1.0/(2.0+math.sqrt(2.0)-(1.0+math.sqrt(2.0))/k)

for k in (0.2,0.5,0.65,0.8,1.0,2.0):
    Gk=U.copy()
    Gk[2]*=k
    ak,Mk,dirk=imtlg_weights(Gk)
    gk=ak@Gk
    lam=lambda_formula(k)
    assert np.max(np.abs(gk-lam*g))<3e-11*max(1.0,abs(lam))
    assert abs(np.linalg.det(Gk))>1e-5
    if k<kstar:
        assert lam<0
        assert np.max(dirk@gk)<-1e-10
        # Descent direction -gk is first-order ascent for every scaled task.
        assert np.min(Gk@(-gk))>1e-10
    elif k>kstar:
        assert lam>0

# General one-negative-coefficient threshold law.
for aj in (-0.05,-0.2,-0.7,-2.0,-10.0):
    ks=-aj/(1.0-aj)
    assert 0.0<ks<1.0
    def den(k):
        return 1.0-aj+aj/k
    assert den(0.5*ks)<0
    assert abs(den(ks))<2e-12
    assert den(0.5*(1.0+ks))>0

# Nonnegative coefficients cannot reverse under positive scaling.
tests=[
    ([0.2,0.3,0.5],[0.1,2.0,9.0]),
    ([0.0,0.4,0.6],[1e-5,7.0,0.2]),
    ([1.0,0.0,0.0],[3.0,0.1,20.0]),
]
for aa,kk in tests:
    D=sum(x/y for x,y in zip(aa,kk))
    assert D>0

print("verification passed")
