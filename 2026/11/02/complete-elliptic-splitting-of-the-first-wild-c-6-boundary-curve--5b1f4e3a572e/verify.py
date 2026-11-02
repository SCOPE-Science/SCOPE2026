"""Finite-field checker for a genus-three Artin--Schreier curve over F2."""
from itertools import product

MOD = {1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def multiply(a,b,n):
    red=MOD[n]; z=0
    while b:
        if b&1:z^=a
        b>>=1; a<<=1
        if a&(1<<n):a^=red
    return z

def power(a,k,n):
    out=1
    while k:
        if k&1:out=multiply(out,a,n)
        a=multiply(a,a,n);k>>=1
    return out

def trace(a,n):
    t=0;b=a
    for i in range(n):t^=b;b=multiply(b,b,n)
    assert t in (0,1)
    return t

def count(n):
    q=1<<n; c=2; e=1; d=2
    for x in range(1,q):
        v=power(x,3,n)^power(power(x,q-2,n),3,n)
        if trace(v,n)==0:c+=2
    for x in range(q):
        t=power(x,3,n)^x
        if trace(t,n)==0:e+=2
        if x:
            u=t^power(x,q-2,n)
            if trace(u,n)==0:d+=2
    return c,e,d

counts=[count(n) for n in range(1,7)]
assert [x[0] for x in counts]==[4,8,4,32,44,56],counts
assert [x[1] for x in counts]==[5,5,5,25,25,65],counts
assert [x[2] for x in counts]==[2,8,8,24,52,56],counts
assert all(c==e+d-(2**n+1) for n,(c,e,d) in enumerate(counts,1))
# The genus-three numerator from the first three counts, Newton identities,
# and the genus-three functional equation is 1+T+2T^2+4T^4+4T^5+8T^6.
a=[1,1,2,0,4,4,8]
for n in range(1,7):
    # sum(alpha_i^n) = -n*a_n - sum_{j=1}^{n-1} a_j*sum(alpha_i^{n-j})
    pass
s=[]
for n in range(1,7):
    sn=-n*a[n]-sum(a[j]*s[n-j-1] for j in range(1,n))
    s.append(sn)
    assert 2**n+1-sn==counts[n-1][0]
# Three pairwise distinct elliptic Frobenius quadratics.
def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out
assert poly_mul(poly_mul([1,2,2],[1,-2,2]),[1,1,2])==a
assert (1+2+2)*(1-2+2)*(1+1+2)==20
print('VERIFY_OK: C/E/D counts n=1..6, functional equation and three elliptic factors')
