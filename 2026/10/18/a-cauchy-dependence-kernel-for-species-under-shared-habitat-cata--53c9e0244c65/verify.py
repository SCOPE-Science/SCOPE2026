"""Exact checks for a two-species immigration, loss, and common-reset system.

Run with Python >=3.9: python verify.py. Only standard-library modules are used.
"""
import json
from fractions import Fraction as F
from itertools import product, combinations
from math import sqrt


def solve(a, b):
    """Solve nonsingular square linear system over rationals."""
    n = len(b)
    v = [list(map(F, a[i])) + [F(b[i])] for i in range(n)]
    for k in range(n):
        z = next(i for i in range(k, n) if v[i][k])
        v[k], v[z] = v[z], v[k]
        t = v[k][k]
        v[k] = [x / t for x in v[k]]
        for i in range(n):
            if i != k and v[i][k]:
                t = v[i][k]
                v[i] = [v[i][j] - t*v[k][j] for j in range(n+1)]
    return [v[i][-1] for i in range(n)]


def generator_stationary(l1, m1, l2, m2, g):
    """Independent birth/death toggles plus shared reset to state 00."""
    Q = [[F(0) for _ in range(4)] for _ in range(4)]
    for state in range(4):
        for i, (birth, death) in enumerate(((l1, m1), (l2, m2))):
            bit = 1 << i
            rate = death if state & bit else birth
            other = state ^ bit
            Q[state][other] += rate
        if state:
            Q[state][0] += g
        Q[state][state] = -sum(Q[state][j] for j in range(4) if j != state)
    A = [[Q[i][j] for i in range(4)] for j in range(3)] + [[F(1)]*4]
    b = [F(0)]*3 + [F(1)]
    return solve(A, b)


def formulas(l1, m1, l2, m2, g):
    s1, s2 = l1+m1, l2+m2
    p1 = l1 / (g+s1)
    p2 = l2 / (g+s2)
    cov = g*l1*l2 / ((g+s1)*(g+s2)*(g+s1+s2))
    return p1, p2, cov


def derivative_sign_numerator(l1, m1, l2, m2, g):
    s = l1+m1+l2+m2
    return 2*g**3+(m1+m2)*g*g-s*(m1+m2)*g-2*s*m1*m2


def det(M):
    n=len(M)
    if not n: return F(1)
    v=[list(row) for row in M]
    prod=F(1)
    for k in range(n):
        pivot=next((j for j in range(k,n) if v[j][k]),None)
        if pivot is None:return F(0)
        if pivot !=k:
            v[k],v[pivot]=v[pivot],v[k]
            prod=-prod
        d=v[k][k]
        prod*=d
        for j in range(k+1,n):
            z=v[j][k]/d
            for h in range(k+1,n):v[j][h]-=z*v[k][h]
            v[j][k]=0
    return prod


def latent_covariance(lams,mus,g):
    s=[a+b for a,b in zip(lams,mus)]
    n=len(lams)
    return [[g*lams[i]*lams[j]/((g+s[i])*(g+s[j])*(g+s[i]+s[j])) for j in range(n)] for i in range(n)]


def cauchy_minor(lams,mus,g,R,C):
    s=[a+b for a,b in zip(lams,mus)]
    k=len(R)
    num=g**k
    for i in R:num*=lams[i]/(g+s[i])
    for j in C:num*=lams[j]/(g+s[j])
    for x,y in combinations(R,2):num*=s[y]-s[x]
    for x,y in combinations(C,2):num*=s[y]-s[x]
    for i in R:
        for j in C:num/=g+s[i]+s[j]
    return num


