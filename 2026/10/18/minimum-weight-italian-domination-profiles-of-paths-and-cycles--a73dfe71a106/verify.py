"""Independent finite checks of minimum Italian domination counts for paths and cycles.
Usage: python3 italian_min_check.py. Python standard library only.
"""
from itertools import product
from collections import defaultdict

def expected(n, cyclic):
    if cyclic:
        assert n >= 3
        return (n + 1) // 2, (6 if n == 3 else 2 if n % 2 == 0 else n)
    assert n >= 1
    return n // 2 + 1, (1 if n % 2 else n // 2 + 2 + (n == 6)) + (n == 3)

def direct(n, cyclic):
    best, count = 2*n+1, 0
    for vals in product(range(3), repeat=n):
        ok=True
        for i,a in enumerate(vals):
            if a: continue
            val=(vals[i-1] if (cyclic or i) else 0)+(vals[(i+1)%n] if (cyclic or i<n-1) else 0)
            if val<2:
                ok=False
                break
        if not ok:continue
        w=sum(vals)
        if w<best:best,count=w,1
        elif w==best:count+=1
    return best,count

def transfer(n, cyclic):
    if n==1 and not cyclic:return (1,1)
    states={}
    for a in range(3):
        for b in range(3):
            if not cyclic and a==0 and b!=2:continue
            states[(a,b,a,b)]=(a+b,1)
    for _ in range(2,n):
        nxt={}
        for (a,b,x,y),(w,ways) in states.items():
            for z in range(3):
                if y==0 and x+z<2:continue
                key=(a,b,y,z)
                val=w+z
                if key not in nxt or val<nxt[key][0]:nxt[key]=val,ways
                elif val==nxt[key][0]:nxt[key]=(val,nxt[key][1]+ways)
        states=nxt
    xys=[]
    for (a,b,x,y),(w,ways) in states.items():
        if cyclic:
            good=(y!=0 or x+a>=2) and (a!=0 or y+b>=2)
        else:
            good=(y!=0 or x==2)
        if good:xys.append((w,ways))
    lowest=min(w for w,k in xys)
    return lowest,sum(k for w,k in xys if w==lowest)

direct_masks=0
for cyclic,start in ((False,1),(True,3)):
    for n in range(start,12):
        exp=expected(n,cyclic)
        a=direct(n,cyclic)
        b=transfer(n,cyclic)
        assert a==exp==b,(n,cyclic,a,b,exp)
        direct_masks+=3**n
    for n in range(start,121):
        got=transfer(n,cyclic)
        exp=expected(n,cyclic)
        assert got==exp,(n,cyclic,got,exp)
print('PASS: direct assignments =', direct_masks)
print('PASS: min weight and exact minimum-function count, paths 1..120, cycles 3..120')
print('PASS: all lengths 1..11 brute-force (cycles 3..11) compared with independent transfer recurrence')
print('Sample: P6 =', expected(6,False),'P12 =',expected(12,False),'C3 =',expected(3,True),'C11 =',expected(11,True))
