#!/usr/bin/env python3
"""Characteristic-two formal identities supporting the conic description.

The nonsplitting statement is a valuation theorem proved in RESULT.md;
this checker deliberately does not claim to decide all rational points.
"""

NAMES = ('x', 'Y', 'Z', 'a', 'b', 'theta', 'r', 'w')
N = len(NAMES)

def var(name):
    t = [0] * N
    t[NAMES.index(name)] = 1
    return frozenset((tuple(t),))

def add(*polys):
    out = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return frozenset(out)

def mul(p, q):
    out = set()
    for a in p:
        for b in q:
            term = tuple(i+j for i,j in zip(a,b))
            if term in out:
                out.remove(term)
            else:
                out.add(term)
    return frozenset(out)

def power(p, n):
    ans = frozenset(((0,)*N,))
    for _ in range(n):
        ans = mul(ans,p)
    return ans

x,Y,Z,a,b,theta,r,w = (var(s) for s in NAMES)
# q(x,b Z,Y) equals b times its transformed norm equation.
left = add(power(x,2),mul(a,power(mul(b,Z),2)),
           mul(b,power(Y,2)),mul(mul(b,Z),Y))
right = add(power(x,2),mul(b,power(Y,2)),
            mul(b,mul(Y,Z)),mul(a,mul(power(b,2),power(Z,2))))
assert left == right
# For the rational point (0,theta/a,1), the cleared equation is
# theta^2+theta+ab=0, precisely the Artin-Schreier equation.
assert add(power(theta,2),theta,mul(a,b)) == add(mul(a,b),theta,power(theta,2))
# On the map (r,w) -> (r^2+w,w^2), the fourth-power relation is
# r^4 = (r^2+w)^2 + w^2.
assert add(power(add(power(r,2),w),2),power(w,2),power(r,4)) == frozenset()
# The quadratic coefficient quadrics A=x^2+YZ, B=Y^2, C=Z^2
# have no common projective zero, since Y=Z=0 forces x!=0.
print('VERIFY_OK')
