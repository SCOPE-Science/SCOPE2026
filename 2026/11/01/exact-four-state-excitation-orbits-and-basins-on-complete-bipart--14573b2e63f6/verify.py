#!/usr/bin/env python3
"""Self-contained finite-support certificate and labelled-state crosschecks for four-color GHM on K_(a,b)."""
from itertools import product
from collections import Counter, defaultdict
from math import comb

Q=4
SUPPORTS=range(1,1<<Q)
PERIODIC_SUPPORTS={(1,1):'fixed',(5,10):'alternating',(10,5):'alternating',(15,15):'full'}

def image(mask,opposite):
    out=0
    for c in range(4):
        if mask & (1<<c):
            out|=1<<(((c+1)%4) if c or (opposite&2) else 0)
    return out

def support_next(z):
    a,b=z
    return image(a,b),image(b,a)

def signature(z):
    x=z
    for k in range(7):
        if x in PERIODIC_SUPPORTS:
            return PERIODIC_SUPPORTS[x],k
        x=support_next(x)
    raise AssertionError('support transient >6')

def surj(n,r):
    return sum((-1)**j*comb(r,j)*(r-j)**n for j in range(r+1))

def formulas(a,b):
    A={r:surj(a,r) for r in range(1,5)}
    B={r:surj(b,r) for r in range(1,5)}
    four_basin=(8*A[2]*B[2]+10*(A[2]*B[3]+A[3]*B[2])
                +3*(A[2]*B[4]+A[4]*B[2])+12*A[3]*B[3]
                +4*(A[3]*B[4]+A[4]*B[3])+A[4]*B[4])
    fixed_basin=4**(a+b)-four_basin
    four_periodic=2*A[2]*B[2]+A[4]*B[4]
    assert four_periodic%4==0
    return fixed_basin,four_basin,four_periodic//4

def state_next(x,a):
    left=x[:a];right=x[a:]
    seen_l=1 in left;seen_r=1 in right
    return tuple((v+1)%4 if v else int(seen_r) for v in left)+tuple((v+1)%4 if v else int(seen_l) for v in right)

def direct_class(x,a):
    seen={};y=x
    for k in range(12):
        if y in seen:
            return k-seen[y],seen[y]
        seen[y]=k
        y=state_next(y,a)
    raise AssertionError('late cycle entry')

def verify_support():
    depths=Counter(); sizes=defaultdict(Counter)
    for x in product(SUPPORTS, repeat=2):
        cl,k=signature(x)
        depths[(cl,k)]+=1
        sizes[cl][(x[0].bit_count(),x[1].bit_count())]+=1
    assert sum(depths.values())==225
    assert sizes['alternating']==Counter({(2,2):8,(2,3):10,(3,2):10,(2,4):3,(4,2):3,(3,3):12,(3,4):4,(4,3):4})
    assert sizes['full']==Counter({(4,4):1})
    assert max(k for _,k in depths)==6
    assert signature((11,15))==('alternating',6)
    # Detect *all* support cycles independently (not merely eventual entry into prescribed states).
    for x in product(SUPPORTS,repeat=2):
        y=x;old={};path=[]
        while y not in old:
            old[y]=len(path);path.append(y);y=support_next(y)
        cyc=path[old[y]:]
        assert (len(cyc)==1 and cyc[0] in ((1,1),(15,15))) or set(cyc)=={(5,10),(10,5)}
    return depths,sizes

def direct_test():
    total=0;rows=[]
    for a,b in product(range(1,5),repeat=2):
        cnt=Counter();per=Counter();max_tail=0
        for x in product(range(4),repeat=a+b):
            period,tail=direct_class(x,a)
            assert period in (1,4)
            cl=('fixed' if period==1 else 'four')
            cnt[cl]+=1
            if tail==0:per[cl]+=1
            max_tail=max(max_tail,tail)
            mask=(sum(1<<c for c in set(x[:a])),sum(1<<c for c in set(x[a:])))
            c2,d2=signature(mask)
            assert (('fixed' if c2=='fixed' else 'four'),d2)==(cl,tail),(a,b,x,c2,d2,cl,tail)
            total+=1
        b1,b4,q4=formulas(a,b)
        assert (cnt['fixed'],cnt['four'],per['four'])==(b1,b4,4*q4),(a,b,cnt,per,formulas(a,b))
        assert per['fixed']==1
        rows.append((a,b,b1,b4,q4,max_tail))
    assert total==sum(4**(a+b) for a,b in product(range(1,5),repeat=2))
    return total,rows

if __name__=='__main__':
    depths,sizes=verify_support()
    total,rows=direct_test()
    assert all(formulas(a,b)[0]+formulas(a,b)[1]==4**(a+b) for a,b in product(range(1,8),repeat=2))
    for a,b in product(range(2,8),repeat=2):
        x=formulas(a,b)
        assert x[2]>=1
        max_support_tail=max(signature((i,j))[1] for i in SUPPORTS if i.bit_count()<=a
                             for j in SUPPORTS if j.bit_count()<=b)
        expected=6 if min(a,b)>=3 and max(a,b)>=4 else 5
        assert max_support_tail==expected, (a,b,max_support_tail,expected)
    print('SUPPORT_CERTIFICATE_OK 225 ordered nonempty support pairs; only recurrent supports fixed (1,1), alternating (5,10)<->(10,5), full (15,15); max support-tail=6')
    print('ALTERNATING_BASIN_CLASS_COEFFICIENTS_OK',dict(sorted(sizes['alternating'].items())))
    print('DIRECT_LABELLED_CONFIGURATIONS_OK',total,'across',len(rows),'ordered pairs a,b=1..4')
    print('FORMULA_AND_SHARP_TAIL_CHECKS_OK all 36 ordered pairs a,b=2..7')
    for a,b,fix,four,orbits,t in rows:
        if (a,b) in ((1,1),(2,2),(2,4),(3,3),(3,4),(4,4)):
            print('CASE',f'a={a}',f'b={b}',f'fixed_basin={fix}',f'four_basin={four}',f'four_orbits={orbits}',f'max_tail={t}')
