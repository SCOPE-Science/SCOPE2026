#!/usr/bin/env python3
"""Exact check for consecutive nonsquare cubic residues in finite fields.

No third-party modules are required. All arithmetic is exact.
"""
import math

LIMIT = 105841
EXPECTED_EXCEPTIONS = (
  7,13,19,25,31,37,43,49,61,67,73,79,97,103,109,121,127,
  157,163,169,229,277,283,343,409,421,457,487,529,577,601,
  625,727,733,1399
)
# Each item (field order, characteristic, degree, lower polynomial coefficients,
# certified primitive element, witness or None); field is F_p[X]/(monic polynomial).
EXTENSIONS = ((25, 5, 2, (3, 0), 7, None), (49, 7, 2, (4, 0), 8, None), (121, 11, 2, (9, 0), 13, None), (169, 13, 2, (11, 0), 15, None), (289, 17, 2, (14, 0), 20, 135), (343, 7, 3, (1, 1, 0), 12, None), (361, 19, 2, (17, 0), 21, 63), (529, 23, 2, (18, 0), 24, None), (625, 5, 4, (2, 0, 0, 0), 6, None), (841, 29, 2, (27, 0), 33, 260), (961, 31, 2, (28, 0), 35, 76), (1369, 37, 2, (35, 0), 39, 535), (1681, 41, 2, (38, 0), 45, 204), (1849, 43, 2, (41, 0), 49, 57), (2197, 13, 3, (1, 4, 0), 15, 5), (2209, 47, 2, (42, 0), 51, 766), (2401, 7, 4, (1, 1, 0, 0), 12, 160), (2809, 53, 2, (51, 0), 55, 370), (3481, 59, 2, (57, 0), 64, 1425), (3721, 61, 2, (59, 0), 63, 319), (4489, 67, 2, (65, 0), 69, 340), (5041, 71, 2, (64, 0), 72, 100), (5329, 73, 2, (68, 0), 77, 83), (6241, 79, 2, (76, 0), 80, 104), (6859, 19, 3, (1, 1, 0), 22, 12), (6889, 83, 2, (81, 0), 85, 206), (7921, 89, 2, (86, 0), 92, 355), (9409, 97, 2, (92, 0), 105, 108), (10201, 101, 2, (99, 0), 103, 302), (10609, 103, 2, (100, 0), 104, 133), (11449, 107, 2, (105, 0), 109, 233), (11881, 109, 2, (107, 0), 113, 772), (12769, 113, 2, (110, 0), 116, 903), (14641, 11, 4, (1, 4, 0, 0), 17, 219), (15625, 5, 6, (2, 1, 0, 0, 0, 0), 5, 154), (16129, 127, 2, (124, 0), 130, 141), (16807, 7, 5, (1, 3, 0, 0, 0), 8, 315), (17161, 131, 2, (129, 0), 133, 413), (18769, 137, 2, (134, 0), 140, 432), (19321, 139, 2, (137, 0), 141, 1392), (22201, 149, 2, (147, 0), 151, 462), (22801, 151, 2, (148, 0), 154, 178), (24649, 157, 2, (155, 0), 163, 470), (26569, 163, 2, (161, 0), 165, 330), (27889, 167, 2, (162, 0), 168, 199), (28561, 13, 4, (1, 1, 0, 0), 17, 33), (29791, 31, 3, (1, 3, 0), 32, 11), (29929, 173, 2, (171, 0), 175, 248), (32041, 179, 2, (177, 0), 182, 373), (32761, 181, 2, (179, 0), 183, 219), (36481, 191, 2, (184, 0), 198, 281), (37249, 193, 2, (188, 0), 200, 229), (38809, 197, 2, (195, 0), 206, 252), (39601, 199, 2, (196, 0), 200, 842), (44521, 211, 2, (209, 0), 213, 1071), (49729, 223, 2, (220, 0), 226, 486), (50653, 37, 3, (1, 5, 0), 38, 13), (51529, 227, 2, (225, 0), 231, 1835), (52441, 229, 2, (227, 0), 232, 556), (54289, 233, 2, (230, 0), 236, 747), (57121, 239, 2, (232, 0), 246, 337), (58081, 241, 2, (234, 0), 248, 758), (63001, 251, 2, (249, 0), 255, 321), (66049, 257, 2, (254, 0), 260, 555), (69169, 263, 2, (258, 0), 272, 365), (72361, 269, 2, (267, 0), 279, 284), (73441, 271, 2, (268, 0), 272, 1150), (76729, 277, 2, (275, 0), 281, 1166), (78961, 281, 2, (278, 0), 285, 2090), (79507, 43, 3, (1, 9, 0), 50, 18), (80089, 283, 2, (281, 0), 287, 301), (83521, 17, 4, (1, 3, 0, 0), 19, 694), (85849, 293, 2, (291, 0), 296, 898), (94249, 307, 2, (305, 0), 311, 368), (96721, 311, 2, (300, 0), 312, 353), (97969, 313, 2, (308, 0), 318, 758), (100489, 317, 2, (315, 0), 319, 1076))

def require(condition, msg):
    if not condition:
        raise ArithmeticError(msg)

