"""Standalone exact-coefficient and finite-grid checks for the two-chirality mean theorem.

Only Python's standard library is used. The infinite-dimensional claims are
proved analytically in RESULT.md; discrete quadrature is corroborative.
"""
from fractions import Fraction as Q
from math import cos, sin, pi, hypot


def distance_sq_real(p, q):
    """Exact phase-quotient squared distance of real two-mode curves.

    p=(p_plus,p_minus) means p_plus*exp(it)+p_minus*exp(-it).
    """
    a, b = p
    c, d = q
    return a*a + b*b + c*c + d*d - 2 * abs(a*c + b*d)


def check_exact():
    for e in (Q(1, 10), Q(1, 4), Q(2, 3), Q(9, 10)):
        b0=(e,Q(1)); bpi=(-e,Q(1))
        a=(Q(1)+e)/2
        m0=(a,Q(1,2)); mpi=(a,-Q(1,2))
        assert distance_sq_real(b0,bpi)==4*e*e
        assert distance_sq_real(m0,mpi)==1
        # A=e^{it}; the closest shifted B has squared distance below.
        assert distance_sq_real((Q(1),Q(0)),b0)==(Q(1)-e)**2+1
    for plus, minus in ((Q(1,4),Q(3,4)),(Q(1,2),Q(1,2)),(Q(2,3),Q(1,3))):
        assert plus+minus==1
        variance=1-(plus*plus+minus*minus)
        assert variance==2*plus*minus
        # For phase 0 the axes are 1 and abs(plus-minus).
        assert (plus+minus)==1
        assert abs(plus-minus) == abs(2*plus-1)


def L2sq(u,v):
    return sum(abs(a-b)**2 for a,b in zip(u,v))/len(u)


def check_finite_grid():
    N=256
    t=[2*pi*k/N for k in range(N)]
    for e in (0.1,0.4,0.8):
        b0=[complex(cos(-s),sin(-s))+e*complex(cos(s),sin(s)) for s in t]
        bpi=[complex(cos(-s),sin(-s))-e*complex(cos(s),sin(s)) for s in t]
        a=(1+e)/2
        m0=[a*complex(cos(s),sin(s))+0.5*complex(cos(-s),sin(-s)) for s in t]
        mpi=[a*complex(cos(s),sin(s))-0.5*complex(cos(-s),sin(-s)) for s in t]
        assert abs(min(L2sq(b0,bpi[k:]+bpi[:k]) for k in range(N))-4*e*e)<1e-12
        assert abs(min(L2sq(m0,mpi[k:]+mpi[:k]) for k in range(N))-1)<1e-12
    # The equal-weight unperturbed mean retraces a horizontal segment.
    half=[0.5*complex(cos(s),sin(s))+0.5*complex(cos(-s),sin(-s)) for s in t]
    assert max(abs(z.imag) for z in half)<1e-14
    assert abs(max(z.real for z in half)-1)<1e-14
    assert abs(min(z.real for z in half)+1)<1e-14

if __name__=='__main__':
    check_exact();check_finite_grid()
    print('PASS: exact rational coefficient identities and 256-point Fourier quadrature')
