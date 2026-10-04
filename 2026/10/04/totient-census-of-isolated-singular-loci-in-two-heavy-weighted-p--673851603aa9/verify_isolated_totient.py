#!/usr/bin/env python3
import math

def phi(n):
    return sum(math.gcd(k,n)==1 for k in range(1,n+1))

def Phi(n):
    return sum(phi(k) for k in range(1,n+1))

def canonical(r,a,b):
    d=b-a
    return 0 <= d <= r and 1 <= a <= r+d

def terminal(r,a,b):
    d=b-a
    return 0 <= d < r and 1 <= a < r+d

def isolated(a,b):
    return math.gcd(a,b)==1

for r in range(2,151):
    canonical_pairs=[(a,a+d) for d in range(r+1) for a in range(1,r+d+1)]
    terminal_pairs=[(a,a+d) for d in range(r) for a in range(1,r+d)]
    ci=sum(isolated(a,b) for a,b in canonical_pairs)
    ti=sum(isolated(a,b) for a,b in terminal_pairs)
    assert ci == 3*Phi(r)
    assert ti == 3*Phi(r-1)
    assert ci-ti == 3*phi(r)

    boundary={(a,b) for a,b in canonical_pairs if not terminal(r,a,b)}
    actual={(a,b) for a,b in boundary if isolated(a,b)}
    predicted={(a,a+r) for a in range(1,2*r+1) if math.gcd(a,r)==1}
    predicted |= {(r+d,r+2*d) for d in range(1,r) if math.gcd(d,r)==1}
    assert actual == predicted

print('VERIFY_OK')
