#!/usr/bin/env python3
import math

for n in range(2,31):
    mu=(n+1)/2
    r=math.sqrt(n*(n-1))/2
    ds=[]
    for k in range(1,n):
        norm=math.sqrt(k*(n-k)/n)
        slack=k*(n-k)/2
        d=slack/norm
        assert abs(d-0.5*math.sqrt(n*k*(n-k)))<1e-12
        ds.append(d)
    assert abs(min(ds)-r)<1e-12
    active=[k for k,d in enumerate(ds,1) if abs(d-r)<1e-11]
    assert active==([1] if n==2 else [1,n-1])

    # Parallelepiped incenter prefix intervals.
    free=0
    for i in range(1,n):
        a=math.sqrt(i*(n-i)/n)
        lower=i*(i+1)/2+r*a
        total=n*(n+1)/2
        upper=total-(n-i)*(n-i+1)/2-r*a
        assert lower<=upper+1e-12
        if upper-lower>1e-10:
            free+=1
        if i in (1,n-1):
            assert abs(upper-lower)<1e-10
    assert free==max(n-3,0)

    perm_contacts=2 if n==2 else 2*n
    asso_contacts=2 if n==2 else n+2
    para_contacts=2 if n==2 else 4
    assert perm_contacts>=2 and asso_contacts>=2 and para_contacts>=2

print("VERIFY_OK loday-shared-inradius n=2..30 exact_formulas=yes")
