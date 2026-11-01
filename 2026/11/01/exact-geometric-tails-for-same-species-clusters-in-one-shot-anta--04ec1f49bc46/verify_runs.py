"""Independent finite-path checks for one-attempt antagonistic adsorption.

Run: python verify_runs.py
Requires only the Python standard library.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial, cosh, sinh, sqrt


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def scale(a, c): return [c*x for x in a]


def integral(a): return [F(0)] + [x / (i+1) for i,x in enumerate(a)]


def polyval(a, t): return sum((v*t**i for i,v in enumerate(a)), F(0))


def endpoint_polynomials(length, p):
    """Exact half-path boundary probabilities as rational polynomials."""
    q = 1-p
    A, B = [F(0), p], [F(0), q]
    for _ in range(2, length+1):
        A, B = add([F(0),p], scale(integral(B), -p)), add([F(0),q], scale(integral(A), -q))
    return A, B


def predicted(n, lo, k, p, t):
    left, _ = endpoint_polynomials(lo+1, p)
    right, _ = endpoint_polynomials(n-lo-k+1, p)
    return (p*t)**(k-2) * polyval(left,t) * polyval(right,t)


def get_counts(n, targets):
    """Exhaustively enumerate ALL active sets, orders and A/B assignments.

    An active subset with m indices has probability t^m(1-t)^(n-m),
    each of its m! priority orders is uniform; proposed labels have
    independent probabilities p and 1-p.
    """
    counts = {tar: defaultdict(int) for tar in targets}
    arrangements = 0
    for m in range(n+1):
        for active in combinations(range(n), m):
            for order in permutations(active):
                for labels in product((-1,1), repeat=m):
                    lab = dict(zip(active, labels))
                    state = [0]*n
                    for i in order:
                        x=lab[i]
                        if ((i==0 or state[i-1]!=-x)
                                and (i==n-1 or state[i+1]!=-x)):
                            state[i]=x
                    a=sum(x==1 for x in labels)
                    for lo,k in targets:
                        if all(x==1 for x in state[lo:lo+k]):
                            counts[(lo,k)][(m,a)] += 1
                    arrangements += 1
    return counts, arrangements


def exact_from_counts(counts, n, p, t):
    q=1-p
    return sum((ct*t**m*(1-t)**(n-m)*p**a*q**(m-a)/factorial(m)
                for (m,a),ct in counts.items()), F(0))


def asymptotic_halfline(p,t):
    pf,tf=float(p),float(t)
    if pf==0: return 0.0
    if pf==1: return tf
    g=sqrt(pf*(1-pf))
    return 1-cosh(g*tf)+(pf/g)*sinh(g*tf)


def run():
    assertions=0; histories=0; cases=0
    for n in range(3,8):
        targets = [(i,k) for k in range(2,n+1)
                   for i in range(n-k+1)
                   if i in (0, (n-k)//2, n-k)]
        targets = sorted(set(targets))
        counts, a = get_counts(n,targets)
        histories+=a
        for p,t in product((F(1,3),F(1,2),F(2,3)),(F(1,2),F(1))):
            for lo,k in targets:
                x=exact_from_counts(counts[(lo,k)],n,p,t)
                y=predicted(n,lo,k,p,t)
                assert x==y, (n,lo,k,p,t,x,y)
                assertions+=1;cases+=1
    for p,t in product((F(1,3),F(1,2),F(2,3)),(F(1,2),F(1))):
        exact=asymptotic_halfline(p,t)
        for length in (4,6,8,10,12):
            poly,_=endpoint_polynomials(length,p)
            val=float(polyval(poly,t))
            err=abs(val-exact)
            # A dependence on a site beyond this finite half-path
            # requires at least length+1 strictly ordered attempt times.
            bd=float(t)**(length+1)/factorial(length+1)
            assert err<=bd+2e-14,(p,t,length,err,bd)
            assertions+=1
    for p,t in ((.5,1),(.35,.6),(.8,1),(.2,.9)):
        c=asymptotic_halfline(p,t)
        for k in range(2,16):
            qk=c*c*(p*t)**(k-2)
            lk=qk*(1-p*t)**2
            assert abs((qk-2*c*c*(p*t)**(k-1)+c*c*(p*t)**k)-lk)<1e-12
            assertions+=1
        assert abs(sum(c*c*(1-p*t)**2*(p*t)**(k-2) for k in range(2,400))
                   -c*c*(1-p*t))<1e-12
        assertions+=1
    print('PASS: %s exact/analytical assertions; %s exhaustive priority-and-label histories; %s finite joint-event comparisons' % (assertions,histories,cases))


if __name__ == '__main__': run()
