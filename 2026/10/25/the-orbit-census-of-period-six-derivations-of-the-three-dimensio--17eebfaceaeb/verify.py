"""Enumerate finite-prime-field conjugacy data for order-six Heisenberg derivations.

The algorithm enumerates the upper-left 2x2 block A of a derivation D.
Every admissible A admits q^2 free central-row choices, all conjugate.
"""
from collections import Counter
from itertools import product

def mul(A,B,p):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def power(A,n,p):
    R=(1,0,0,1)
    while n:
        if n&1: R=mul(R,A,p)
        A=mul(A,A,p); n//=2
    return R

def verify_prime(p):
    I=(1,0,0,1)
    totals=Counter()
    classes=Counter()
    for A in product(range(p),repeat=4):
        t=(A[0]+A[3])%p
        if t==0: continue
        passes={j:power(A,j,p)==I and pow(t,j,p)==1 for j in (1,2,3,6)}
        for j in passes:
            if passes[j]: totals[j]+=1
        if passes[6] and not passes[3] and not passes[2]:
            det=(A[0]*A[3]-A[1]*A[2])%p
            classes[t,det]+=1
    if p==7:
        expected_n=12*p*(p+1)+3
        expected_classes=15
        sizes=Counter({p*(p+1):12, 1:3})
        assert totals[3]==3 and totals[6]==12*p*(p+1)+6
    elif p%6==1:
        expected_n=6*p*(p+1)
        expected_classes=6
        sizes=Counter({p*(p+1):6})
        assert totals[3]==0 and totals[6]==expected_n
    else:
        expected_n=2*p*(p-1)
        expected_classes=2
        sizes=Counter({p*(p-1):2})
        assert totals[3]==0 and totals[6]==expected_n
    assert totals[1]==totals[2]==0
    assert sum(classes.values())==expected_n
    assert len(classes)==expected_classes, (p,classes)
    observed_sizes=Counter(classes.values())
    assert observed_sizes==sizes, (p,observed_sizes,sizes)
    print('q=%2s classes=%2s derivations=%8s orbit_sizes=%s PASS'%(p,len(classes),p*p*expected_n,dict(observed_sizes)))

if __name__=='__main__':
    for p in (5,7,11,13,19): verify_prime(p)
    print('PERIODIC_DERIVATIONS_OK')
