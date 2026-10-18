"""Exact finite-state and finite-graph checks for finite-memory Pólya threshold graphs.
Run: python verify.py (requires SymPy).
Finite checks corroborate but do not substitute for the asymptotic proof.
"""
from itertools import product
from sympy import Matrix, Rational, eye, ones, zeros, diag, rf, simplify


def covariance_sequence(M, a, b, n):
    k = a+b
    rho = Rational(a,k)
    v = rho*(1-rho)
    cs=[v] + [v/(k+1)]*min(M,n-1)
    for h in range(M+1,n):
        cs.append(sum(cs[h-j] for j in range(1,M+1))/(k+M))
    return cs


def explicit_markov_check(M, a, b):
    states=list(product((0,1), repeat=M))
    ix={s:i for i,s in enumerate(states)}
    L=len(states)
    pi=Matrix([[rf(a,sum(s))*rf(b,M-sum(s))/rf(a+b,M) for s in states]])
    P=zeros(L,L)
    for i,s in enumerate(states):
        p=Rational(a+sum(s),a+b+M)
        P[i,ix[s[1:]+(1,)]] += p
        P[i,ix[s[1:]+(0,)]] += 1-p
    assert pi*P==pi and sum(pi)==1
    rho=Rational(a,a+b)
    v=rho*(1-rho)
    centered=Matrix([s[-1]-rho for s in states])
    h=(eye(L)-P+ones(L,1)*pi).inv()*centered
    tau=simplify(2*(pi*diag(*centered)*h)[0]/v-1)
    proposed=Rational((M+a+b)*(M+a+b+1),(a+b)*(a+b+1))
    assert tau==proposed
    return tau


def finite_graph_check(M,a,b,n):
    k=a+b
    mean=Rational(a,k)*n*(n-1)/2
    E=0
    E2=0
    total=0
    for z in product((0,1), repeat=n):
        s=sum(z[:M])
        prob=rf(a,s)*rf(b,M-s)/rf(k,M)
        for j in range(M,n):
            p=Rational(a+sum(z[j-M:j]),k+M)
            prob*=p if z[j] else (1-p)
        edges=sum(j*z[j] for j in range(1,n))
        E+=prob*edges
        E2+=prob*edges*edges
        total+=prob
    assert total==1 and E==mean
    cs=covariance_sequence(M,a,b,n)
    predicted=sum((j*j)*cs[0] for j in range(1,n))
    for h in range(1,n-1):
        predicted+=2*cs[h]*sum(j*(j+h) for j in range(1,n-h))
    assert simplify(E2-E*E-predicted)==0


if __name__=='__main__':
    n_markov=0
    for M,a,b in [(M,1,1) for M in range(1,6)]+[(M,2,3) for M in range(1,4)]:
        explicit_markov_check(M,a,b)
        n_markov+=1
    n_graph=0
    for a,b in [(1,1),(2,3)]:
        for M in range(1,4):
            for n in range(max(3,M+1),9):
                finite_graph_check(M,a,b,n)
                n_graph+=1
    print(f'PASS: {n_markov} exact stationary Markov-chain long-run variance checks; '
          f'{n_graph} exhaustive exact finite-graph moment checks.')
