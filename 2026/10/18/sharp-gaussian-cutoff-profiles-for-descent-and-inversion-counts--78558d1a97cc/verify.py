from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from math import factorial, comb


def vals(p):
    d=sum(p[i]>p[i+1] for i in range(len(p)-1))
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return d,inv

def exact(n,rmax):
    states={tuple(range(1,n+1)):Fraction(1)}
    all_p=list(permutations(range(1,n+1)))
    S=[[0]*(n+1) for _ in range(rmax+1)];S[0][0]=1
    for r in range(1,rmax+1):
        for k in range(1,n+1):S[r][k]=k*S[r-1][k]+S[r-1][k-1]
    cnt=0
    for r in range(rmax+1):
        # K exactly k occupied draws; for each k choose prefix k of uniform perm and sort suffix
        expected=defaultdict(Fraction)
        for k in range(n+1):
            if S[r][k]==0:continue
            falling=factorial(n)//factorial(n-k)
            w=Fraction(S[r][k]*falling,n**r*factorial(n))
            for p in all_p:
                new=p[:k]+tuple(sorted(p[k:]))
                expected[new]+=w
        assert states==expected,(n,r,len(states),len(expected))
        cnt+=len(states)
        d=sum(w*vals(p)[0] for p,w in states.items())
        i=sum(w*vals(p)[1] for p,w in states.items())
        # inversion exact identity
        I=Fraction(n*(n-1),4)*(1-Fraction(n-2,n)**r)
        assert i==I,(n,r,i,I)
        if r==rmax: break
        upd=defaultdict(Fraction)
        for p,w in states.items():
            for j in range(n):
                q=(p[j],)+p[:j]+p[j+1:]
                upd[q]+=w/n
        states=dict(upd)
    return cnt

if __name__=='__main__':
 for n,r in ((3,10),(4,10),(5,8),(6,6)):
  print(n,r,exact(n,r))

# Further exact identities and a finite-instance evaluation of the distributional comparison.
def checks():
    from math import erf,sqrt,exp,log
    for n in range(3,20):
        for r in range(0,13):
            mean=Fraction(n*(n-1)**r,n**r)
            both=Fraction(n*(n-2)**r,n**r)
            var=mean+Fraction(n*(n-1)*(n-2)**r,n**r)-mean*mean
            assert Fraction(0)<=var<=mean
            # the inversion mean is known exactly from the stationary Lehmer law
            i_mean=Fraction(n*(n-1),4)*(1-Fraction(n-2,n)**r)
            assert i_mean>=0
            # check conditional tail formulas against independent discrete uniform variables
        for missing in range(0,n+1):
            mu=Fraction(missing*(missing-1),4)
            v=Fraction(missing*(missing-1)*(2*missing+5),72)
            seq_mu=sum(Fraction(j,2) for j in range(missing))
            seq_var=sum(Fraction(j*(j+2),12) for j in range(missing))
            assert mu==seq_mu and v==seq_var
    for c in (-1.,0.,1.,3.):
        # These checks cover finite-size occupancy means, not a proof of weak convergence.
        for n in (500,5000,50000):
            for alpha,power in ((.5,.5),(.25,.75)):
                r=int(alpha*n*log(n)+c*n)
                observed=n*(1-1/n)**r / (n**power)
                desired=exp(-c)
                assert abs(observed-desired)<.10, (c,n,alpha,observed,desired)
    return True

if __name__=='__main__':
    checks()
    print('PASS: exact chain/mixture distributions, inversion moments, occupancy and Lehmer-tail formulas; finite-window consistency')
