"""Independent finite quadrature check of the analytic moment expansion (not a proof)."""
import numpy as np
from numpy.polynomial.legendre import leggauss

def nodes(intervals, order=64):
    x0,w0=leggauss(order)
    xx=[];ww=[]
    for a,b in intervals:
        xx.extend((a+b)/2+(b-a)*x0/2)
        ww.extend((b-a)*w0/2)
    return np.asarray(xx),np.asarray(ww)

def calc(intervals, widths):
    x,w=nodes(intervals,64)
    m=w.sum();p=w/m;center=np.dot(p,x);v=x-center
    mom={j:np.dot(p,v**j) for j in (2,3,4,6)}
    A=mom[2];B=mom[3];C=mom[4];D=mom[6]
    coeffs=(-A/3,(2*C+A*A)/45,-D/315-2*A*C/189+A**3/135+23*B**2/945)
    print('intervals',intervals,'mass',m,'moments',mom,'coefficient ε^3',coeffs[2])
    for W in widths:
        dist=(x[:,None]-x[None,:])*W
        kern=np.sinc(dist)*np.sqrt(w[:,None]*w[None,:])*W
        exact=np.linalg.eigvalsh(kern)[-1]
        eps=(np.pi*W)**2
        pred=m*W*(1+coeffs[0]*eps+coeffs[1]*eps**2+coeffs[2]*eps**3)
        print(' W',W,'eigen',format(exact,'.15g'),'formula',format(pred,'.15g'),'residual',format(exact-pred,'.6g'),'normed O(W^8)',format((exact-pred)/(m*W*eps**4),'.6g'))

if __name__=='__main__':
    calc([(-1,-.3),(.1,1.0)],[.12,.17,.22])
    calc([(-1,1)],[.12,.17,.22])
