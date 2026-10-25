"""Exact, standalone checks for the empty-row/empty-column theorem.

No external packages required. Verification is finite; the all-size theorem
and limiting covariance require the separate written proof.
"""
from math import comb, factorial, exp, log1p
from fractions import Fraction
from itertools import combinations


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def falling(n, k):
    out = 1
    for j in range(k):
        out *= n-j
    return out


def probabilities(a, b, m, r, s):
    n = a*b
    den = choose(n, m)
    p = Fraction(choose((a-r)*b,m),den)
    q = Fraction(choose(a*(b-s),m),den)
    both = Fraction(choose((a-r)*(b-s),m),den)
    return p,q,both


def ratio_product(a,b,m,r,s):
    n=a*b
    u=Fraction(1,1)
    for j in range(m):
        u *= 1-Fraction(r*s*j,((a-r)*b-j)*(a*(b-s)-j))
    return u


def exact_formula_checks():
    checks=0
    for a in range(2,10):
        for b in range(2,10):
            n=a*b
            for r in range(1,a):
                for s in range(1,b):
                    for m in range(n+1):
                        p,q,h=probabilities(a,b,m,r,s)
                        assert h <= p*q
                        if m >= 2 and p*q:
                            assert h < p*q
                        if m<= (a-r)*(b-s):
                            assert h == p*q*ratio_product(a,b,m,r,s)
                        checks += 1
    return checks


def enumeration_checks():
    checks=0; configurations=0
    for a,b in [(2,2),(2,3),(3,2),(3,3),(3,4),(4,3),(4,4)]:
        n=a*b
        by_m = [dict() for _ in range(n+1)]
        for m in range(n+1):
            counts = [[0]*(b+1) for _ in range(a+1)]
            for cells in combinations(range(n),m):
                rows={u//b for u in cells}
                cols={u%b for u in cells}
                counts[a-len(rows)][b-len(cols)]+=1
                configurations += 1
            for r in range(a+1):
                for s in range(b+1):
                    obs=sum(falling(i,r)*falling(j,s)*counts[i][j]
                            for i in range(a+1) for j in range(b+1))
                    target=(falling(a,r)*falling(b,s)*choose((a-r)*(b-s),m))
                    assert obs==target,(a,b,m,r,s,obs,target)
                    checks += 1
    return checks,configurations


def sparse_limit_checks():
    # Certified benchmark asymptotic only via proof; this is a numerical check.
    c = 2.0
    target = -c*c*exp(-2*c)/2
    ratios=[]
    for n in [64,128,256,512,1024,2048,4096]:
        m=int(c*n)
        p=1.0
        N=n*n
        for j in range(m):
            p *= (N-n-j)/(N-j)
        logratio=sum(log1p(-j/((N-n-j)**2)) for j in range(m))
        cov=(n*n)*(p*p)*(__import__('math').expm1(logratio))
        ratios.append((n,cov,target))
    assert abs(ratios[-1][1]-target) < 0.002
    return ratios


def main():
    a=exact_formula_checks()
    b,states=enumeration_checks()
    sparse=sparse_limit_checks()
    print(f'PASS exact_formula_cases={a} independent_enumeration_checks={b} binary_matrices={states}')
    for n,cov,goal in sparse:
        print(f'  balanced_n={n} covariance={cov:.12f} limit={goal:.12f}')

if __name__=='__main__':
    main()
