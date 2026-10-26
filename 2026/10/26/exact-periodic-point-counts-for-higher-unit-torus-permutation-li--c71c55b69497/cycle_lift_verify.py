#!/usr/bin/env python3
"""Exact small-field checks of fixed-point formula for higher unit-torus lifts.
No third-party packages or external data required.
"""
from math import gcd
from itertools import product

def irreducible_prime_field_poly(coeff, p):
    """Trial-divide a monic polynomial by every monic degree <= half its degree."""
    n=len(coeff)-1
    assert n>0 and coeff[-1]==1
    for d in range(1,n//2+1):
        for prefix in product(range(p),repeat=d):
            factor=list(prefix)+[1]
            rem=list(coeff)
            for shift in range(n-d,-1,-1):
                c=rem[shift+d]
                if c:
                    for j in range(d+1): rem[shift+j]=(rem[shift+j]-c*factor[j])%p
            if all(v==0 for v in rem): return False
    return True

def gf_mul(a,b,poly,degree):
    mask=(1<<degree)-1
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&(1<<degree): a^=poly
        a&=mask
    return out

def gf_pow(a,e,poly,degree):
    ret=1
    while e:
        if e&1: ret=gf_mul(ret,a,poly,degree)
        a=gf_mul(a,a,poly,degree);e>>=1
    return ret

def cycle_counts(f):
    assert set(f)==set(range(len(f)))
    visited=set();counts={}
    for x in range(len(f)):
        if x in visited:continue
        y=x; k=0
        while y not in visited:
            visited.add(y);k+=1;y=f[y]
        assert y==x
        counts[k]=counts.get(k,0)+1
    return counts

def verify_instance(q,n,s,poly,degree,r,coeff):
    size=1<<degree
    assert size==q**(n*s)
    M=(q**n-1)//(q-1)
    N=size-1
    assert gcd(s,M)==1 and gcd(r,N)==1 and r%(q**n-1)==1
    S=N//M
    T=(pow(s,-1,M)*S)%N
    mul=lambda x,y:gf_mul(x,y,poly,degree)
    pw=lambda x,e:gf_pow(x,e,poly,degree)
    Lset=[x for x in range(size) if pw(x,q**n)==x]
    Bset=[x for x in range(size) if pw(x,q)==x]
    assert len(Lset)==q**n and len(Bset)==q
    assert all(c in Lset for c in coeff)
    es=[(q**i-1)//(q-1) for i in range(n)]
    def L(z):
        acc=0
        for i,a in enumerate(coeff): acc^=mul(a,pw(z,q**i))
        return acc
    def F(x):
        if x==0:return 0
        acc=0
        for i,a in enumerate(coeff): acc^=mul(a,pw(x, (r+es[i]*T)%N))
        return acc
    assert set(L(z) for z in Lset)==set(Lset)
    Flist=[F(x) for x in range(size)]
    assert set(Flist)==set(range(size))
    c=cycle_counts(Flist)
    # validate fixed count for every m from 1 through twice largest cycle length.
    for m in range(1,2*max(c)+1):
        true=sum(1 for x in range(size) if next_iter(F,x,m)==x) if m<=8 else sum(j*nc for j,nc in c.items() if m%j==0)
        g=gcd(pow(r,m,S)-1,S)
        admissible=[lam for lam in Bset if lam!=0 and pw(lam,S//g)==1]
        total=0
        for lam in admissible:
            nz=sum(1 for z in Lset if z!=0 and iter_L(L,z,m)==mul(lam,z))
            # test subspace-size condition, counts one less a power of q
            assert (nz+1) in [q**j for j in range(n+1)]
            total+=g*nz
        assert total%(q-1)==0
        predicted=1+total//(q-1)
        assert true==predicted,(q,n,s,r,m,predicted,true)
    # special r=1 cycle replication
    if r==1:
        lc=cycle_counts([L(z) for z in Lset]) if Lset==list(range(q**n)) else None
        # independent cycle count using set coordinates
        remaining=set(Lset); lc={}
        while remaining:
            z=min(remaining); y=z; k=0
            while y in remaining:
                remaining.remove(y);k+=1;y=L(y)
            assert y==z
            lc[k]=lc.get(k,0)+1
        t=N//(q**n-1)
        for j in set(lc)|set(c):
            expected=t*lc.get(j,0)-(t-1 if j==1 else 0)
            assert c.get(j,0)==expected,(j,c.get(j,0),expected)
    print('CASE_OK', {'q':q,'n':n,'s':s,'r':r,'N':N,'M':M,'S':S,'T':T,'coeff':coeff,'cycles':c})

def iter_L(L,x,m):
    for _ in range(m): x=L(x)
    return x

def next_iter(F,x,m):
    for _ in range(m):x=F(x)
    return x

if __name__=='__main__':
    assert irreducible_prime_field_poly([1,1,0,0,0,0,1],2)
    assert irreducible_prime_field_poly([1,1,0,1,1,0,0,0,1],2)
    # Irreducible x^6+x+1; GF(64), q=2, n=3, s=2.
    verify_instance(2,3,2,0x43,6,1,[0,1,0])
    verify_instance(2,3,2,0x43,6,8,[0,1,0])
    # Irreducible x^8+x^4+x^3+x+1; GF(256), q=4, n=2, s=2.
    subfield=[x for x in range(256) if gf_pow(x,16,0x11b,8)==x]
    b=next(x for x in subfield if x not in (0,1) and gf_pow(x,5,0x11b,8)!=1)
    verify_instance(4,2,2,0x11b,8,1,[1,b])
    verify_instance(4,2,2,0x11b,8,16,[1,b])
    print('CERTIFICATE_OK')

# An odd-characteristic independent implementation with base-3 polynomial arithmetic.
def odd_field_check():
    p=3; deg=6; size=p**deg
    # t^6 + t + 2 is irreducible over GF(3).
    poly=(2,1,0,0,0,0,1)
    assert irreducible_prime_field_poly(poly,3)
    digits=[]
    for x in range(size):
        v=[]; t=x
        for _ in range(deg): v.append(t%p);t//=p
        digits.append(v)
    def add(a,b): return sum(((x+y)%p)*p**i for i,(x,y) in enumerate(zip(digits[a],digits[b])))
    def mul(a,b):
        d=[0]*(2*deg-1)
        for i,ai in enumerate(digits[a]):
            for j,bj in enumerate(digits[b]): d[i+j]=(d[i+j]+ai*bj)%p
        for k in range(2*deg-2,deg-1,-1):
            c=d[k]
            if c:
                for j in range(deg):d[k-deg+j]=(d[k-deg+j]-c*poly[j])%p
                d[k]=0
        return sum(d[i]*p**i for i in range(deg))
    def pw(a,e):
        out=1
        while e:
            if e&1: out=mul(out,a)
            a=mul(a,a);e>>=1
        return out
    q=3;n=2;s=3
    M=(q**n-1)//(q-1);N=size-1;S=N//M
    T=(pow(s,-1,M)*S)%N
    Lset=[z for z in range(size) if pw(z,q**n)==z]
    Bset=[z for z in range(size) if pw(z,q)==z]
    assert len(Lset)==9 and len(Bset)==3
    b=next(z for z in Lset if z and pw(z,4)==2)
    def L(z):return add(z,mul(b,pw(z,q)))
    assert set(L(z) for z in Lset)==set(Lset)
    def iterate_L(z,m):
        for _ in range(m):z=L(z)
        return z
    for r in (1,9,17):
        assert r%8==1 and gcd(r,N)==1
        def F(z): return 0 if z==0 else add(pw(z,r),mul(b,pw(z,(r+T)%N)))
        mapping=[F(z) for z in range(size)]
        assert set(mapping)==set(range(size))
        cycles=cycle_counts(mapping)
        for m in range(1,2*max(cycles)+1):
            true=sum(j*c for j,c in cycles.items() if m%j==0)
            g=gcd(pow(r,m,S)-1,S)
            total=0
            for lam in Bset:
                if lam==0 or pw(lam,S//g)!=1:continue
                nz=sum(1 for z in Lset if z and iterate_L(z,m)==mul(lam,z))
                assert nz+1 in (1,3,9)
                total+=g*nz
            assert total%(q-1)==0
            predicted=1+total//(q-1)
            assert true==predicted,(r,m,predicted,true)
        print('ODD_CASE_OK',{'q':q,'n':n,'s':s,'r':r,'T':T,'coeff':[1,b],'cycles':cycles})

if __name__ == '__main__':
    odd_field_check()
    print('ODD_CERTIFICATE_OK')
