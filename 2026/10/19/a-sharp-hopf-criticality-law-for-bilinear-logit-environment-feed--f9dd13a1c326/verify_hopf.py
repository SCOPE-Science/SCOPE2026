"""Exact first-Lyapunov calculation and independent tensor contraction.

Run with Python 3, SymPy and NumPy: python verify_hopf.py
The derivation is for the planar logit/environment system defined in RESULT.md.
"""
import math
import numpy as np
import sympy as sp

u, v, s, w, a, q, T, U = sp.symbols('u v s w a q T U', real=True)
H = s * (1 - s)
D = 1 - 6*s + 6*s**2
C = -a*w/(H*q)
z = u-w*v
# Taylor coefficients at a Hopf point in canonical rotation coordinates.
f = sp.expand(((1-2*s)/(2*H))*z**2 + H*C*u*v
              + D/(6*H**2)*z**3 + (1-2*s)*C*u*v*z)
g = T*u*v + U*u*v*v

def dd(expr, i, j):
    return sp.diff(expr, u, i, v, j).subs({u:0, v:0})

l1 = ((dd(f,3,0)+dd(f,1,2)+dd(g,2,1)+dd(g,0,3))/16
      + (dd(f,1,1)*(dd(f,2,0)+dd(f,0,2))
         -dd(g,1,1)*(dd(g,2,0)+dd(g,0,2))
         -dd(f,2,0)*dd(g,2,0)+dd(f,0,2)*dd(g,0,2))/(16*w))
r=sp.symbols('r',real=True)
target = ((r-2)*w**2-(r+2))/(16*H)
assert sp.simplify(l1.subs(a,r*q/(1-2*s))-target)==0
print('Exact symbolic planar coefficient identity: PASS')

# Independently evaluate the multilinear Hopf normal form using the full
# quadratic and cubic tensors; unlike the scalar formula this uses matrix
# inverses and the complex eigenvector pairing.
def kuznet_check(a0,b0,c0,d0,kappa,lam,eps):
    ss=lam/kappa; HH=ss*(1-ss); qq=a0*ss+c0
    L=math.log(ss/(1-ss))
    nn=(L*HH*b0 - b0*ss-d0)/(qq-L*HH*a0)
    bb=1/(HH*(a0*nn+b0))
    assert 0<ss<1 and 0<nn<1 and qq<0 and bb>0
    AA=qq/(a0*nn+b0); BB=eps*kappa*nn*(1-nn)
    ww=math.sqrt(-AA*BB); kk=BB/ww
    CC=bb*a0*kk; DD=1-6*ss+6*ss**2
    uu,vv=sp.symbols('uu vv')
    zz=uu-ww*vv
    FF=sp.expand((1-2*ss)/(2*HH)*zz**2+HH*CC*uu*vv
                 +DD/(6*HH**2)*zz**3+(1-2*ss)*CC*uu*vv*zz)
    GG=eps*kappa*(1-2*nn)*uu*vv-eps*kappa*kk*uu*vv**2
    vars=[uu,vv]; functions=[FF,GG]
    Btensor=np.empty((2,2,2),dtype=complex)
    Ctensor=np.empty((2,2,2,2),dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                Btensor[i,j,k]=complex(sp.diff(functions[i],vars[j],vars[k]).subs({uu:0,vv:0}))
                for l in range(2):
                    Ctensor[i,j,k,l]=complex(sp.diff(functions[i],vars[j],vars[k],vars[l]).subs({uu:0,vv:0}))
    Jac=np.array([[0,-ww],[ww,0]],dtype=complex)
    eigvec=np.array([1,-1j],dtype=complex)
    dual=eigvec/2
    B=lambda xx,yy:np.einsum('ijk,j,k->i',Btensor,xx,yy)
    Ct=lambda xx,yy,zz:np.einsum('ijkl,j,k,l->i',Ctensor,xx,yy,zz)
    G21=np.vdot(dual,Ct(eigvec,eigvec,eigvec.conj())
        +B(eigvec.conj(),np.linalg.solve(2j*ww*np.eye(2)-Jac,B(eigvec,eigvec)))
        -2*B(eigvec,np.linalg.solve(Jac,B(eigvec,eigvec.conj()))))
    rr=a0*(1-2*ss)/qq
    exact=((rr-2)*ww**2-(rr+2))/(16*HH)
    assert abs(G21.real-8*exact)<3e-10
    assert abs(bb*(qq*nn+b0*ss+d0)-L)<1e-10
    assert abs(bb*HH*(a0*nn+b0)-1)<1e-10
    return nn,bb,ww**2,rr,exact,G21.real

# Source's numerical game: supercritical for all positive timescales.
for ep in [0.5,1.0,3.0,1000.0]:
    nn,bb,w2,rr,ell,g21=kuznet_check(-2.25,2,0.25,-0.5,1.8,1,ep)
    assert ell<0
    print('Source game eps=%g: n*=%.12f beta*=%.12f omega^2=%.9f ell1=%.9f tensor=%.9f PASS'
          % (ep,nn,bb,w2,ell,g21))

# A rational-payoff model with the opposite Hopf criticalities, depending on
# the environmental time scale, while the equilibrium and Hopf beta stay fixed.
for ep in [1.0,200.0]:
    nn,bb,w2,rr,ell,g21=kuznet_check(10,0.5,-10.5,-0.1,1.25,1,ep)
    assert abs(rr-12/5)<1e-12 and (ell<0 if ep==1 else ell>0)
    print('Second game eps=%g: n*=%.12f beta*=%.12f omega^2=%.9f ell1=%.9f tensor=%.9f PASS'
          % (ep,nn,bb,w2,ell,g21))
print('All verification checks passed.')
