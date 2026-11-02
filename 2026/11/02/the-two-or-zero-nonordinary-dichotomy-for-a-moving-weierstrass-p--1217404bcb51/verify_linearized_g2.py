#!/usr/bin/env python3
"""Independent finite-characteristic checks for the genus-two nonordinary divisor theorem.

Requires only Python 3 standard library. The geometric theorem for arbitrary
algebraically closed fields of characteristic three is proved in RESULT.md;
this program checks coefficient identities and all 3^5 monic quintics over F3.
"""
from itertools import product

P = 3

def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)

def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    rem = a[:]
    quotient = [0] * max(1, len(a)-len(b)+1)
    while rem != [0] and len(rem) >= len(b):
        off = len(rem)-len(b)
        coef = rem[-1] * pow(b[-1], -1, P) % P
        quotient[off] = coef
        for i, x in enumerate(b):
            rem[off+i] -= coef*x
        rem = trim(rem)
    return trim(quotient), rem

def gcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, divmod_poly(a, b)[1]
    return trim([x * pow(a[-1], -1, P) for x in a]) if a != [0] else [0]

def deriv(a):
    return trim([i*a[i] for i in range(1,len(a))])

def evalpoly(a, t):
    v = 0
    for c in reversed(a):
        v = (v*t+c) % P
    return v

def determinant(a):
    a = [[v % P for v in row] for row in a]
    n = len(a)
    d = 1
    for j in range(n):
        k = next((i for i in range(j,n) if a[i][j]),None)
        if k is None:
            return 0
        if k != j:
            a[j],a[k] = a[k],a[j]
            d = -d
        pivot = a[j][j]
        d = d*pivot % P
        inv = pow(pivot,-1,P)
        for i in range(j+1,n):
            q=a[i][j]*inv % P
            for l in range(j,n):
                a[i][l] = (a[i][l]-q*a[j][l]) % P
    return d%P

def sylvester_resultant(f,g):
    # Standard Sylvester matrix: deg(g) shifts of f, then deg(f) shifts of g.
    m,n=len(f)-1,len(g)-1
    ff=list(reversed(f)); gg=list(reversed(g))
    mat=[]
    for i in range(n):
        mat.append([0]*i+ff+[0]*(n-1-i))
    for i in range(m):
        mat.append([0]*i+gg+[0]*(m-1-i))
    return determinant(mat)

def hw(f):
    f = trim(f)
    c=lambda j:f[j] if j<len(f) else 0
    return [[c(2),c(1)],[c(5),c(4)]]

def det2(m):
    return (m[0][0]*m[1][1]-m[0][1]*m[1][0])%P

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))%P
             for j in range(2)] for i in range(2)]

def rank2(m):
    if det2(m):
        return 2
    return 1 if any(v%P for row in m for v in row) else 0

def coeffs(a):
    a0,a1,a2,a3,a4=a
    A=(a2*a4-a1)%P
    B=(a0-a2*a3)%P
    C=(a1*a3-a0*a4)%P
    return A,B,C

# Two independent expansions of the determinant and discriminant resultant.
# h=x^3*g + a2*x^2+a1*x+a0, g=x^2+a4*x+a3.
# h mod g = (-A)*x+B, where A=a2*a4-a1, B=a0-a2*a3.
# The exact identities are C=-A*a3-B*a4 and
# Disc(A*T^2+B*T+C)=B^2-A*C=Res(h,g)=A^2*a3+A*B*a4+B^2.
count=0
special={"two":0,"double":0,"infty":0}
for a in product(range(P),repeat=5):
    a0,a1,a2,a3,a4=a
    h=[a0,a1,a2,a3,a4,1]
    g=[a3,a4,1]
    A,B,C=coeffs(a)
    assert (C+A*a3+B*a4)%P == 0
    assert (B*B-A*C)%P == (A*A*a3+A*B*a4+B*B)%P
    assert sylvester_resultant(h,g)==(B*B-A*C)%P
    bezout_left=mul(deriv(h),g)
    bezout_right=mul([a4,2],h)
    assert add(bezout_left,[-v for v in bezout_right])==trim([C,B,A])
    if gcd(h,deriv(h)) != [1]:
        continue
    count+=1
    assert any([A,B,C]), "Separable quintic cannot make the determinant identically zero"
    for t in range(P):
        f=mul(h,[(-t)%P,1])
        H=hw(f)
        expected=[[(a1-t*a2)%P,(a0-t*a1)%P],
                  [(a4-t)%P,(a3-t*a4)%P]]
        assert H==expected
        assert det2(H)==evalpoly([C,B,A],t)
        if evalpoly(h,t):
            assert rank2(H)>=1
            if det2(H)==0:
                assert rank2(H)==1
        if evalpoly(h,t)==0 and det2(H)==0:
            assert evalpoly(g,t)==0
            assert (2*A*t+B)%P==0
        if evalpoly(h,t)==0 and evalpoly(g,t)==0:
            assert det2(H)==0
    Hinf=hw(h)
    assert det2(Hinf)==A
    assert Hinf==[[a2,a1],[1,a4]]
    if A==0:
        assert B!=0, "Infinity nonordinary zero must be simple"
        special['infty']+=1
    disc=(B*B-A*C)%P
    if disc==0:
        assert A!=0
        t0=(B*pow(A,-1,P))%P # -B/(2A) = B/A in characteristic 3
        assert evalpoly(h,t0)==evalpoly(g,t0)==0
        assert gcd([C,B,A],h)!=[1]
        special['double']+=1
    else:
        assert gcd([C,B,A],h)==[1]
        assert gcd([C,B,A],[B,(2*A)%P])==[1]
        special['two']+=1
assert count==162

# Two different p-ranks at the two distinct smooth nonordinary parameters.
a=(0,1,0,1,1)
h=[0,1,0,1,1,1]
A,B,C=coeffs(a)
assert [C,B,A]==[1,0,2]
for t,expected_rank,expected_count in [(1,1,6),(2,0,4)]:
    assert evalpoly(h,t)!=0
    H=hw(mul(h,[(-t)%P,1]))
    assert det2(H)==0 and rank2(H)==1
    assert rank2(mm(H,H))==expected_rank
    n_aff=sum(1 for x in range(P) for y in range(P)
              if (y*y-evalpoly(mul(h,[(-t)%P,1]),x))%P==0)
    assert n_aff+2==expected_count
# Concentration of both formal nonordinary zeros at a singular branch parameter.
h=[0,1,0,0,0,1]
assert gcd(h,deriv(h))==[1]
assert coeffs(h[:5])==(2,0,0)
print('LINEARIZED_GENUS2_CHAR3_RESULTANT_REDUCED_NONORDINARY_DIVISOR_PASS')
print(f'Exhausted {count} separable monic quintics over F3; parameter strata={special}')
print('Explicit genus-two p-rank pair: (t=1,r=1,#F3=6), (t=-1,r=0,#F3=4).')
