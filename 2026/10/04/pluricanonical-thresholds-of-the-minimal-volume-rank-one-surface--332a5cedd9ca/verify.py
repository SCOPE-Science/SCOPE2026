from fractions import Fraction
from math import gcd, lcm

C73 = [2]*9 + [4,2,2]
C87 = [2]*4 + [10,2]

def det_chain(c):
    if not c:
        return 1
    d0, d1 = 1, c[0]
    for a in c[1:]:
        d0, d1 = d1, a*d1-d0
    return d1

assert det_chain(C73) == 73
assert det_chain(C73[1:]) == 66
assert det_chain(C87) == 87
assert det_chain(C87[1:]) == 70

idx73 = 73 // gcd(73, 1+66)
idx87 = 87 // gcd(87, 1+70)
assert (idx73, idx87) == (73,87)
global_index = lcm(idx73, idx87)
assert global_index == 6351
assert Fraction(global_index,6351) == 1

def matrix(c):
    n=len(c)
    M=[[Fraction(0) for _ in range(n)] for __ in range(n)]
    for i,a in enumerate(c):
        M[i][i] = -a
        if i+1<n:
            M[i][i+1] = M[i+1][i] = 1
    return M

def solve(A,b):
    A=[list(map(Fraction,row))+[Fraction(rhs)] for row,rhs in zip(A,b)]
    n=len(A)
    for col in range(n):
        p=next(i for i in range(col,n) if A[i][col])
        A[col],A[p]=A[p],A[col]
        q=A[col][col]
        A[col]=[x/q for x in A[col]]
        for i in range(n):
            if i != col and A[i][col]:
                q=A[i][col]
                A[i]=[A[i][j]-q*A[col][j] for j in range(n+1)]
    return [A[i][-1] for i in range(n)]

def discrepancy(c):
    return solve(matrix(c), [2-a for a in c])

b73=discrepancy(C73)
b87=discrepancy(C87)
assert b73 == [Fraction(x,73) for x in [6,12,18,24,30,36,42,48,54,60,40,20]]
assert b87 == [Fraction(x,87) for x in [16,32,48,64,80,40]]

def frac(q):
    return q - q.numerator//q.denominator

def delta(c,b,n):
    f=[frac(n*x) for x in b]
    M=matrix(c)
    Kdot=sum(Fraction(a-2)*f[i] for i,a in enumerate(c))
    quad=sum(f[i]*M[i][j]*f[j] for i in range(len(c)) for j in range(len(c)))
    return Fraction(1,2)*(Kdot+quad)

def P(n):
    return (Fraction(1)
            + Fraction(n*(n-1), 2*6351)
            + delta(C73,b73,n)
            + delta(C87,b87,n))

vals={}
for n in range(2,99):
    p=P(n)
    assert p.denominator == 1
    assert p >= 0
    vals[n]=int(p)

assert all(vals[n]==0 for n in range(2,11))
assert vals[11] == 1

ones_expected = [
    11,22,33,37,44,48,49,55,59,60,61,66,70,71,72,73,74,77,
    81,82,83,84,85,86,87,88,92,93,94,95,96,97
]
ones_actual=[n for n in range(2,98) if vals[n]==1]
assert ones_actual == ones_expected
assert all(vals[n] in (0,1) for n in range(2,98))
assert vals[98] == 2

print("C73_det_tail=73,66")
print("C87_det_tail=87,70")
print("local_indices=73,87")
print("global_canonical_index=6351")
print("index_times_volume=1")
print("b73=" + ",".join(str(x) for x in b73))
print("b87=" + ",".join(str(x) for x in b87))
print("first_positive_plurigenus_degree=11")
print("first_degree_with_Pn_at_least_2=98")
print("ones_2_to_97=" + ",".join(map(str,ones_actual)))
print("P98=2")
print("VERIFY_OK")
