#!/usr/bin/env python3
"""Exact coefficient identities and the F_7 normal-form parameter census."""
P = 7

def clean(a):
    return {k: v % P for k, v in a.items() if v % P}

def add(a, b):
    out = a.copy()
    for k, v in b.items():
        out[k] = (out.get(k, 0) + v) % P
    return clean(out)

def neg(a):
    return clean({k: -v for k, v in a.items()})

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            m = (i + k, j + l)
            out[m] = (out.get(m, 0) + v*w) % P
    return clean(out)

def scale(a, c):
    return clean({k: c*v for k, v in a.items()})

zero = {}
one = {(0, 0): 1}
s = {(1, 0): 1}
t = {(0, 1): 1}
g = [one, s, add(t, scale(one, 2)), s, one]

def convolution(f, h, multiply, sum_terms, z):
    out = [z.copy() for _ in range(len(f)+len(h)-1)]
    for i, a in enumerate(f):
        for j, b in enumerate(h):
            out[i+j] = sum_terms(out[i+j], multiply(a,b))
    return out

g3 = convolution(convolution(g, g, mul, add, zero), g, mul, add, zero)

def gamma(index):
    if (index-3)%2 or index<3:
        return zero
    k=(index-3)//2
    return g3[k] if 0<=k<len(g3) else zero

M = [[gamma(7*(i+1)-(j+1)) for j in range(4)] for i in range(4)]
A=scale(s, 3)
C=scale(mul(s, add(add(mul(s,s),mul(t,t)),add(scale(t,6),scale(one,10)))),3)
D=scale(add(add(mul(mul(s,s), t),scale(mul(s,s),4)),add(mul(t,t),add(scale(t,4),scale(one,5)))),3)
want = [[zero,A,zero,one], [C,zero,D,zero], [zero,D,zero,C], [one,zero,A,zero]]
assert M == want, 'symbolic Cartier-Manin identity failed'
H=sub(mul(A,C), D)
H_expected=add(add(add(scale(mul(mul(s,s),mul(s,s)),2),scale(mul(mul(s,s),mul(t,t)),2)),add(scale(mul(mul(s,s),t),2),mul(s,s))),add(add(scale(mul(t,t),4),scale(t,2)),neg(one)))
assert H == H_expected, 'symbolic degeneracy equation failed'
print('SYMBOLIC_IDENTITY_OK',sorted(H.items()))

def conv_num(f,h):
    res=[0]*(len(f)+len(h)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(h):
            res[i+j]=(res[i+j]+a*b)%P
    return res

def mat_num(sv,tv):
    f=[0]*10
    for i,value in ((1,1),(3,sv),(5,tv+2),(7,sv),(9,1)):
        f[i]=value%P
    f3=conv_num(conv_num(f,f),f)
    return [[f3[7*(i+1)-(j+1)] for j in range(4)] for i in range(4)]

def rank(matrix):
    a=[row[:] for row in matrix]
    m=len(a);n=len(a[0]);r=0
    for j in range(n):
        pivot=next((k for k in range(r,m) if a[k][j]%P),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,P)
        a[r]=[(x*inv)%P for x in a[r]]
        for k in range(m):
            if k!=r:
                c=a[k][j]
                a[k]=[(a[k][v]-c*a[r][v])%P for v in range(n)]
        r+=1
        if r==m:break
    return r

def product_mat(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%P for j in range(len(b[0]))] for i in range(len(a))]

def polynomial_value(poly, sv,tv):
    return sum(c*pow(sv,i,P)*pow(tv,j,P) for (i,j),c in poly.items())%P

smooth_pairs=[]
exceptional=[]
for sv in range(P):
    for tv in range(P):
        disc=((sv*sv-4*tv)*((tv+4)**2-4*sv*sv))%P
        if not disc:
            continue
        smooth_pairs.append((sv,tv))
        matrix=mat_num(sv,tv)
        direct_rank=rank(matrix)
        expect_rank=2 if polynomial_value(H,sv,tv)==0 else 4
        assert direct_rank==expect_rank, (sv,tv,direct_rank,expect_rank)
        if direct_rank==2:
            exceptional.append((sv,tv))
            assert product_mat(matrix,matrix)==[[0]*4 for _ in range(4)]
assert len(smooth_pairs)==31, len(smooth_pairs)
assert exceptional==[(2,5),(5,5)],exceptional
print('F7_CENSUS_OK: smooth_pairs=31, rank4=29, rank2=2, rank2_parameters=',exceptional)
print('P_RANK_ZERO_CHECK_OK for both exceptional F7 parameters (matrix square is zero)')
