#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math

def H(m,p=1):
    return sum((Fraction(1,k**p) for k in range(1,m+1)),Fraction(0))

def trees(n):
    for pars in product(*[range(1,j) for j in range(2,n+1)]):
        parents=[None,None]+list(pars)
        children=[0]*(n+1)
        D=0
        for j in range(2,n+1):
            p=parents[j]
            children[p]+=1
            D += (p==1)
        L=sum(children[i]==0 for i in range(2,n+1))
        yield D,L,parents,children

def run():
    trees_checked=0
    labeled_leaf_cov_checks=0
    attachment_leaf_cov_checks=0
    global_cov_checks=0
    marginal_checks=0
    recursion_checks=0
    correlation_checks=0

    for n in range(2,10):
        vals=list(trees(n))
        N=math.factorial(n-1)
        assert len(vals)==N
        trees_checked+=N
        meanD=Fraction(sum(v[0] for v in vals),N)
        meanL=Fraction(sum(v[1] for v in vals),N)
        covDL=Fraction(sum(v[0]*v[1] for v in vals),N)-meanD*meanL
        varD=Fraction(sum(v[0]*v[0] for v in vals),N)-meanD*meanD
        varL=Fraction(sum(v[1]*v[1] for v in vals),N)-meanL*meanL

        assert meanD==H(n-1,1)
        assert meanL==Fraction(n,2)
        assert varD==H(n-1,1)-H(n-1,2)
        if n>=3:
            assert varL==Fraction(n,12)
        else:
            assert varL==0
        marginal_checks+=4

        for i in range(2,n+1):
            meanY=Fraction(sum(v[3][i]==0 for v in vals),N)
            meanDY=Fraction(sum(v[0]*(v[3][i]==0) for v in vals),N)
            cov=meanDY-meanD*meanY
            assert meanY==Fraction(i-1,n-1)
            assert cov==Fraction(n-i,(n-1)*(n-1))
            labeled_leaf_cov_checks+=2

        for j in range(2,n+1):
            meanA=Fraction(sum(v[2][j]==1 for v in vals),N)
            meanAL=Fraction(sum((v[2][j]==1)*v[1] for v in vals),N)
            cov=meanAL-meanA*meanL
            target=Fraction(0) if j==2 else Fraction(1,2*(n-1))
            assert cov==target
            attachment_leaf_cov_checks+=1

        assert covDL==Fraction(n-2,2*(n-1))
        global_cov_checks+=1
        if n>=3:
            rho2=covDL*covDL/(varD*varL)
            target=Fraction(3*(n-2)*(n-2),(n-1)*(n-1)*n)/varD
            assert rho2==target
            correlation_checks+=1

    # Independent first/second-moment recursion for leaves.
    mu=Fraction(1)
    second=Fraction(1)
    for n in range(3,501):
        # L_n=L_{n-1}+1-B, B|L~Bernoulli(L/(n-1)).
        old_mu=mu
        old_second=second
        mu=old_mu+1-old_mu/Fraction(n-1)
        second=old_second+2*old_mu+1-(2*old_second+old_mu)/Fraction(n-1)
        assert mu==Fraction(n,2)
        assert second-mu*mu==Fraction(n,12)
        recursion_checks+=2

    print(
        "VERIFY_OK "
        f"trees_checked={trees_checked} "
        f"labeled_leaf_cov_checks={labeled_leaf_cov_checks} "
        f"attachment_leaf_cov_checks={attachment_leaf_cov_checks} "
        f"global_cov_checks={global_cov_checks} "
        f"marginal_checks={marginal_checks} "
        f"recursion_checks={recursion_checks} "
        f"correlation_checks={correlation_checks}"
    )

if __name__=="__main__":
    run()
