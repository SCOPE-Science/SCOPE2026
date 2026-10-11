#!/usr/bin/env python3
from fractions import Fraction

checks=0
for m in range(2,8):
    for n in range(1,8):
        d=m+n
        mu=Fraction(d+1,2)
        r2=Fraction(d*(d-1),4)
        for mask in range(1,(1<<d)-1):
            J=[i+1 for i in range(d) if (mask>>i)&1]
            a=sum(1 for j in J if j<=m)
            c=0
            if d in J:
                q=d
                while q>m and q in J:
                    c+=1
                    q-=1
            tail=sum(1 for j in J if j>m)
            b=tail-c
            u=a+c
            s=len(J)

            z=Fraction(u*(u+1),2)+b
            slack=mu*s-z
            doubled=s*(d-s)+b*(s+u-1)
            assert 2*slack==doubled

            norm2=Fraction(s*(d-s),d)
            dist2=slack*slack/norm2

            closed=Fraction(d,4*s*(d-s))*doubled*doubled
            assert dist2==closed
            assert dist2>=r2

            eq=(dist2==r2)
            predicted=(s==1) or (s==d-1 and b==0)
            assert eq==predicted,(m,n,J,a,b,c,dist2,r2)
            checks+=1

print(f"VERIFY_OK higher-Hochschild-shells subset_checks={checks} exact=yes")
