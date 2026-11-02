"""Exact-moment replay for the centered Gaussian hint control-variate quadratic model.

Only standard-library dependencies.  A symmetric five-atom rational cubature
reproduces moments of a standard Gaussian through degree four in each coordinate.
The test expands the actual random update, rather than reusing the closed-form
moment recurrence under test. Run: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, isclose

ATOMS = [(-2,Q(1,12)), (-1,Q(1,6)), (0,Q(1,2)), (1,Q(1,6)), (2,Q(1,12))]

def direct_moment(d,k,beta,s,x):
    v=w=Q(0)
    for entries in product(ATOMS,repeat=d):
        u=[a for a,_ in entries]
        prob=Q(1)
        for _,p in entries: prob *= p
        residual=sum(Q(u[i]) * (x[i] - (beta*x[i] if i<k else Q(0))) for i in range(d))
        z=[x[i]-s*((beta*x[i] if i<k else Q(0)) + Q(u[i])*residual) for i in range(d)]
        v += prob*sum(t*t for t in z[:k])
        w += prob*sum(t*t for t in z[k:])
    return v,w

def predicted(d,k,beta,s,x):
    r=d-k
    eta=1-beta
    v0=sum(t*t for t in x[:k]); w0=sum(t*t for t in x[k:])
    base=(1-s)**2
    return ((base+s*s*(k+1)*eta*eta)*v0+s*s*k*w0,
            s*s*r*eta*eta*v0+(base+s*s*(r+1))*w0)

def rate(d,k,beta,s):
    r=d-k; t=float((1-beta)**2)
    tr=(k+1)*t+(r+1)
    root=sqrt(max(0,tr*tr-4*(d+1)*t))
    lam=(tr+root)/2
    return (1-float(s))**2+float(s)**2*lam,lam

def main():
    n=0
    for d in [2,3,4,5]:
        x=[Q((-1)**i*(i+1),i+2) for i in range(d)]
        for k in range(1,d):
            for beta in [Q(-1),Q(0),Q(1,3),Q(1),Q(5,3),Q(2),Q(3)]:
                for s in [Q(1,7),Q(1,2),Q(1)]:
                    actual=direct_moment(d,k,beta,s,x)
                    expect=predicted(d,k,beta,s,x)
                    assert actual==expect,(d,k,beta,s,actual,expect)
                    n+=1
    print('EXACT_GAUSSIAN_MOMENT_REPLAYS',n)
    # Independent characteristic polynomial, minimizer and comparison checks.
    n2=0
    for d in range(2,60):
        for k in range(1,d):
            for beta in [Q(-2),Q(-1),Q(0),Q(1,3),Q(1),Q(5,3),Q(2),Q(3)]:
                r=d-k; t=(1-beta)**2
                tr=(k+1)*t+r+1
                det=(d+1)*t
                rho,lam=rate(d,k,beta,Q(1,7))
                assert isclose(lam*lam-float(tr)*lam+float(det),0,abs_tol=1e-7,rel_tol=1e-10)
                sstar=1/(lam+1)
                assert isclose((1-sstar)**2+sstar*sstar*lam,lam/(lam+1),rel_tol=1e-11)
                assert ((lam < d+1) == (0<beta<2)) or beta in [Q(0),Q(2)]
                if beta in [Q(0),Q(2)]: assert isclose(lam,d+1,abs_tol=1e-10)
                if beta==1: assert isclose(lam,r+1,abs_tol=1e-10)
                n2+=1
    print('SPECTRAL_PARAMETER_CHECKS',n2)
    # Critical scaling window at fixed residual dimension.
    n3=0
    for r in [1,2,4,8]:
        for c in [0,0.3,1,3]:
            lamlim=(r+1+c*c+sqrt((r+1+c*c)**2-4*c*c))/2
            vals=[]
            for d in [100,10000,1000000]:
                _,v=rate(d,d-r,1-c/sqrt(d),Q(1,7))
                vals.append(abs(v-lamlim))
            assert vals[-1]<0.0002 and vals[0]>=vals[1]>=vals[2],(r,c,vals)
            n3+=1
    print('SCALING_WINDOW_CHECKS',n3)
    print('VERIFY_OK',n+n2+n3)
if __name__=='__main__': main()
