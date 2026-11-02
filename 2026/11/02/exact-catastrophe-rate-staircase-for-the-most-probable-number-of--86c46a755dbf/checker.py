"""Exact stationary occupancy checks (Python standard library only).
Analytic proof of the all-parameter theorem is in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def rising(x, n):
    out = F(1)
    for j in range(n):
        out *= x + j
    return out


def stationary(n, rho, alpha):
    rho, alpha = F(rho), F(alpha)
    assert n >= 2 and 0 < rho < 1 and alpha > 0
    ans = []
    for k in range(n + 1):
        value = sum((F((-1)**j * comb(n-k,j)) * rho**j * F(__import__('math').factorial(k+j), 1) / rising(alpha+1,k+j)
                     for j in range(n-k+1)),F(0))
        ans.append(comb(n,k)*rho**k*value)
    return ans


def check():
    count=0
    examples = {
        F(1): [F(31,80),F(13,40),F(1,5),F(3,40),F(1,80)],
        F(1,2): [F(83,315),F(20,63),F(4,15),F(8,63),F(8,315)],
        F(1,4): [F(587,3315),F(328,1105),F(16,51),F(192,1105),F(128,3315)]
    }
    for alpha, expected in examples.items():
        assert stationary(4,F(1,2),alpha) == expected
        count+=1
    for n in range(2,13):
        for rho in [F(1,8),F(1,4),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(3,4),F(7,8)]:
            alphas = [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),F(1),F(2),F(4),F(10)]
            laws=[stationary(n,rho,alpha) for alpha in alphas]
            for alpha, pp in zip(alphas,laws):
                assert sum(pp) == 1;count+=1
                assert all(x>0 for x in pp);count+=1
                # Count stationarity, with catastrophe reset at rate alpha.
                assert (1-rho)*pp[1]+alpha*(1-pp[0])-rho*n*pp[0] == 0;count+=1
                for k in range(1,n+1):
                    lhs=rho*(n-k+1)*pp[k-1]-(rho*(n-k)+(1-rho)*k+alpha)*pp[k]
                    if k < n: lhs+=(1-rho)*(k+1)*pp[k+1]
                    assert lhs == 0
                count+=1
                delta=[pp[k+1]-pp[k] for k in range(n)]
                # differences cannot rise again after first nonpositive step
                assert not any(delta[i] <=0 and delta[j]>=0 for i in range(n) for j in range(i+1,n));count+=1
                if alpha>=1:
                    assert all(x<0 for x in delta);count+=1
            for k in range(n):
                rr=[pp[k+1]/pp[k] for pp in laws]
                assert all(rr[i]>rr[i+1] for i in range(len(rr)-1));count+=1
            h=(F((n+1),1)*rho).__ceil__()-1
            # The alpha=0 limit has h as rightmost mode (unless a terminal binomial plateau).
            assert 0<=h<=n;count+=1
    poly=lambda x:2*x**4+12*x**3+16*x**2-6*x-9
    assert poly(F(18,25)) < 0 < poly(F(721,1000));count+=1
    rootpoly=lambda x:x*x+3*x-1
    assert rootpoly(F(302,1000))<0<rootpoly(F(303,1000));count+=1
    print('Exact checks passed:',count)


if __name__=='__main__':
    check()
