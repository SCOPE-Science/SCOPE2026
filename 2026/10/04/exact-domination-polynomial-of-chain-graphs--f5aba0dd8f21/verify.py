from itertools import product
from math import comb


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def add_shift(target, poly, shift):
    for k,v in enumerate(poly):
        target[shift+k]+=v


def binomial_poly(r):
    return [comb(r,k) for k in range(r+1)]


def formula(alpha,beta):
    p=len(alpha)
    a=[0]
    b=[0]
    for z in alpha: a.append(a[-1]+z)
    for z in beta: b.append(b[-1]+z)
    m=a[-1]; n=b[-1]
    coeff=[0]*(m+n+1)
    # Cut sets C_i=A_1...A_i union B_{i+1}...B_p, including i=0,p.
    for i in range(p+1):
        coeff[a[i]+n-b[i]] += 1
    # Two-sided sets with boundary indices 1 <= j <= i <= p.
    for j in range(1,p+1):
        for i in range(j,p+1):
            q=[1]
            for t in range(j,i):
                q=mul(q,binomial_poly(alpha[t-1]))
            qA=binomial_poly(alpha[i-1]); qA[0]-=1
            q=mul(q,qA)
            qB=binomial_poly(beta[j-1]); qB[0]-=1
            q=mul(q,qB)
            for t in range(j+1,i+1):
                q=mul(q,binomial_poly(beta[t-1]))
            shift=a[j-1] + n-b[i]
            add_shift(coeff,q,shift)
    return coeff


def build(alpha,beta):
    m=sum(alpha); n=sum(beta); N=m+n
    A=[]; s=0
    for z in alpha:
        A.append(list(range(s,s+z))); s+=z
    B=[]; s=m
    for z in beta:
        B.append(list(range(s,s+z))); s+=z
    adj=[set() for _ in range(N)]
    for i,Ai in enumerate(A):
        for j in range(i+1):
            for u in Ai:
                for v in B[j]:
                    adj[u].add(v); adj[v].add(u)
    return adj


def brute(alpha,beta):
    adj=build(alpha,beta); N=len(adj)
    coeff=[0]*(N+1)
    checked=0
    for mask in range(1<<N):
        checked += 1
        ok=True
        for v in range(N):
            if (mask>>v)&1:
                continue
            if not any((mask>>u)&1 for u in adj[v]):
                ok=False; break
        if ok:
            coeff[mask.bit_count()] += 1
    return coeff,checked


def main():
    graph_types=0; subset_checks=0; coefficient_checks=0; max_order=0
    for p in range(1,5):
        for alpha in product(range(1,4), repeat=p):
            for beta in product(range(1,4), repeat=p):
                N=sum(alpha)+sum(beta)
                if N>11:
                    continue
                got,checks=brute(alpha,beta)
                want=formula(alpha,beta)
                if got != want:
                    raise AssertionError((alpha,beta,got,want))
                # Check total-count closed form at x=1.
                a=[0]; b=[0]
                for z in alpha: a.append(a[-1]+z)
                for z in beta: b.append(b[-1]+z)
                total=p+1
                for j in range(1,p+1):
                    for i in range(j,p+1):
                        total += (2**(a[i-1]-a[j-1] + b[i]-b[j]))*(2**alpha[i-1]-1)*(2**beta[j-1]-1)
                if total != sum(got):
                    raise AssertionError(('total',alpha,beta,total,sum(got)))
                graph_types += 1
                subset_checks += checks
                coefficient_checks += N+1
                max_order=max(max_order,N)
    # Explicit boundary specializations.
    if formula((1,),(1,)) != [0,2,1]:
        raise AssertionError('K2')
    if formula((1,),(4,)) != brute((1,),(4,))[0]:
        raise AssertionError('star')
    print(f'VERIFY_OK graph_types={graph_types} subset_checks={subset_checks} coefficient_checks={coefficient_checks} max_order={max_order}')

if __name__=='__main__':
    main()
