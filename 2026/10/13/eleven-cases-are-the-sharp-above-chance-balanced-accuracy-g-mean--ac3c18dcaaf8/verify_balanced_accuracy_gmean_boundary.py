#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def tables(N,P):
    Q=N-P
    for tp in range(1,P):
        fn=P-tp
        for fp in range(1,Q):
            tn=Q-fp
            B=(Fraction(tp,P)+Fraction(tn,Q))/2
            if B <= Fraction(1,2):
                continue
            G2=Fraction(tp,P)*Fraction(tn,Q)
            yield (tp,fp,fn,tn,B,G2)

def sign(x): return (x>0)-(x<0)

stats={}
weak={}; strict={}
for N in range(4,12):
    tcount=pcnt=wcnt=scnt=0
    weak[N]=[]; strict[N]=[]
    for P in range(2,N-1):
        ts=list(tables(N,P)); tcount+=len(ts)
        for x,y in combinations(ts,2):
            pcnt+=1
            db=sign(x[4]-y[4]); dg=sign(x[5]-y[5])
            if db!=dg:
                wcnt+=1; weak[N].append((P,x[:4],y[:4],x[4],y[4],x[5],y[5]))
            if db*dg<0:
                scnt+=1; strict[N].append((P,x[:4],y[:4],x[4],y[4],x[5],y[5]))
    stats[N]=(tcount,pcnt,wcnt,scnt)

expected={
4:(0,0,0,0),5:(2,0,0,0),6:(3,0,0,0),7:(10,8,0,0),
8:(15,17,2,0),9:(26,48,4,0),10:(38,93,6,0),11:(60,216,16,6)
}
assert stats==expected, stats
assert all(len(strict[N])==0 for N in range(4,11))

# First weak-order split at N=8: one pair and its global class-label complement.
expected_weak8=[
 (3,(1,1,2,4),(2,3,1,2),Fraction(17,30),Fraction(8,15),Fraction(4,15),Fraction(4,15)),
 (5,(2,1,3,2),(4,2,1,1),Fraction(8,15),Fraction(17,30),Fraction(4,15),Fraction(4,15)),
]
assert weak[8]==expected_weak8, weak[8]

expected_strict11=[
 (3,(1,1,2,7),(2,4,1,4),Fraction(29,48),Fraction(7,12),Fraction(7,24),Fraction(1,3)),
 (4,(1,1,3,6),(2,3,2,4),Fraction(31,56),Fraction(15,28),Fraction(3,14),Fraction(2,7)),
 (5,(3,3,2,3),(4,4,1,2),Fraction(11,20),Fraction(17,30),Fraction(3,10),Fraction(4,15)),
 (6,(2,1,4,4),(3,2,3,3),Fraction(17,30),Fraction(11,20),Fraction(4,15),Fraction(3,10)),
 (7,(4,2,3,2),(6,3,1,1),Fraction(15,28),Fraction(31,56),Fraction(2,7),Fraction(3,14)),
 (8,(4,1,4,2),(7,2,1,1),Fraction(7,12),Fraction(29,48),Fraction(1,3),Fraction(7,24)),
]
assert strict[11]==expected_strict11, strict[11]

# Check global class-label complement symmetry.
def comp(t):
    tp,fp,fn,tn=t
    return (tn,fn,fp,tp)
for i in range(3):
    P,a,b,ba,bb,ga,gb=expected_strict11[i]
    P2,a2,b2,ba2,bb2,ga2,gb2=expected_strict11[-1-i]
    assert P2==11-P
    assert comp(a)==b2 and comp(b)==a2
    assert ba==bb2 and bb==ba2 and ga==gb2 and gb==ga2

# Structural identity G^2=B^2-delta^2, with delta half the sensitivity-specificity gap.
for N in range(5,12):
    for P in range(2,N-1):
        Q=N-P
        for tp,fp,fn,tn,B,G2 in tables(N,P):
            s=Fraction(tp,P); c=Fraction(tn,Q)
            delta=abs(s-c)/2
            assert G2 == B*B-delta*delta
            # Positive BA above 1/2 is exactly positive determinant/Youden association.
            assert (tp*tn-fp*fn)>0
            assert Fraction(tp*tn-fp*fn,P*Q) == s+c-1

print('VERIFY_OK')
for N in range(4,12): print('N',N,'eligible_tables_pairs_weak_strict',stats[N])
print('first_weak_total',8)
print('first_strict_total',11)
print('strict_layer',strict[11])
