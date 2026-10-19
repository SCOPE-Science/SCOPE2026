"""Finite corroboration for the one-step Gaussian RPLU cubic-tail theorem.

Requires Python 3, NumPy, and SciPy. Analytical proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.special import gammaln


def tail_constant(m, n):
    assert m >= 2 and n >= 2
    return math.exp(
        math.log(16.0*m*n / (3.0*(m*n+3)*math.sqrt(2*math.pi)))
        + gammaln((m+2)/2.0)-gammaln((m-1)/2.0)
        + gammaln((n+2)/2.0)-gammaln((n-1)/2.0)
    )


def mean_square(m,n):
    return 2.0*m*(m-1)*n*(n-1)/(m*n+2)


def deterministic_minor_check(rng):
    checks = 0
    for m,n in ((2,2),(2,3),(3,3),(3,4),(5,4)):
        for _ in range(35):
            A = rng.normal(size=(m,n))
            S = np.sum(A*A)
            left = 0.0
            for i in range(m):
                for j in range(n):
                    R = A-np.outer(A[:,j],A[i,:])/A[i,j]
                    left += A[i,j]**2/S * np.sum(R*R)
            right = 4.0/S * sum((A[i,j]*A[k,l]-A[i,l]*A[k,j])**2
                    for i in range(m) for k in range(i+1,m)
                    for j in range(n) for l in range(j+1,n))
            assert np.isclose(left,right,rtol=2e-12,atol=1e-10)
            checks+=1
    return checks


def simulate(m,n,count,rng):
    thresholds=(7.0,11.0,16.0)
    tally=np.zeros(len(thresholds),dtype=np.int64)
    sumsq=0.0
    done=0
    while done<count:
        batch=min(100000,count-done)
        A=rng.standard_normal((batch,m,n))
        weight=A*A
        cum=np.cumsum(weight.reshape(batch,-1),axis=1)
        piv=np.sum(cum<rng.random(batch)[:,None]*cum[:,-1,None],axis=1)
        rows=piv//n; cols=piv%n
        rr=np.arange(batch)
        x=A[rr,rows,cols]
        residual=A-A[rr,:,cols][:,:,None]*A[rr,rows,:][:,None,:]/x[:,None,None]
        z=np.linalg.norm(residual.reshape(batch,-1),axis=1)
        sumsq+=float(np.dot(z,z))
        tally+=np.array([np.count_nonzero(z>t) for t in thresholds])
        done+=batch
    const=tail_constant(m,n)
    est=11.0**3 * tally[1]/count
    assert abs(sumsq/count - mean_square(m,n)) < 0.16*mean_square(m,n)
    assert 0.7*const < est < 1.3*const
    return thresholds,tally,est,sumsq/count


def main():
    rng=np.random.default_rng(2026)
    assert math.isclose(tail_constant(2,2),64/(21*math.pi*math.sqrt(2*math.pi)),rel_tol=1e-14)
    count=deterministic_minor_check(rng)
    print('EXACT_ORIENTED_MINOR_IDENTITIES:',count,'PASS')
    for m,n,N in ((2,2,2000000),(2,3,1200000),(3,3,900000)):
        t,tally,estimate,ms=simulate(m,n,N,rng)
        print('SIZE',m,n,'trials',N,'tail coefficient analytic',format(tail_constant(m,n),'.12g'),
              'empirical t=11',format(estimate,'.12g'),'squared mean',format(ms,'.12g'),
              'analytic mean',format(mean_square(m,n),'.12g'))
        print('THRESHOLDS',t,'TAIL_COUNTS',tally.tolist())
    print('FINITE_REPRODUCTION_OK; infinite claims require the analytic proof')

if __name__=='__main__':
    main()
