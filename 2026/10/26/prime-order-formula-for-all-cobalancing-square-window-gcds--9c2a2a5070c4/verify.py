#!/usr/bin/env python3
"""Independent exact-arithmetic checks for the cobalancing square-window formula."""
from math import gcd, isqrt

def factors(n):
    out = {}
    p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out

def mul(a,b,p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)

def powunit(a,n,p):
    r=(1,0)
    while n:
        if n&1:r=mul(r,a,p)
        a=mul(a,a,p);n//=2
    return r

def order_alpha(p):
    assert p>=3
    # The norm-one group has order p - (2|p).
    legendre = pow(2,(p-1)//2,p)
    bound = p-1 if legendre==1 else p+1
    assert powunit((3,2),bound,p)==(1,0)
    r=bound
    for q in factors(bound):
        while r%q==0 and powunit((3,2),r//q,p)==(1,0):r//=q
    assert powunit((3,2),r,p)==(1,0)
    return r

def predicted(k):
    fs=factors(k)
    v2=fs.get(2,0)
    g=2**max(2,v2+1)
    if k%12==0:g*=3**fs.get(3,0)
    if k%6==0:g*=5**(1+fs.get(5,0))
    for p,e in fs.items():
        if p>=7 and k%order_alpha(p)==0:g*=p**e
    return g

def gcd_first_windows_exact(k,count=10):
    seq=[0,0]
    for j in range(k+count+3):seq.append(6*seq[-1]-seq[-2]+2)
    y=sum(x*x for x in seq[1:k+1])
    z=0
    for n in range(count):
        z=gcd(z,y)
        y+=seq[n+k+1]**2-seq[n+1]**2
    return z

def gcd_windows_modbound(k,count=12):
    mod=40*k
    seq=[0,0]
    for j in range(k+count+3):seq.append((6*seq[-1]-seq[-2]+2)%mod)
    sq=[(x*x)%mod for x in seq]
    y=sum(sq[1:k+1])%mod;z=mod
    for n in range(count):
        z=gcd(z,y)
        y=(y+sq[n+k+1]-sq[n+1])%mod
    return z

def check():
    for p in [3,5,7,11,13,17,19,23,29,31,41,43,101,103,109]:
        r=order_alpha(p)
        assert r>=3
    assert order_alpha(3)==4 and order_alpha(5)==6 and order_alpha(7)==3
    # Test genuine GCD of the first ten windows without an imposed modulus.
    for k in range(1,351):
        actual=gcd_first_windows_exact(k)
        expected=predicted(k)
        assert actual==expected,(k,actual,expected)
    # Extended independent modular window checks, including prime-power factors.
    for k in range(351,2501):
        actual=gcd_windows_modbound(k)
        expected=predicted(k)
        assert actual==expected,(k,actual,expected)
    # Check the two-adic block congruence uniformly across shifts.
    for h in range(8):
        length=4*(2**h)
        mod=2**(h+2)
        t=[0,0]
        for j in range(2*length+60):t.append(6*t[-1]-t[-2]+1)
        for n in range(40):
            assert sum(x*x for x in t[n+1:n+length+1])%mod==2**(h+1)
    # Exact quadratic unit powers that control the exceptional 5-adic lift.
    z=(1,0)
    for _ in range(6):z=(3*z[0]+4*z[1],2*z[0]+3*z[1])
    assert z==(19601,13860)
    assert (z[0]-1)%5==0 and z[1]%5==0
    assert ((z[0]-1)//5)%5==0 and (z[1]//5)%5==2
    print('PASS: 350 exact first-window GCDs; 2150 further modular GCDs;')
    print('PASS: 2-adic block congruences h=0..7, 40 shifts each;')
    print('PASS: exceptional 3/5/7 orders and exact 5-adic lift.')

if __name__=='__main__':check()
