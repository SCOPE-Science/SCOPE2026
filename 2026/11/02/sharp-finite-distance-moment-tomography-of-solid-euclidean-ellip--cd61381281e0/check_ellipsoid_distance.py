"""Checks exact rational identities for chord-moment reconstruction of solid ellipsoids.
Scientific calculations are purely symbolic/rational; this does not certify literature priority.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product


def compositions(n, d):
    if d == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for z in compositions(n-k, d-1):
                yield (k,) + z


def poch(a, k):
    z = F(1)
    for i in range(k):
        z *= a + i
    return z


def ball_even_coord_moment(a):
    d = len(a)
    p = F(1)
    for x in a:
        p *= poch(F(1,2), x)
    return p / poch(F(d,2)+1, sum(a))


def direct_pair_distance_moment(s, k):
    d=len(s)
    total=F(0)
    for a in compositions(k,d):
        coeff=F(factorial(k))
        for v,ax in zip(s,a):
            coeff *= F(v)**ax / factorial(ax)
        z=F(0)
        for p in product(*(range(x+1) for x in a)):
            term=ball_even_coord_moment(p)*ball_even_coord_moment([ai-pi for ai,pi in zip(a,p)])
            for ai,pi in zip(a,p):
                term *= comb(2*ai,2*pi)
            z += term
        total += coeff*z
    return total


def b_unit_ball_pair(d,k):
    out=F(1)
    for j in range(1,k+1):
        out *= F(2*(d+2*j-1)*(d+2*j-2), (d+2*j)*(d+j))
    return out


def generating_angular_moment(s,k):
    d=len(s)
    v=F(0)
    for a in compositions(k,d):
        z=F(1)
        for si,ai in zip(s,a):
            z *= poch(F(1,2),ai)*F(si)**ai/factorial(ai)
        v+=z
    return v*factorial(k)/poch(F(d,2),k)


def recover_polynomial(moment_list):
    d=len(moment_list)-1
    c=[F(1)] + [poch(F(d,2),k)*moment_list[k]/(factorial(k)*b_unit_ball_pair(d,k)) for k in range(1,d+1)]
    h=[F(1)]
    for k in range(1,d+1):
        h.append(-sum(c[j]*h[k-j] for j in range(1,k+1)))
    return [sum(h[j]*h[k-j] for j in range(k+1)) for k in range(d+1)]


def factored_coeff(s):
    p=[F(1)]
    for si in s:
        q=[F(0)]*(len(p)+1)
        for k,v in enumerate(p):
            q[k]+=v
            q[k+1]-=F(si)*v
        p=q
    return p


def test():
    for d in range(2,6):
        s=[F(i+1) for i in range(d)]
        moments=[F(1)]
        for k in range(1,d+1):
            direct=direct_pair_distance_moment(s,k)
            angular=b_unit_ball_pair(d,k)*generating_angular_moment(s,k)
            assert direct==angular,(d,k,direct,angular)
            moments.append(direct)
        assert recover_polynomial(moments)==factored_coeff(s),(d,recover_polynomial(moments),factored_coeff(s))
        # Equal-axis multiplicities test
        s=[F(2)]*d
        moments=[F(1)]+[direct_pair_distance_moment(s,k) for k in range(1,d+1)]
        assert recover_polynomial(moments)==factored_coeff(s)
        print('DIMENSION',d,'RATIONAL_DOUBLE_BALL_MOMENTS_AND_INVERSION_PASSED')
    for d in range(2,9):
        b1=b_unit_ball_pair(d,1)
        assert b1==F(2*d,d+2)
        b2=b_unit_ball_pair(d,2)
        assert b2==F(2*d,d+4)+F(2*d,d+2)
    print('UNIT_BALL_RADIAL_NORMALIZATION_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    test()
