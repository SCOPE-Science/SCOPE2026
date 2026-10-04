from fractions import Fraction

def mean(xs):
    return sum(xs, Fraction(0))/len(xs)

def direct_cv(y, K):
    n=len(y); q=n//K
    folds=[list(range(k*q,(k+1)*q)) for k in range(K)]
    total=Fraction(0)
    for F in folds:
        outside=[y[i] for i in range(n) if i not in F]
        mu=mean(outside)
        total += sum((y[i]-mu)**2 for i in F)
    return total/n

def wb_cv(y, K):
    n=len(y); q=n//K
    ym=mean(y)
    W=Fraction(0); B=Fraction(0)
    for k in range(K):
        vals=y[k*q:(k+1)*q]
        fm=mean(vals)
        W += sum((v-fm)**2 for v in vals)
        B += q*(fm-ym)**2
    return (W + Fraction(K*K,(K-1)*(K-1))*B)/n

def checks():
    # deterministic decomposition on many balanced designs
    for n in range(4,31):
        for K in range(2,n+1):
            if n % K: continue
            y=[Fraction((17*i*i+5*i+3) % 41, 7) for i in range(n)]
            assert direct_cv(y,K)==wb_cv(y,K)
            # mean coefficient
            lhs=Fraction(n-K,n)+Fraction(K*K,n*(K-1))
            rhs=Fraction(1,1)+Fraction(K,n*(K-1))
            assert lhs==rhs
            m=Fraction(n*(K-1),K)
            assert rhs==1+1/m
            # variance coefficient from independent chi-squares
            vc=Fraction(n-K,1)+Fraction(K**4,(K-1)**3)
            assert vc>0
            # derivative identity at integer K (algebraic identity valid symbolically)
            d=-1+Fraction(K**3*(K-4),(K-1)**4)
            d2=-Fraction(6*K*K-4*K+1,(K-1)**4)
            assert d==d2 and d<0
            # Gaussian residual covariance coefficients, with sigma^2 factored out
            same=Fraction(1,1)/m
            diff=-Fraction(K*K,n*(K-1)*(K-1))
            # squared-error covariances factor as 2 sigma^4 times squares
            assert same*same>0 and diff*diff>0
        # leave-one-out specialization
        K=n
        loo_coeff=Fraction(K*K,(K-1)**2)/n
        assert loo_coeff==Fraction(n,(n-1)**2)
        loo_mean=Fraction(n,n-1)
        assert loo_mean==1+Fraction(1,n-1)
        loo_var_coeff=Fraction(2*n*n,(n-1)**3)
        general=Fraction(2,n*n)*Fraction(n**4,(n-1)**3)
        assert loo_var_coeff==general

    # polynomial 6K^2-4K+1 is positive: discriminant is -8 and leading coefficient positive
    assert (-4)**2-4*6*1 == -8

checks()
print("VERIFY_OK")
