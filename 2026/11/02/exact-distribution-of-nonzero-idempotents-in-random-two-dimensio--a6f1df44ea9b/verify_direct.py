#!/usr/bin/env python3
"""Independent exhaustive prime-field idempotent census using vector equations directly."""
from itertools import product
from collections import Counter
from fractions import Fraction
for q in (2,3,5,7):
    hist=Counter()
    for a,b,c,d in product(range(q),repeat=4):
        if (a*d-b*c)%q==0: continue
        N=0
        for x,y in product(range(q),repeat=2):
            if not (x or y):continue
            if (a*x*x+b*y*y-x)%q==0 and (c*x*x+d*y*y-y)%q==0:
                N+=1
        hist[N]+=1
    size=q*(q-1)**2*(q+1)
    assert sum(hist.values())==size
    assert hist[0]==size//3
    assert set(hist)<=set(range(4))
    print('q='+str(q)+' '+str([hist[k] for k in range(4)]))
print('DIRECT_VERIFY_OK')
