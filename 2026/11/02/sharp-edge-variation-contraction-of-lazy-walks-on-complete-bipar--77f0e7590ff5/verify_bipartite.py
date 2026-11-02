"""Exact-rational checks for sharp graph-edge variation of bipartite neighbor averaging.

No external dependencies. All comparisons are exact. Finite tests supplement the
written proof; they do not establish its all-size validity.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def param_formula(p, q, alpha):
    M = max(p, q)
    return max(1 - 2*alpha, 1 - 2*(1-alpha)/M)


def direct_operator(f, p, q, alpha):
    aa, bb = f[:p], f[p:]
    ma = sum(aa, F(0))/p
    mb = sum(bb, F(0))/q
    return [alpha*x+(1-alpha)*mb for x in aa] + [alpha*y+(1-alpha)*ma for y in bb]


def variation(f, p, q):
    return sum((abs(f[i] - f[p+j]) for i in range(p) for j in range(q)), F(0))


def cut_ratio_by_counts(p, q, alpha, r, s):
    E = p*q
    U = r*(q-s)
    V = (p-r)*s
    D = U + V
    if D == 0:
        return None
    delta = F(U-V,E)
    k=1-alpha
    return (U*abs(alpha-k*delta) + V*abs(alpha+k*delta)
            + (E-D)*k*abs(delta))/D


def run():
    alpha_cases = [F(0), F(1,10), F(1,5), F(1,3), F(1,2),
                   F(2,3), F(4,5), F(1)]
    direct_checks = 0
    all_cut_checks = 0
    count_checks = 0
    equality_checks = 0
    for p in range(2,6):
        for q in range(2,6):
            local_alphas = sorted(set(alpha_cases+[F(1,max(p,q)+1)]))
            for alpha in local_alphas:
                target = param_formula(p,q,alpha)
                worst = F(0)
                # Completely direct computations on all nonconstant binary
                # signals (not using the reduced count formula).
                for bits in product((0,1), repeat=p+q):
                    f = list(map(F, bits))
                    denominator = variation(f,p,q)
                    if denominator == 0:
                        continue
                    out = direct_operator(f,p,q,alpha)
                    z = variation(out,p,q)/denominator
                    worst = max(worst,z)
                    assert z <= target,(p,q,alpha,bits,z,target)
                    all_cut_checks += 1
                assert worst == target,(p,q,alpha,worst,target)
                equality_checks += 1
                for r in range(p+1):
                    for s in range(q+1):
                        if not (0<r*(q-s)+(p-r)*s):
                            continue
                        by_formula = cut_ratio_by_counts(p,q,alpha,r,s)
                        f = list(map(F,[1]*r+[0]*(p-r)+[1]*s+[0]*(q-s)))
                        by_direct = variation(direct_operator(f,p,q,alpha),p,q)/variation(f,p,q)
                        assert by_formula == by_direct
                        count_checks += 1
    # Arbitrary real-valued rational data: direct sharp inequality.
    rand = Random(173)
    for _ in range(1200):
        p=rand.randrange(2,8);q=rand.randrange(2,8)
        alpha=F(rand.randrange(0,17),16)
        f=[F(rand.randrange(-50,51),rand.randrange(1,16)) for _ in range(p+q)]
        den=variation(f,p,q)
        if den:
            assert variation(direct_operator(f,p,q,alpha),p,q) <= param_formula(p,q,alpha)*den
            direct_checks += 1
    # Point extremizers realize the descending and ascending affine branches.
    for p in range(2,15):
        for q in range(2,15):
            M=max(p,q)
            for alpha in [F(0),F(1,M+1),F(1,2),F(1)]:
                target=param_formula(p,q,alpha)
                full_side=[F(1)]*p+[F(0)]*q
                one_large=[F(0)]*(p+q)
                one_large[0 if p>=q else p]=F(1)
                vals=[]
                for f in (full_side,one_large):
                    vals.append(variation(direct_operator(f,p,q,alpha),p,q)/variation(f,p,q))
                assert max(vals)==target,(p,q,alpha,vals,target)
                equality_checks += 1
    print('PASS exact direct indicator checks:',all_cut_checks)
    print('PASS independent count-formula checks:',count_checks)
    print('PASS arbitrary rational input checks:',direct_checks)
    print('PASS equality/extremizer cases:',equality_checks)
    print('No floating-point tolerance used.')

if __name__ == '__main__':
    run()
