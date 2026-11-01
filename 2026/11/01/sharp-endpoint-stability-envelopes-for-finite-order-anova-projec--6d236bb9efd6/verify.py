"""Exact arithmetic replay for finite-order product ANOVA endpoint amplification."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb


def subsets(n, k):
    return [tuple(s) for t in range(k + 1) for s in combinations(range(n), t)]


def kernel_match(match, p, k):
    n = len(p)
    z = [(F(1, 1) / p[i] - 1) if match[i] else F(-1) for i in range(n)]
    return sum((product_f(z[i] for i in S) for S in subsets(n, k)), F(0))


def product_f(xs):
    t = F(1)
    for x in xs: t *= x
    return t


def reduced_norm(p, k):
    n = len(p)
    return sum((product_f(p[i] if match[i] else (1-p[i]) for i in range(n))
                * abs(kernel_match(match, p, k)) for match in product([False, True], repeat=n)), F(0))


def actual_norm(marginals, k):
    n = len(marginals)
    space = list(product(*[range(len(m)) for m in marginals]))
    fs = subsets(n, k)
    ans = F(0)
    for x in space:
        row=F(0)
        for y in space:
            w=product_f(marginals[i][y[i]] for i in range(n))
            kern=F(0)
            for S in fs:
                term=F(1)
                for i in range(n):
                    if i in S:
                        term *= (F(1,1)/marginals[i][x[i]]-1 if y[i]==x[i] else F(-1))
                kern += term
            row += w*abs(kern)
        if row>ans:ans=row
    return ans


def norm_from_marginals(marginals,k):
    return reduced_norm([min(v) for v in marginals],k)


def sharp(d,k):
    return sum((-1)**(k-j)*2**j*comb(d,j) for j in range(k+1))


def run():
    nrows=0; monotonic=0; rare=0
    samples=[[F(1,2),F(1,2)], [F(1,3),F(2,3)], [F(1,4),F(3,4)], [F(1,5),F(1,5),F(3,5)], [F(1,2),F(1,3),F(1,6)]]
    for n in range(1,5):
        for setting in product(range(len(samples)),repeat=n):
            if n==4 and any(len(samples[i])>2 for i in setting): continue
            marg=[samples[i] for i in setting]
            if product_f([len(x) for x in marg])>80: continue
            for k in range(n+1):
                got=actual_norm(marg,k)
                want=norm_from_marginals(marg,k)
                assert got==want, (n,k,setting,got,want)
                nrows+=1
    vals=[F(1,100),F(1,20),F(1,5),F(1,2)]
    for d in range(1,8):
        for k in range(d+1):
            prev=None
            for p in vals:
                now=reduced_norm([p]*d,k)
                assert now<=sharp(d,k), (d,k,p,now,sharp(d,k))
                if prev is not None: assert now<=prev,(d,k,p,now,prev)
                prev=now
                monotonic+=1
            if k not in (0,d):
                a=reduced_norm([F(1,1000000)]*d,k)
                assert abs(a-sharp(d,k))<F(1,4), (d,k,a,sharp(d,k))
                rare+=1
    # Test triangular coefficient identity: higher-order rare matching patterns.
    for d in range(1,15):
        for k in range(d):
            s=sum(comb(d,t)*comb(d-t-1,k-t) for t in range(k+1))
            assert s==sharp(d,k),(d,k,s,sharp(d,k))
    print('VERIFY_OK independent_direct_matrix_checks=%d monotone_and_bounded_checks=%d sharp_rare_samples=%d binomial_identites=%d'%(nrows,monotonic,rare,sum(range(1,15))))

if __name__=='__main__': run()
