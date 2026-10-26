"""Exact integer-semigroup and polynomial-identity checks for Jacobian blowup charts."""

def semigroup(r, limit):
    return {2*a+r*b for a in range(limit+1) for b in range(limit+1)}

def verify():
    for m in range(3,42,2):
        for label,r in [('wild',m),('tame',m-2)]:
            S=semigroup(r,4*m)
            gaps=[n for n in range(2*m) if n not in S]
            assert gaps==list(range(1,r-1,2)), (m,label,gaps)
            assert len(gaps)==(r-1)//2
            assert all(n in S for n in range(r-1,2*m))
            assert r-2 not in S if r>=3 else True
        assert (m-1)//2-(m-3)//2==1
        assert (m-1)-(m-3)==2
    # On the x-chart with t=y/x, wild: tx^2=z^m, tame:
    # xu=z^(m-1), tx^2=z^m, eliminate x via x=zu/t:
    # u^2=t*z^(m-2), checked symbolically via monomial exponents.
    for m in range(3,42,2):
        # Set z=s^2/t and u=s^(m-2)/t^((m-3)/2).
        # Their squares agree with t*z^(m-2).
        assert (2*(m-2), -(m-3))==(2*(m-2),1-(m-2))
        # Set x=s^m/t^((m+1)/2); t*x^2=z^m.
        assert (2*m,1-(m+1))==(2*m,-m)
        # xu=z^(m-1).
        assert (m+(m-2),-((m+1)//2+(m-3)//2))==(2*m-2,-(m-1))
    print('CHECK_OK: odd m 3..41, numerical semigroups, conductors, charts, normalizations')

if __name__=='__main__': verify()
