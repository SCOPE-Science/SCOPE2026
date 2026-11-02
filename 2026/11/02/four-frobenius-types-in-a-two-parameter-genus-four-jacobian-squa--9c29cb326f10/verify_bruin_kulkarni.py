#!/usr/bin/env python3
"""Independent finite-field checks for the Bruin--Kulkarni genus-four family.
Only standard Python, no mathematical packages or external data required.
Checks polynomial separability, rational roots, Frobenius cycle types and their
full parameter frequencies in selected prime fields. Finite tests corroborate,
but do not replace, the separate universal proof.
"""
from math import comb


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def modpoly(a,b,p):
    a=trim(a)
    b=trim(b)
    if b==[0]:
        raise ZeroDivisionError
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        c=a[-1]*inv%p
        d=len(a)-len(b)
        for i in range(len(b)):
            a[i+d]=(a[i+d]-c*b[i])%p
        a=trim(a)
    return a


def gcdpoly(a,b,p):
    a,b=trim(a),trim(b)
    while b != [0]:
        a,b=b,modpoly(a,b,p)
    if a==[0]:
        return [0]
    inv=pow(a[-1],-1,p)
    return trim([(z*inv)%p for z in a])


def mulmod(a,b,f,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    c[i+j]=(c[i+j]+x*y)%p
    return modpoly(c,f,p)


def powmod_x(e,f,p):
    r=[1]
    x=[0,1]
    while e:
        if e & 1:
            r=mulmod(r,x,f,p)
        e >>= 1
        if e:
            x=mulmod(x,x,f,p)
    return r


def chi(a,p):
    a%=p
    if not a:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def branch_polynomial(u,v,p):
    # (X^2+1)[v(X^2+1)^4 + 4u X^2(X^2+1)^2 +16X^4].
    a=[0]*11
    for i,val in enumerate([v,4*u+5*v,12*u+10*v+16,
                            12*u+10*v+16,4*u+5*v,v]):
        a[2*i]=val%p
    return trim(a)


def cycle_type_from_polynomial(f,p):
    assert len(f)==11 and f[-1]!=0
    fp=[(i*z)%p for i,z in enumerate(f)][1:]
    assert gcdpoly(f,fp,p)==[1],('nonseparable',p,f)
    n=[]
    for degree in (1,2,4):
        xqd=powmod_x(p**degree,f,p)
        if len(xqd)<2:
            xqd += [0]*(2-len(xqd))
        xqd[1]=(xqd[1]-1)%p
        n.append(len(gcdpoly(f,xqd,p))-1)
    assert n[-1]==10,('unexpected splitting degree',p,n,f)
    assert (n[1]-n[0])%2==0 and (n[2]-n[1])%4==0
    return (n[0],(n[1]-n[0])//2,(n[2]-n[1])//4)


def expected_cycle_type(u,v,p,square_roots):
    base=(2,0,0) if chi(-1,p)==1 else (0,1,0)
    delta=(u*u-4*v)%p
    if chi(delta,p)==1:
        d=square_roots[delta]
        roots=((-u+d)*pow(2,-1,p)%p,(-u-d)*pow(2,-1,p)%p)
        m=sum(chi(t,p)==1 and chi(1-t,p)==1 for t in roots)
        return (base[0]+4*m,base[1]+2*(2-m),0),('split',m)
    assert chi(delta,p)==-1
    if chi(v,p)==chi(1+u+v,p)==1:
        return (base[0],base[1]+4,0),('irreducible',2)
    return (base[0],base[1],2),('irreducible',4)


def test_prime(p):
    square_roots={x*x%p:x for x in range(p)}
    freq={'S2':0,'S1':0,'S0':0,'S4':0}
    valid=0
    for u in range(p):
        for v in range(p):
            if v==0 or (u*u-4*v)%p==0 or (1+u+v)%p==0:
                continue
            valid+=1
            f=branch_polynomial(u,v,p)
            predicted,extra=expected_cycle_type(u,v,p,square_roots)
            observed=cycle_type_from_polynomial(f,p)
            assert observed==predicted,(p,u,v,extra,observed,predicted)
            # Direct rational-root count is independent of polynomial gcd.
            rational=sum(sum(f[j]*pow(x,j,p) for j in range(11))%p==0
                         for x in range(p))
            assert rational==predicted[0],(p,u,v,rational,predicted)
            if predicted[2]:
                freq['S4']+=1
            elif predicted[0]==(2 if chi(-1,p)==1 else 0)+8:
                freq['S2']+=1
            elif predicted[0]==(2 if chi(-1,p)==1 else 0)+4:
                freq['S1']+=1
            else:
                freq['S0']+=1
    eps=chi(-1,p)
    g=(p-4-eps)//4
    predicted_freq={
       'S2':comb(g,2),
       'S1':g*(p-2-g),
       'S0':comb(p-2-g,2)+(p-1)*(p-3)//8,
       'S4':3*(p*p-1)//8,
    }
    assert freq==predicted_freq,(p,freq,predicted_freq)
    assert valid==p*p-3*p+3==sum(freq.values())
    print('p=%s admissible=%s g=%s frequencies=%s PASS' %
          (p,valid,g,','.join('%s:%d'%(k,freq[k]) for k in ('S2','S1','S0','S4'))))


if __name__=='__main__':
    for p in (3,5,7,11,13,17,19,23):
        test_prime(p)
    print('BRUIN_KULKARNI_GENUS4_WEIERSTRASS_FROBENIUS_PASS')


def invariant_two_torsion_order(cycles):
    """Count fixed classes of even branch subsets modulo complementation."""
    n=sum(cycles)
    assert n==10
    permutation=[]
    offset=0
    for length in cycles:
        permutation.extend(list(range(offset+1,offset+length))+[offset])
        offset+=length
    full=(1<<n)-1
    canonical=lambda m: min(m,m^full)
    reps={canonical(m) for m in range(1<<n) if m.bit_count()%2==0}
    assert len(reps)==2**8
    def apply(m):
        return sum(1<<permutation[j] for j in range(n) if (m>>j)&1)
    return sum(canonical(apply(m))==m for m in reps)


def test_two_torsion():
    types=[
        ((1,)*10,256),
        ((1,)*6+(2,2),64),
        ((1,1)+(2,)*4,16),
        ((1,1,4,4),4),
        ((1,)*8+(2,),128),
        ((1,)*4+(2,)*3,32),
        ((2,)*5,16),
        ((2,4,4),4),
    ]
    for cycles,expected in types:
        actual=invariant_two_torsion_order(cycles)
        assert actual==expected,(cycles,actual,expected)
    print('EIGHT_JACOBIAN_TWO_TORSION_PATTERNS_PASS')


class QuadraticField:
    """GF(p^2)=GF(p)[r]/(r^2-d), with d a quadratic nonsquare."""
    def __init__(self,p):
        self.p=p
        self.q=p*p
        self.d=next(i for i in range(1,p) if chi(i,p)==-1)
    def c(self,n):
        return n%self.p
    def add(self,x,y):
        p=self.p
        return (x%p+y%p)%p+p*((x//p+y//p)%p)
    def neg(self,x):
        p=self.p
        return (-x%p)+p*(-(x//p)%p)
    def sub(self,x,y):
        return self.add(x,self.neg(y))
    def mul(self,x,y):
        p=self.p
        a,b=x%p,x//p
        c,d=y%p,y//p
        return ((a*c+self.d*b*d)%p)+p*((a*d+b*c)%p)
    def power(self,x,n):
        y=1
        while n:
            if n&1:
                y=self.mul(y,x)
            x=self.mul(x,x)
            n//=2
        return y
    def character(self,x):
        if x==0:
            return 0
        return 1 if self.power(x,(self.q-1)//2)==1 else -1


def test_quadratic_field(p):
    F=QuadraticField(p)
    q=F.q
    g=(q-4-F.character(F.neg(1)))//4
    expected_freq=(comb(g,2),g*(q-2-g),
                   comb(q-2-g,2)+(q-1)*(q-3)//8,3*(q*q-1)//8)
    square_roots={F.mul(t,t):t for t in range(q)}
    seen=[0,0,0,0]
    zero=0
    for u in range(q):
        for v in range(q):
            discr=F.sub(F.mul(u,u),F.mul(F.c(4),v))
            border=F.add(F.add(1,u),v)
            if v==0 or discr==0 or border==0:
                continue
            zero+=1
            if F.character(discr)==1:
                d=square_roots[discr]
                inv2=F.c(pow(2,-1,p))
                t1=F.mul(F.sub(d,u),inv2)
                t2=F.mul(F.neg(F.add(u,d)),inv2)
                m=sum(F.character(t)==1 and F.character(F.sub(1,t))==1
                      for t in (t1,t2))
                pos=2-m
            else:
                pos=2 if (F.character(v)==1 and F.character(border)==1) else 3
            seen[pos]+=1
            # Direct root evaluation from the *displayed* degree-10 polynomial.
            fixed=0
            for x in range(q):
                x2=F.mul(x,x)
                x4=F.mul(x2,x2)
                x6=F.mul(x4,x2)
                x8=F.mul(x4,x4)
                Q=F.add(F.mul(v,x8),F.mul(F.mul(F.c(4),F.add(u,v)),x6))
                Q=F.add(Q,F.mul(F.add(F.add(F.mul(F.c(8),u),
                                              F.mul(F.c(6),v)),F.c(16)),x4))
                Q=F.add(Q,F.mul(F.mul(F.c(4),F.add(u,v)),x2))
                Q=F.add(Q,v)
                if F.mul(F.add(x2,1),Q)==0:
                    fixed+=1
            expected_fixed=(2 if F.character(F.neg(1))==1 else 0)+(8 if pos==0 else 4 if pos==1 else 0)
            assert fixed==expected_fixed,(q,u,v,pos,expected_fixed,fixed)
    assert zero==q*q-3*q+3
    assert tuple(seen)==expected_freq,(q,seen,expected_freq)
    print('q=%s prime-power cases=%s g=%s frequencies=%s PASS' % (q,zero,g,seen))


if __name__=='__main__':
    test_two_torsion()
    for p in (3,5):
        test_quadratic_field(p)
    print('BRUIN_KULKARNI_PRIME_POWER_AND_TWO_TORSION_PASS')
