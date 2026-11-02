"""Exact arithmetic checks for the two-patch mean-extinction-time allocation theorem.

Run: python verify.py
No external modules required. Finite checks supplement the analytical proof.
"""
from fractions import Fraction as F
from itertools import product


def solve(A, rhs):
    """Solve a finite linear system by exact rational elimination."""
    n = len(rhs)
    aug = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(A)]
    for i in range(n):
        pivot = next(k for k in range(i, n) if aug[k][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        den = aug[i][i]
        aug[i] = [x / den for x in aug[i]]
        for k in range(n):
            if k != i:
                m = aug[k][i]
                aug[k] = [x-m*y for x, y in zip(aug[k], aug[i])]
    return [row[-1] for row in aug]


def independently_invert_generator(a, b, B, c):
    d = B-c
    # State order: both (11), first only (10), second only (01).
    # The chain stops at the extinct state (00).
    A = [[a+b, -b, -a], [-c, a+c, F(0)], [-d, F(0), b+d]]
    return solve(A, [1,1,1])


def formulas(a,b,B,c):
    d=B-c
    den = a*b*(a+b+B)
    both = (a*a+a*b+b*b+(a+b)*B+c*d)/den
    first = (b+c)*(a+b+d)/den
    second = (a+d)*(a+b+c)/den
    return [both, first, second]


def clamp(v,B):
    return max(F(0), min(B,v))

n = 0
for a,b,B in product([F(1,3),F(1),F(3),F(7,2)], [F(1,2),F(2),F(5)],
                       [F(1,4),F(1),F(4)]):
    for c in [F(0), B/4, B/2, 3*B/4, B]:
        inv = independently_invert_generator(a,b,B,c)
        closed = formulas(a,b,B,c)
        assert inv == closed and all(t>0 for t in closed)
        n+=3
    for w10,w01 in [(F(0),F(0)), (F(1),F(0)), (F(0),F(1)),
                    (F(1,4),F(1,2)), (F(1,3),F(1,3)), (F(2,5),F(1,5))]:
        w11 = 1-w10-w01
        optimum = clamp((B+a*w10-b*w01)/2,B)
        def mean(c):
            v = formulas(a,b,B,c)
            return w11*v[0] + w10*v[1] + w01*v[2]
        # Quadratic exact difference from unconstrained vertex and strict global optimality.
        for c in [F(0), B/8,B/3, B/2, 2*B/3, 7*B/8, B, optimum]:
            assert mean(optimum) >= mean(c)
            if c != optimum: assert mean(optimum) > mean(c)
            n += 1
        # All three pure-state objectives have universal, exact negative curvature.
        for s in [F(0), B/4, B/2]:
            h=B/16
            if s+h <= B:
                assert (mean(s+2*h)-2*mean(s+h)+mean(s))/(h*h) == -F(2)/(a*b*(a+b+B))
                n+=1
# A completely symmetric landscape favors three different choices based on initial occupancy.
a=b=B=F(1)
assert clamp((B+a)/2,B)==B
assert clamp((B-b)/2,B)==0
assert clamp(B/2,B)==F(1,2)
assert formulas(a,b,B,F(1))[1] == F(4,3)
assert formulas(a,b,B,F(1,2))[1] == F(5,4)
assert formulas(a,b,B,F(1,2))[0] - formulas(a,b,B,F(1))[0] == F(1,12)
print('PASS:',n,'exact generator, curvature and global-optimum assertions; exact symmetric example PASS')
