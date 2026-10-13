#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_POSITIVE_TABLES_NORMALIZED = {4:0,5:1,6:2,7:5,8:9,9:13,10:22}
EXPECTED_REVERSALS_NORMALIZED = {4:0,5:0,6:0,7:0,8:0,9:0,10:1}

def direct_metrics(N,P,x,y):
    # Reference-positive count P, reference-negative Q=N-P.
    # x=TP, P-x=FN, y=TN, Q-y=FP.
    Q=N-P
    po=Fraction(x+y,N)
    pred_pos=x+(Q-y)
    pe=Fraction(P*pred_pos + Q*(N-pred_pos), N*N)
    assert pe < 1
    k=(po-pe)/(1-pe)
    return po,k,pred_pos

def closed_kappa(N,P,x,y):
    Q=N-P
    M=x+(Q-y)
    return Fraction(2*(Q*x + P*y - P*Q), P*(N-M)+Q*M)

def tables(N,P):
    Q=N-P
    out=[]
    for x in range(1,P):
        for y in range(1,Q):
            a,k,m=direct_metrics(N,P,x,y)
            assert k==closed_kappa(N,P,x,y)
            if k>0:
                out.append((x,y,a,k,m))
    return out

# Exhaustive classification, quotienting only the global positive/negative label swap
# by restricting P <= N-P. All four cells are positive and both compared kappas positive.
for N in range(4,11):
    positive=0
    reversals=[]
    for P in range(2,N//2+1):
        cfg=tables(N,P)
        positive += len(cfg)
        for a,b in combinations(cfg,2):
            if (a[2]-b[2])*(a[3]-b[3]) < 0:
                reversals.append((P,a,b))
    assert positive == EXPECTED_POSITIVE_TABLES_NORMALIZED[N], (N,positive)
    assert len(reversals) == EXPECTED_REVERSALS_NORMALIZED[N], (N,reversals)

# Unique first reversal up to positive/negative class exchange.
N=10; P=3
A=(1,5)  # TP=1, FN=2, TN=5, FP=2
B=(2,3)  # TP=2, FN=1, TN=3, FP=4
assert direct_metrics(N,P,*A)[:2] == (Fraction(3,5),Fraction(1,21))
assert direct_metrics(N,P,*B)[:2] == (Fraction(1,2),Fraction(2,27))
assert Fraction(3,5)>Fraction(1,2)
assert Fraction(1,21)<Fraction(2,27)

# Structural family for every N>=10 with P=3.
# A_N: TP=1,FN=2,TN=N-5,FP=2.
# B_N: TP=2,FN=1,TN=N-7,FP=4.
for N in range(10,501):
    P=3
    A=(1,N-5)
    B=(2,N-7)
    aA,kA,_=direct_metrics(N,P,*A)
    aB,kB,_=direct_metrics(N,P,*B)
    assert aA == Fraction(N-4,N)
    assert aB == Fraction(N-5,N)
    assert kA == Fraction(N-9,3*(N-3))
    assert kB == Fraction(4*(N-9),9*(N-4))
    assert aA>aB
    assert kA>0 and kB>0 and kA<kB
    # Direct cross-multiplication of the positive kappa factors.
    assert 4*3*(N-3) > 9*(N-4)

print('VERIFY_OK')
print('positive_kappa_table_counts_normalized', EXPECTED_POSITIVE_TABLES_NORMALIZED)
print('strict_reversal_counts_normalized', EXPECTED_REVERSALS_NORMALIZED)
print('first_reversal_N', 10)
print('witness_A_accuracy_kappa', Fraction(3,5), Fraction(1,21))
print('witness_B_accuracy_kappa', Fraction(1,2), Fraction(2,27))
print('family_checked_N_10_to_500')
