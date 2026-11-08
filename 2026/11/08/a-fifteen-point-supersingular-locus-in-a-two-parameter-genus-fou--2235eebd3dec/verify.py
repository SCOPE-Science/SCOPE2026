#!/usr/bin/env python3
"""Exact characteristic-five certificates for a two-parameter genus-four family.
No dependencies outside Python's standard library. All polynomial arithmetic mod 5.
"""
P = 5

def trim(a):
    a = [v%P for v in a]
    while a and a[-1]==0: a.pop()
    return a

def plus(a,b):
    o=[0]*max(len(a),len(b))
    for i,c in enumerate(a):o[i]+=c
    for i,c in enumerate(b):o[i]+=c
    return trim(o)

def neg(a):return trim([-x for x in a])
def minus(a,b):return plus(a,neg(b))
def scale(a,c):return trim([c*x for x in a])
def mul(a,b):
    if not a or not b:return []
    o=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):o[i+j]+=c*d
    return trim(o)

def power(a,n):
    v=[1]
    while n:
        if n&1:v=mul(v,a)
        a=mul(a,a);n//=2
    return v

def divmodp(a,b):
    a=trim(a);b=trim(b)
    if not b:raise ZeroDivisionError
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b)
        c=a[-1]*pow(b[-1],-1,P)%P
        q[k]=c
        a=minus(a,[0]*k+scale(b,c))
    return trim(q),a

def rem(a,b):return divmodp(a,b)[1]
def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return scale(a,pow(a[-1],-1,P)) if a else []
def xpowmod(e,mod):
    a=[0,1]; b=[1]
    while e:
        if e&1:b=rem(mul(b,a),mod)
        a=rem(mul(a,a),mod);e//=2
    return b

def deriv(a):return trim([i*a[i] for i in range(1,len(a))])
def eq(a,b):return trim(a)==trim(b)

def field_coeff_matrix():
    # Expand f(x)^2 where f=(x^4+u x^2+v)(x+1), coefficients in F5[u,v].
    # Terms are ((exponent in x, power of u, power of v), coefficient).
    f={5:{(0,0):1},4:{(0,0):1},3:{(1,0):1},2:{(1,0):1},1:{(0,1):1},0:{(0,1):1}}
    coeff={}
    for i,di in f.items():
        for j,dj in f.items():
            z=coeff.setdefault(i+j,{})
            for (ui,vi),ci in di.items():
                for (uj,vj),cj in dj.items():
                    k=(ui+uj,vi+vj)
                    z[k]=(z.get(k,0)+ci*cj)%5
    def clean(d):return {k:v for k,v in d.items() if v%5}
    return [[clean(coeff[5*i-j]) for j in (1,2)] for i in (1,2)]

assert field_coeff_matrix() == [
    [{(2,0):1,(1,1):2,(0,1):2},{(1,1):4}],
    [{(0,0):2},{(1,0):2,(0,0):1}]
]

u=[0,1]; one=[1]
L=minus(minus([2],power(u,2)),scale(u,2))
K=plus(scale(power(u,3),2),power(u,2))
# If det M=0 then L*v+K=0. gcd(L,K)=1 guarantees L != 0 there.
assert gcd(L,K)==[1]
A_num=minus(mul(power(u,2),L),mul(plus(u,one),scale(K,2)))
assert eq(A_num,scale(power(u,3),2))
# The other rank-zero condition is A^5+(2u+1)=0.
E=plus(power(A_num,5),mul(plus(scale(u,2),one),power(L,5)))
H=[1,2,0,0,0,4,3,0,0,0,2,4,0,0,0,1]
assert eq(E,scale(H,2))
J=[1,1,4,1,4,0,3,2,3,2,0,4,1,4,1]
assert eq(H,mul(plus(u,one),J))
assert gcd(H,deriv(H))==[1]  # exactly 15 reduced geometric points
assert gcd(H,L)==[1]
# Parameter involution (u,v) -> (U,V)=(-u-2,1+u+v).
# It fixes the determinant equation P(u,v)=K(u)+L(u)*v,
# and negates H(u), hence preserves the supersingular locus.
def compose(f, g):
    out=[]
    for c0 in f[::-1]:out=plus(mul(out,g),[c0])
    return out
U=minus(neg(u),[2])
assert eq(compose(L,U),L)
assert eq(plus(compose(K,U),mul(L,plus(u,one))),K)
assert eq(compose(H,U),neg(H))
# Check all three genus-two smoothness factors after v=-K/L:
S1=K # v != 0
S2=plus(mul(power(u,2),L),scale(K,4)) # u^2-4v != 0
S3=minus(mul(plus(one,u),L),K) # 1+u+v != 0
for z in (S1,S2,S3): assert gcd(H,z)==[1]
# Rabin irreducibility test for J of degree 14, prime factors 2 and 7.
assert eq(xpowmod(5**14,J),u)
for n in (2,7):assert gcd(J,minus(xpowmod(5**(14//n),J),u))==[1]

# Direct prime-field census of all normalized smooth parameters.
counts={0:0,2:0,4:0}; found=[]
for a in range(5):
    for b in range(5):
        if (b*(a*a-4*b)*(1+a+b))%5==0:continue
        A=(a*a+2*a*b+2*b)%5
        D=(2*a+1)%5
        B=4*a*b%5
        if (A*D-2*B)%5!=0:rank=4
        elif (pow(A,5,5)+D)%5!=0:rank=2
        else:rank=0;found.append((a,b))
        counts[rank]+=1
assert counts=={0:1,2:0,4:12},(counts,found)
assert found==[(4,2)]

# Independent point counts over F5 and F25 for the exceptional parameter.
# Model F25=F5[t]/(t^2-2), t^2=2.
def fadd(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
def fmul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
def fpow(a,n):
    b=(1,0)
    while n:
        if n&1:b=fmul(b,a)
        a=fmul(a,a);n//=2
    return b
def cint(n):return(n%5,0)
def fsum(*args):
    r=cint(0)
    for a in args:r=fadd(r,a)
    return r

def count(q):
    elements=[(a,b) for a in range(5) for b in (range(5) if q==25 else (0,))]
    u,v=cint(4),cint(2)
    nc=q+1
    nx=q+1+(1 if fpow(v,(q-1)//2)==cint(1) else -1)
    for x in elements:
        x2=fpow(x,2);x4=fpow(x,4);x6=fpow(x,6);x8=fpow(x,8)
        fc=fmul(fsum(x4,fmul(u,x2),v),fadd(x,cint(1)))
        fx=fmul(fadd(x2,cint(1)),fsum(fmul(v,x8),fmul(cint(4),fmul(fadd(u,v),x6)),fmul(fsum(fmul(cint(8),u),fmul(cint(6),v),cint(16)),x4),fmul(cint(4),fmul(fadd(u,v),x2)),v))
        for label,val in [('C',fc),('X',fx)]:
            ch=0 if val==cint(0) else 1 if fpow(val,(q-1)//2)==cint(1) else -1
            if label=='C':nc+=ch
            else:nx+=ch
    return nc,nx
assert count(5)==(6,6)
assert count(25)==(26,26)
print('VERIFY_SQUARE_JAC_P5_OK', 'geometric_supersingular_parameters=15', 'frobenius_orbits=1+14', 'F5_ordinary=12', 'F5_supersingular=1', 'counts_F5=(6,6)', 'counts_F25=(26,26)')