def primes_below(n):
    sieve = bytearray(b'\x01')*n
    sieve[:2] = b'\x00\x00'
    for k in range(2,math.isqrt(n-1)+1):
        if sieve[k]:
            sieve[k*k:n:k]=b'\x00'*len(sieve[k*k:n:k])
    return [k for k in range(n) if sieve[k]]

def prime_factors(n):
    v=n;out=[];i=2
    while i*i<=v:
        if v%i==0:
            out.append(i)
            while v%i==0:v//=i
        i+=1
    if v>1:out.append(v)
    return out

def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a

def rem(a,b,p):
    a=trim([int(z)%p for z in a]); b=trim([int(z)%p for z in b])
    require(bool(b),'division by zero polynomial')
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        z=a[-1]*inv%p
        shift=len(a)-len(b)
        for i in range(len(b)):
            a[shift+i]=(a[shift+i]-z*b[i])%p
        a=trim(a)
    return a

def gcd(a,b,p):
    while b:a,b=b,rem(a,b,p)
    return trim(a)

def pmul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return trim(out)

def ppow(a,e,mod,p):
    z=[1]
    while e:
        if e&1:z=rem(pmul(z,a,p),mod,p)
        a=rem(pmul(a,a,p),mod,p)
        e>>=1
    return z

def irreducible(p,m,lower):
    f=list(lower)+[1]
    x=[0,1]
    require(len(lower)==m,'bad polynomial degree')
    require(lower[0]%p !=0,'zero constant coefficient')
    for r in prime_factors(m):
        y=ppow(x,p**(m//r),f,p)
        z=trim([( (y[i] if i<len(y) else 0) -(x[i] if i<len(x) else 0))%p for i in range(max(len(y),2))])
        if len(gcd(f,z,p))>1:return False
    return ppow(x,p**m,f,p)==x

class Field:
    def __init__(self,p,m,lower):
        self.p=p;self.m=m;self.lower=tuple(lower);self.q=p**m
    def mul(self,a,b):
        p=self.p;m=self.m
        if m==2 and self.lower[1]==0:
            a0,a1=divmod(a,p)[1],a//p
            b0,b1=divmod(b,p)[1],b//p
            d=(-self.lower[0])%p
            return ((a0*b0+d*a1*b1)%p)+p*((a0*b1+a1*b0)%p)
        aa=[];bb=[]
        for _ in range(m):
            aa.append(a%p);bb.append(b%p);a//=p;b//=p
        t=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):t[i+j]+=aa[i]*bb[j]
        for k in range(2*m-2,m-1,-1):
            z=t[k]%p
            for j in range(m):t[k-m+j]-=z*self.lower[j]
        return sum((t[i]%p)*p**i for i in range(m))
    def power(self,a,e):
        out=1
        while e:
            if e&1:out=self.mul(out,a)
            a=self.mul(a,a);e>>=1
        return out
    def shift(self,a,k):
        return a+(k%self.p) if a%self.p+k<self.p else a+k-self.p
    def good(self,a):
        return a!=0 and self.power(a,(self.q-1)//6)==self.p-1
    def triple(self,a):
        return self.good(a) and self.good(self.shift(a,1)) and self.good(self.shift(a,2))

def verify():
    primes=primes_below(LIMIT)
    observed=[];nprime=0
    for p in primes:
        if p%6!=1:continue
        nprime+=1
        exp=(p-1)//6
        witness=None
        for a in range(1,p-2):
            if pow(a,exp,p)==p-1 and pow(a+1,exp,p)==p-1 and pow(a+2,exp,p)==p-1:
                witness=a;break
        if witness is None:observed.append(p)
        else:
            require(all(pow(witness+k,exp,p)==p-1 for k in (0,1,2)),f'prime witness failed: {p}')
    expect_powers=[]
    for p in primes:
        if p*p>=LIMIT:break
        q=p*p;m=2
        while q<LIMIT:
            if q%6==1:expect_powers.append((q,p,m))
            q*=p;m+=1
    expect_powers.sort()
    require([x[:3] for x in EXTENSIONS]==expect_powers,'missing prime-power case')
    for q,p,m,coeff,g,x in EXTENSIONS:
        require(irreducible(p,m,coeff),f'polynomial reducible: {q}')
        f=Field(p,m,coeff)
        require(all(f.power(g,(q-1)//r)!=1 for r in prime_factors(q-1)),f'not primitive: {q}')
        require(f.power(g,q-1)==1,f'wrong primitive order: {q}')
        if x is None:
            observed.append(q)
            # Direct Euler criterion for every element; independent of
            # the primitive-root coset enumeration used to find the table.
            require(not any(f.triple(a) for a in range(q)),f'exception false: {q}')
        else:
            require(f.triple(x),f'extension witness failed: {q}')
    observed=tuple(sorted(observed))
    require(observed==EXPECTED_EXCEPTIONS,f'wrong exception set {observed}')
    require(nprime==5009+28,f'wrong prime case count: {nprime}')
    print(f'VERIFY_OK primes={nprime} extensions={len(EXTENSIONS)} exceptions={len(observed)} limit={LIMIT}')

if __name__=='__main__':verify()
