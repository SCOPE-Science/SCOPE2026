#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_TOTAL_TABLES={4:1,5:4,6:10,7:20}
EXPECTED_WITHIN_PREVALENCE_PAIRS={4:0,5:2,6:12,7:42}
EXPECTED_REVERSALS={4:0,5:0,6:0,7:3}


def tables(n,p):
    q=n-p
    out=[]
    for tp in range(1,p):
        fn=p-tp
        for fp in range(1,q):
            tn=q-fp
            f1=Fraction(2*tp, 2*tp+fp+fn)
            num=tp*tn-fp*fn
            den2=(tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)
            out.append((tp,fp,fn,tn,f1,num,den2))
    return out


def mcc_cmp(a,b):
    # Compare num/sqrt(den2) exactly, allowing either sign.
    na,da=a[5],a[6]
    nb,db=b[5],b[6]
    if na<0<=nb: return -1
    if nb<0<=na: return 1
    if na==0 and nb==0: return 0
    if na==0: return -1 if nb>0 else 1
    if nb==0: return 1 if na>0 else -1
    sq=(na*na*db > nb*nb*da) - (na*na*db < nb*nb*da)
    return sq if na>0 else -sq


def is_reversal(a,b):
    cf=(a[4]>b[4])-(a[4]<b[4])
    cm=mcc_cmp(a,b)
    return cf*cm<0

reversal_rows={}
for n in range(4,8):
    total_tables=0
    total_pairs=0
    rev=[]
    for p in range(2,n-1):
        ts=tables(n,p)
        total_tables+=len(ts)
        total_pairs+=len(ts)*(len(ts)-1)//2
        for a,b in combinations(ts,2):
            if is_reversal(a,b):
                rev.append((p,a[:4],b[:4]))
    assert total_tables==EXPECTED_TOTAL_TABLES[n], (n,total_tables)
    assert total_pairs==EXPECTED_WITHIN_PREVALENCE_PAIRS[n], (n,total_pairs)
    assert len(rev)==EXPECTED_REVERSALS[n], (n,rev)
    reversal_rows[n]=rev

assert reversal_rows[7]==[
    (3,(1,1,2,3),(2,3,1,1)),
    (4,(1,1,3,2),(2,2,2,1)),
    (4,(2,1,2,2),(3,2,1,1)),
]

# Positive-MCC witness in the first layer.
A=(2,1,2,2)
B=(3,2,1,1)

def metrics(t):
    tp,fp,fn,tn=t
    f1=Fraction(2*tp,2*tp+fp+fn)
    num=tp*tn-fp*fn
    den2=(tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)
    return f1,num,den2

fa,na,da=metrics(A)
fb,nb,db=metrics(B)
assert fa==Fraction(4,7) and fb==Fraction(2,3)
assert na==2 and da==144 and nb==1 and db==120
assert fa<fb
assert na>0 and nb>0 and na*na*db > nb*nb*da

# Exact polynomial helpers to certify the two infinite-family factorizations.
def add(a,b):
    m=max(len(a),len(b)); c=[0]*m
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def sub(a,b): return add(a,[-x for x in b])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def powp(a,n):
    r=[1]
    for _ in range(n): r=mul(r,a)
    return r

def lin(c0,c1=1): return [c0,c1]

# Odd n=2k+7:
# (na^2 db - nb^2 da)=(k+3)(k+4)(2k+7)(3k^2+11k+4).
nao=[2,4,1]; nbo=[1,4,1]
dao=mul(powp(lin(3),2),powp(lin(4),2))
dbo=mul(mul(lin(5),lin(4)),mul(lin(3),lin(2)))
lhs_odd=sub(mul(powp(nao,2),dbo),mul(powp(nbo,2),dao))
rhs_odd=mul(mul(lin(3),lin(4)),mul([7,2],[4,11,3]))
assert lhs_odd==rhs_odd

# Even n=2k+8:
# difference=4(k+3)(k+4)^2(k+5)(3k+2).
nae=[4,5,1]; nbe=[2,5,1]
dae=mul(powp(lin(4),2),mul(lin(5),lin(3)))
dbe=mul(mul(lin(6),lin(5)),mul(lin(3),lin(2)))
lhs_even=sub(mul(powp(nae,2),dbe),mul(powp(nbe,2),dae))
rhs_even=[4*x for x in mul(mul(lin(3),powp(lin(4),2)),mul(lin(5),[2,3]))]
assert lhs_even==rhs_even

# Replay the persistent same-prevalence family for n=7..500.
for n in range(7,501):
    s=n-7
    a=(s+1)//2
    b=s//2
    A=(2+a,1,2,2+b)
    B=(3+a,2,1,1+b)
    assert sum(A)==sum(B)==n
    assert A[0]+A[2]==B[0]+B[2]
    assert A[1]+A[3]==B[1]+B[3]
    ma=metrics(A); mb=metrics(B)
    assert ma[0] < mb[0]
    assert ma[1] > 0 and mb[1] > 0
    assert ma[1]*ma[1]*mb[2] > mb[1]*mb[1]*ma[2]

print('VERIFY_OK')
print('total_positive_cell_tables',EXPECTED_TOTAL_TABLES)
print('within_prevalence_pair_counts',EXPECTED_WITHIN_PREVALENCE_PAIRS)
print('strict_reversal_counts',EXPECTED_REVERSALS)
print('first_layer',reversal_rows[7])
print('positive_MCC_witness_F1',fa,fb)
print('positive_MCC_witness_MCC2',Fraction(na*na,da),Fraction(nb*nb,db))
print('persistent_family_checked_n_7_to_500')
