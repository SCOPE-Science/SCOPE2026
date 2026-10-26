"""Exact, standalone checker for task-conditioned RS collision statistics.
Run: python3 verify.py (requires only Python standard library)."""
import itertools
from collections import Counter
from fractions import Fraction
from math import comb


def C(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def avoidance(q, K, r):
    return sum((-1)**t * C(r,t) * (q**(K-t)-1)
               for t in range(min(r,K-1)+1))


def predicted(q, K, T, S):
    return [C(T,j)*sum((-1)**h*C(j,h)*C(avoidance(q,K,T-j+h),S)
                        for h in range(j+1)) for j in range(T+1)]


def brute(q, K, T, S):
    # q prime in this verifier; deterministic enumeration of every test family.
    ps = list(itertools.product(range(q),repeat=K))[1:]
    # 1: skips all-zero coefficients in product order
    root_masks = []
    for p in ps:
        mask=0
        for x in range(T):
            if sum(a*pow(x,i,q) for i,a in enumerate(p))%q==0:
                mask |= 1 << x
        root_masks.append(mask)
    out=Counter()
    for inds in itertools.combinations(range(len(ps)), S):
        m=0
        for idx in inds: m |= root_masks[idx]
        out[m.bit_count()]+=1
    return [out[i] for i in range(T+1)]


def exact_mean_var(q,K,T,S):
    M=q**K-1
    total=C(M,S)
    a=Fraction(C(avoidance(q,K,1),S),total)
    b=Fraction(C(avoidance(q,K,2),S),total) if T>=2 else a
    mean=1-a
    var=(a*(1-a)+(T-1)*(b-a*a))/T
    return mean,var


def exact_maximizers(q,K,T,S):
    L=S*(K-1)
    if K == 1: return C(q-1,S)
    if L>T:return None
    num=C(T,L)
    # Partition L chosen roots into S unlabeled size K-1 groups.
    from math import factorial
    return num*factorial(L)//(factorial(K-1)**S*factorial(S))*(q-1)**S


def main():
    count=0
    for q in (2,3,5):
        for K in range(1,min(q,3)+1):
            for T in range(K,q+1):
                M=q**K-1
                Ss=range(M+1) if M<=24 else range(4)
                for S in Ss:
                    if C(M,S)>20000:continue
                    got=brute(q,K,T,S)
                    want=predicted(q,K,T,S)
                    assert want==got,(q,K,T,S,want,got)
                    assert sum(want)==C(M,S)
                    assert all(n>=0 for n in want)
                    assert max(i for i,x in enumerate(want) if x) == min(T,S*(K-1)), (q,K,T,S,want)
                    mean,var=exact_mean_var(q,K,T,S)
                    brute_mean=Fraction(sum(i*v for i,v in enumerate(got)),T*C(M,S))
                    brute_var=Fraction(sum(i*i*v for i,v in enumerate(got)),T*T*C(M,S))-brute_mean**2
                    assert mean==brute_mean and var==brute_var, (q,K,T,S,mean,brute_mean,var,brute_var)
                    witness=exact_maximizers(q,K,T,S)
                    if witness is not None:assert witness==got[S*(K-1)],(q,K,T,S,witness,got)
                    count+=1
    print('ALL_COMPLETE_FAMILY_GRIDS',count)
    print('EXAMPLE q=3 K=2 T=3 S=2:',predicted(3,2,3,2))
    print('EXAMPLE expected false positive:',exact_mean_var(3,2,3,2))
    print('VERIFY_OK')

if __name__=='__main__':main()
