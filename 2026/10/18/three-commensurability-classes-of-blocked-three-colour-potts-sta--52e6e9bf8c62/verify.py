#!/usr/bin/env python3
"""Finite independent checks for three-colour antiferromagnetic Potts blocking.
The theorem for all sizes is proved analytically; these checks are finite tests.
Uses only the Python standard library.
"""
import itertools
import math
from collections import defaultdict


def triples(n):
    return [(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)]


def blocked_matrix(rows):
    for i in range(3):
        outside = tuple(sum(rows[j][c] for j in range(3) if j != i) for c in range(3))
        lowest = min(outside)
        if any(rows[i][c] and outside[c] != lowest for c in range(3)):
            return False
    return True


def energy(rows):
    return sum(rows[i][c]*rows[j][c] for i in range(3) for j in range(i+1,3) for c in range(3))


def spin_blocked_direct(spins,n):
    def H(v):
        return sum(v[i*n+a] == v[j*n+b]
                   for i in range(3) for j in range(i+1,3)
                   for a in range(n) for b in range(n))
    before=H(spins)
    for t in range(3*n):
        for color in range(3):
            if color == spins[t]:
                continue
            changed=list(spins)
            changed[t]=color
            if H(changed) < before:
                return False
    return True


def multinomial(n,counts):
    return math.factorial(n)//math.prod(math.factorial(v) for v in counts)


def profile_census(n):
    allrows=triples(n)
    distribution=defaultdict(int)
    matrices=0
    for a in allrows:
        for b in allrows:
            for c in allrows:
                z=(a,b,c)
                if blocked_matrix(z):
                    matrices+=1
                    cnt=math.prod(multinomial(n,r) for r in z)
                    distribution[energy(z)]+=cnt
    return dict(distribution), matrices


def formula_nontriple(n):
    result={0:6}
    if n % 2 == 0:
        b=math.comb(n,n//2)
        result[n*n//2]=9*b*b
        result[3*n*n//4]=6*b*b*b
    return result


def main():
    checks=0
    # No occupancy matrix is silently treated as a labeled microstate:
    # check labeled microstates directly for n=1..3.
    for n in (1,2,3):
        direct=defaultdict(int)
        for s in itertools.product(range(3),repeat=3*n):
            if spin_blocked_direct(s,n):
                rows=tuple(tuple(sum(s[i*n+t] == c for t in range(n)) for c in range(3)) for i in range(3))
                assert blocked_matrix(rows)
                direct[energy(rows)]+=1
            else:
                rows=tuple(tuple(sum(s[i*n+t] == c for t in range(n)) for c in range(3)) for i in range(3))
                assert not blocked_matrix(rows)
            checks+=1
        count,_=profile_census(n)
        assert dict(direct)==count, (n,direct,count)
        checks+=1
    for n in range(1,13):
        observed,matrix_count=profile_census(n)
        assert observed.get(0,0)==6
        checks+=1
        if n%3:
            assert observed==formula_nontriple(n),(n,observed,formula_nontriple(n))
            checks+=1
        else:
            r=n//3
            expected=multinomial(n,(r,r,r))**3
            assert sum(observed.values())>=expected
            assert sum(observed.values())<=3**(3*n)
            checks+=2
        print('n',n,'profiles',matrix_count,'total',sum(observed.values()),'energies',observed)
    print('PASS independent direct-spin and profile-enumeration tests; assertions',checks)

if __name__=='__main__':
    main()
