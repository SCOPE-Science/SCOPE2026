"""Exact finite checks for the qutrit irrational-gap passivity theorem.

Only stdlib integer comparisons are used for the classification checks.
"""
from fractions import Fraction
from math import sqrt


def phi_sign(a, b):
    """Sign of a+b*phi for integer a,b with phi=(1+sqrt(5))/2."""
    u = 2*a + b
    v = b
    if v == 0:
        return (u > 0) - (u < 0)
    if u >= 0 and v > 0:
        return 1
    if u <= 0 and v < 0:
        return -1
    # Opposite signs; decide without floating point.
    cmp = u*u - 5*v*v
    if cmp == 0:
        raise AssertionError('unexpected irrational equality')
    if u > 0:
        return (cmp > 0) * 2 - 1
    return (cmp < 0) * 2 - 1


def interval_hit(p, q, delta):
    assert p > 0 and q > 0 and delta > 0
    # phi < p/q < phi+delta.
    # Exact integer computation: phi < p/q iff p-q*phi>0.
    if phi_sign(p,-q) <= 0:
        return False
    return phi_sign(p*delta.denominator-q*delta.numerator, -q*delta.denominator) < 0


def irrational_boundary_first(k):
    # The endpoint is delta=F_(2k+3)/F_(2k+2)-phi.
    # Therefore phi < p/q < phi+delta means phi < p/q < U_k.
    pk=fibonacci(2*k+3)
    qk=fibonacci(2*k+2)
    target=fibonacci(2*k+6)
    for N in range(2,target+1):
        for p in range(1,N):
            q=N-p
            if phi_sign(p,-q)>0 and p*qk<pk*q:
                return N,p,q
    return None


def pair_violates(high, low, delta):
    # count triples (n0,n1,n2), energy = n1+(1+phi)*n2
    # minus log(prob)/beta = n1+(1+phi+delta)*n2 (+ const)
    d1 = high[1] - low[1]
    d2 = high[2] - low[2]
    en = phi_sign(d1+d2,d2)
    cost = phi_sign((d1+d2)*delta.denominator+d2*delta.numerator,
                    d2*delta.denominator)
    return en*cost < 0


def is_active_exhaustive(N,delta):
    occ = [(N-b-c,b,c) for b in range(N+1) for c in range(N-b+1)]
    for i,x in enumerate(occ):
        for y in occ[i+1:]:
            if pair_violates(x,y,delta):
                return True
    return False


def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def predicted(delta):
    k=0
    while True:
        p=fibonacci(2*k+3)
        q=fibonacci(2*k+2)
        if interval_hit(p,q,delta):
            return p+q,p,q,k
        k+=1
        if k>1000:
            raise RuntimeError('no rational approximation found')


def brute_fraction(delta, nmax):
    for N in range(2,nmax+1):
        for p in range(1,N):
            if interval_hit(p,N-p,delta):
                return N,p,N-p
    return None


def run():
    vals=[Fraction(1,2),Fraction(2,5),Fraction(1,3),Fraction(1,4),
          Fraction(1,10),Fraction(1,20),Fraction(1,50),Fraction(1,100),
          Fraction(1,200),Fraction(1,500),Fraction(1,1000),
          Fraction(1,2000),Fraction(1,10000)]
    rows=[]
    for delta in vals:
        N,p,q,k=predicted(delta)
        assert brute_fraction(delta,N)==(N,p,q), ('rational',delta,N,p,q)
        if N<=24:
            for n in range(1,N+2):
                assert is_active_exhaustive(n,delta)==(n>=N), (delta,n,N)
        rows.append((str(delta),N,p,q,k))
    for k in range(0,8):
        p=fibonacci(2*k+3)
        q=fibonacci(2*k+2)
        assert p*q>0
        assert phi_sign(p,-q)>0
        if k:
            pu=fibonacci(2*k+1)
            qu=fibonacci(2*k)
            pl=fibonacci(2*k+2)
            ql=fibonacci(2*k+1)
            assert pu*ql-pl*qu==1
            assert p==pu+pl and q==qu+ql
    for k in range(6):
        nxt=(fibonacci(2*k+5),fibonacci(2*k+4))
        assert irrational_boundary_first(k)==(sum(nxt),*nxt), ('strict_boundary',k)
    print('VERIFY_OK rational_Farey_cases=%d exact_occupancy=%d fibonacci_neighbors=8 irrational_boundaries=6' % (len(vals),sum(predicted(d)[0]<=24 for d in vals)))
    for x in rows:
        print('delta=%s N=%d p=%d q=%d step=%d' % x)
    print('asymptotic_envelope',((1+sqrt(5))/2)**2/(5**0.25),((1+sqrt(5))/2)**4/(5**0.25))
if __name__=='__main__':run()
