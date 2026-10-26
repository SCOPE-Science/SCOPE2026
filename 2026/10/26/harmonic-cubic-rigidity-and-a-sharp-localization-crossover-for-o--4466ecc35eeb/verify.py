"""Exact-rational checks for full-frame finite-difference risk identities.

Run with Python 3: python verify.py. The analytic theorem uses spherical
sixth-moment identities; the finite tests here detect algebra/transcription
mistakes and are not substitutes for the proof.
"""
from fractions import Fraction as F
from itertools import product


def pairings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for i in range(1, len(items)):
        second = items[i]
        for rest in pairings(items[1:i] + items[i+1:]):
            yield ((first, second),) + rest

PAIRS4 = tuple(pairings(tuple(range(4))))
PAIRS6 = tuple(pairings(tuple(range(6))))
assert len(PAIRS4) == 3 and len(PAIRS6) == 15


def sphere_moment(indices, n, pairlist):
    denom = n
    for j in range(2, len(indices), 2):
        denom *= n+j
    count = sum(all(indices[a] == indices[b] for a,b in p) for p in pairlist)
    return F(count, denom)


def tensor(n, values):
    # Sum of three symmetric rank-one cubic tensors with rational directions.
    vecs = [[F((i+2*j+1) % 5 - 2, j+2) for i in range(n)] for j in range(3)]
    return {(i,j,k): sum(F(values[q])*v[i]*v[j]*v[k] for q,v in enumerate(vecs))
            for i,j,k in product(range(n), repeat=3)}


def moments(n,T):
    rng=range(n)
    trace=[sum(T[i,j,j] for j in rng) for i in rng]
    norm=sum(x*x for x in T.values())
    tnorm=sum(x*x for x in trace)
    true_mean=[F(0) for _ in rng]
    for i,j,k,a in product(rng, repeat=4):
        true_mean[a] += T[i,j,k]*sphere_moment((i,j,k,a), n, PAIRS4)
    true_mean=[x*F(n,6) for x in true_mean]
    mean_expected=[F(x,1)*F(1,2*(n+2)) for x in trace]
    assert true_mean == mean_expected, (true_mean, mean_expected)
    sixth=F(0)
    for i,j,k,a,b,c in product(rng, repeat=6):
        sixth += T[i,j,k]*T[a,b,c]*sphere_moment((i,j,k,a,b,c),n,PAIRS6)
    expected_sixth=F(6*norm+9*tnorm,n*(n+2)*(n+4))
    assert sixth==expected_sixth, (sixth,expected_sixth)
    E2=F(n,36)*sixth
    predicted_E2=F(6*norm+9*tnorm,36*(n+2)*(n+4))
    assert E2==predicted_E2
    variance=E2-sum(x*x for x in true_mean)
    predicted_var=F(1,6*(n+2)*(n+4))*(norm-F(3,n+2)*tnorm)
    assert variance==predicted_var and variance>=0
    return variance


def rankone_crossovers(n):
    cutoff=F(15,(n+2)*(n+4))
    assert F(1,n*n)<cutoff<1
    sparse=F(1)
    dense=F(1,n*n)
    assert sparse>cutoff and dense<cutoff
    # Sharp worst ratio for fixed-coordinate versus Haar orientation and converse.
    assert F(1,cutoff)==F((n+2)*(n+4),15)
    assert cutoff/dense==F(15*n*n,(n+2)*(n+4))
    return cutoff


def check_trace_pure(n):
    rng=range(n)
    t=[F(i+1,7) for i in rng]
    T={(i,j,k): (t[i]*int(j==k)+t[j]*int(i==k)+t[k]*int(i==j))/F(n+2)
       for i,j,k in product(rng, repeat=3)}
    assert moments(n,T)==0


def check_basis(n):
    if n!=2: return
    # Orthogonal rational rotation; check a pure-trace cubic remains deterministic.
    q=[F(2,3),F(-1,4)]
    def T(i,j,k):
        return (q[i]*int(j==k)+q[j]*int(i==k)+q[k]*int(i==j))/F(n+2)
    bases=[[[F(1),F(0)],[F(0),F(1)]],
           [[F(3,5),F(4,5)],[F(-4,5),F(3,5)]]]
    for basis in bases:
        z=[F(0),F(0)]
        for u in basis:
            cubic=sum(T(i,j,k)*u[i]*u[j]*u[k] for i,j,k in product(range(2),repeat=3))
            for i in range(2):z[i]+=cubic*u[i]/6
        assert z==[x/F(2*(n+2)) for x in q]


def main():
    tests=0
    for n in (2,3,4):
        for values in ((1,2,-1),(-2,1,3)):
            v=moments(n,tensor(n,values)); assert v>=0;tests+=1
        check_trace_pure(n);tests+=1
        check_basis(n)
        print('n',n,'rank-one crossover',rankone_crossovers(n))
    for n in range(2,101):
        rankone_crossovers(n);tests+=1
    # f(x)=||x||^2/2+s^3/6+s^4/24 has Hessian I+(s+s^2/2)aa^T
    # and s+s^2/2 = (s+1)^2/2-1/2 >= -1/2.
    for s in (F(-100),F(-2),F(-1),F(-1,2),F(0),F(1),F(99)):
        assert F(1)+s+s*s/2>=F(1,2)
    print('PASS',tests,'exact tensor/crossover test cases, plus strong-convexity samples')

if __name__=='__main__':main()
