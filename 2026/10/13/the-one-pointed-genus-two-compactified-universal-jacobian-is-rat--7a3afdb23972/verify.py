#!/usr/bin/env python3
P=3
# low-to-high coefficient lists over F_3
def trim(a):
    a=[x%P for x in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%P
    return trim(c)

def sub(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%P
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%P
    return trim(c)

def divmodp(a,b):
    a=trim(a[:]); b=trim(b[:])
    if b==[0]: raise ZeroDivisionError
    q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]*inv%P; q[k]=c
        for j in range(len(b)): a[k+j]=(a[k+j]-c*b[j])%P
        a=trim(a)
    return trim(q),trim(a)

def mod(a,f): return divmodp(a,f)[1]
def gcd(a,b):
    a=trim(a); b=trim(b)
    while b!=[0]: a,b=b,mod(a,b)
    inv=pow(a[-1],-1,P)
    return trim([(x*inv)%P for x in a])
def powmod(a,n,f):
    r=[1]; a=mod(a,f)
    while n:
        if n&1:r=mod(mul(r,a),f)
        a=mod(mul(a,a),f); n//=2
    return r

betti=[1,5,15,20,15,5,1]
assert betti==betti[::-1]
f=[c%3 for c in betti] # 1 + 2 t + 0 t^2 + 2 t^3 + 0 t^4 + 2 t^5 + t^6
assert f==[1,2,0,2,0,2,1]
x=[0,1]
# Rabin criterion degree 6 over F3
g2=gcd(f,sub(powmod(x,3**2,f),x))
g3=gcd(f,sub(powmod(x,3**3,f),x))
frob=sub(powmod(x,3**6,f),x)
assert g2==[1]
assert g3==[1]
assert trim(frob)==[0]
print('betti='+str(betti))
print('mod3_polynomial_low_to_high='+str(f))
print('gcd_q2='+str(g2))
print('gcd_q3='+str(g3))
print('frobenius_degree6_remainder='+str(trim(frob)))
print('IRREDUCIBLE_MOD_3')
print('VERIFY_OK')
