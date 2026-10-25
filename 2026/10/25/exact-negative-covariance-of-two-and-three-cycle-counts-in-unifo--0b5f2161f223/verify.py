"""Exact finite-state replay for parallel-pair / triangle mixed covariance.
Uses unlabelled vertex-pair multiplicities for triangle counting, independent of the analytic indicator expansion.
"""
from itertools import product, combinations
from math import factorial
from fractions import Fraction as Q

def solve(n,m):
    choices=[list(product(range(1,j),repeat=m)) for j in range(2,n+1)]
    Tsum=Psum=PTsum=0
    cases=0
    for cfg in product(*choices):
        adjacency={}
        P=0
        for j, targets in enumerate(cfg,2):
            for a,b in combinations(range(m),2):
                P += targets[a]==targets[b]
            for target in targets:
                adjacency[(target,j)]=adjacency.get((target,j),0)+1
        T=sum(adjacency.get((i,j),0)*adjacency.get((i,k),0)*adjacency.get((j,k),0) for i,j,k in combinations(range(1,n+1),3))
        Psum += P
        Tsum += T
        PTsum += P*T
        cases+=1
    covariance=Q(PTsum,cases)-Q(Psum,cases)*Q(Tsum,cases)
    predicted=-m*m*(m-1)*sum((Q(q-1,q**3) for q in range(2,n)),Q(0))
    assert covariance==predicted,(n,m,covariance,predicted)
    return cases, covariance, Q(Psum,cases), Q(Tsum,cases)

def main():
    counts=0
    for n,m in [(2,2),(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(5,3),(3,4),(4,4)]:
        k,cov,mean_p,mean_t=solve(n,m)
        counts+=k
        print('PASS',n,m,'cases',k,'cov',cov,'means',mean_p,mean_t)
    print('VERIFY_OK',counts,'exact attachment configurations')
if __name__=='__main__':main()
