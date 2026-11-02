"""Independent finite-state and asymptotic consistency tests for a capacity-two exclusion gas.
Only Python's standard library is required. Numerical tests are not used as infinite proofs.
"""
from itertools import product
from math import factorial, sqrt, exp, isclose


def occupancy_terms(L, n, z):
    lo, hi = max(0, n-L), n//2
    return [(m, factorial(L)/(factorial(m)*factorial(n-2*m)*factorial(L-n+m)) * z**m)
            for m in range(lo, hi+1)]


def double_moments(L, n, z):
    terms=occupancy_terms(L,n,z)
    norm=sum(w for _,w in terms)
    mu=sum(m*w for m,w in terms)/norm
    var=sum((m-mu)**2*w for m,w in terms)/norm
    return mu, var


def bessel_integer(h, arg):
    x=arg/2
    term=x**h/factorial(h)
    total=term
    for j in range(1,1000):
        term*=x*x/(j*(j+h))
        total+=term
        if abs(term)<1e-16*abs(total): break
    else: raise AssertionError('series did not converge')
    return total


def mass_stability(L,n,t,q):
    states=[s for s in product((0,1,2),repeat=L) if sum(s)==n]
    masses={s: (t**s.count(0))*((1+t)**s.count(1)) for s in states}
    normal=sum(masses.values())
    residual={s:0.0 for s in states}
    ti=[0,1,1+t]
    for s in states:
        prob=masses[s]/normal
        for i in range(L):
            j=(i+1)%L
            for origin,target,direction in ((i,j,1.0),(j,i,q)):
                if s[origin]==0 or s[target]==2: continue
                rate=direction*ti[s[origin]]*(1+t-ti[s[target]])
                next_s=list(s);next_s[origin]-=1;next_s[target]+=1
                dest=tuple(next_s)
                residual[s]-=prob*rate
                residual[dest]+=prob*rate
    return max(abs(x) for x in residual.values())


def stable_root(r,z):
    low=max(0,r-1); high=r/2
    for _ in range(110):
        u=(low+high)/2
        val=z*(r-2*u)**2-u*(1-r+u)
        if val>0:low=u
        else: high=u
    return (low+high)/2


def test():
    count=0
    for L in range(3,6):
        for n in range(1,2*L):
            for t in (.21,1,3.7):
                for q in (0,.4,1):
                    assert mass_stability(L,n,t,q)<1e-11,(L,n,t,q)
                    count+=1
                z=t/(1+t)**2
                em,varm=double_moments(L,n,z)
                if 2<=n<=2*L-2:
                    assert varm>0
                count+=1
    for L in (3,5,9,14):
        for n in range(0,2*L+1):
            em,_=double_moments(L,n,.25)
            v=n/L+2*em/L-(n/L)**2
            target=n*(1/L)*(1-1/L)*(2*L-n)/(2*L-1)
            assert abs(v-target)<1e-10,(L,n,v,target)
            count+=1
    for L in (5,8,12):
        for n in range(2,2*L-1):
            vals=[double_moments(L,n,z)[0] for z in (1e-6,.001,.04,.18,.25)]
            assert vals==sorted(vals) and len(set(vals))==len(vals)
            count+=1
    for a in (.1,1,5):
        for k in (-2,-1,0,1,2):
            h=abs(k); b=sqrt(a)*bessel_integer(h+1,2*sqrt(a))/bessel_integer(h,2*sqrt(a))
            for L in (80,200,400):
                em,_=double_moments(L,L+k,a/(L*L))
                target=(max(k,0)+b)
                assert abs(em-target)<.2,(a,k,L,em,target)
                count+=1
    for xi in (-4,-1,0,2,5):
        z=1e-8;r=1+xi*sqrt(z)
        u=stable_root(r,z)
        target=(xi+sqrt(xi*xi+4))/2
        v=r+2*u-r*r
        assert abs(u/sqrt(z)-target)<.005,(xi,u/sqrt(z),target)
        assert abs(v/sqrt(z)-sqrt(xi*xi+4))<.005,(xi,v/sqrt(z))
        count+=2
    print('PASS',count,'independent tests: generator balance, exact finite occupancy, parameter monotonicity, Bessel scaling and critical crossover')

if __name__=='__main__': test()
