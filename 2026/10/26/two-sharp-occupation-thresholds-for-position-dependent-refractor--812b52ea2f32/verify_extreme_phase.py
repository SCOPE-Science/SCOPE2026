"""Independent numerical and analytic checks for position-weighted refractory occupation."""
import mpmath as mp
mp.mp.dps = 65

def qcoef(a, j):
    q=a*a
    out=mp.mpf(1)
    for m in range(1,j+1):out*=1-q**m
    return (-1)**j*a**(j*j)/out

def pdf(a,c,x):
    prod=mp.qp(a*a,a*a)
    s=mp.fsum(qcoef(a,j)*mp.exp(-c*abs(x)/a**j) for j in range(16))
    return c*s/(2*prod)

def gpdf(a,c,x):return pdf(a,c,x/a)/a

def m_series(a,c,lam):
    prod=mp.qp(a*a,a*a)
    return c/(a*prod)*mp.fsum(qcoef(a,j)/(c/a**(j+1)-lam) for j in range(20))

def m_integral(a,c,lam):
    f=lambda x:2*mp.exp(lam*x)*gpdf(a,c,x)
    return mp.quad(f,[0,mp.mpf('0.5'),2,6,16,48,mp.inf])

def main():
    a=mp.mpf('0.5');c=mp.mpf('1');eta=mp.mpf('0.7')
    P=mp.qp(a*a,a*a)
    lam_star=c*(1/a-1); lam_stat=c/a
    assert lam_star==1 and lam_stat==2
    assert abs(m_series(a,c,0)-1)<mp.mpf('1e-48')
    for lam in [mp.mpf('.25'),mp.mpf('1'),mp.mpf('1.5')]:
        ms=m_series(a,c,lam)
        mi=m_integral(a,c,lam)
        assert mp.almosteq(ms,mi,rel_eps=mp.mpf('1e-30')),(lam,ms,mi)
        piE=1/(1+eta*ms)
        piR=eta*ms/(1+eta*ms)
        assert mp.almosteq(piE+piR,1)
        def odds(x):return eta*mp.exp(lam*x)*gpdf(a,c,x)/pdf(a,c,x)
        x=mp.mpf('20')
        expected=eta/a*mp.exp((lam-lam_star)*x)
        assert abs(odds(x)/expected-1)<mp.mpf('1e-7'),(lam,odds(x)/expected)
        print('lambda',float(lam),'rest_integral',float(ms),'active_prob',float(piE),'odds_20',float(odds(x)))
    for eps in [mp.mpf('.1'),mp.mpf('.03'),mp.mpf('.01')]:
        lam=lam_stat-eps
        ms=m_series(a,c,lam)
        test=eps*ms/(c/(a*P))
        assert abs(test-1) < 4*eps, (eps,test)
        piE=1/(1+eta*ms)
        test2=piE/eps/(a*P/(eta*c))
        assert abs(test2-1) < 4*eps,(eps,test2)
        print('endpoint_eps',float(eps),'M_residue_ratio',float(test),'active_slope_ratio',float(test2))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
