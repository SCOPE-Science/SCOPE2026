"""Exact checks for competing SI infections on K_{2,n}.

Requires only Python's standard library. All finite-state checks use Fractions.
The asymptotic theorem is proved analytically in RESULT.md; numerical
convergence checks here are diagnostic, not a substitute for that proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, pi, sqrt


def finite_integral(n, alpha, beta):
    """Exact rational integral for the opposite type taking the second hub."""
    alpha, beta = F(alpha), F(beta)
    assert n >= 2 and alpha > 0 and beta > 0
    d = (n - 1) * alpha + beta
    return beta * sum((F(factorial(n-2), factorial(n-2-k)) * alpha**k / d**(k+1)
                       for k in range(n-1)), F(0))


def conditional_first_hub_pmf(n, alpha, beta, first_type):
    """Final number of type-1 vertices, conditional on first hub type."""
    alpha, beta = F(alpha), F(beta)
    r = (n-1)*alpha+beta
    answer = [F(0)]*(n+3)
    reach = F(1)
    for k in range(1,n):
        # k peripheral vertices have the first hub's infection type.
        # All other peripheral vertices, except the opposite seed, remain susceptible.
        chance_split = reach*beta/r
        left = n-k-1
        q = alpha/(alpha+beta)
        # J = number of remaining leaves of first hub's type.
        for j in range(left+1):
            chance = chance_split * F(comb(left,j)) * q**j * (1-q)**(left-j)
            n_type1 = k+1+j if first_type == 1 else 2+left-j
            answer[n_type1] += chance
        # Second hub gets the first hub's type; only the opposite seed loses.
        answer[n+1 if first_type == 1 else 1] += reach * alpha*k/r
        reach *= alpha*left/r
    assert reach == 0
    assert sum(answer) == 1
    return tuple(answer)


def pmf_via_race(n, lam1, lam2):
    q = F(lam1)/(F(lam1)+F(lam2))
    a = conditional_first_hub_pmf(n,lam1,lam2,1)
    b = conditional_first_hub_pmf(n,lam2,lam1,2)
    return tuple(q*x+(1-q)*y for x,y in zip(a,b))


def pmf_via_independent_ctmc(n, lam1, lam2):
    """Directly solve the full acyclic four-count epidemic CTMC."""
    lam1, lam2 = F(lam1), F(lam2)
    @lru_cache(None)
    def solve(x,y,h1,h2):
        if x+y==n and h1 and h2:
            z=[F(0)]*(n+3)
            z[x+(h1==1)+(h2==1)]=F(1)
            return tuple(z)
        moves=[]
        uninfected=n-x-y
        for typ,rr in ((1,lam1),(2,lam2)):
            hubs=(h1==typ)+(h2==typ)
            if hubs and uninfected:
                moves.append((rr*hubs*uninfected,
                             (x+(typ==1),y+(typ==2),h1,h2)))
        for idx,h in enumerate((h1,h2)):
            if h==0:
                for typ,count,rr in ((1,x,lam1),(2,y,lam2)):
                    if count:
                        hh=[h1,h2]
                        hh[idx]=typ
                        moves.append((rr*count,(x,y,hh[0],hh[1])))
        total=sum((rr for rr,_ in moves),F(0))
        assert total>0
        out=[F(0)]*(n+3)
        for rr,state in moves:
            sub=solve(*state)
            for i,val in enumerate(sub):out[i]+=rr*val/total
        return tuple(out)
    return solve(1,1,0,0)


def split_prob(n,lam1,lam2):
    q=F(lam1)/(F(lam1)+F(lam2))
    return q*finite_integral(n,lam1,lam2)+(1-q)*finite_integral(n,lam2,lam1)


def main():
    assertions=0
    rates=((1,1),(2,1),(1,4),(3,2),(F(1,3),F(2,5)))
    for n in range(2,11):
        for a,b in rates:
            p1=pmf_via_race(n,a,b)
            p2=pmf_via_independent_ctmc(n,a,b)
            for x,y in zip(p1,p2):
                assert x==y
                assertions+=1
            p=split_prob(n,a,b)
            assert p==1-p1[1]-p1[n+1]
            assertions+=1
            assert sum(p1)==1
            assertions+=1
            # Directly check the two no-split terminal masses.
            q=F(a)/(F(a)+F(b))
            assert p1[n+1]==q*(1-finite_integral(n,a,b))
            assert p1[1]==(1-q)*(1-finite_integral(n,b,a))
            assertions+=2
            assert p==split_prob(n,b,a)
            assertions+=1
            if n>2:
                assert p<split_prob(n-1,a,b)
                assertions+=1
    # An asymptotic diagnostic, not proof. Rational rate pairs and exact sums.
    for a,b in rates:
        aa=float(a);bb=float(b)
        for n in (100,300,1000):
            p=float(split_prob(n,a,b))
            expansion=sqrt(pi/(2*n))-(aa/bb+bb/aa-F(2,3))/n
            assert abs(p-expansion)<20/n**1.5
            assertions+=1
    assert split_prob(2,1,1)==F(1,2)
    assert split_prob(4,1,1)==F(13,32)
    assertions+=2
    print('PASS:',assertions,'exact-rational assertions and asymptotic diagnostics')
    print('P(split), n=4, equal rates =',split_prob(4,1,1))
    print('P(split), n=8, rates 2:1 =',split_prob(8,2,1))

if __name__=='__main__':main()
