"""Independent numerical checks of a two-degree spherical Slepian spectrum.

Execute with Python 3, NumPy, and SciPy. All infinite statements are proved
analytically in the accompanying mathematical note; this is a finite check.
"""
import math
import numpy as np
from scipy.special import lpmv, gammaln
from numpy.polynomial.legendre import leggauss


def b(j):
    return math.exp(math.lgamma(2*j + 1) - 2*math.lgamma(j + 1) - j*math.log(4))


def c_formula(l, m):
    k = math.sqrt((2*l+1)*(2*l+3)) / (4*(l+1))
    s, t = l+m, l-m
    if (l+m)%2 == 0:
        u, v = s//2, t//2
        return k*math.sqrt((s+1)*(t+1))*b(u)*b(v)
    u, v = (s-1)//2, (t-1)//2
    return k*s*t/math.sqrt((s+1)*(t+1))*b(u)*b(v)


def c_quadrature(l,m,x,w):
    # Normalizations are for the standard spherical harmonics on S^2.
    n1 = (2*l+1)/2*math.exp(gammaln(l-m+1)-gammaln(l+m+1))
    n2 = (2*l+3)/2*math.exp(gammaln(l+2-m)-gammaln(l+2+m))
    return math.sqrt(n1*n2)*float(np.dot(w,lpmv(m,l,x)*lpmv(m,l+1,x)))


def main():
    x,w=leggauss(180); x=(x+1)/2;w=w/2
    largest_error=0.0; count=0
    for l in range(0,35):
        values=[]
        for m in range(l+1):
            predicted=c_formula(l,m)
            observed=c_quadrature(l,m,x,w)
            largest_error=max(largest_error,abs(predicted-observed))
            assert abs(predicted-observed)<3e-10,(l,m,predicted,observed)
            assert 0<predicted<0.5
            values.append(predicted)
            count+=1
        primary=[values[m] for m in range(l+1) if (l+m)%2==0]
        secondary=[values[m] for m in range(l+1) if (l+m)%2==1]
        assert all(a<b for a,b in zip(primary,primary[1:]))
        assert all(a>b for a,b in zip(secondary,secondary[1:]))
        assert not secondary or min(primary)>max(secondary)
        assert max(values)==values[l]
        top=(2*l+1)*math.sqrt(2*l+3)/(4*(l+1))*b(l)
        assert abs(top-values[l])<2e-14
    # Exact spectral matrix (not just the off-diagonal formula) by quadrature.
    checked=0; max_eigen_error=0.0
    for l in range(0,16):
        for m in range(l+1):
            # The two harmonics with this order give the 2-by-2 Gram block.
            expected=np.array([0.5-c_formula(l,m),0.5+c_formula(l,m)])
            aa=c_quadrature(l,m,x,w)
            g=np.array([[0.5,aa],[aa,0.5]])
            eig=np.linalg.eigvalsh(g)
            max_eigen_error=max(max_eigen_error,max(abs(eig-expected)))
            assert max(abs(eig-expected))<2e-10
            checked+=1
    for l in range(0,300):
        c0=c_formula(l,l); c1=c_formula(l+1,l+1)
        assert c0>c1
        assert c0>1/math.sqrt(2*math.pi)-2e-13
    print('VERIFY_OK quadrature_pairs=%d direct_blocks=%d max_integral_error=%.3e max_spectral_error=%.3e monotonic_l=0..299' % (count, checked, largest_error,max_eigen_error))
    for l in [0,1,2,4,8,32,128]:
        print('l=%d best=%.12f min=%.12f' % (l,0.5+c_formula(l,l),0.5-c_formula(l,l)))
    print('limiting_best=%.12f' % (0.5+1/math.sqrt(2*math.pi)))

if __name__=='__main__': main()
