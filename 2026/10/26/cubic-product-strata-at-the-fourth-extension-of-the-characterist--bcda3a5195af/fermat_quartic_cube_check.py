"""Exact finite-field verification for the cubic-product strata of a Fermat quartic.
Run with Python 3, no third-party dependencies.
"""
P = 5


def trim(a):
    a = [int(z) % P for z in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def neg(a):
    return trim([-z for z in a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b)
        z = a[-1] * pow(b[-1], -1, P) % P
        q[k] = z
        a = sub(a, [0]*k + [z*y for y in b])
    return trim(q), a


def mod(a, b):
    return divrem(a, b)[1]


def gcd(a, b):
    while b != [0]:
        a, b = b, mod(a, b)
    return trim([x*pow(a[-1], -1, P) for x in a])


def power(a, n, modulus=None):
    result = [1]
    while n:
        if n & 1:
            result = mul(result, a)
            if modulus is not None:
                result = mod(result, modulus)
        a = mul(a, a)
        if modulus is not None:
            a = mod(a, modulus)
        n //= 2
    return result


X = [0, 1]
A = sub(power(X, 156), [1])
B = sub(power(add(X, [1]), 156), [1])
G = gcd(A, B)
assert len(G)-1 == 41, len(G)-1
assert gcd(G, X) == [1]  # nonzero roots; x and G coprime
# f'(X) need squarefreeness for exact root counts
Gprime = trim([i*G[i] for i in range(1,len(G))])
assert gcd(G, Gprime) == [1]
H = sub(power(mul(X, add(X,[1])), 208, G), [1])
R = gcd(G, H)
assert R == [4,0,4,1,0,1], R  # X^5+X^3-X^2-1
assert gcd(R, trim([i*R[i] for i in range(1,len(R))])) == [1]
assert mod(R, G) != [0]  # R is proper, degree five
assert mod(G,R) == [0]

# Second, independently realize F_625 = F_5[t]/(t^4+t-1).
# Elements are stored in base-5 coefficient encoding.
def coeff(z):
    out = []
    for _ in range(4):
        out.append(z % 5)
        z //= 5
    return out


def enc(a):
    return sum((z % 5)*5**i for i,z in enumerate(a))


def fadd(x,y):
    return enc([(u+v)%5 for u,v in zip(coeff(x),coeff(y))])


def fmul(x,y):
    a,b=coeff(x),coeff(y)
    c=[0]*7
    for i in range(4):
        for j in range(4):
            c[i+j]=(c[i+j]+a[i]*b[j])%5
    for i in range(6,3,-1):
        z=c[i];c[i]=0
        c[i-4]=(c[i-4]+z)%5
        c[i-3]=(c[i-3]-z)%5
    return enc(c[:4])


def fpow(x,n):
    out=1
    while n:
        if n&1:
            out=fmul(out,x)
        x=fmul(x,x)
        n//=2
    return out

# Degree four irreducibility criterion: no roots in F_5 or F_25,
# and t^625=t modulo the defining quartic.
F = [4,1,0,0,1]
assert mod(sub(power(X,625,F),X),F)==[0]
assert gcd(F,sub(power(X,25,F),X))==[1]
assert gcd(F,sub(power(X,5,F),X))==[1]
assert fpow(5,625)==5
fourth=[fpow(x,4) for x in range(625)]
image=set(fourth[1:])
assert len(image)==156
assert all(fourth.count(z)==4 for z in image)
classes={}
for a in image:
    b=fadd(4,fmul(4,a))
    if b in image:
        c=fpow(fmul(a,b),208)
        classes[c]=classes.get(c,0)+1
assert classes=={1:5,249:18,530:18}, classes
assert fpow(249,3)==fpow(530,3)==1
assert fmul(249,530)==1
assert sum(classes.values())==41
assert 16*sum(classes.values())==656
assert 16*classes[1]==80
assert 16*classes[249]==16*classes[530]==288
# One noncube rational point in the affine chart w=1:
u,v=28,227
assert fadd(fadd(fpow(u,4),fpow(v,4)),1)==0
assert fpow(fmul(u,v),208)==530
# Each of three coordinate lines has four transverse rational intersections.
assert len([z for z in range(625) if fourth[z]==4])==4
assert 656+3*4==668
print('VERIFY_OK: gcd degrees 41/5; exact cube classes 80/288/288; 668 points')
