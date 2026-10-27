"""Numerical and exact-algebra checks for mechanical switching-work fluctuations.

Run with Python >=3.9: python verify_work.py
No nonstandard packages are needed. Finite computations are consistency
checks for the independent analytic martingale proof, not infinite proofs.
"""
from fractions import Fraction as Q
from math import comb, isclose


def exact_checks(D, k, a, b):
    D, k, a, b = [Q(x) for x in (D, k, a, b)]
    p0, p1 = a/(a+b), b/(a+b)
    u1 = D/k
    u0 = (2*D*p0 + a*u1)/b
    h1 = 3*D*(u0+u1)/k
    h0 = (12*D*u0 + a*h1)/b
    assert p0+p1 == 1
    assert 2*D*p0 - b*u0+a*u1 == 0
    assert 2*D*p1 -(2*k+a)*u1+b*u0 == 0
    assert 12*D*u0-b*h0+a*h1==0
    assert 12*D*u1-(4*k+a)*h1+b*h0==0
    c = D*k/(a+b)
    mu = D*k*a/(a+b)
    # Coefficients of the pointwise equation j + Lg = mu:
    assert D*k-b*c == mu
    assert a*c == mu
    assert b*k/2-b*k/2 == 0
    assert -a*k/2+a*k/2 == 0
    vv = 2*D*k*k*u0+(b*p0+a*p1)*c*c
    closed = 2*D*D*k*k*a/b*(1/k+2/(a+b)) + 2*D*D*k*k*a*b/(a+b)**3
    assert vv == closed
    return float(mu), float(vv), (p0,p1,u0,u1,h0,h1)


def moment_system(D,k,a,b):
    mu,V,(p0,p1,u0,u1,h0,h1)=exact_checks(D,k,a,b)
    D,k,a,b=map(float,(D,k,a,b))
    states = [(p,m,s) for p,ms in ((0,(0,1,2)),(1,(0,1)),(2,(0,))) for m in ms for s in (0,1)]
    idx = {v:i for i,v in enumerate(states)}
    n=len(states)
    mat=[[0.0]*n for _ in range(n)]
    for (p,m,s),i in idx.items():
        q = b if s==0 else a
        other = a if s==0 else b
        delta = k/2 if s==1 else -k/2  # 0->1 injects +k x^2/2
        mat[i][i]-=q+2*m*k*s
        if m:mat[i][idx[p,m-1,s]] += 2*m*(2*m-1)*D
        for j in range(p+1):
            mat[i][idx[j,m+p-j,1-s]] += other*comb(p,j)*delta**(p-j)
    y=[0.0]*n
    for m,v0,v1 in ((0,p0,p1),(1,u0,u1),(2,h0,h1)):
        y[idx[0,m,0]] = float(v0)
        y[idx[0,m,1]] = float(v1)
    return mat,y,idx,mu,V


def integrate(D,k,a,b,t_end=300.0,step=0.025):
    M,y,idx,mu,V=moment_system(D,k,a,b)
    n=len(y)
    steps=int(t_end/step)
    h=t_end/steps
    def f(z):
        return [sum(M[i][j]*z[j] for j in range(n)) for i in range(n)]
    def plus(z,delta,scale):
        return [z[j]+scale*delta[j] for j in range(n)]
    def variance(z):
        wm=sum(z[idx[1,0,s]] for s in (0,1))
        w2=sum(z[idx[2,0,s]] for s in (0,1))
        return wm, w2-wm*wm
    prior=None
    for q in range(steps):
        k1=f(y)
        k2=f(plus(y,k1,h/2))
        k3=f(plus(y,k2,h/2))
        k4=f(plus(y,k3,h))
        y=[y[j]+h/6*(k1[j]+2*k2[j]+2*k3[j]+k4[j]) for j in range(n)]
        if q+1==steps//2:
            prior=variance(y)[1]
    mean,now=variance(y)
    slope=(now-prior)/(t_end-(steps//2)*h)
    assert isclose(mean/t_end,mu,rel_tol=2e-5,abs_tol=2e-5), (mean/t_end,mu)
    assert isclose(slope,V,rel_tol=4e-4,abs_tol=2e-3), (slope,V)
    return slope,V,mean/t_end,mu


def main():
    params=[('1','1','1','1'),('0.7','2.5','0.4','1.3'),('1.5','0.9','2.2','0.3'),('1','1','0.1','0.1')]
    for t in params:
        got,V,m,mu=integrate(*t)
        print('PASS',','.join(t),'variance rate ODE',format(got,'.10g'),'formula',format(V,'.10g'),'mean',format(m,'.10g'))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
