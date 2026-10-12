"""Exact coefficient and polynomial checks for dyadic overpartition-tuple differences.

Requires only Python 3 standard library. Finite tests corroborate, but do not prove,
the uniform polynomial induction described in RESULT.md.
"""
from math import isqrt

def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def cheb(n,mod):
    t=[[1],[0,1]]
    for k in range(1,n):
        a=[0]*(len(t[k])+1)
        for j,c in enumerate(t[k]): a[j+1]+=2*c
        for j,c in enumerate(t[k-1]): a[j]-=c
        t.append([v%mod for v in a])
    return t

def operator_s(p,T,mod):
    q=[0]*(2*(len(p)-1)+1)
    for j,a in enumerate(p):
        if a:
            for k,b in enumerate(T[2*j]): q[k]=(q[k]+a*b)%mod
    return trim(q)

def quotient_at_one(p,mod):
    assert sum(p)%mod==0
    q=[0]*(len(p)-1)
    carry=0
    for j in range(len(p)-1,0,-1):
        carry=(carry+p[j])%mod
        q[j-1]=carry
    return trim(q)

def val(a):
    if a==0: return 10**4
    return (a&-a).bit_length()-1

def shifted_coefficients(poly,mod):
    from math import comb
    return [sum(poly[j]*comb(j,k) for j in range(k,len(poly)))%mod for k in range(len(poly))]

MOD=1<<48
p_checks=0
for m in range(2,25,2):
    # Iterate over Chebyshev polynomials for both initial parity branches.
    h=m//2
    initial_index=0 if m%4==0 else 1
    old=([0]*(m//4)+[1]) if m%4==0 else cheb(h,MOD)[h]
    T=cheb(2**6*(h+1),MOD)
    for i in range(initial_index+1,7):
        current=operator_s(old,T,MOD)
        L=max(len(current),len(old))
        difference=[((current[j] if j<len(current) else 0)-(old[j] if j<len(old) else 0))%MOD for j in range(L)]
        R=quotient_at_one(difference,MOD)
        if (m%4==0 and i>=2) or (m%4==2 and i>=3):
            s=val(m)
            v_expected=(3*i+2*s-9) if s>=2 else (3*i-8)
            assert min(val(t) for t in R)==v_expected,(m,i,'polynomial valuation')
            z=shifted_coefficients(R,MOD)
            assert val(z[0])==v_expected+1 and val(z[1])==v_expected
            assert (z[0]//(1<<(v_expected+1)))%4 == (z[1]//(1<<v_expected))%4
            assert (z[0]//(1<<(v_expected+1)))%2 ==1
            assert (z[1]//(1<<v_expected))%2 ==1
            p_checks+=1
        old=current

# Reconstruct the closed initial-value and derivative identities directly.
for h in range(1,13):
    t=cheb(2*h,MOD)
    source=t[h]
    target=operator_s(source,t,MOD)
    length=max(len(source),len(target))
    difference=[((target[j] if j<len(target) else 0)-(source[j] if j<len(source) else 0))%MOD for j in range(length)]
    R=quotient_at_one(difference,MOD)
    value=h*h*(4*h*h+5)//3
    derivative=h*h*(h*h+3)*(4*h*h-1)*(4*h*h+101)//630
    assert sum(R)%MOD==value%MOD,(h,'initial value')
    assert sum(j*c for j,c in enumerate(R))%MOD==derivative%MOD,(h,'initial derivative')

# Independent coefficient check, via odd-parts product and repeated squaring.
N=256
mod=1<<36
base=[0]*(N+1);base[0]=1
for odd in range(1,N+1,2):
    b=base[:]
    for n in range(odd,N+1):b[n]=(b[n]+b[n-odd])%mod
    base=[(b[n]+(b[n-odd] if n>=odd else 0))%mod for n in range(N+1)]

def convolution(a,b):
    c=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j in range(N-i+1):c[i+j]=(c[i+j]+x*b[j])%mod
    return c

def power(a,m):
    p=[0]*(N+1);p[0]=1
    while m:
        if m&1:p=convolution(p,a)
        m//=2
        if m:a=convolution(a,a)
    return p

c_checks=0
for m in (2,4,6,8,10,12,16,24):
    coeff=power(base,m)
    s=val(m)
    for i in range(2 if s>=2 else 3,6):
        e=(3*i+2*s-5) if s>=2 else (3*i-4)
        modulus=1<<(e+1)
        for n in range(N//(1<<i)+1):
            actual=(coeff[(1<<i)*n]-coeff[(1<<(i-1))*n])%modulus
            r=isqrt(n)
            expected=(1<<e) if r*r==n and r%2==1 else 0
            assert actual==expected,(m,i,n,actual,expected)
            c_checks+=1
print('VERIFY_OK polynomial_invariant_checks=%d series_coefficient_checks=%d even_parameters=2..24 exact_integer_moduli=yes analytic_induction=separate' % (p_checks,c_checks))
