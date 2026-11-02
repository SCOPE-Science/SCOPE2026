#!/usr/bin/env python3
"""Independent finite-field checks for harmonic quadratic-irreducibility tuples.
Python 3, standard library only. Run: python3 verify.py
"""

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**.5)+1))

def field(p, extension=False):
    if not extension:
        q=p
        def sub(a,b): return (a-b)%p
        def mul(a,b): return (a*b)%p
        def power(a,n): return pow(a,n,p)
        return q,range(q),sub,mul,power
    assert p==7
    # F_{7^3}=F_7[X]/(X^3+X+1), an irreducible cubic.
    q=343
    def unpack(a): return a%7,(a//7)%7,(a//49)%7
    def pack(a): return (a[0]%7)+7*(a[1]%7)+49*(a[2]%7)
    def sub(a,b): return pack([x-y for x,y in zip(unpack(a),unpack(b))])
    def mul(a,b):
        x=unpack(a); y=unpack(b)
        c=[0]*5
        for i in range(3):
            for j in range(3): c[i+j]+=x[i]*y[j]
        for k in (4,3):
            c[k-3]-=c[k]
            c[k-2]-=c[k]
        return pack(c)
    def power(a,n):
        out=1
        while n:
            if n&1: out=mul(out,a)
            a=mul(a,a); n//=2
        return out
    return q,range(q),sub,mul,power

def inspect_field(p, extension=False):
    q,elts,sub,mul,power=field(p,extension)
    assert q%8==7
    def chi(a):
        if a==0:return 0
        r=power(a,(q-1)//2)
        if r==1:return 1
        assert r==sub(0,1), (q,a,r)
        return -1
    roots=[t for t in elts if sub(sub(mul(t,t),mul(6,t)),sub(0,1))==0]
    # t*t-6*t+1 =0
    assert len(roots)==2,(q,roots)
    for t in roots:
        shifts=[sub(0,t),sub(0,1),1,t]
        assert len(set(shifts))==4
        n=sum(all(chi(sub(z,s))==-1 for s in shifts) for z in elts)
        assert n==(q-7)//16,(q,t,n,(q-7)//16)
        quarter=sum(chi(mul(sub(mul(z,z),1),sub(mul(z,z),mul(t,t)))) for z in elts)
        assert quarter==-1,(q,t,quarter)
        corrections=sum(__import__('math').prod(1-chi(sub(s,r)) for r in shifts if r!=s) for s in shifts)
        assert corrections==(q-7)%16,(q,corrections)
        for z in elts:
            A=sub(mul(sub(1,t),z),sub(0,mul(2,t)))
            B=sub(mul(2,z),sub(1,t))
            P=lambda z:mul(sub(mul(z,z),1),sub(mul(z,z),mul(t,t)))
            left=mul(sub(mul(A,A),mul(B,B)),sub(mul(A,A),mul(mul(t,t),mul(B,B))))
            factor=mul(sub(0,1),power(sub(t,sub(0,1)),4))
            assert left==mul(factor,P(z)),(q,t,z,left,mul(factor,P(z)))
    return q,len(roots),n

def main():
    cases=[]
    for p in range(7,500):
        if p%8==7 and prime(p): cases.append(inspect_field(p))
    cases.append(inspect_field(7,True))
    print('VERIFY_OK field_cases=%s q_values=%s' % (len(cases),[x[0] for x in cases]))

if __name__=='__main__': main()
