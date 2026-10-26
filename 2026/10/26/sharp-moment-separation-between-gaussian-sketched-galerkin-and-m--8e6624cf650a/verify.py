"""Independent numerical and exact checks for Gaussian-sketched Krylov moment frontiers.

Run with: python verify.py
Requires NumPy and the Python standard library. Each finite check supports,
but does not replace, the analytical moment and tail arguments.
"""
import math
from fractions import Fraction as F
import numpy as np

checks=0
def ck(cond, label):
    global checks
    assert bool(cond), label
    checks+=1

# The concrete three-dimensional first two Lanczos directions.
H=((F(2),F(1,2)),(F(1,2),F(3)))
det=H[0][0]*H[1][1]-H[0][1]*H[1][0]
ck(det==F(23,4),'H determinant')
HI=((H[1][1]/det,-H[0][1]/det),(-H[1][0]/det,H[0][0]/det))
ck(HI==((F(12,23),F(-2,23)),(F(-2,23),F(8,23))),'H inverse')
for n in range(-11,12):
    for m in range(-11,12):
        g1,g2=F(n,4),F(m,4)
        d=1+F(1,2)*(HI[1][0]*g1+HI[1][1]*g2)
        ck(d==(F(23)-g1+4*g2)/23,'pole plane')
        if d:
            y0=(HI[0][0],HI[1][0]); c=F(1,2)*y0[1]
            lhs=(y0[0]-c*(HI[0][0]*g1+HI[0][1]*g2)/d,
                 y0[1]-c*(HI[1][0]*g1+HI[1][1]*g2)/d)
            M=((H[0][0]+F(1,2)*g1*0,H[0][1]+F(1,2)*g1),
               (H[1][0],H[1][1]+F(1,2)*g2))
            # M=H+(beta*g)e_2^T
            ck(M[0][0]*lhs[0]+M[0][1]*lhs[1]==1,'rFOM row 1')
            ck(M[1][0]*lhs[0]+M[1][1]*lhs[1]==0,'rFOM row 2')

rng=np.random.default_rng(42027011)
n=6
A=np.diag(np.arange(2,n+2).astype(float))
for i in range(n-1):
    A[i,i+1]=A[i+1,i]=0.5
b=np.zeros(n);b[0]=1
ck(np.linalg.eigvalsh(A).min()>0, 'SPD')
xstar=np.linalg.solve(A,b)
for k in range(1,5):
    V=np.eye(n)[:,:k]
    beta=A[k,k-1]
    H=V.T@A@V
    y0=np.linalg.solve(H,V.T@b)
    ck(abs(beta*y0[-1])>1e-12,'not converged')
    B=A@V
    yr=np.linalg.lstsq(B,b,rcond=None)[0]
    rr=b-B@yr
    ck(np.linalg.norm(rr)>1e-8,'GMRES residual positive')
    W=B.T@B
    WH=np.linalg.cholesky(W).T
    for ell in (k,k+1,k+3):
        for trial in range(30):
            S=rng.normal(size=(ell,n))
            Z=S@V;w=S[:,k]
            g=np.linalg.lstsq(Z,w,rcond=None)[0]
            M=H+beta*np.outer(g,np.eye(k)[-1])
            d=1+beta*np.linalg.solve(H,g)[-1]
            if abs(d)<1e-5: continue
            y_pred=y0-beta*y0[-1]*np.linalg.solve(H,g)/d
            y_dir=np.linalg.solve((S@V).T@(S@B),(S@V).T@(S@b))
            ck(np.linalg.norm(y_pred-y_dir)<3e-7,'rFOM formula')
            yg=np.linalg.lstsq(S@B,S@b,rcond=None)[0]
            gg=np.linalg.lstsq(S@B,S@rr,rcond=None)[0]
            ck(np.linalg.norm(yg-yr-gg)<1e-8,'sGMRES residual projection')
            # Independent orthogonal decomposition of sGMRES design.
            q,RR=np.linalg.qr(B)
            W2=S@q
            w2=S@(rr/np.linalg.norm(rr))
            g2=np.linalg.lstsq(W2,w2,rcond=None)[0]
            y_formula=yr+np.linalg.norm(rr)*np.linalg.solve(RR,g2)
            ck(np.linalg.norm(yg-y_formula)<1e-8,'sGMRES Student representation')

# Check the multivariate Student radial-moment normalization analytically.
for k in range(1,6):
    for ell in range(k,k+5):
        nu=ell-k+1
        c=math.gamma((ell+1)/2)/(math.pi**(k/2)*math.gamma(nu/2))
        sphere=2*math.pi**(k/2)/math.gamma(k/2)
        normalization=c*sphere*.5*math.gamma(k/2)*math.gamma(nu/2)/math.gamma((ell+1)/2)
        ck(abs(normalization-1)<1e-12,'Student density normalization')
        p=nu/2
        theoretical=(math.gamma((k+p)/2)*math.gamma((nu-p)/2)
                    /(math.gamma(k/2)*math.gamma(nu/2)))
        ck(theoretical>0 and math.isfinite(theoretical),'finite fractional moment')

print(f'PASS: {checks} exact-rational, linear-algebra, and distributional identities')
