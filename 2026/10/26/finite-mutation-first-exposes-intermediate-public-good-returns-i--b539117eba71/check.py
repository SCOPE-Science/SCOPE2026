"""Exact finite-state and independent perturbation verification for a public-goods model."""
from fractions import Fraction as Q
from itertools import product
from math import comb, exp


def hyp(a, b, draws, x):
    if not (0 <= x <= a and 0 <= draws-x <= b):
        return Q(0)
    return Q(comb(a,x)*comb(b,draws-x),comb(a+b,draws))


def payoff_gap(N,n,returns,c,k):
    if k==0 or k==N: return Q(0)
    cc=Q(0); dd=Q(0)
    for j in range(n):
        cc += hyp(k-1,N-k,n-1,j)*(Q(j+1,n)*returns[j+1]*c-c)
        dd += hyp(k,N-k-1,n-1,j)*Q(j,n)*returns[j]*c
    return cc-dd


def transition(N,mu,k):
    plus=Q(N-k,N)*(mu+(1-mu)*Q(k,2*(N-1)))
    minus=Q(k,N)*(mu+(1-mu)*Q(N-k,2*(N-1)))
    return plus,minus


def deriv_transition(N,mu,k,D):
    plus=Q(N-k,N)*(1-mu)*Q(k,N-1)*D/4
    minus=-Q(k,N)*(1-mu)*Q(N-k,N-1)*D/4
    return plus,minus


def stationary_and_slope(N,mu,gaps):
    # Computation A: full first-order perturbation of detailed-balance ratios.
    weights=[Q(1)]; dp=[Q(0)]
    for k in range(1,N+1):
        b, bp=transition(N,mu,k-1)[0],deriv_transition(N,mu,k-1,gaps[k-1])[0]
        d, dpn=transition(N,mu,k)[1],deriv_transition(N,mu,k,gaps[k])[1]
        ratio=b/d; ratio_d=bp/d-b*dpn/(d*d)
        dp.append(dp[-1]*ratio+weights[-1]*ratio_d)
        weights.append(weights[-1]*ratio)
    z=sum(weights); dz=sum(dp)
    ps=[v/z for v in weights]
    mean=sum(Q(i,N)*weights[i] for i in range(N+1))/z
    slope=(sum(Q(i,N)*dp[i] for i in range(N+1))*z-sum(Q(i,N)*weights[i] for i in range(N+1))*dz)/(z*z)
    return ps,mean,slope


def drift_slope(N,mu,gaps,ps):
    # Computation B: exact global stationary-drift identity.
    return (1-mu)/(4*mu*N*(N-1))*sum(ps[k]*k*(N-k)*gaps[k] for k in range(1,N))


def formula(mu,u,v,w,c=Q(1)):
    return c*(1-mu)*((w-9)+mu*(2*v+2*w-u-27))/(12*(1+3*mu)*(1+11*mu))


def numeric_stationary(N,n,mu,returns,c,delta):
    # Computation C: original nonlinear Fermi dynamics at nonzero selection.
    gaps=[float(payoff_gap(N,n,returns,c,k)) for k in range(N+1)]
    p=[1.0]
    for k in range(1,N+1):
        m=float(mu)
        f=lambda x: 1/(1+exp(-x))
        up=(N-k+1)/N*(m+(1-m)*(k-1)/(N-1)*f(delta*gaps[k-1]))
        down=k/N*(m+(1-m)*(N-k)/(N-1)*f(-delta*gaps[k]))
        p.append(p[-1]*up/down)
    z=sum(p)
    return sum(k*v for k,v in enumerate(p))/(N*z)


def test():
    trials=0
    for mu in [Q(1,7),Q(1,2),Q(4,5)]:
        for u,v,w in product([Q(1),Q(2),Q(8),Q(9)],repeat=3):
            returns=[Q(0),u,v,w]
            gaps=[payoff_gap(4,3,returns,Q(1),k) for k in range(5)]
            assert gaps[1]==(u-9)/9 and gaps[2]==(-u+2*v-9)/9 and gaps[3]==(-2*v+3*w-9)/9
            ps,mean,slope=stationary_and_slope(4,mu,gaps)
            assert mean==Q(1,2)
            den=(1+3*mu)*(1+11*mu)
            assert ps==[(1+mu)*(1+2*mu)/(2*den),4*mu*(1+2*mu)/den,3*mu*(1+5*mu)/den,4*mu*(1+2*mu)/den,(1+mu)*(1+2*mu)/(2*den)]
            assert slope==formula(mu,u,v,w)
            assert slope==drift_slope(4,mu,gaps,ps)
            trials+=1
    # For all these sizes, group size 2 has no first-order dependence on r(1).
    for N in range(3,12):
        for mu in [Q(1,10),Q(1,3),Q(3,4)]:
            old=None
            for r1 in [Q(1),Q(2),Q(7),Q(13)]:
                ret=[Q(0),r1,Q(9)]
                gaps=[payoff_gap(N,2,ret,Q(1),k) for k in range(N+1)]
                _,_,slope=stationary_and_slope(N,mu,gaps)
                if old is not None: assert slope==old
                old=slope
                trials+=1
    for v,expected in [(2,Q(-7,780)),(8,Q(5,780))]:
        mu=Q(1,2); ret=[Q(0),Q(2),Q(v),Q(9)]
        gaps=[payoff_gap(4,3,ret,Q(1),k) for k in range(5)]
        _,_,slope=stationary_and_slope(4,mu,gaps)
        assert slope==expected
        h=1e-5
        num=(numeric_stationary(4,3,mu,ret,Q(1),h)-numeric_stationary(4,3,mu,ret,Q(1),-h))/(2*h)
        assert abs(num-float(expected))<1e-8,(v,num,expected)
        assert (numeric_stationary(4,3,mu,ret,Q(1),0.001)>0.5)==(v==8)
        trials+=1
    print('PASS:',trials,'exact-rational comparisons; two direct nonlinear-transition tests')

if __name__=='__main__': test()
