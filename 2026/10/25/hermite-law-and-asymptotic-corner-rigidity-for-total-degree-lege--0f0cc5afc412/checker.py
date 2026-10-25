"""Independent numerical diagnostics for the total-degree Legendre-kernel asymptotic.
Requires Python 3 and NumPy. These are finite checks, not a proof.
"""
import math
import numpy as np


def legendre_values(a, m):
    out = [np.ones_like(a), a]
    for j in range(1, m):
        out.append(((2*j+1)*a*out[-1]-j*out[-2])/(j+1))
    return out[:m+1]


def kernel(x, yy, m):
    # Coefficient t^0+...+t^m of the product of univariate reproducing generating polynomials.
    n = yy.shape[0]
    acc = np.zeros((m+1, n), dtype=np.float64)
    acc[0] = 1.0
    for i, xi in enumerate(x):
        px = legendre_values(np.array(xi),m)
        py = legendre_values(yy[:,i],m)
        a = np.stack([(2*j+1)*px[j]*py[j] for j in range(m+1)],axis=0)
        nxt = np.zeros_like(acc)
        for k in range(m+1):
            for j in range(k+1):
                nxt[k] += acc[k-j]*a[j]
        acc = nxt
    return np.sum(acc,axis=0)


def hermite_prob(x,m):
    if m==0: return np.ones_like(x)
    if m==1: return x
    a,b=np.ones_like(x),x
    for j in range(1,m): a,b=b,x*b-j*a
    return b


def expected_abs_hermite(m):
    # Exact integration by parts over sign intervals, numerically located roots.
    coef=np.zeros(m+1);coef[-1]=1
    roots=np.sort(np.polynomial.hermite_e.hermeroots(coef)).real
    boundaries=np.r_[[-math.inf],roots,[math.inf]]
    total=0.0
    for lo,hi in zip(boundaries[:-1],boundaries[1:]):
        left=0. if math.isinf(lo) else hermite_prob(lo,m-1)*math.exp(-lo*lo/2)/math.sqrt(2*math.pi)
        right=0. if math.isinf(hi) else hermite_prob(hi,m-1)*math.exp(-hi*hi/2)/math.sqrt(2*math.pi)
        total+=abs(left-right)
    return total


def main():
    rng=np.random.default_rng(20261023)
    for m in (1,2,3):
        c=3**(m/2)*expected_abs_hermite(m)/math.factorial(m)
        print('m',m,'exact leading constant',f'{c:.12f}')
        for d in (16,64,256):
            n=10000 if d<=64 else 8000
            yy=rng.uniform(-1.,1.,size=(n,d))
            if m==1: kinds=('corner',)
            else: kinds=('corner','half_zero','center_half')
            for kind in kinds:
                x=np.ones(d)
                if kind=='half_zero':x[d//2:]=0
                if kind=='center_half':x[:]=.5
                aa=kernel(x,yy,m)
                rho=np.mean(x*x)
                estimate=np.mean(np.abs(aa))/d**(m/2)
                goal=c*rho**(m/2)
                print('d',d,'kind',kind,'observed',round(estimate,6),'predicted',round(goal,6))
                assert abs(estimate-goal)<(0.5 if d<64 else 0.22), (d,kind,estimate,goal)
    # Exact kernel identity for m=2, random configurations and dimensions.
    for d in range(1,7):
        for _ in range(20):
            x=rng.uniform(-1,1,size=d)
            yy=rng.uniform(-1,1,size=(10,d))
            A=(yy*x[None,:]).sum(axis=1)
            K=1+3*A+5*np.sum(((3*x*x-1)/2)[None,:]*((3*yy*yy-1)/2),axis=1)+4.5*(A*A-np.sum(yy*yy*x[None,:]**2,axis=1))
            assert np.allclose(K,kernel(x,yy,2),atol=1e-10,rtol=1e-10)
    print('PASS: 120 exact-formula comparisons and dimension/asymptotic diagnostics')

if __name__=='__main__':main()
