"""Exact and high-precision checks for the four-speed sorting transition.

The proof is analytic; these checks replay rational endpoint inequalities,
central-cut symmetry, the finite-state rate involution, and the threshold.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import permutations


def f(r, z):
    return 1/z + 1/(1-z) + 1/(r+1-z) + 1/(r+2-z)


def fp(r, z):
    return -1/(z*z)+1/((1-z)*(1-z))+1/((r+1-z)*(r+1-z))+1/((r+2-z)*(r+2-z))


def k(r):
    return 4/r+4/(r+2)


def rational_check():
    z=Q(1,2)
    r=Q(107,100)
    assert k(r)>f(r,z), 'lower threshold witness failed'
    r=Q(27,25)
    assert k(r) < f(r,z)-fp(r,z)**2/Q(64), 'strong-convexity upper threshold witness failed'
    assert k(Q(1))==Q(16,3)
    assert f(Q(1),z)==Q(76,15)
    assert k(Q(2))==Q(3)
    print('PASS exact-rational threshold bracket, 1 < r* < 2, uniform curvature witness')


def invariant_rates():
    r=Q(27,25)
    v=(Q(0),Q(1),1+r,2+r)
    assert all(v[i]+v[3-i]==v[3] for i in range(4))
    checked=0
    def transform(p):return tuple(3-i for i in reversed(p))
    for state in permutations(range(4)):
        st=transform(state)
        assert transform(st)==state
        for j in range(3):
            left,right=state[j],state[j+1]
            if left>right:
                successor=list(state)
                successor[j],successor[j+1]=right,left
                succ=tuple(successor)
                left2,right2=st[2-j],st[3-j]
                assert left2>right2
                assert v[left]-v[right]==v[left2]-v[right2]
                stsucc=list(st)
                stsucc[2-j],stsucc[3-j]=stsucc[3-j],stsucc[2-j]
                assert tuple(stsucc)==transform(succ)
                checked+=1
    assert checked==36,(checked,36)
    print('PASS 36 allowed adjacent transitions on all 24 four-type states under reflection involution')


def high_precision_threshold():
    with localcontext() as ctx:
        ctx.prec=58
        one=Decimal(1)
        zero=Decimal(0)
        def optimum(r):
            lo=Decimal('0.000000000000001')
            hi=one-lo
            for _ in range(205):
                mid=(lo+hi)/2
                if fp(r,mid)>0:hi=mid
                else:lo=mid
            z=(lo+hi)/2
            return f(r,z),z
        lo=Decimal('1.07');hi=Decimal('1.08')
        for _ in range(205):
            mid=(lo+hi)/2
            val=k(mid)-optimum(mid)[0]
            if val>0:lo=mid
            else:hi=mid
        rc=(lo+hi)/2
        minval,zc=optimum(rc)
        assert Decimal('1.075949895620') < rc <Decimal('1.075949895623')
        assert abs(k(rc)-minval)<Decimal('1e-48')
        # Transversality of the macroscopic sorting cusp.
        edge_derivative=-(1/(rc+1-zc)**2+1/(rc+2-zc)**2)/4
        middle_derivative=-(1/(rc*rc)+1/(rc+2)**2)
        assert edge_derivative>middle_derivative
        print('PASS threshold rc=',str(rc)[:39])
        print('PASS edge minimizer zc=',str(zc)[:39])
        print('PASS one-sided slopes, left=',str(middle_derivative)[:26], 'right=',str(edge_derivative)[:26])

if __name__=='__main__':
    rational_check()
    invariant_rates()
    high_precision_threshold()
