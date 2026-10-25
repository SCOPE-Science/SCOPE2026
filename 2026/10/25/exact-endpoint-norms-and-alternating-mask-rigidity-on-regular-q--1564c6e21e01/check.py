"""Exact rational checks for finite regular-branching martingale-level projections."""
from fractions import Fraction as F
from itertools import product

checks = 0

def verify(ok):
    global checks
    assert ok
    checks += 1

def vector(mask, n):
    return tuple((mask >> k) & 1 for k in range(n))

def norm_by_kernel(q, bits):
    n = len(bits)
    weighted = sum((q-1)*q**k*bits[k] for k in range(n))
    ans = F(weighted, q**n)
    prefix = 0
    for j in range(1,n+1):
        row = prefix - q**(j-1)*bits[j-1]
        ans += F(q-1,q**j)*abs(row)
        prefix += (q-1)*q**(j-1)*bits[j-1]
    return ans

def norm_by_variation(q, bits):
    r = F(0)
    ans = F(0)
    for b in bits:
        nxt = (r+(q-1)*b)/q
        ans += abs(nxt-r)
        r = nxt
    return ans+r

def formula(q,n):
    l=F(1,q);c=1-l
    if n==1:return 2*c
    if n%2:
        m=(n-1)//2
        interaction = l*sum((m+1-j)*l**(2*(j-1)) for j in range(1,m+1))
        return 2*c*(m+1-c*interaction)
    m=n//2
    interaction = l*sum((m-j)*l**(2*(j-1)) for j in range(1,m))
    interaction += sum(l**(2*j) for j in range(m))
    return 2*c*(m+1-c*interaction)

def expected(q,n):
    if n==1:return {(1,)}
    if n==2:return {(1,1)}
    if n%2:
        return {tuple(int(k%2==0) for k in range(n))}
    a=[int(k%2==0) for k in range(n)]
    a[-1]=1
    b=[int(k%2==0) for k in range(n)]
    b[0]=1;b[1]=1
    # b is 11010...01: after initial 11, alternate 0,1
    b=[1,1]+[int(k%2==1) for k in range(2,n)]
    return {tuple(a),tuple(b)}

for q in range(3,8):
    for n in range(1,11):
        data=[]
        for mask in range(1<<n):
            bits=vector(mask,n)
            x=norm_by_variation(q,bits)
            verify(x==norm_by_kernel(q,bits))
            data.append((x,bits))
        opt=max(v for v,b in data)
        winners={b for v,b in data if v==opt}
        verify(opt==formula(q,n))
        verify(winners==expected(q,n))

# Inspect exact projection matrix kernels independently for small depths.
for q in (3,4):
    for n in range(1,5):
        if q**n>256:continue
        points=list(product(range(q),repeat=n))
        for mask in range(1<<n):
            bits=vector(mask,n)
            row=F(0)
            x=points[0]
            for y in points:
                k=next((i for i,(a,b) in enumerate(zip(x,y)) if a!=b),n)
                entry=F(0)
                for j,b in enumerate(bits):
                    if b:
                        entry+=(q**(j+1) if k>=j+1 else 0)-(q**j if k>=j else 0)
                row+=abs(entry)/q**n
            verify(row==norm_by_variation(q,bits))

# Check the dynamic-programming envelope on the two analytically proposed
# branches using exact rational grid values for all small depths.
for q in range(3,8):
    l=F(1,q);c=1-l
    for n in range(2,10):
        for j in range(0,31):
            r=F(j,30)
            vals=[]
            for mask in range(1<<n):
                bits=vector(mask,n)
                state=r;total=F(0)
                for b in bits:
                    nxt=l*state+c*b
                    total+=abs(nxt-state)
                    state=nxt
                vals.append((total+state,bits))
            vmax=max(v for v,b in vals)
            def L(n):
                if n==1:return (1,)
                return (1,)+H(n-1)
            def H(n):
                if n==1:return (1,)
                return (0,)+L(n-1)
            w=L(n) if r <= (l if n%2==0 else c) else H(n)
            verify(next(v for v,b in vals if b==w)==vmax)

print('PASS', checks, 'exact-rational assertions')
