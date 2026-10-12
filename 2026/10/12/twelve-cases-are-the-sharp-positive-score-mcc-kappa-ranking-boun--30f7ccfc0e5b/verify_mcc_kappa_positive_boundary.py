#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def tables(N,P):
    Q=N-P
    for tp in range(1,P):
        fn=P-tp
        for fp in range(1,Q):
            tn=Q-fp
            yield (tp,fp,fn,tn)


def determinant(t):
    tp,fp,fn,tn=t
    return tp*tn-fp*fn


def kappa(t):
    tp,fp,fn,tn=t
    N=sum(t)
    P=tp+fn; Q=fp+tn
    R=tp+fp; S=fn+tn
    D=determinant(t)
    return Fraction(2*D, P*S+Q*R)


def mcc_num_den(t):
    tp,fp,fn,tn=t
    P=tp+fn; Q=fp+tn
    R=tp+fp; S=fn+tn
    D=determinant(t)
    return D, P*Q*R*S


def cmp_mcc(a,b):
    na,da=mcc_num_den(a)
    nb,db=mcc_num_den(b)
    assert na>0 and nb>0
    left=na*na*db
    right=nb*nb*da
    return (left>right)-(left<right)


def cmp_fraction(a,b):
    return (a>b)-(a<b)

weak={}
strict={}
eligible_matrices={}
pair_counts={}
for N in range(4,13):
    weak[N]=[]; strict[N]=[]
    eligible_matrices[N]=0; pair_counts[N]=0
    for P in range(2,N-1):
        ts=[t for t in tables(N,P) if determinant(t)>0]
        eligible_matrices[N]+=len(ts)
        pair_counts[N]+=len(ts)*(len(ts)-1)//2
        for a,b in combinations(ts,2):
            ck=cmp_fraction(kappa(a),kappa(b))
            cm=cmp_mcc(a,b)
            if ck!=cm:
                weak[N].append((P,a,b,ck,cm))
            if ck*cm<0:
                strict[N].append((P,a,b))

assert all(strict[N]==[] for N in range(4,12))
assert all(weak[N]==[] for N in range(4,10))
assert len(weak[10])==4 and strict[10]==[]
assert weak[11]==[] and strict[11]==[]

first_weak=(3,(1,1,2,6),(2,3,1,4))
assert first_weak[:3] == weak[10][0][:3]
a=first_weak[1]; b=first_weak[2]
assert kappa(a)==Fraction(4,19)
assert kappa(b)==Fraction(1,5)
na,da=mcc_num_den(a); nb,db=mcc_num_den(b)
assert na==4 and da==336 and nb==5 and db==525

expected_strict=[
    (4,(2,3,2,5),(3,5,1,3)),
    (8,(3,1,5,3),(5,2,3,2)),
]
assert strict[12]==expected_strict

A=(2,3,2,5); B=(3,5,1,3)
assert determinant(A)==determinant(B)==4
assert kappa(A)==Fraction(2,17)
assert kappa(B)==Fraction(1,10)
na,da=mcc_num_den(A); nb,db=mcc_num_den(B)
assert (na,da)==(4,1120)
assert (nb,db)==(4,1024)
assert cmp_mcc(A,B)==-1
assert kappa(A)>kappa(B)
# 4/sqrt(1120)=1/sqrt(70) and 4/sqrt(1024)=1/8.
assert 70>64

# The second strict reversal is exactly the global class-label complement
# of the first pair, with pair order exchanged.
def complement(t):
    tp,fp,fn,tn=t
    return (tn,fn,fp,tp)
assert complement(A)==expected_strict[1][2]
assert complement(B)==expected_strict[1][1]

# Structural formulas used in the proof, checked on every eligible matrix.
for N in range(4,13):
    for P in range(2,N-1):
        Q=N-P
        for t in tables(N,P):
            if determinant(t)<=0:
                continue
            tp,fp,fn,tn=t
            R=tp+fp; S=fn+tn; D=determinant(t)
            assert kappa(t)==Fraction(2*D,P*S+Q*R)
            assert mcc_num_den(t)==(D,P*Q*R*S)

print('VERIFY_OK')
print('eligible_matrices', eligible_matrices)
print('pair_counts', pair_counts)
print('pairs_checked_through_11', sum(pair_counts[n] for n in range(4,12)))
print('first_weak_total',10)
print('first_weak_layer_size',len(weak[10]))
print('first_strict_total',12)
print('first_strict_layer',strict[12])
