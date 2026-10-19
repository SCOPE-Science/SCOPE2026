"""Reproduce rational cylinder counts and independently check transfer-series estimates."""
from fractions import Fraction as F
from itertools import product
import math


def order_bias_by_cylinders(p,n):
    q=1-p
    total=F(0)
    for bits in product((0,1),repeat=n):
        a,s=F(0),F(1)
        for b in bits[::-1]:
            if b==0: a,s=p*a,p*s
            else: a,s=1-q*a,-q*s
        root=a/(1-s)
        assert 0<=root<=1
        total+=abs(s)*(1-root)
    return total-F(1,2)


def modes(p,n):
    q=1-p; alpha=2*p-1; beta=p**3+q**3
    eta=p**4-q**4; sigma=p**4+q**4
    S=lambda u,v: sum(u**(n-1-j)*v**j for j in range(n))
    head=F(1,2)*alpha**n+q**2*S(alpha,beta)-q**3*S(beta,eta)
    residual_bound=n*q**4/p*sigma**(n-1)
    return head,residual_bound


def full_k_series(p,n,K=80):
    q=1-p
    sm=F(0)
    for k in range(K):
        ak=p**(k+1)+(-1)**k*q**(k+1)
        ak1=p**(k+2)+(-1)**(k+1)*q**(k+2)
        bk=(-1)**k*q**(k+1)
        sm+=bk*sum(ak**(n-1-j)*ak1**j for j in range(n))
    return F(1,2)-sm,n*q**(K+1)/p


def main():
    cases=0; signed=0
    for p in (F(1,5),F(1,3),F(2,5),F(1,2),F(2,3),F(4,5)):
        for n in range(1,10):
            w=order_bias_by_cylinders(p,n)
            head,bd=modes(p,n)
            assert abs(w-head)<=bd
            cases+=1
            if n<=6:
                sw,err=full_k_series(p,n,100)
                assert abs(w-sw)<=err
                signed+=1
            if p==F(1,2):
                assert w==F(1,2*(4**n-1))
            if p==F(2,3):
                explicit=(F(n,3)+F(1,4))*F(1,3)**n+F(1,4)*F(5,27)**n
                assert abs(w-explicit)<=F(n,54)*F(17,81)**(n-1)
    assert modes(F(1,3),12)[1] < F(1,1000000)
    print('VERIFY_OK:',cases,'exact rational cylinder-to-three-mode bounds;',signed,
          'independent finite-k power-series estimates; symmetric exact probabilities and resonant inequalities')
    print('Numerical asymptotic demonstrations (not infinite proofs):')
    for p in (F(1,5),F(1,3),F(2,5),F(2,3),F(4,5)):
        for n in (20,80):
            head,bd=modes(p,n)
            print(' p=',str(p),' n=',n,' head=',format(float(head),'.10g'),
                  ' rigorous_tail_le=',format(float(bd),'.3g'))
if __name__=='__main__': main()
