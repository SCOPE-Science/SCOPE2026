"""Reproduce finite-mutation weak-selection identities for public-goods imitation.

Run: python verify.py. Python standard library only.
All symbolic equalities in this checker use exact Fraction arithmetic.
"""
from fractions import Fraction as F
from math import comb, exp


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def payoff_difference(N, group, returns, k):
    """Exact C minus D payoff, contribution cost normalized to one."""
    denom = comb(N - 1, group - 1)
    cooperator = F(-1)
    defector = F(0)
    for j in range(group):
        p_c = F(choose(k - 1, j) * choose(N - k, group - 1 - j), denom)
        p_d = F(choose(k, j) * choose(N - k - 1, group - 1 - j), denom)
        cooperator += p_c * F((j + 1) * returns[j], group)
        if j >= 1:
            defector += p_d * F(j * returns[j - 1], group)
    return cooperator - defector


def neutral_probabilities(N, mutation):
    """Stationary weights via birth--death detailed balance; distinct peer."""
    def plus(k):
        return F(N-k, N) * (mutation + (1-mutation) * F(k, 2*(N-1)))
    def minus(k):
        return F(k, N) * (mutation + (1-mutation) * F(N-k, 2*(N-1)))
    weights = [F(1)]
    for k in range(1, N+1):
        weights.append(weights[-1] * plus(k-1) / minus(k))
    Z = sum(weights)
    return [v/Z for v in weights], plus, minus


def derivative_by_chain(N, group, returns, mutation):
    """Differentiate exact stationary detailed-balance products at w=0."""
    pi, plus, minus = neutral_probabilities(N, mutation)
    log_derivs = [F(0)]
    for k in range(1, N+1):
        left = k-1
        right = k
        pp = (1-mutation)*F(left*(N-left), N*(N-1)) * payoff_difference(N,group,returns,left)/4 if 0<left<N else F(0)
        mm = -(1-mutation)*F(right*(N-right), N*(N-1)) * payoff_difference(N,group,returns,right)/4 if 0<right<N else F(0)
        log_derivs.append(log_derivs[-1] + pp/plus(left) - mm/minus(right))
    mean_log = sum(pi[k]*log_derivs[k] for k in range(N+1))
    return sum(F(k,N)*pi[k]*(log_derivs[k]-mean_log) for k in range(N+1))


def derivative_by_drift(N, group, returns, mutation):
    """Independent stationary mean-drift balance linearization."""
    pi,_,_ = neutral_probabilities(N, mutation)
    return (1-mutation)/(4*mutation) * sum(pi[k]*F(k*(N-k),N*(N-1))*payoff_difference(N,group,returns,k) for k in range(1,N))


def three_group_formula(N, returns, mutation):
    r1,r2,r3=returns
    u=mutation
    numerator = (3*(N-3)*(1+(N-2)*u)*r3
                 +(N-3)*(N-1)*u*(2*r2-r1)
                 -3*(N-1)*(3+(4*N-7)*u))
    return (1-u)*numerator / (12*(3+(4*N-7)*u)*(1+(4*N-5)*u))


def mean_at_selection(N, group, returns, mutation, selection):
    """Floating check only, independent of the exact proof."""
    def step(k, direction):
        if direction == 1:
            if k==N: return 0.
            delta=float(payoff_difference(N,group,returns,k)) if k else 0.
            return (N-k)/N*(float(mutation)+(1-float(mutation))*k/(N-1)/(1+exp(-selection*delta)))
        if not k: return 0.
        delta=float(payoff_difference(N,group,returns,k)) if k<N else 0.
        return k/N*(float(mutation)+(1-float(mutation))*(N-k)/(N-1)/(1+exp(selection*delta)))
    weights=[1.0]
    for k in range(1,N+1):weights.append(weights[-1]*step(k-1,1)/step(k,-1))
    return sum(k*w for k,w in enumerate(weights))/(N*sum(weights))


def run():
    count=0
    for N in range(4,11):
        for mu in (F(1,50),F(1,5),F(1,2),F(4,5)):
            for r in ((2,3,10),(2,7,10),(1,5,11),(3,4,7),(7,13,19)):
                r=tuple(map(F,r))
                a=derivative_by_chain(N,3,r,mu)
                b=derivative_by_drift(N,3,r,mu)
                c=three_group_formula(N,r,mu)
                assert a==b==c,(N,mu,r,a,b,c)
                count+=1
    for N in range(3,11):
        for mu in (F(1,50),F(1,5),F(1,2),F(4,5)):
            a=derivative_by_chain(N,2,(F(1),F(11)),mu)
            b=derivative_by_chain(N,2,(F(7),F(11)),mu)
            assert a==b,(N,mu,a,b)
            count+=1
    mu=F(1,2)
    low=derivative_by_chain(4,3,(F(2),F(3),F(10)),mu)
    high=derivative_by_chain(4,3,(F(2),F(7),F(10)),mu)
    assert low==F(-1,780) and high==F(7,780)
    assert mean_at_selection(4,3,(2,3,10),mu,0.01)<0.5
    assert mean_at_selection(4,3,(2,7,10),mu,0.01)>0.5
    # At mu=1/3 the low schedule has exactly zero first-order response.
    assert derivative_by_chain(4,3,(F(2),F(3),F(10)),F(1,3))==0
    assert derivative_by_chain(4,3,(F(2),F(7),F(10)),F(1,3))>0
    print(f"PASS: {count} exact chain/drift/formula and two-player checks; exact example and numerical sign checks.")
    print('N=4, mutation=1/2: low =',low,', high =',high)

if __name__=='__main__':
    run()
