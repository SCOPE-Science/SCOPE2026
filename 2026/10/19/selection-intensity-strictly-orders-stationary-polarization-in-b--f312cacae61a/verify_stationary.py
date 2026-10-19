"""Exact finite-population verification for a public-goods Fermi process.

All checks use fractions. Reproduction: python3 verify_stationary.py
This finite computation supplements, and does not replace, the analytic theorem.
"""
from fractions import Fraction as F
from math import comb


def hypergeom_prob(total, successes, draws, k):
    if not (0 <= k <= successes and 0 <= draws-k <= total-successes):
        return F(0)
    return F(comb(successes, k)*comb(total-successes, draws-k), comb(total, draws))


def actual_gap(N, n, r1, rn, cost, i):
    def benefit(k):
        return cost * F(k, n) * (r1 + F(k-1, n-1)*(rn-r1))
    # Other cooperators are sampled without replacement. The two focal
    # strategies see populations with i-1 and i cooperating others.
    co = sum((hypergeom_prob(N-1, i-1, n-1, k)*benefit(k+1)
              for k in range(n)), F(0)) - cost
    de = sum((hypergeom_prob(N-1, i, n-1, k)*benefit(k)
              for k in range(n)), F(0))
    return co-de


def exact_gap(N,n,r1,rn,cost,i):
    return cost*(F(N-n,n*(N-1))*(r1 + F(2*(i-1),N-2)*(rn-r1))-1)


def transition(N,mu,sign,R,i):
    # The actual intensity is w=log(R)/abs(kappa), so exp(w Delta_i)
    # =R^(sign*(2i-N)). No transcendental rounding is used.
    z = F(R)**(sign*(2*i-N)) if sign else F(1)
    imitation = F(i*(N-i),N*N)
    up=(1-mu)*imitation*z/(1+z)+mu*F(N-i,N)
    down=(1-mu)*imitation/(1+z)+mu*F(i,N)
    return up,down


def stationary(N,mu,sign,R):
    weights=[F(1)]
    for i in range(N):
        up=transition(N,mu,sign,R,i)[0]
        down=transition(N,mu,sign,R,i+1)[1]
        assert up>0 and down>0
        weights.append(weights[-1]*up/down)
    denom=sum(weights)
    p=[x/denom for x in weights]
    for i in range(N+1):
        assert p[i]==p[N-i]
        up,down=transition(N,mu,sign,R,i)
        assert up+down<=1
        if i<N:
            assert p[i]*up==p[i+1]*transition(N,mu,sign,R,i+1)[1]
    assert sum(p)==1
    return p


def distance_distribution(p):
    N=len(p)-1
    distances=sorted(set(abs(2*i-N) for i in range(N+1)))
    mass=[sum((p[i] for i in range(N+1) if abs(2*i-N)==d),F(0)) for d in distances]
    return distances,mass


def strict_order(a,b,direction):
    # direction +1 means b strictly more polarized than a.
    assert len(a)==len(b) and len(a)>1
    checks=0
    for cut in range(1,len(a)):
        old=sum(a[cut:]); new=sum(b[cut:])
        assert (new>old if direction>0 else new<old)
        checks+=1
    # A stronger family of inequalities: the likelihood ratio b/a
    # is strictly monotone in distance.
    for i in range(len(a)-1):
        assert (b[i+1]*a[i]>b[i]*a[i+1] if direction>0
                else b[i+1]*a[i]<b[i]*a[i+1])
        checks+=1
    return checks


def main():
    pay_checks=stat_checks=order_checks=0
    for N in range(3,14):
        for n in range(2,N):
            rn=F(n*(N-1),N-n)
            for r1,sign in ((rn/4,1),(2*rn,-1),(rn,0)):
                cost=F(5,7)
                for i in range(1,N):
                    delta=actual_gap(N,n,r1,rn,cost,i)
                    assert delta==exact_gap(N,n,r1,rn,cost,i)
                    kappa=cost*F(N-n,n*(N-1)*(N-2))*(rn-r1)
                    assert delta==kappa*(2*i-N)
                    pay_checks+=2
                for mu in (F(1,17),F(1,3),F(3,4)):
                    levels=[]
                    for R in (1,2,3,5):
                        p=stationary(N,mu,sign,R)
                        ds,m=distance_distribution(p)
                        levels.append(m)
                        stat_checks+=1
                    for lo,hi in zip(levels,levels[1:]):
                        if sign:
                            order_checks+=strict_order(lo,hi,sign)
                        else:
                            assert lo==hi
                            order_checks+=len(lo)
    print('PASS: hypergeometric/payoff identities',pay_checks)
    print('PASS: stationary distributions and balance',stat_checks)
    print('PASS: strict ordering inequalities/equalities',order_checks)
    print('PASS: exact-rational finite verification complete')

if __name__=='__main__': main()
