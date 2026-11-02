#!/usr/bin/env python3
"""Exact integer polynomial certificate for spherical harmonic sampling ranks.
No external packages. Run: python3 verify.py
"""
from math import factorial,gcd
from functools import reduce
from hashlib import sha256

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def scale(a,m):return [m*x for x in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power(a,k):
    t=[1]
    while k:
        if k&1:t=mul(t,a)
        a=mul(a,a);k//=2
    return t

def value(a,z):
    y=0
    for v in a[::-1]:y=y*z+v
    return y

def synthetic(a,z):
    assert value(a,z)==0 and len(a)>=2
    b=[0]*(len(a)-1);b[-1]=a[-1]
    for j in range(len(a)-2,0,-1):b[j-1]=a[j]+z*b[j]
    return b

def remove_known(a):
    for z in (0,3,4):
        while len(a)>1 and value(a,z)==0:a=synthetic(a,z)
    d=reduce(gcd,(abs(v) for v in a));return [x//d for x in a]

def primefactors_small(m):
    out=[];m=abs(m)
    if m==1:return out
    for p in range(2,1001):
        if m%p==0:
            exponent=0
            while m%p==0:m//=p;exponent+=1
            out.append((p,exponent))
        if m==1:break
    assert m==1, 'Unexpected constant factor; certificate requires expansion'
    return out

def divisors(factors):
    ds=[1]
    for p,e in factors:
        base=1;new=[]
        for _ in range(e+1):
            new.extend(d*base for d in ds);base*=p
        ds=new
    return ds

def integer_roots_ge5(a):
    assert a[0]!=0
    # Rational root theorem: every integer root divides the constant term.
    candidates=(d for d in divisors(primefactors_small(a[0])) if d>=5)
    # Exact modular rejection; survivors are evaluated by exact Horner arithmetic.
    moduli=(101,103,107)
    allowed=[{z for z in range(p) if value(a,z)%p==0} for p in moduli]
    return sorted(d for d in candidates
                  if all(d%p in S for p,S in zip(moduli,allowed))
                  and value(a,d)==0)

def polynomial_rows(k):
    falling=[1];rising=[1]
    for j in range(k):
        falling=mul(falling,[-3+2*j,1]);rising=mul(rising,[-3+j,1])
    R=scale(mul(power([-2,1],k),rising),2**k)
    def U(z):
        v=[0]
        for j in range(k//2+1):
            a=[1]
            for h in range(k-j):a=mul(a,[-3+2*h,1])
            c=(-1)**j*factorial(k)*2**j//(factorial(j)*factorial(k-2*j))
            assert c*factorial(j)*factorial(k-2*j)==(-1)**j*factorial(k)*2**j
            t=mul(mul(a,power(z,k-2*j)),power([-2,1],2*j))
            v=add(v,scale(t,c))
        return v
    u=U([-4,1]);v=U([-4])
    e0=add(add(scale(R,2),scale(mul([-2,1],u),4)),mul(mul([-2,1],[-3,1]),v))
    e1=add(add(R,mul([-4,1],u)),scale(mul([-3,1],v),-1))
    e2=add(add(R,scale(u,-2)),v)
    return [e0,e1,e2]

def main():
    expected={3:[[],[8],[]],4:[[8],[],[]],5:[[16],[],[]]}
    table=[];digest=sha256();checked=0
    for k in range(3,21):
        roots=[]
        for j,e in enumerate(polynomial_rows(k)):
            assert any(e)
            e=remove_known(e)
            found=integer_roots_ge5(e)
            roots.append(found)
            digest.update((str(k)+'/'+str(j)+':'+','.join(map(str,e))+'\n').encode())
            checked+=1
        assert roots==expected.get(k,[[],[],[]]),(k,roots)
        table.append((k,roots))
    # Check 7 conic quadratics are squarefree and pairwise coprime, using
    # integer Gaussian coefficients, by direct root-separation algebra:
    # the seven lines in (s,t,u) have normals the coordinate basis and
    # four tetrahedral sign vectors; no normal is isotropic and any
    # pair intersects s²+t²+u²=0 only at the origin.
    lines=[(1,0,0),(0,1,0),(0,0,1),
           (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    for i,v in enumerate(lines):
        assert sum(a*a for a in v) in (1,3)
        for w in lines[:i]:
            c=(v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
            assert sum(a*a for a in c)>0, (v,w)
    print('HYPERSIMPLEX_SAMPLING_CERTIFICATE_OK')
    print('Exact integer-root sectors:',checked)
    print('Exceptional roots:',[(k,r) for k,r in table if any(r)])
    print('Coefficient digest SHA256:',digest.hexdigest())

if __name__=='__main__':main()
