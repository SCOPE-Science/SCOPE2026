import math


def compositions(n,m,prefix=()):
    if m==1:
        yield prefix+(n,)
        return
    for k in range(n+1):
        yield from compositions(n-k,m-1,prefix+(k,))


def f(k):
    return 0.0 if k==0 else k*math.log(k)


def d2_f(k):
    return f(k+2)-2*f(k+1)+f(k)


def bin_prob(N,k,q):
    return math.comb(N,k)*(q**k)*((1-q)**(N-k))


def curvature_formula(n,m,h):
    q=1/m
    e=sum(bin_prob(n-2,y,q)*(h(y+2)-2*h(y+1)+h(y)) for y in range(n-1))
    return (n-1)*(m-1)/m*e


def g_cov_formula(n,m):
    q=1/m
    e=sum(bin_prob(n-2,y,q)*d2_f(y) for y in range(n-1))
    return 2*(n-1)*(m-1)/m*e


def enumerate_moments(n,m,h=None):
    factn=math.factorial(n)
    EX=EG=EXG=ET=EXT=mass=0.0
    for counts in compositions(n,m):
        mult=factn
        for z in counts:
            mult//=math.factorial(z)
        p=mult/(m**n)
        mass+=p
        X=sum((z-n/m)**2/(n/m) for z in counts)
        G=2*sum(0.0 if z==0 else z*math.log(z/(n/m)) for z in counts)
        EX+=p*X
        EG+=p*G
        EXG+=p*X*G
        if h is not None:
            T=sum(h(z) for z in counts)
            ET+=p*T
            EXT+=p*X*T
    return mass, EXG-EX*EG, (EXT-EX*ET if h is not None else None)


def run():
    direct_checks=0
    for m in range(2,8):
        for n in range(2,10):
            mass,cov_g,_=enumerate_moments(n,m)
            assert abs(mass-1)<2e-12
            assert abs(cov_g-g_cov_formula(n,m))<2e-10
            assert g_cov_formula(n,m)>0
            h=lambda k:k*k
            _,_,cov_h=enumerate_moments(n,m,h)
            formula=curvature_formula(n,m,h)
            assert abs(cov_h-formula)<2e-10
            assert abs((m/n)*formula-2*(m-1)*(n-1)/n)<2e-12
            direct_checks+=4

    lambdas=[-0.75,-0.5,-0.25,0.25,2/3,1.0,2.0]
    power_checks=0
    for m in range(2,6):
        for n in range(2,8):
            for lam in lambdas:
                scale=2*(m/n)**lam/(lam*(lam+1))
                h=lambda k,lam=lam: 0.0 if k==0 else k**(lam+1)
                _,_,direct=enumerate_moments(n,m,h)
                direct*=scale
                formula=scale*curvature_formula(n,m,h)
                assert abs(direct-formula)<3e-9
                assert formula>0
                power_checks+=1

    asymptotic_checks=0
    for m in (2,3,5,10):
        n=5000
        q=1/m
        logs=[]
        mx=-1e300
        for y in range(n-1):
            lp=(math.lgamma(n-1)-math.lgamma(y+1)-math.lgamma(n-1-y)
                +y*math.log(q)+(n-2-y)*math.log1p(-q))
            logs.append(lp)
            mx=max(mx,lp)
        den=sum(math.exp(lp-mx) for lp in logs)
        e=sum(math.exp(lp-mx)*d2_f(y) for y,lp in enumerate(logs))/den
        cov=2*(n-1)*(m-1)/m*e
        assert abs(cov/(2*(m-1))-1)<0.01
        asymptotic_checks+=1

    print('VERIFY_OK')
    print(f'direct_formula_checks={direct_checks}')
    print(f'power_family_checks={power_checks}')
    print(f'asymptotic_checks={asymptotic_checks}')


if __name__=='__main__':
    run()
