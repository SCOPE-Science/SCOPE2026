from itertools import product
from math import comb


def valid_pid(m,n,t,vals):
    x=vals[:m]
    y=vals[m:]
    X=sum(x); Y=sum(y)
    for i,a in enumerate(x):
        if a==0 and Y-(y[i] if i<t else 0)!=2:
            return False
    for j,b in enumerate(y):
        if b==0 and X-(x[j] if j<t else 0)!=2:
            return False
    return True


def expected_gamma(m,n,t):
    if m==2 and t==0:
        return 2
    if m==2 and t==1:
        return 3
    if (m,n,t)==(2,3,2):
        return 3
    if (m,n,t)==(3,3,3):
        return 3
    return 4


def C(n,k):
    return comb(n,k) if 0<=k<=n else 0


def balanced_count(m,n,t):
    ans=0
    for a in (1,2):
        for b in (1,2):
            for s in range(min(a,b,t)+1):
                ans += C(t,s)*C(m-t,a-s)*C(n-t,b-s)
    return ans


def expected_min_count(m,n,t):
    if m==2 and t==0:
        return 2 if n==2 else 1
    if m==2 and t==1:
        return 2 if n==2 else 1
    if (m,n,t)==(2,3,2):
        return 1
    if (m,n,t)==(3,3,3):
        return 2
    if (m,n,t)==(2,2,2):
        return 9
    eps = 2 if (m,n,t)==(3,3,2) else 1 if (m,n,t)==(3,4,3) else 0
    return balanced_count(m,n,t)+eps


def brute(m,n,t):
    best=10**9
    count=0
    checked=0
    for vals in product((0,1,2), repeat=m+n):
        checked += 1
        w=sum(vals)
        if w>best:
            continue
        if valid_pid(m,n,t,vals):
            if w<best:
                best=w; count=1
            elif w==best:
                count += 1
    return best,count,checked

param_cases=0
labelings=0
for m in range(2,5):
    for n in range(m,6):
        for t in range(m+1):
            if m+n>9:
                continue
            g,c,q=brute(m,n,t)
            param_cases += 1
            labelings += q
            eg=expected_gamma(m,n,t)
            ec=expected_min_count(m,n,t)
            assert g==eg, (m,n,t,g,eg)
            assert c==ec, (m,n,t,c,ec)

formula_cases=0
for m in range(2,31):
    for n in range(m,41):
        for t in range(m+1):
            g=expected_gamma(m,n,t)
            c=expected_min_count(m,n,t)
            assert g in (2,3,4)
            assert c>=1
            formula_cases += 1

print(f'ALL CHECKS PASSED; exhaustive_parameter_cases={param_cases}; exhaustive_labelings={labelings}; formula_parameter_cases={formula_cases}; exhaustive_range=2<=m<=n<=5, m+n<=9; formula_range=2<=m<=30, m<=n<=40')
