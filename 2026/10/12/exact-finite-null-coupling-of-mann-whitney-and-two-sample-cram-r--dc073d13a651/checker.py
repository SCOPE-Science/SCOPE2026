from fractions import Fraction
from itertools import combinations
from math import comb

def one_pair(m,n):
    N=m+n
    total=comb(N,m)
    sum_q2=Fraction(0)
    sum_s=Fraction(0)
    sum_q2s=Fraction(0)
    sum_t=Fraction(0)
    bridge_checks=0
    norm_checks=0
    for pos in combinations(range(1,N+1),m):
        Aset=set(pos)
        R=sum(pos)
        Q=Fraction(2*R-m*(N+1),2)
        a=0
        S=0
        area=0
        for j in range(1,N):
            if j in Aset:
                a+=1
            B=N*a-m*j
            area+=B
            S+=B*B
        assert area == -N*Q
        bridge_checks += 1
        T=Fraction(S,m*n*N*N)
        assert T == Fraction(S,m*n*N*N)
        norm_checks += 1
        sum_q2 += Q*Q
        sum_s += S
        sum_q2s += Q*Q*S
        sum_t += T
    Eq2=sum_q2/total
    ES=sum_s/total
    Eq2S=sum_q2s/total
    ET=sum_t/total
    s=m*n
    target_q2=Fraction(s*(N+1),12)
    target_S=Fraction(s*N*(N+1),6)
    target_mix=Fraction(N*(N+1)*s*((11*N+13)*s-2*N*(2*N+1)),360)
    target_raw=Fraction(N*(N+1)*s*((3*N+4)*s-N*(2*N+1)),180)
    cov_raw=Eq2S-Eq2*ES
    target_cov_z2_t=Fraction((3*N+4)*s-N*(2*N+1),15*s*N)
    cov_z2_t=(Eq2S/Fraction(s*N*N) - Eq2*ET) / target_q2
    assert Eq2 == target_q2
    assert ES == target_S
    assert Eq2S == target_mix
    assert cov_raw == target_raw
    assert ET == Fraction(N+1,6*N)
    assert cov_z2_t == target_cov_z2_t
    if N==2:
        assert target_cov_z2_t == 0
    else:
        assert target_cov_z2_t > 0
    return 6, bridge_checks, norm_checks, total

def check(max_N=14):
    formula_checks=0
    bridge_checks=0
    norm_checks=0
    words=0
    pairs=0
    for N in range(2,max_N+1):
        for m in range(1,N):
            n=N-m
            f,b,z,w=one_pair(m,n)
            formula_checks += f
            bridge_checks += b
            norm_checks += z
            words += w
            pairs += 1
    print('VERIFY_OK')
    print(f'max_N={max_N}')
    print(f'pairs_checked={pairs}')
    print(f'words_enumerated={words}')
    print(f'formula_checks={formula_checks}')
    print(f'bridge_identity_checks={bridge_checks}')
    print(f'normalization_checks={norm_checks}')

if __name__=='__main__':
    check()
