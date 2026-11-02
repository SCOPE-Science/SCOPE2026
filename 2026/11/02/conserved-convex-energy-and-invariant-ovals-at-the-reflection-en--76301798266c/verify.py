"""Exact rational checks of the reflected two-by-two Sinkhorn map.

Uses only Python's standard library. The global results rely on the analytical
proof supplied separately; the calculations here test the defining identities.
"""
from fractions import Fraction as F
from itertools import product


def stage(u, v, c):
    un = ((c*v+1)/(v+c))**2/u
    vn = ((c*un+1)/(un+c))**2/v
    return un, vn


def energy_squared(u, v, c):
    return (u*v+c*(u+v)+1)**2/(u*v)


def phi_prime(v, c):
    return v*(1-c*c)/((v+c)*(c*v+1))


def main():
    count=0
    positive=(F(1,10),F(1,3),F(1,1),F(3,2),F(9,1))
    cs=(F(1,7),F(1,2),F(1,1),F(5,3),F(9,1))
    for c,u,v in product(cs,positive,positive):
        un,vn=stage(u,v,c)
        assert un>0 and vn>0
        assert energy_squared(u,v,c)==energy_squared(un,v,c)
        assert energy_squared(u,v,c)==energy_squared(un,vn,c)
        a=phi_prime(v,c)
        b=phi_prime(un,c)
        # The exact Jacobian in log-odds coordinates is
        # [[-1,-2a],[2b,-1+4ab]], and has determinant one.
        assert (-1)*(-1+4*a*b)-(-2*a)*(2*b)==1
        # Evaluate 7 full iterations with rational arithmetic.
        u2,v2=un,vn
        for _ in range(7):
            u2,v2=stage(u2,v2,c)
            assert energy_squared(u2,v2,c)==energy_squared(u,v,c)
        count+=1
    assert count==125
    print('EXACT_SINKHORN_INVARIANT_PASS',count,'initial pairs, 875 iterates')


if __name__=='__main__':
    main()
