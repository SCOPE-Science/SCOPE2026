from fractions import Fraction
from itertools import product
from math import floor

def accepted(n, x, e):
    return all((e[j] ^ e[0]) == (x[j-1] ^ x[j]) for j in range(1, n))

def distances(n):
    min_joint = 99
    min_wrong = 99
    pure_x = []
    pure_e = []
    for x in product((0,1), repeat=n):
        for e in product((0,1), repeat=n):
            if not accepted(n, x, e):
                continue
            wx = sum(x); we = sum(e); w = wx + we
            if w:
                min_joint = min(min_joint, w)
            if e[0]:
                min_wrong = min(min_wrong, w)
            if we == 0 and wx:
                pure_x.append(wx)
            if wx == 0 and we:
                pure_e.append(we)
    return min_joint, min_wrong, min(pure_x), min(pure_e)

for n in range(2, 11):
    mj, mw, mx, me = distances(n)
    assert mj == 2
    assert mw == floor(n/2) + 1
    assert mx == n
    assert me == n

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matpow(A,k):
    I=[[Fraction(int(i==j),1) for j in range(len(A))] for i in range(len(A))]
    while k:
        if k & 1:
            I=matmul(I,A)
        A=matmul(A,A)
        k//=2
    return I

def G(n,r,q):
    M=[[1-q,q*r],[(1-q)*r,q]]
    P=matpow(M,n-1)
    left=[1-q,q]
    v=[sum(P[i][j] for j in range(2)) for i in range(2)]
    return sum(left[i]*v[i] for i in range(2))

def direct(n,p,q):
    A0=Fraction(0,1); A1=Fraction(0,1)
    for x in product((0,1), repeat=n):
        px=(q**sum(x))*((1-q)**(n-sum(x)))
        s=[x[j]^x[j+1] for j in range(n-1)]
        for e0 in (0,1):
            e=[e0]+[e0^sj for sj in s]
            pe=(p**sum(e))*((1-p)**(n-sum(e)))
            if e0: A1 += px*pe
            else: A0 += px*pe
    return A0,A1

for n in range(2,8):
    for p,q in [(Fraction(1,10),Fraction(1,20)),(Fraction(1,4),Fraction(1,3))]:
        A0,A1=direct(n,p,q)
        F0=(1-p)**n * G(n,p/(1-p),q)
        F1=p**n * G(n,(1-p)/p,q)
        assert A0 == F0
        assert A1 == F1

# Multi-patch parity identity.
for M in range(1,8):
    for qerr in [Fraction(1,10), Fraction(2,7)]:
        odd=sum(Fraction(__import__('math').comb(M,k),1)*(qerr**k)*((1-qerr)**(M-k)) for k in range(1,M+1,2))
        closed=(1-(1-2*qerr)**M)/2
        assert odd == closed

print("VERIFY_OK")