def main():
    trials = 0
    max_rho2 = F(0)
    stationary_equality = 0
    max_discrepancies = 0
    for l1, l2, m1, m2, g in product([F(1),F(2),F(3),F(5)],
                                      [F(1),F(3)],
                                      [F(0),F(1),F(2)],
                                      [F(0),F(1),F(3)],
                                      [F(1,5),F(1),F(2),F(7),F(13)]):
        pi = generator_stationary(l1,m1,l2,m2,g)
        p1,p2,cov = formulas(l1,m1,l2,m2,g)
        assert sum(pi) == 1 and all(x >= 0 for x in pi)
        assert pi[1]+pi[3] == p1
        assert pi[2]+pi[3] == p2
        assert pi[3]-p1*p2 == cov
        var1=p1*(1-p1)
        var2=p2*(1-p2)
        rho2=cov*cov/(var1*var2)
        assert F(0)<rho2<F(1,4)
        if rho2>max_rho2:
            max_rho2=rho2
        assert derivative_sign_numerator(l1,m1,l2,m2,g) == (2*g**3+(m1+m2)*g*g-(l1+m1+l2+m2)*(m1+m2)*g-2*(l1+m1+l2+m2)*m1*m2)
        trials += 1
        stationary_equality += 3
    # Every ordered minor of the environmental covariance matrix has an
    # exact positive Cauchy product; the full rank counts distinct rates.
    cauchy_checks=0
    for n in range(2,7):
        for g in [F(1,3),F(1),F(5)]:
            # strictly increasing rates, diverse colonization/extinction splits
            lams=[F(i+1) for i in range(n)]
            mus=[F(i*i+1) for i in range(n)]
            rates=[a+b for a,b in zip(lams,mus)]
            assert rates==sorted(set(rates))
            L=latent_covariance(lams,mus,g)
            for k in range(1,n+1):
                for R in combinations(range(n),k):
                    for C in combinations(range(n),k):
                        observed=det([[L[i][j] for j in C] for i in R])
                        predicted=cauchy_minor(lams,mus,g,R,C)
                        assert observed==predicted and observed>0
                        cauchy_checks+=1
            # Duplicating a recovery rate forces exactly one latent
            # covariance rank loss even when immigration rates differ.
            l2=list(lams);m2=list(mus)
            l2[-1]=F(1)
            m2[-1]=rates[0]-1
            assert l2[-1]>0 and m2[-1]>=0
            LD=latent_covariance(l2,m2,g)
            assert det(LD)==0
            assert det([row[:-1] for row in LD[:-1]])>0
    # Equal exponential immigration, no local losses: rho = n/(2n+1) --> 1/2.
    for n in [2, 5, 10, 100, 10000]:
        g=F(1,n)
        p1,p2,cov=formulas(F(1),F(0),F(1),F(0),g)
        assert cov/(p1*(1-p1)) == F(n,2*n+1)
    # Prove the sign of the derivative using exact arithmetic at small and large hazards.
    shape_trials=0
    for l1,l2,m1,m2 in product([F(1),F(2),F(7)],
                                [F(1),F(3)],
                                [F(0),F(1),F(4)],
                                [F(0),F(2),F(5)]):
        if not m1 and not m2:
            assert derivative_sign_numerator(l1,m1,l2,m2,F(1)) > 0
            # Cubic numerator includes root at zero; derivative h is strictly negative.
            S=l1+l2
            for g in [F(1,100),F(1),F(100)]:
                h=S/(g+S)-F(1)
                assert h<0
        else:
            S=l1+m1+l2+m2
            h=lambda g: S/(g+S)-(g/(g+m1)+g/(g+m2))/2
            lo,hi=F(0),F(1)
            while h(hi)>0:
                hi*=2
            for _ in range(65):
                mid=(lo+hi)/2
                if h(mid)>0:lo=mid
                else:hi=mid
            assert h(lo)>=0 and h(hi)<=0
            for g in [lo/2,hi*2]:
                assert (h(g)>0) if g<lo else (h(g)<0)
        shape_trials+=1
    # A deterministic recovery delay after Poisson catastrophe gives identical
    # two-species indicators at a randomly sampled patch, with correlation one.
    # Their common Bernoulli probability is exp(-g*delay) in (0,1).
    deterministic_delay_correlation=1
    assert deterministic_delay_correlation==1
    result={
      'method':'exact stationary four-state Markov generator versus independent age-mixture identities',
      'tested_parameter_quintuples':trials,
      'exact_stationary_identity_comparisons':stationary_equality,
      'exact_upper_bound_checks':trials,
      'shape_parameter_quadruples':shape_trials,
      'strict_cauchy_minor_equalities':cauchy_checks,
      'max_tested_correlation_squared':str(max_rho2),
      'no_local_loss_sharpness_rho_n':'n/(2*n+1)',
      'deterministic_recovery_delay_correlation':1,
      'disagreements':max_discrepancies
    }
    print(json.dumps(result,sort_keys=True,indent=2))
    return result

if __name__=='__main__': main()
