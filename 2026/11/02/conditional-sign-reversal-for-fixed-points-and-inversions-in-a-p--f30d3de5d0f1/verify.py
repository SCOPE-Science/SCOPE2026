"""Reproduce finite exact checks for overhand packet-reversal covariance formulas.

Python 3 standard library only. All finite model calculations use Fraction.
"""
from fractions import Fraction as Q
from itertools import combinations

checks = 0

def check(expr, context):
    global checks
    checks += 1
    if not expr:
        raise AssertionError(context)

def compositions(n, m):
    for cuts in combinations(range(1, n), m - 1):
        points = (0,) + cuts + (n,)
        yield [b - a for a, b in zip(points, points[1:])]

def rewards(parts):
    return sum(v & 1 for v in parts), sum(v*(v-1)//2 for v in parts)

def reg(n, m, f):
    s = Q(n-2*m+f, 2)
    return m-f+(5-Q(2*f,m))*s+Q(4*s*(s-1),m+1)

def ecov(rows):
    size = len(rows)
    ef = Q(sum(x for x, _ in rows), size)
    ei = Q(sum(y for _, y in rows), size)
    cov = Q(sum(x*y for x,y in rows), size) - ef*ei
    return ef, ei, cov

for n in range(2, 13):
    rows_by_m = {}
    for m in range(1, n+1):
        rows = [rewards(c) for c in compositions(n, m)]
        rows_by_m[m] = rows
        check(len(rows) == __import__('math').comb(n-1,m-1), (n,m,'size'))
        ef,ei,cv = ecov(rows)
        expected_positive = 2+(n%2) <= m <= n-2
        check((cv > 0) == expected_positive, (n,m,'conditional sign',cv))
        check(cv >= 0, (n,m,'nonnegative'))
        for f in set(x for x,_ in rows):
            values = [y for x,y in rows if x==f]
            check(Q(sum(values),len(values)) == reg(n,m,f), (n,m,f,'regression'))
        for f in set(x for x,_ in rows):
            if f+2 in set(x for x,_ in rows):
                delta = reg(n,m,f+2)-reg(n,m,f)
                target = Q(2*n*(m-1)-m*m+3*m-4*f-4,m*(m+1))
                check(delta==target and delta>0,(n,m,f,'regression increment'))
    for p in [Q(1,4), Q(1,3), Q(1,2), Q(3,4)]:
        w = [(p**(m-1)*(1-p)**(n-m),r) for m,rows in rows_by_m.items() for r in rows]
        ef = sum((wt*f for wt,(f,i) in w),Q(0))
        ei = sum((wt*i for wt,(f,i) in w),Q(0))
        efi = sum((wt*f*i for wt,(f,i) in w),Q(0))
        check(sum((wt for wt,_ in w),Q(0))==1,(n,p,'normalization'))
        check(efi-ef*ei<0,(n,p,'unconditional negative covariance'))

# Exact symbolic moment identities evaluated at several rational values.
for p in [Q(1,8), Q(1,5), Q(1,3), Q(1,2), Q(3,4), Q(9,10)]:
    q=1-p
    EL=1/p
    EL2=(2-p)/p**2
    EL3=(p*p-6*p+6)/p**3
    EL4=(24-36*p+14*p*p-p**3)/p**4
    ER=1/(2-p)
    ELR=(p*p-2*p+2)/(p*(2-p)**2)
    EJ=q/p**2
    ELJ=q*(3-p)/p**3
    ERJ=q*q*(p*p-2*p+4)/(p*p*(2-p)**3)
    EJ2=q*(p*p-6*p+6)/p**4
    muR=ER/EL
    muJ=EJ/EL
    Vf=p*(ER-2*muR*ELR+muR**2*EL2)
    Vj=p*(EJ2-2*muJ*ELJ+muJ**2*EL2)
    C=p*(ERJ-muJ*ELR-muR*ELJ+muR*muJ*EL2)
    check(muR==p/(2-p) and muJ==q/p, ('means',p))
    check(Vf==4*p*q/(2-p)**3,('var F',p))
    check(Vj==q*(2-p)/p**3,('var I',p))
    check(C==-2*q*(p*p-2*p+2)/(p*(2-p)**3),('cov',p))
    check(C<0 and C*C<Vf*Vj,('nondegenerate',p))
print('PASS:', checks, 'exact-rational assertions')
