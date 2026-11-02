"""Exact finite checks for Ewens remote-fixed-point / local-shape covariances.
Uses only the Python standard library. Infinite-size proof is separate.
"""
from fractions import Fraction
from itertools import permutations
from math import comb


def classify(x, y, z):
    if x < y < z:
        return 'up'
    if x > y > z:
        return 'down'
    if y > max(x, z):
        return 'peak'
    return 'valley'


def cycles(perm):
    n = len(perm)
    seen = 0
    count = 0
    for k in range(n):
        if seen >> k & 1:
            continue
        count += 1
        a = k
        while not (seen >> a & 1):
            seen |= 1 << a
            a = perm[a] - 1
    return count


def theory(n, theta):
    a = theta - 1
    den3 = (theta+n-1)*(theta+n-2)*(theta+n-3)
    pup = (comb(n,3) + a*comb(n,2)+a*a*n+a*a*a)/den3
    ppeak = (2*comb(n,3) + a*n*(n-2)+a*a*(n-2))/den3
    dd = (theta+n-4)*(theta+n-3)*(theta+n-2)*(theta+n-1)**2
    cr = {
        'up':theta**2*(theta-1)*(n+2*theta-3)/dd,
        'down':-theta**2*(theta-1)*(n-5)/dd,
        'peak':-theta**2*(theta-1)*(theta+1)/dd,
        'valley':-theta**2*(theta-1)*(theta+1)/dd,
    }
    return {'up':pup,'down':1-pup-2*ppeak,'peak':ppeak,'valley':ppeak},cr


def run():
    checks = 0
    enumerated=0
    for n in range(4,9):
        raw = [ [0 for shape in range(4)] for _ in range(n-2)]
        perms = []
        for perm in permutations(range(1,n+1)):
            enumerated += 1
            perms.append((perm,cycles(perm)))
        for theta in (Fraction(1,2), Fraction(1),Fraction(2),Fraction(3)):
            wsum = sum(theta**c for _,c in perms)
            e_shapes = [dict.fromkeys(('up','down','peak','valley'),Fraction(0)) for i in range(n-2)]
            e_fixed=[Fraction(0) for j in range(n)]
            e_joint=[[dict.fromkeys(('up','down','peak','valley'),Fraction(0)) for j in range(n)] for i in range(n-2)]
            for p,c in perms:
                w=theta**c
                indicators=[j for j,v in enumerate(p) if v==j+1]
                for j in indicators: e_fixed[j]+=w
                for i in range(n-2):
                    sh=classify(*p[i:i+3]);e_shapes[i][sh]+=w
                    for j in indicators:
                        if not (i<=j<=i+2):
                            e_joint[i][j][sh]+=w
            expected,covs=theory(n,theta)
            for i in range(n-2):
                for sh in expected:
                    assert e_shapes[i][sh]/wsum == expected[sh],(n,theta,i,sh,'marginal')
                    checks+=1
                for j in range(n):
                    if i<=j<=i+2:continue
                    assert e_fixed[j]/wsum == theta/(theta+n-1),(n,theta,i,j,'fixed marginal')
                    checks+=1
                    for sh in covs:
                        cv=e_joint[i][j][sh]/wsum-e_fixed[j]*e_shapes[i][sh]/wsum**2
                        assert cv==covs[sh],(n,theta,i,j,sh,cv,covs[sh])
                        checks+=1
    print('PASS exact assertions',checks,'enumerated permutations (per n, not per theta)',enumerated)

if __name__=='__main__':run()
