#!/usr/bin/env python3
"""Exact Hasse--Witt and rank-drop verification for a genus-five pencil.
All arithmetic uses only Python's standard library and the finite field F_13.
"""
P = 13

def trim(x):
    x = [i % P for i in x]
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x

def add(x, y):
    return trim([(x[i] if i < len(x) else 0) +
                 (y[i] if i < len(y) else 0) for i in range(max(len(x), len(y)))])

def neg(x):
    return trim([-i for i in x])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    r = [0] * (len(x) + len(y) - 1)
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            r[i+j] += u*v
    return trim(r)

def powpoly(x, n):
    r = [1]
    while n:
        if n & 1:
            r = mul(r, x)
        x = mul(x, x)
        n //= 2
    return r

def ev(poly, x, field_add, field_mul, zero, one):
    r = zero
    for c in reversed(poly):
        r = field_add(field_mul(r, x), field_mul(one, (c, 0)))
    return r

a = [0, 1]
Fz = [[-1], sub([1], a), sub(a, [1]), [1]]
F6 = [[1]]
for _ in range(6):
    new = [[0] for _ in range(len(F6) + len(Fz) - 1)]
    for j, q in enumerate(F6):
        for k, r in enumerate(Fz):
            new[j+k] = add(new[j+k], mul(q,r))
    F6 = new
assert len(F6) == 19
assert all(F6[j] == F6[18-j] for j in range(19))
Ppoly = mul(sub(a,[6]), add(add(powpoly(a,2), mul([3],a)),[6]))
Qpoly = mul(add(a,[6]), add(sub(powpoly(a,2),[4]),mul([5],a)))
assert F6[6] == mul(powpoly(add(a,[2]),3),Ppoly)
assert F6[9] == mul(mul([6], powpoly(add(a,[2]),3)), Qpoly)
assert add(F6[3], F6[2]) == mul([-6],powpoly(add(a,[2]),3))
assert sub(F6[3], F6[2]) == mul([-6],Qpoly)
assert F6[2] == mul([2],mul(sub(a,[4]),sub(a,[1])))
assert F6[3] == mul([-6],mul(add(a,[1]),add(add(powpoly(a,2),a),[5])))

# GF(13^2) = GF(13)[t]/(t^2-2). 2 is a nonsquare modulo 13.
assert all((j*j)%13 != 2 for j in range(13))
Z = (0, 0)
ONE = (1, 0)
def plus(x,y): return ((x[0]+y[0])%13,(x[1]+y[1])%13)
def minus(x,y): return ((x[0]-y[0])%13,(x[1]-y[1])%13)
def times(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%13,(x[0]*y[1]+x[1]*y[0])%13)
def inv(x):
    n = (x[0]*x[0]-2*x[1]*x[1])%13
    assert n != 0
    d = pow(n,-1,13)
    return ((x[0]*d)%13,(-x[1]*d)%13)
def evaluate(v,pol):
    ans=Z
    for coeff in reversed(pol):
        ans=plus(times(ans,v),(coeff,0))
    return ans

def matrix_for(v):
    co = [evaluate(v,c) for c in F6]
    M=[]
    for i in range(1,6):
        row=[]
        for j in range(1,6):
            e=13*i-j
            row.append(co[e//4] if e>=0 and e%4==0 and e//4<=18 else Z)
        M.append(row)
    return M

def rank(matrix):
    B=[r[:] for r in matrix]
    m,n=len(B),len(B[0]); h=0
    for j in range(n):
        v=next((r for r in range(h,m) if B[r][j] != Z),None)
        if v is None:continue
        B[h],B[v]=B[v],B[h]
        factor=inv(B[h][j]); B[h]=[times(x,factor) for x in B[h]]
        for r in range(m):
            if r==h:continue
            c=B[r][j]
            B[r]=[minus(x,times(c,y)) for x,y in zip(B[r],B[h])]
        h+=1
        if h==m:break
    return h

special=[]
for u in range(13):
    for v in range(13):
        t=(u,v)
        if t in ((2,0),(11,0)):continue
        p_zero=evaluate(t,Ppoly)==Z
        q_zero=evaluate(t,Qpoly)==Z
        assert not(p_zero and q_zero)
        r=rank(matrix_for(t))
        assert r==(3 if p_zero or q_zero else 5),(t,r,p_zero,q_zero)
        if p_zero or q_zero:special.append((t,'P' if p_zero else 'Q'))
assert len(special)==6,special
assert special==[
    ((4,6),'Q'),((4,7),'Q'),((5,4),'P'),((5,9),'P'),
    ((6,0),'P'),((7,0),'Q')], special
for t in ((6,0),(7,0),(0,0),(5,9),(4,7)):
    M=matrix_for(t)
    assert M[0][0]==M[4][4] and M[0][4]==M[4][0]
    assert M[1][1]==M[3][3]
    assert sum(1 for i in range(5) for j in range(5) if M[i][j]!=Z and not (i==j or (i,j) in ((0,4),(4,0))))==0

# The formal determinant, up to the forbidden point a=-2, is a square:
# det M = 8 (a+2)^12 P(a)^2 Q(a)^2 modulo 13.
c2,c3,c6,c9=F6[2],F6[3],F6[6],F6[9]
determinant=mul(mul(sub(powpoly(c3,2),powpoly(c2,2)),powpoly(c6,2)),c9)
closed=mul([8],mul(powpoly(add(a,[2]),12),mul(powpoly(Ppoly,2),powpoly(Qpoly,2))))
assert determinant==closed
print('VERIFY_OK')
print('exceptional F_169 parameters:',special)
print('Hasse--Witt determinant:',determinant)
