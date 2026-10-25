"""Reproducible finite checks for isolated-vertex cross covariance in bipartite ensembles.
All asserted small-instance identities use exact integer/rational arithmetic.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb, exp, log


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def law_fixed(a,b,m):
    N=a*b
    P=lambda s: Fraction(choose(s,m),choose(N,m))
    return a*b*(P((a-1)*(b-1))-P((a-1)*b)*P(a*(b-1)))


def moments_exact(a,b,m):
    # All labeled simple bipartite graphs with exactly m edges.
    sx=sy=sxy=0
    N=a*b
    num=0
    for edges in combinations(range(N),m):
        row=[0]*a;col=[0]*b
        for e in edges:
            i,j=divmod(e,b)
            row[i]+=1;col[j]+=1
        x=row.count(0);y=col.count(0)
        sx+=x;sy+=y;sxy+=x*y;num+=1
    return Fraction(sxy,num)-Fraction(sx*sy,num*num)


def verify_finite():
    count=0
    for a in range(2,5):
        for b in range(2,5):
            N=a*b
            for m in range(N+1):
                c=law_fixed(a,b,m)
                assert moments_exact(a,b,m)==c,(a,b,m)
                sign_range= 2<=m<=N-max(a,b)
                assert (c<0)==sign_range,(a,b,m,c)
                if not sign_range:assert c==0,(a,b,m,c)
                if m<=(a-1)*(b-1):
                    R=N-b;C=N-a
                    pleft=Fraction(choose(R,m),choose(N,m))
                    pright=Fraction(choose(C,m),choose(N,m))
                    ratio=Fraction(1)
                    for t in range(m):
                        ratio*=1-Fraction(t,(R-t)*(C-t))
                    assert c==a*b*pleft*pright*(ratio-1)
                count+=1
    print('FIXED_EXHAUSTIVE_PASS',count,'(a,b,m) strata, up to 2^16 matrices')


def verify_binomial():
    count=0
    for a in range(2,4):
        for b in range(2,4):
            N=a*b
            for p in [Fraction(1,4),Fraction(2,5),Fraction(3,4)]:
                q=1-p
                sx=sy=sxy=sm=sxm=sym=sm2=Fraction(0)
                for mask in range(1<<N):
                    edges=[e for e in range(N) if mask>>e&1]
                    row=[0]*a;col=[0]*b
                    for e in edges:
                        i,j=divmod(e,b)
                        row[i]+=1;col[j]+=1
                    x=row.count(0);y=col.count(0);s=len(edges)
                    w=p**s*q**(N-s)
                    sx+=w*x; sy+=w*y; sxy+=w*x*y
                    sm+=w*s;sxm+=w*x*s;sym+=w*y*s;sm2+=w*s*s
                cov=sxy-sx*sy
                assert cov==N*p*q**(a+b-1)
                assert cov == (sxm-sx*sm)*(sym-sy*sm)/(sm2-sm*sm)
                count+=1
    print('BERNOULLI_EXHAUSTIVE_PASS',count,'parameter triples')


def verify_with_replacement():
    count=0
    for a,b in [(2,2),(2,3),(3,2),(3,3)]:
        N=a*b
        for m in range(4):
            sx=sy=sxy=0
            tot=N**m
            for seq in product(range(N),repeat=m):
                used_rows={e//b for e in seq}
                used_cols={e%b for e in seq}
                x=a-len(used_rows);y=b-len(used_cols)
                sx+=x;sy+=y;sxy+=x*y
            assert Fraction(sxy,tot)==Fraction(sx*sy,tot**2)
            count+=1
    print('REPLACEMENT_EXHAUSTIVE_PASS',count,'parameter triples')


def verify_asymptotic():
    target=-exp(-2)/2
    errors=[]
    for n in [20,40,80,160,320,640]:
        m=n;N=n*n;R=N-n
        log_prob=sum(log((R-t)/(N-t)) for t in range(m))
        log_ratio=sum(__import__('math').log1p(-t/((R-t)*(R-t))) for t in range(m))
        val=n*n*exp(2*log_prob)*__import__('math').expm1(log_ratio)
        errors.append(abs(val-target))
    assert all(u>v for u,v in zip(errors,errors[1:]))
    assert errors[-1]<1e-4
    print('SPARSE_LIMIT_DIAGNOSTIC_PASS',errors[-1])


if __name__=='__main__':
    verify_finite()
    verify_binomial()
    verify_with_replacement()
    verify_asymptotic()
    print('VERIFY_OK')
