"""Exact integer and modular checks for Touchard fixed divisors."""
from math import gcd, comb
def primerange(lo, hi):
    for n in range(lo, hi):
        if n > 1 and all(n % d for d in range(2, int(n**0.5)+1)):
            yield n

def touchard_row(n):
    row=[1]
    for j in range(n):
        new=[0]*(len(row)+1)
        for k,v in enumerate(row):
            new[k+1]+=v
            if k:
                new[k]+=k*v
        row=new
    return row

def val(coeff,x):
    a=0
    for v in reversed(coeff):a=a*x+v
    return a

# Fixed-divisor finite difference theorem: for deg n, gcd of all values
# equals gcd of values at 0,1,...,n. Compute independently via Newton differences.
for p in list(primerange(2,65)):
    c=touchard_row(p)
    values=[val(c,x)-2*x for x in range(p+1)]
    d=0
    for v in values:d=gcd(d,v)
    dif=values[:]
    dd=0
    while dif:
        dd=gcd(dd,dif[0])
        dif=[dif[i+1]-dif[i] for i in range(len(dif)-1)]
    assert d==dd and d%p==0 and (d//p)%p!=0, (p,d)
    if p==5:assert d==10
    if p==29:assert d==174

# Modular dynamic check of prime-to-q periods for every element of F_q.
# B_{n+1}(x)=x(B_n(x)+B_n'(x)), evaluated by direct Stirling row.
for q in (2,3,5):
    limit=q**q-1
    rows=[]; row=[1]
    for n in range(limit+q+2):
        rows.append([val(row,x)%q for x in range(q)])
        new=[0]*(len(row)+1)
        for k,v in enumerate(row):
            new[k+1]+=v
            if k:new[k]+=k*v
        row=[z%q for z in new]
    for n in range(1,q+2):
        assert rows[n]==rows[n+limit],(q,n)
    assert rows[q]==[(2*x)%q for x in range(q)]
    if q in (2,3):
        good=[n for n in range(1,limit+1) if rows[n]==[(2*x)%q for x in range(q)]]
        assert good==[q],(q,good)

# Independent finite-field algebra: the shift polynomial z^q-z-x is
# squarefree and every root in F_{q^q}^*, tested via formal powering.
def mul(a,b,q,x):
    n=q
    c=[0]*(2*n-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]=(c[i+j]+ai*bj)%q
    for k in range(2*n-2,n-1,-1):
        t=c[k]
        if t:
            c[k-n+1]=(c[k-n+1]+t)%q
            c[k-n]=(c[k-n]+t*x)%q
    return c[:n]

def ppow(q,x,n):
    r=[1]+[0]*(q-1)
    z=[0,1]+[0]*(q-2)
    while n:
        if n&1:r=mul(r,z,q,x)
        z=mul(z,z,q,x)
        n//=2
    return r
for q in (2,3,5,7,11):
    for x in range(1,q):
        assert ppow(q,x,q**q-1)==[1]+[0]*(q-1),(q,x)
print('VERIFY_OK finite_difference_primes=18 fixed_divisor_examples={5:10,29:174} modular_periods={2:3,3:26,5:3124} algebra_finite_fields={2,3,5,7,11}')
