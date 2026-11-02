"""Independent genus-two quotient calculation and F_5^6 Frobenius checks.
Run: python3 verify_quotient.py. Standard library only.
"""
from math import gcd
p=5

def trim(v):
    v=list(v)
    while v and v[-1]%p==0:v.pop()
    return [x%p for x in v]

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def neg(a):return trim([-x for x in a])

def sub(a,b):return add(a,neg(b))

def mul(a,b):
    c=[0]*(len(a)+len(b)-1) if a and b else []
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def divrem(a,b):
    a=trim(a);b=trim(b)
    if not b:raise ZeroDivisionError
    quo=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b); coeff=a[-1]*pow(b[-1],-1,p)%p;quo[k]=coeff
        for i,y in enumerate(b):a[i+k]=(a[i+k]-coeff*y)%p
        a=trim(a)
    return trim(quo),a

def mod(a,b):return divrem(a,b)[1]

def power(a,n,f):
    v=[1]
    while n:
        if n&1:v=mod(mul(v,a),f)
        a=mod(mul(a,a),f);n>>=1
    return v

def pgcd(a,b):
    while b:a,b=b,mod(a,b)
    return trim([x*pow(a[-1],-1,p)%p for x in a]) if a else []

# Independent calculation on the hyperelliptic quotient H_l:
# V^2=(r^3+l*r+1)^2-4*r^3.
# Expand with two variables (r, l), mod 5.
def pmul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,h),y in b.items():c[i+k,j+h]=(c.get((i+k,j+h),0)+x*y)%p
    return {k:v for k,v in c.items() if v}

def padd(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=(c.get(k,0)+v)%p
    return {k:v for k,v in c.items() if v}

A={(3,0):1,(1,1):1,(0,0):1}
f=padd(pmul(A,A),{(3,0):1}) # -4r^3 = +r^3 modulo 5.
f2=pmul(f,f)
def h(i,j):return trim([f2.get((5*i-j,k),0) for k in range(7)])
H2=[[h(i,j) for j in (1,2)] for i in (1,2)]
assert H2==[[[0,1,0,0,1],[1,0,0,4]],[[1],[0,0,1]]],H2
D=[4,0,0,2,0,0,1]
det=sub(mul(H2[0][0],H2[1][1]),mul(H2[0][1],H2[1][0]))
assert det==D,(det,D)
# Monic sextic is irreducible: no factors of degree 1,2,3 and divides x^(5^6)-x.
x=[0,1]
assert all(pgcd(D,sub(power(x,5**e,D),x))==[1] for e in (1,2,3))
assert mod(sub(power(x,5**6,D),x),D)==[]
roots=[power(x,5**i,D) for i in range(6)]
assert len(set(map(tuple,roots)))==6
# Check all six Frobenius-conjugate roots: D(root)=0, smooth root !=0 and root^3!=1.
def evalpoly(coeffs,xv):
    s=[]
    for a in reversed(coeffs):s=mod(add(mul(s,xv),[a]),D)
    return s
for root in roots:
    assert evalpoly(D,root)==[]
    assert root and sub(power(root,3,D),[1])
    B=[[power(root,2,D),sub([1],power(root,3,D))],[[1],add(power(root,4,D),root)]]
    assert mod(sub(mul(B[0][0],B[1][1]),mul(B[0][1],B[1][0])),D)==[]
    v=[B[0][0],B[1][0]]
    vp=[power(c,5,D) for c in v]
    image=[mod(add(mul(B[i][0],vp[0]),mul(B[i][1],vp[1])),D) for i in range(2)]
    scale=mod(mul(root,sub(power(root,3,D),[1])),D)
    assert scale
    assert image==[mod(mul(scale,component),D) for component in v]
    # Independent quotient Frobenius: 2x2 semilinear square is nonzero.
    H=[[evalpoly(H2[i][j],root) for j in range(2)] for i in range(2)]
    HP=[[power(H[i][j],5,D) for j in range(2)] for i in range(2)]
    comp=[[mod(add(mul(H[i][0],HP[0][j]),mul(H[i][1],HP[1][j])),D) for j in range(2)] for i in range(2)]
    assert any(comp[i][j] for i in range(2) for j in range(2))
print('QUOTIENT_AND_FIELD_OK; H2=',H2,'; D irreducible; exceptional Frobenius orbit length=6; stable rank=1')
