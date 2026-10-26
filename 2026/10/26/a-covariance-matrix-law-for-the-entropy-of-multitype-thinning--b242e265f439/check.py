#!/usr/bin/env python3
"""Direct finite-law checks for multitype Bernoulli thinning."""
from math import comb, exp, factorial, log, isclose
from fractions import Fraction

def bernbin(m, n):
    # Binomial(2*m,1/n) probabilities.
    return [comb(2*m,k)*(1/n)**k*(1-1/n)**(2*m-k) for k in range(2*m+1)]

def prob_law(n):
    N=2*n
    p=[[0.0]*(N+1) for _ in range(N+1)]
    for m in range(n+1):
        w=comb(n,m)/2**n
        b=bernbin(m,n)
        for k,bk in enumerate(b):
            row=p[k]
            z=w*bk
            for ell,bl in enumerate(b):
                row[ell] += z*bl
    return p

def KL_PQ(p):
    N=len(p)-1
    q=[exp(-1.)/factorial(k) for k in range(N+1)]
    D=0.; marg=[0.]*(N+1)
    for k,row in enumerate(p):
        for l,prob in enumerate(row):
            if prob>0:
                D += prob*log(prob/(q[k]*q[l]))
            marg[k]+=prob
    Dm=sum(pk*log(pk/q[k]) for k,pk in enumerate(marg) if pk)
    return D,Dm

def rational_charlier_checks():
    # Q_1 C_1^2 = 1; Q_1 C_2^2=2; Q_1 C_1*C_2=0,
    # established independently by factorial-moment identities.
    # coefficients of exp(w)w^j recover the factorial-polynomial basis.
    from fractions import Fraction as F
    for k in range(10):
        c1=F(k-1,1)
        c2=F(k*k-3*k+1,1)
        assert c2 == F(k*(k-1)-2*k+1,1)
        # derivative identities k=0,..,9
        def falling(a,b):
            if a<b: return 0
            z=1
            for t in range(b): z*=a-t
            return z
        assert c2==falling(k,2)-2*k+1
    # Exact Poisson expectation: use falling factorial moment E(K)_j=1.
    # Polynomial k moments E k^p, Bell numbers for p up to 4.
    E={0:1,1:1,2:2,3:5,4:15}
    def ev(pol): return sum(a*E[j] for j,a in enumerate(pol))
    assert ev([1,-2,1])==1            # (k-1)^2
    assert ev([1,-3,1])==0            # C2
    assert ev([-1,4,-4,1])==0        # C1*C2 = (k-1)(k^2-3k+1)
    assert ev([1,-6,11,-6,1])==2     # (k^2-3k+1)^2
    print('Poisson-Charlier exact moments: pass')

def exact_covariance_checks():
    for n in range(1,25):
        # Conditional on M~Bin(n,1/2), each coordinate is Bin(2M,1/n),
        # independently of the other coordinate given M.
        w=[Fraction(comb(n,m),2**n) for m in range(n+1)]
        m1=sum(w[m]*Fraction(2*m,n) for m in range(n+1))
        mfall=sum(w[m]*Fraction(2*m*(2*m-1),n*n) for m in range(n+1))
        cross=sum(w[m]*Fraction(4*m*m,n*n) for m in range(n+1))
        assert m1==1 and mfall==1
        assert cross==1+Fraction(1,n)
    print('Exact finite-n mean, marginal equidispersion and cross-covariance: 24 cases pass')

def main():
    rational_charlier_checks()
    exact_covariance_checks()
    vals=[]
    for n in (4,8,16,24,40,64):
        p=prob_law(n)
        assert abs(sum(map(sum,p))-1.)<5e-11
        D,Dm=KL_PQ(p)
        vals.append((n,n*n*D,n**4*Dm))
        print(f'n={n}: n^2 joint KL={n*n*D:.9f}; n^4 marginal KL={n**4*Dm:.9f}')
        assert D >= -1e-12 and Dm>=-1e-12
    # Asymptotic approach is not treated as a proof.
    assert abs(vals[-1][1]-0.5)<0.12, vals[-1]
    assert abs(vals[-1][1]-0.5)<abs(vals[1][1]-0.5)
    print('Direct finite-law checks: pass; infinite-limit theorem requires analytic proof.')

if __name__=='__main__': main()
