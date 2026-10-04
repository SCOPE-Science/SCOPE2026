from collections import defaultdict
from math import lcm

def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1

def e(m):
    return m*(v2(m)+2)

def fiber_formula(n):
    ell=v2(n)
    w=n>>ell
    out=[]
    for t in range(ell+1):
        a=ell+2-t
        if v2(a)!=t:
            continue
        b=a>>t
        if w % b:
            continue
        m=(1<<(ell-t))*(w//b)
        out.append((t,m))
    return out

# Exhaustive cross-check on every target n <= 400000.
B=200000
fib=defaultdict(list)
for m in range(1,B+1):
    n=e(m)
    if n<=2*B:
        fib[n].append(m)
for n in range(1,2*B+1):
    brute=sorted(fib.get(n,[]))
    form=sorted(m for _,m in fiber_formula(n))
    if brute!=form:
        raise AssertionError((n,brute,form))

# Explicit branching construction for R=1,2,3.
a=[None,1]
for j in range(1,4):
    a.append(a[j]+(1<<a[j]))
constructed=[]
for R in range(1,4):
    L=a[R+1]
    ell=L-2
    ts=[0]+a[1:R+1]
    bs=[]
    for t in ts:
        x=L-t
        assert v2(x)==t
        bs.append(x>>t)
    w=1
    for b in bs:
        w=lcm(w,b)
    n=(1<<ell)*w
    f=fiber_formula(n)
    chosen={t:m for t,m in f if t in ts}
    if len(chosen)!=R+1:
        raise AssertionError((R,ts,f))
    for t,m in chosen.items():
        assert e(m)==n
    constructed.append((R,ell,ts,bs,len(f),n.bit_length()))

print('VERIFY_OK exhaustive_targets=400000 source_m=200000 constructions='+repr(constructed))
