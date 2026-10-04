from decimal import Decimal, getcontext
from itertools import product
getcontext().prec = 60

def s_star(p,q):
    p=Decimal(p); q=Decimal(q)
    return (p-Decimal(2))/Decimal(4) * ((Decimal(1)+Decimal(8)*q/((p-Decimal(1))*(p-Decimal(2)))).sqrt()-Decimal(1))

def candidate_s(p,q):
    return max(Decimal(1), s_star(p,q))

def curv_formulas(p,q,s):
    dx=Decimal(p-1)*s+Decimal(q)
    da=s+Decimal(p-2)
    leaf=Decimal(2)/dx
    inner=(s+Decimal(p-1))/da
    num=Decimal(2*(p-1))*s*s+Decimal((p-1)*(p-2))*s-Decimal(q*(p-2))
    xa=num/(dx*da)
    return leaf,inner,xa

def brute_xa(p,q,s):
    dx=Decimal(p-1)*s+Decimal(q)
    da=s+Decimal(p-2)
    best=None
    for zs in product((Decimal(0),Decimal(1)), repeat=p-2):
        for ls in product((Decimal(-1),Decimal(0),Decimal(1)), repeat=q):
            # x=0, a=1. These choices are all edge-Lipschitz: clique values in {0,1}; leaves in {-1,0,1}.
            delx=(s + s*sum(zs) + sum(ls))/dx
            dela=(-s + sum(zs)-Decimal(p-2))/da
            val=delx-dela
            if best is None or val<best: best=val
    return best

checks=0
for p in range(3,13):
    for q in range(1,61):
        s=candidate_s(p,q)
        leaf,inner,xa=curv_formulas(p,q,s)
        assert leaf>0 and inner>0 and xa>=Decimal('-1e-45')
        root=s_star(p,q)
        threshold=Decimal(p*(p-1))/Decimal(p-2)
        assert (s==Decimal(1)) == (Decimal(q)<=threshold)
        # root equation when the nontrivial branch is active
        if s>1:
            lhs=Decimal(q)
            rhs=Decimal(p-1)*s*(Decimal(1)+Decimal(2)*s/Decimal(p-2))
            assert abs(lhs-rhs)<Decimal('1e-45')
        checks += 1

# Independent finite minimization of the x--clique-edge dual objective.
brute=0
for p in range(3,8):
    for q in range(1,5):
        s=candidate_s(p,q)
        direct=brute_xa(p,q,s)
        formula=curv_formulas(p,q,s)[2]
        assert abs(direct-formula)<Decimal('1e-45')
        brute += 1

print(f'ALL CHECKS PASSED; parameter_pairs={checks}; brute_dual_cases={brute}; max_p=12; max_q=60')
