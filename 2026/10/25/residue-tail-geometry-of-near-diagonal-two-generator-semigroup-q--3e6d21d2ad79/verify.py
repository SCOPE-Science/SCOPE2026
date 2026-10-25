"""Exact finite regression tests for the near-diagonal numerical-semigroup quotient identities.
This checks finitely many parameters; the symbolic arguments establish the universal claim.
"""
from math import gcd


def thresholds(a, k):
    return [a*t - k*((a-1)*t//(k+1)) for t in range(1,k+1)]


def member_by_modular_coin(a,k,n):
    """Independent two-coin congruence criterion, not based on t-thresholds."""
    if n == 0: return True
    amount=(a-1)*n
    # (a+k)y = amount mod a; y0 is the smallest allowed nonnegative y.
    y0=((amount % a) * pow(k,-1,a)) % a
    return (a+k)*y0 <= amount


def member_by_formula(a,k,n,U):
    if n==0:return True
    return any(n%k==(a*t)%k and n>=U[t-1] for t in range(1,k+1))


def elementary_generator_check(a,U):
    o,e=U
    def inside(n): return member_by_modular_coin(a,2,n)
    observed=[n for n in range(1,2*max(o,e)+a+20)
              if inside(n) and not any(inside(j) and inside(n-j) for j in range(1,n))]
    predicted=list(range(o,o+e,2))+list(range(e,2*o,2))
    assert observed==sorted(predicted),(a,observed,predicted)
    assert len(observed)==o


def test():
    count=0; total_cells=0; gen_cases=0
    for a in range(2,91):
        for k in range(1,51):
            if gcd(a,k)!=1: continue
            U=thresholds(a,k)
            assert all(v>0 for v in U)
            assert len({(a*t)%k for t in range(1,k+1)})==k
            F=max(v-k for v in U)
            G=sum((v-1)//k for v in U)
            direct_gap=[]
            for n in range(1,max(F,0)+k+16):
                exact=member_by_modular_coin(a,k,n)
                predicted=member_by_formula(a,k,n,U)
                assert exact==predicted,(a,k,n,U,exact,predicted)
                if not exact:direct_gap.append(n)
                total_cells+=1
            assert (max(direct_gap) if direct_gap else -1)==F,(a,k,'F',F,direct_gap[-5:])
            assert len(direct_gap)==G,(a,k,'G',G,len(direct_gap))
            count+=1
            if k==2 and a>=3 and a%2==1:
                elementary_generator_check(a,U)
                gen_cases+=1
    print('VERIFY_OK',f'parameter_pairs={count}',f'checked_memberships={total_cells}',f'maximal_embedding_examples={gen_cases}', 'integer_exact=PASS', 'finite_only=YES')


if __name__=='__main__': test()
