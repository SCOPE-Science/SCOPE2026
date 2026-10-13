from fractions import Fraction
from itertools import permutations

def exhaustive(n):
    ps = permutations(range(1,n+1))
    N = 1
    for k in range(2,n+1):
        N *= k
    sumX=sumX2=sumD=sumD2=sumXD=0
    sumEi=[0]*n
    sumEiD=[0]*n
    weight_sets=[
        list(range(1,n+1)),
        [(-1)**j*(j+1) for j in range(n)],
        [1]*n,
        [j*j+3*j+1 for j in range(1,n+1)],
    ]
    sumL=[0]*len(weight_sets)
    sumEiL=[[0]*n for _ in weight_sets]
    for p in ps:
        e=[int(p[i]>i+1) for i in range(n)]
        X=sum(e)
        D=sum((p[i]-(i+1))**2 for i in range(n))
        sumX += X; sumX2 += X*X
        sumD += D; sumD2 += D*D; sumXD += X*D
        for i in range(n):
            sumEi[i] += e[i]
            sumEiD[i] += e[i]*D
        for q,w in enumerate(weight_sets):
            L=sum(w[j]*p[j] for j in range(n))
            sumL[q] += L
            for i in range(n):
                sumEiL[q][i] += e[i]*L
    EX=Fraction(sumX,N); ED=Fraction(sumD,N)
    varX=Fraction(sumX2,N)-EX*EX
    varD=Fraction(sumD2,N)-ED*ED
    covXD=Fraction(sumXD,N)-EX*ED
    assert varX == Fraction(n+1,12)
    assert covXD == Fraction(n*(n+1),12)
    scale=-Fraction(6,n*(n*n-1))
    varR=scale*scale*varD
    covXR=scale*covXD
    assert varR == Fraction(1,n-1)
    assert covXR == -Fraction(1,2*(n-1))
    assert covXR*covXR/(varX*varR) == Fraction(3,n*n-1)
    local_checks=0
    weight_checks=0
    for i0 in range(n):
        i=i0+1
        EI=Fraction(sumEi[i0],N)
        assert EI == Fraction(n-i,n)
        covED=Fraction(sumEiD[i0],N)-EI*ED
        assert covED == Fraction(i*(n-i)*(n+1-2*i),2*(n-1))
        covER=scale*covED
        assert covER == -Fraction(3*i*(n-i)*(n+1-2*i),n*(n-1)*(n-1)*(n+1))
        local_checks += 2
        if n-i:
            meanRgiven = scale*(Fraction(sumEiD[i0],sumEi[i0])-ED)
            assert meanRgiven == -Fraction(3*i*(n+1-2*i),(n-1)*(n-1)*(n+1))
            local_checks += 1
        for q,w in enumerate(weight_sets):
            EL=Fraction(sumL[q],N)
            cov=Fraction(sumEiL[q][i0],N)-EI*EL
            W=sum(w)
            want=Fraction(i*(n-i),2*n*(n-1))*(n*w[i0]-W)
            assert cov == want
            weight_checks += 1
    return N,local_checks,weight_checks,5

def closed_checks(max_n=1000):
    c=0
    for n in range(2,max_n+1):
        # conditional means and local Spearman specialization
        for i in range(1,n+1):
            if i<n:
                mu=Fraction(n+1,2)
                mui=Fraction(n+i+1,2)
                muo=Fraction(n*n-i-1,2*(n-1))
                assert mui-mu == Fraction(i,2)
                assert muo-mu == -Fraction(i,2*(n-1))
                c += 2
            covD=Fraction(i*(n-i)*(n+1-2*i),2*(n-1))
            covR=-Fraction(6,n*(n*n-1))*covD
            assert covR == -Fraction(3*i*(n-i)*(n+1-2*i),n*(n-1)*(n-1)*(n+1))
            c += 1
        # sample pairwise identities at early, middle, and late locations
        pairs=[]
        if n>=3:
            pairs.append((1,2))
        if n>=4:
            pairs.append((max(1,n//2-1), min(n-1,n//2+1)))
        if n>=3:
            pairs.append((n-2,n-1))
        for i,j in pairs:
            if not (1 <= i < j <= n-1):
                continue
            pi=Fraction(n-i,n)
            pij=Fraction((n-j)*(n-i-1),n*(n-1))
            cov=pij-pi*Fraction(n-j,n)
            assert cov == -Fraction(i*(n-j),n*n*(n-1))
            c += 1
        # closed sums of indicator variances and pair covariances
        sum_var=Fraction(n*n-1,6*n)
        pair_sum=n*(n-1)*(n+1)*(n-2)//24
        var=sum_var-Fraction(2*pair_sum,n*n*(n-1))
        assert var == Fraction(n+1,12)
        c += 1
        s=n*(n-1)*(n+1)//6
        assert Fraction(s,2*(n-1)) == Fraction(n*(n+1),12)
        c += 1
    return c

def run():
    perms=local=weights=global_checks=0
    for n in range(2,10):
        a,b,c,d=exhaustive(n)
        perms += a; local += b; weights += c; global_checks += d
    closed=closed_checks()
    print('VERIFY_OK')
    print(f'permutations_checked={perms}')
    print(f'local_spearman_checks={local}')
    print(f'arbitrary_weight_checks={weights}')
    print(f'global_formula_checks={global_checks}')
    print(f'closed_identity_checks={closed}')
    print('max_exhaustive_n=9')
    print('max_closed_n=1000')

if __name__=='__main__':
    run()
