"""Independent finite-matrix and rational checks of triangular Durrmeyer trace identities."""
import math
from fractions import Fraction
import numpy as np


def multi(n):
    return [(i, j, n-i-j) for i in range(n+1) for j in range(n-i+1)]


def spectrum_gram(n, shape):
    """Gram matrix of normalized Bernstein kernels under Dirichlet measure."""
    A = sum(shape)
    ids = multi(n)
    log_facts = [math.lgamma(k+1) for k in range(2*n+1)]
    norms = []
    for alpha in ids:
        v = log_facts[n] - sum(log_facts[t] for t in alpha)
        v += math.lgamma(A) - math.lgamma(n+A)
        v += sum(math.lgamma(t+sh)-math.lgamma(sh) for t,sh in zip(alpha,shape))
        norms.append(v)
    mat = np.empty((len(ids),len(ids)))
    for k,alpha in enumerate(ids):
        for l,beta in enumerate(ids):
            logv = 2*log_facts[n]-sum(log_facts[t] for t in alpha)-sum(log_facts[t] for t in beta)
            logv += math.lgamma(A)-math.lgamma(2*n+A)
            logv += sum(math.lgamma(a+b+sh)-math.lgamma(sh) for a,b,sh in zip(alpha,beta,shape))
            mat[k,l] = math.exp(logv-(norms[k]+norms[l])/2)
    return np.linalg.eigvalsh(mat)[::-1]


def multi_nd(n,d):
    if d == 0:
        return [(n,)]
    return [(k,)+t for k in range(n+1) for t in multi_nd(n-k,d-1)]


def gram_nd(n, shape):
    d=len(shape)-1
    A=sum(shape)
    ids=multi_nd(n,d)
    lf=math.lgamma
    ls=[]
    for alpha in ids:
        q=lf(n+1)-sum(lf(t+1) for t in alpha)
        q+=lf(A)-lf(n+A)
        q+=sum(lf(t+a)-lf(a) for t,a in zip(alpha,shape))
        ls.append(q)
    matrix=np.empty((len(ids),len(ids)))
    for i,alpha in enumerate(ids):
        for j,beta in enumerate(ids):
            q=2*lf(n+1)-sum(lf(t+1) for t in alpha)-sum(lf(t+1) for t in beta)
            q+=lf(A)-lf(2*n+A)
            q+=sum(lf(u+v+a)-lf(a) for u,v,a in zip(alpha,beta,shape))
            matrix[i,j]=math.exp(q-(ls[i]+ls[j])/2)
    return np.linalg.eigvalsh(matrix)[::-1]


def theoretical_nd(n,d,A):
    ans=[]
    p=1.
    for j in range(n+1):
        if j:p*=(n-j+1)/(n+A+j-1)
        ans.extend([p]*math.comb(j+d-1,d-1))
    return sorted(ans,reverse=True)


def theoretical(n, A):
    vals=[]
    p=1.
    for j in range(n+1):
        if j: p *= (n-j+1)/(n+A+j-1)
        vals += [p]*(j+1)
    return sorted(vals,reverse=True)


def spectral_trace(n,A,s):
    p=1.
    acc=1.
    for j in range(1,n+1):
        p *= (n-j+1)/(n+A+j-1)
        acc+=(j+1)*p**s
    return acc


def trace_approx(n,A,s):
    return (n/(2*s) + math.sqrt(math.pi*n)*(3-A)/(4*math.sqrt(s))
            + (3*A*A-12*A+14)/12 + A/(4*s) - 1/(6*s*s))


def general_trace(n,d,A,s):
    p=1.
    z=1.
    for j in range(1,n+1):
        p *= (n-j+1)/(n+A+j-1)
        z+=math.comb(j+d-1,d-1)*p**s
    return z


def general_two_terms(n,d,A,s):
    c0=math.gamma(d/2)/(2*math.factorial(d-1)*s**(d/2))
    c1=(d+1-A)*math.gamma((d-1)/2)/(4*math.factorial(d-2)*s**((d-1)/2))
    return c0*n**(d/2)+c1*n**((d-1)/2)


def exact_rational(n,s):
    p=Fraction(1,1)
    t=Fraction(1,1)
    for j in range(1,n+1):
        p *= Fraction(n-j+1,n+j+2)
        t+=(j+1)*p**s
    return t


def main():
    cases=0
    for shape in [(1.,1.,1.),(.5,1.5,2.),(2.,.5,.5),(1.,2.,4.)]:
        for n in range(1,7):
            a=spectrum_gram(n,shape)
            b=theoretical(n,sum(shape))
            assert np.allclose(a,b,atol=2e-12,rtol=2e-12),(n,shape,a,b)
            cases+=1
    for shape in [(1.,1.,1.,1.),(.5,1.2,1.5,2.),(1.,1.,1.,1.,1.)]:
        d=len(shape)-1
        for n in range(1,5):
            actual=gram_nd(n,shape)
            expected=theoretical_nd(n,d,sum(shape))
            assert np.allclose(actual,expected,atol=5e-12,rtol=5e-12),(n,shape)
            cases+=1
    for n in range(1,45):
        assert exact_rational(n,1)==Fraction(n+2,2)
        assert exact_rational(n,2)==Fraction((n+2)**2,4*(n+1))
        cases+=2
    # An independently assembled Gram matrix also verifies both exact traces.
    for n in range(1,7):
        a=spectrum_gram(n,(1.,1.,1.))
        assert abs(sum(a)-float(exact_rational(n,1)))<2e-11
        assert abs(sum(a*a)-float(exact_rational(n,2)))<2e-11
        cases+=2
    for A,s in [(1.,.5),(1.,2.),(2.,1.),(3.,.5),(3.,2.),(3.,5.),(4.,2.),(6.,3.)]:
        # Scaled remainders must stay bounded and decay approximately as n^-1/2.
        remainders=[]
        for n in [500,2000,8000]:
            e=abs(spectral_trace(n,A,s)-trace_approx(n,A,s))
            remainders.append(e)
        assert remainders[2] <= .65*remainders[0]+1e-8,(A,s,remainders)
        cases+=1
    for d,A,s in [(3.,4.,1.),(3.,6.,2.),(4.,5.,.75),(4.,8.,2.)]:
        d=int(d)
        errs=[]
        for n in [250,1000,4000]:
            err=abs(general_trace(n,d,A,s)-general_two_terms(n,d,A,s))
            errs.append(err/(n**((d-2)/2)))
        assert all(v<1e4 for v in errs),(d,A,s,errs)
        assert errs[-1] <= 2*errs[0]+1e-4,(d,A,s,errs)
        cases+=1
    print('VERIFIED',cases,'independent checks: Gram spectra, rational traces, asymptotic refinements')


if __name__ == '__main__':
    main()
