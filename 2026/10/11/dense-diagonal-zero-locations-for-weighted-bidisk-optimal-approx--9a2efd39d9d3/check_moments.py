"""Finite checks for diagonal zeros of linear optimal approximants in Dirichlet-type bidisc spaces."""
from cmath import exp, phase
from math import acos, isfinite

def moments(m, target, alpha, shift):
    radius=abs(target)
    assert 0<radius<1 and m>=1 and shift>=2 and alpha>0
    angle=phase(target); theta=acos(radius)
    a=exp(1j*(angle+theta)); b=exp(1j*(angle-theta))
    h={(k,l):(a.conjugate()**k*b.conjugate()**l + b.conjugate()**k*a.conjugate()**l)
       for k in range(m+1) for l in range(m+1)}
    mh={}
    for (k,l),v in h.items():
        mh[k+1,l]=mh.get((k+1,l),0)+v
        mh[k,l+1]=mh.get((k,l+1),0)+v
    lin=lambda u,v,weighted:sum(x*v.get(idx,0).conjugate()*( (shift+idx[0]+1)**alpha * (shift+idx[1]+1)**alpha if weighted else 1) for idx,x in u.items())
    z0=lin(h,mh,False); n0=lin(mh,mh,False).real
    zw=lin(h,mh,True); nw=lin(mh,mh,True).real
    lam=1/(4*(m+1)**2)
    # Orthogonal coefficient supports for shift >=2; constant basis contributes ||M||^2=2^(alpha+1)
    opa_zero=(2**(alpha+1) + lam*lam*nw)/(2*lam*lam*zw)
    hardy_zero=n0/(2*z0)
    return hardy_zero,opa_zero

if __name__=='__main__':
  for target in [0.2,0.25+0.2j,-0.3+0.2j]:
    for m in [15,50,150]:
      z0,za=moments(m,target,1.0,10**12)
      print('target',target,'degree_each',m,'Hardy block root',round(z0.real,6)+1j*round(z0.imag,6),'weighted final root',round(za.real,6)+1j*round(za.imag,6))
      assert abs(za-z0)<1e-5, (za,z0)
    assert abs(za-target)<0.05,(za,target)
  for alpha in [0.25,0.5,2.0]:
    z0,za=moments(80,0.4+0.2j,alpha,10**24)
    print('alpha',alpha,'root',za,'Hardy',z0)
    assert abs(za-z0)<1e-5
  print('all checks passed')
