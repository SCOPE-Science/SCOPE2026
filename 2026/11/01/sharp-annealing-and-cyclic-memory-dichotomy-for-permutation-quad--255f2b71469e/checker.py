"""Exact finite-iterate checks for an inhomogeneous permutation QSO.

Run: python verify_permutation_annealing.py
Only finite algebraic identities are tested; infinite-limit claims use proofs.
"""
from fractions import Fraction as F
from itertools import permutations


def permute(z, permutation):
    return tuple(z[permutation[i]] for i in range(len(z)))


def qso_step(x, permutation, alpha):
    s = x[-1]
    z = x[:-1]
    pz = permute(z, permutation)
    return tuple(2*s*(alpha*z[i]+(1-alpha)*pz[i]) for i in range(len(z))) + (s*s+(1-s)*(1-s),)


def mixed(z, permutation, alpha):
    pz = permute(z, permutation)
    return tuple(alpha*a+(1-alpha)*b for a,b in zip(z,pz))


def normalized_exact(x0, permutation, alphas):
    s0 = x0[-1]
    u0 = 2*s0-1
    z = tuple(t/(1-s0) for t in x0[:-1])
    for a in alphas:
        z = mixed(z, permutation, a)
    u = u0 ** (2**len(alphas))
    return tuple((1-u)*q/2 for q in z) + ((1+u)/2,)


def compose_perm(p, q):
    return tuple(q[p[i]] for i in range(len(p)))


def perm_power(p, n):
    out = tuple(range(len(p)))
    for _ in range(n):
        out = compose_perm(out, p)
    return out


def rotating_factor(z, p, alphas):
    b = 0
    q = tuple(z)
    inv = tuple(p.index(i) for i in range(len(p)))
    for a in alphas:
        delta = min(a, 1-a)
        is_rotation = a < F(1, 2)
        b += is_rotation
        q = mixed(q, inv if is_rotation else p, 1-delta)
    return permute(q, perm_power(p, b))


def check():
    tested = 0
    for k in range(2, 6):
        candidates = list(permutations(range(k)))
        for p in candidates[::max(1, len(candidates)//15)]:
            for s0 in (F(1, 7), F(2, 5), F(3, 4)):
                z0 = tuple(F(j+1, k*(k+1)//2) for j in range(k))
                x0 = tuple((1-s0)*t for t in z0)+(s0,)
                patterns = (
                    (F(0), F(1), F(0), F(1)),
                    (F(1,2), F(3,4), F(2,5)),
                    (F(1,4), F(1,5), F(1,6), F(1,7), F(1,8)),
                    (F(9,10), F(99,100), F(1), F(0), F(1,30)),
                )
                for aa in patterns:
                    x = x0
                    for n in range(len(aa)+1):
                        assert sum(x)==1 and all(t>=0 for t in x)
                        assert x == normalized_exact(x0, p, aa[:n])
                        z = tuple(t/(1-s0) for t in x0[:-1])
                        for a in aa[:n]:
                            z = mixed(z,p,a)
                        assert z == rotating_factor(z0,p,aa[:n])
                        tested+=1
                        if n < len(aa):
                            x = qso_step(x,p,aa[n])
    # Exact annihilation on every two-cycle at the 50:50 step.
    p=(1,0,3,2)
    z=tuple(map(F,(1,0,0,0)))
    zz=mixed(z,p,F(1,2))
    assert zz==mixed(zz,p,F(0))==mixed(zz,p,F(1))
    # For a three-cycle the same step does not annihilate the 120-degree mode.
    p=(1,2,0)
    z=(F(1),F(0),F(0))
    assert mixed(z,p,F(1,2))!= (F(1,3),)*3
    print('PASS:',tested,'exact iterate/factorization identities, plus exceptional-mode checks.')

if __name__=='__main__':
    check()
