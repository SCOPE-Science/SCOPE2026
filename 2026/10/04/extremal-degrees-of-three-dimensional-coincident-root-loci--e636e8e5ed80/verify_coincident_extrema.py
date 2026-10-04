from collections import Counter
from math import factorial

def parts3(d):
    for a in range(1, d+1):
        for b in range(a, d+1):
            c=d-a-b
            if c<b:
                continue
            if c<1:
                continue
            yield (a,b,c)

def degree(lam):
    p=1
    for x in lam:
        p*=x
    den=1
    for m in Counter(lam).values():
        den*=factorial(m)
    return 6*p//den

def predicted_max(d):
    if d==3: return (1,(1,1,1))
    if d==4: return (6,(1,1,2))
    if d==5: return (12,(1,2,2))
    q,r=divmod(d,3)
    if r==0:
        p=(q-1,q,q+1); v=6*q*(q*q-1)
    elif r==1:
        p=(q-1,q,q+2); v=6*q*(q-1)*(q+2)
    else:
        p=(q-1,q+1,q+2); v=6*(q-1)*(q+1)*(q+2)
    return v,p

def predicted_min(d):
    if d==3: return (1,(1,1,1))
    if d==4: return (6,(1,1,2))
    if d==5: return (9,(1,1,3))
    if d==6: return (8,(2,2,2))
    return (3*(d-2),(1,1,d-2))

checks=0
for d in range(3,501):
    vals=[(degree(p),p) for p in parts3(d)]
    lo=min(v for v,p in vals); hi=max(v for v,p in vals)
    los=[p for v,p in vals if v==lo]
    his=[p for v,p in vals if v==hi]
    pmin=predicted_min(d); pmax=predicted_max(d)
    assert (lo,los)==(pmin[0],[pmin[1]]), (d,lo,los,pmin)
    assert (hi,his)==(pmax[0],[pmax[1]]), (d,hi,his,pmax)
    checks += len(vals)
print('VERIFY_OK d=3..500 partitions=',checks)
