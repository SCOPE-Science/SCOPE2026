from fractions import Fraction
from itertools import product
from math import comb


def p(N):
    return Fraction(comb(2*N,N),4**N)


def simple_formula(n):
    N=n//2
    pn=p(N)
    cov=-Fraction(2*N*(2*N+1),3)*pn
    mu=Fraction(2*N+1)*pn-1
    varL=2*N-3*mu-mu*mu
    varE=2*n*(n-1)
    return cov,mu,varL,varE


def simple_stats(n):
    total=1<<n
    EL=Fraction(0); EE=Fraction(0); ELE=Fraction(0); EL2=Fraction(0); EE2=Fraction(0)
    for bits in range(total):
        s=0; L=0
        for i in range(n):
            s += 1 if (bits>>i)&1 else -1
            if s==0:
                L += 1
        E=s*s
        EL += Fraction(L,total)
        EE += Fraction(E,total)
        ELE += Fraction(L*E,total)
        EL2 += Fraction(L*L,total)
        EE2 += Fraction(E*E,total)
    return EL,EE,ELE-EL*EE,EL2-EL*EL,EE2-EE*EE


def weighted_walk_check(n):
    # Centered but nonsymmetric increments: P(-1)=1/2, P(0)=1/4, P(2)=1/4.
    vals=[-1,0,2]
    probs=[Fraction(1,2),Fraction(1,4),Fraction(1,4)]
    tau=sum(pr*x*x for x,pr in zip(vals,probs))
    EL=Fraction(0); EE=Fraction(0); ELE=Fraction(0)
    returns=[Fraction(0) for _ in range(n+1)]
    for inds in product(range(3), repeat=n):
        pr=Fraction(1)
        s=0; L=0
        path=[]
        for t,j in enumerate(inds,1):
            pr*=probs[j]
            s+=vals[j]
            path.append(s)
            if s==0:
                L+=1
        E=s*s
        EL+=pr*L; EE+=pr*E; ELE+=pr*L*E
        for k,x in enumerate(path,1):
            if x==0:
                returns[k]+=pr
    cov=ELE-EL*EE
    rhs=-tau*sum(Fraction(k)*returns[k] for k in range(1,n+1))
    assert cov==rhs
    return tau,cov


enum_checks=0
paths=0
for n in range(2,19):
    EL,EE,cov,varL,varE=simple_stats(n)
    f_cov,mu,f_varL,f_varE=simple_formula(n)
    assert EL==mu
    assert EE==n
    assert cov==f_cov
    assert varL==f_varL
    assert varE==f_varE
    paths += 1<<n
    enum_checks += 5

weighted_checks=0
for n in range(1,9):
    tau,cov=weighted_walk_check(n)
    assert tau==Fraction(3,2)
    weighted_checks += 1

binomial_checks=0
s1=Fraction(0)
s2=Fraction(0)
for N in range(1,1501):
    pn=p(N)
    s1 += pn
    s2 += N*pn
    rhs1=Fraction(2*N+1)*pn-1
    assert s1==rhs1
    rhs2=Fraction(N*(2*N+1),3)*pn
    assert s2==rhs2
    binomial_checks += 2

print('VERIFY_OK')
print(f'simple_paths_enumerated={paths}')
print(f'simple_exact_checks={enum_checks}')
print(f'nonsymmetric_general_checks={weighted_checks}')
print(f'central_binomial_checks={binomial_checks}')
print('max_simple_n=18')
print('max_binomial_N=1500')
