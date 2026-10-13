import mpmath as mp
mp.mp.dps = 40

def A(m,a):
    return mp.gamma(m)*mp.gamma(a+1)/mp.gamma(m+a)

def cov_formula(m,a):
    return m*A(m,a)*(m*(mp.digamma(m+a)-mp.digamma(m))-(mp.digamma(a+1)-mp.digamma(1)))

def var_greenwood(m):
    return mp.mpf(4)*(m-1)/((m+1)**2*(m+2)*(m+3))

def var_moran(m):
    return m*mp.pi**2/6-m*m*mp.polygamma(1,m)

def corr2(m):
    c=mp.mpf(m-1)/(m+1)**2
    return c*c/(var_greenwood(m)*var_moran(m))

def direct_m2(a):
    a=mp.mpf(a)
    P=lambda x: x**a+(1-x)**a
    M=lambda x: -mp.log(2*x)-mp.log(2*(1-x))
    ep=mp.quad(lambda x:P(x),[0,1])
    em=mp.quad(lambda x:M(x),[0,1])
    epm=mp.quad(lambda x:P(x)*M(x),[0,1])
    return epm-ep*em

def direct_m3(a):
    a=mp.mpf(a)
    def P(x,y):
        return x**a+y**a+(1-x-y)**a
    def M(x,y):
        return -mp.log(3*x)-mp.log(3*y)-mp.log(3*(1-x-y))
    ep=2*mp.quad(lambda x: mp.quad(lambda y:P(x,y),[0,1-x]),[0,1])
    em=2*mp.quad(lambda x: mp.quad(lambda y:M(x,y),[0,1-x]),[0,1])
    epm=2*mp.quad(lambda x: mp.quad(lambda y:P(x,y)*M(x,y),[0,1-x]),[0,1])
    return mp.re(epm-ep*em)

def run():
    direct_checks=0
    for a in [mp.mpf('0.5'),mp.mpf('2'),mp.mpf('2.7')]:
        assert abs(direct_m2(a)-cov_formula(2,a)) < mp.mpf('1e-28')
        direct_checks += 1
    for a in [mp.mpf('0.5'),mp.mpf('2')]:
        assert abs(direct_m3(a)-cov_formula(3,a)) < mp.mpf('1e-25')
        direct_checks += 1

    finite_checks=0
    for m in range(2,10001):
        target=mp.mpf(m-1)/(m+1)**2
        assert abs(cov_formula(m,2)-target) < mp.mpf('1e-32')
        assert var_greenwood(m) > 0
        assert var_moran(m) > 0
        c2=corr2(m)
        assert 0 < c2 < 1
        finite_checks += 4

    limit=1/(4*(mp.pi**2/6-1))
    assert abs(corr2(100000)-limit) < mp.mpf('2e-5')
    print('VERIFY_OK')
    print(f'direct_simplex_covariance_checks={direct_checks}')
    print(f'finite_formula_checks={finite_checks}')
    print('max_finite_m=10000')
    print('asymptotic_check_m=100000')

if __name__=='__main__':
    run()
