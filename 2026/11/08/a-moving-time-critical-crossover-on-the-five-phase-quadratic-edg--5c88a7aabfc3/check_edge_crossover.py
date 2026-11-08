"""Reproducibility checks for an invariant-edge crossover of a five-phase map."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def W(x, p):
    x1,x2,x3,x4,x5=x
    return (x5*(1+p*(x1-x2+x3-x4)),
            x1*(1+p*(x2-x3+x4-x5)),
            x2*(1-p*(x1-x3+x4-x5)),
            x3*(1+p*(x1-x2+x4-x5)),
            x4*(1-p*(x1-x2+x3-x5)))


def f(z,p):
    return z*(1+p*(1-z))


def T(t,q):
    return q*t+(1-q)*t*t


for p in [Q(-1),Q(-1,2),Q(0),Q(1,3),Q(4,5),Q(1)]:
    for s in [Q(1,7),Q(3,5),Q(8,9)]:
        x=(s,1-s,Q(0),Q(0),Q(0))
        for _ in range(5): x=W(x,p)
        scalar=s
        for _ in range(5): scalar=f(scalar,p)
        assert x==(scalar,1-scalar,Q(0),Q(0),Q(0))
        t=1-s
        for _ in range(5):t=T(t,1-p)
        assert t==1-scalar
print('FIVE_STEP_RETURN_EXACT_RATIONAL_OK')

for s in [Q(1,7),Q(2,5),Q(9,10)]:
    t0=1-s
    x=s
    for n in range(1,5):
        for _ in range(5):x=f(x,Q(1))
        assert x==1-t0**(32**n)
    x=s
    for n in range(1,5):
        for _ in range(5):x=f(x,Q(-1))
        assert x==s**(32**n)
print('SINGULAR_EXACT_POWERS_OK')

with localcontext() as ctx:
    ctx.prec=210
    t0=Decimal('0.8'); c=Decimal('1.7')
    previous=None
    for n in [1,2,3]:
        m=5*n
        vm=t0**(2**m)
        q=vm/c
        tj=t0
        for j in range(m):tj=T(tj,q)
        r0=tj/q
        # The analytic bound guarantees convergence, independently of these tests.
        bound=Decimal(2**m-1)*vm.sqrt()/c
        assert r0>=c
        if n<=2:
            assert (r0/c).ln()<=bound*Decimal('1.00000000001')
        else:
            assert abs(r0-c)<Decimal('1e-190')
        for _ in range(5):tj=T(tj,q)
        r1=tj/(q**6)
        target=c+c*c
        error=abs(r1-target)
        if previous is not None: assert error<previous
        previous=error
        print('n',n,'transitional_relative_error',str(error)[:55])
    assert previous<Decimal('1e-150')
print('MOVING_TIME_CROSSOVER_AND_BOUND_OK')
