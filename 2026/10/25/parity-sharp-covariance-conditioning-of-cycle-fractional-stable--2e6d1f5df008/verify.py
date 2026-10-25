"""Reproducible finite cross-checks for cycle fractional stable-set covariance.

Uses only the Python standard library. These computations corroborate, but do
not replace, the analytic infinite-dimensional proof in RESULT.md.
"""
import math
from fractions import Fraction as F

PI=math.pi

def spectrum_symbol(t, terms=15000):
    s=0.
    for k in range(1,terms+1):
        rho=(-1)**k/(2*k+1)
        j=k if k%2 else k+1
        a2=4/(PI**4*j**4)
        s+=a2*(1-rho*rho)/(1-2*rho*t+rho*rho)
    return s

def symbol_derivative(t, terms=15000):
    s=0.
    for k in range(1,terms+1):
        rho=(-1)**k/(2*k+1)
        j=k if k%2 else k+1
        a2=4/(PI**4*j**4)
        s+=2*a2*rho*(1-rho*rho)/(1-2*rho*t+rho*rho)**2
    return s

def finite_covariance(n, cutoff=175):
    """Independent finite spectral trace implementation, truncated basis."""
    rho=[(-1.)**k/(2*k+1) for k in range(cutoff)]
    def integral_j(m):
        if m==0:return 0.5
        return -2/(PI**2*m*m) if m%2 else 0.0
    # M_kl=<phi_k, x phi_l> exactly from elementary cosine integral.
    M=[[integral_j(abs(k-l))+integral_j(k+l+1)
         for l in range(cutoff)] for k in range(cutoff)]
    trace=sum(r**n for r in rho)
    mean=sum(M[k][k]*rho[k]**n for k in range(cutoff))/trace
    d2=lambda k:1/3-2/(PI**2*(2*k+1)**2)
    diagonal=sum(d2(k)*rho[k]**n for k in range(cutoff))/trace-mean*mean
    vals=[diagonal]
    for r in range(1,n):
        temp=0.0
        for k in range(cutoff):
            left=rho[k]**r
            for l in range(cutoff):
                temp+=M[k][l]**2*left*rho[l]**(n-r)
        vals.append(temp/trace-mean*mean)
    eig=[sum(vals[r]*math.cos(2*PI*j*r/n) for r in range(n)) for j in range(n)]
    return eig

def direct_tetrahedron_n3():
    # Tetrahedron with vertices 0, e_i and (1/2,1/2,1/2).
    # This lists exactly the vertices of FRAC(C_3); simplex barycentric
    # moments give Cov = [4*sum(v v^T)-sum(v)sum(v)^T]/80.
    verts=[[F(0)]*3,[F(1),F(0),F(0)],
           [F(0),F(1),F(0)],[F(0),F(0),F(1)],
           [F(1,2)]*3]
    # Correct vertex set has five vertices: origin, three unit vectors,
    # and the all-half vector; it is NOT a tetrahedron. Integrate by
    # decomposing the hull into 2 tetrahedra sharing base e1,e2,e3.
    lower=verts[:4]
    upper=verts[1:]
    # lower volume 1/6; upper volume 1/12, total 1/4.
    def moments(simplex):
        s=[sum(v[i] for v in simplex) for i in range(3)]
        m=[si/F(4) for si in s]
        sec=[[ (s[i]*s[j]+sum(v[i]*v[j] for v in simplex))/F(20)
               for j in range(3)] for i in range(3)]
        return m,sec
    L=F(1,6); U=F(1,12)
    m1,s1=moments(lower);m2,s2=moments(upper)
    mean=[(L*m1[i]+U*m2[i])/(L+U) for i in range(3)]
    c=[[ (L*s1[i][j]+U*s2[i][j])/(L+U)-mean[i]*mean[j]
         for j in range(3)] for i in range(3)]
    assert mean==[F(7,24)]*3,mean
    assert all(c[i][i]==F(23,576) for i in range(3)),c
    assert all(c[i][j]==-F(29,2880) for i in range(3) for j in range(3) if i!=j),c
    return c

def main():
    cov=direct_tetrahedron_n3()
    lo=(12-PI*PI)/PI**4
    hi=1/12
    assert abs(spectrum_symbol(1)-lo)<2e-13
    assert abs(spectrum_symbol(-1)-hi)<2e-13
    assert abs(symbol_derivative(-1)+PI*PI/80)<2e-13
    for t in [-1,-.85,-.25,0,.25,.8,1]:
        assert symbol_derivative(t)<-1e-4,(t,symbol_derivative(t))
    kinf=hi/lo
    for n in [3,4,5,6,9,10,15,16,21,22]:
        eig=finite_covariance(n)
        sample=[spectrum_symbol(math.cos(2*PI*j/n)) for j in range(n)]
        err=max(abs(x-y) for x,y in zip(eig,sample))
        if n>=10:
            assert err<12*n*(1/3)**n,(n,err)
        if n==3:
            assert abs(max(eig)/min(eig)-F(48,19))<3e-5
        if n>=15:
            assert eig.index(min(eig))==0
            assert eig.index(max(eig))==n//2
        assert min(eig)>0,n
    assert abs(kinf-3.8102896274214535)<1e-12
    print('VERIFY_OK exact_small_simplex=1 sampled_spectral_lengths=10 symbol_checks=10')

if __name__=='__main__':main()
