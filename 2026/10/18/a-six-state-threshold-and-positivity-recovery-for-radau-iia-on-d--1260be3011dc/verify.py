"""Exact polynomial and rational-matrix checks for Radau IIA on directed cycles.

Run: python3 verify.py
No third-party packages are needed.
"""
from fractions import Fraction as F

# Integer coefficient arrays are written from constant to highest power.
DEN = {
    2: [3, 4, 2],
    3: [12, 24, 22, 12, 3],
    4: None,
    5: [1296, 4320, 6840, 6720, 4520, 2200, 800, 200, 25],
    6: None,
}
NUM = {
 2: [[3, 1, 1], [0, 3, 1]],
 3: [[12, 12, 4, 2, 1], [0, 12, 12, 4, 1], [0, 0, 6, 6, 1]],
 4: [[54, 90, 63, 19, 3, 3, 1],
     [0, 54, 90, 63, 22, 5, 1],
     [0, 0, 27, 45, 27, 7, 1],
     [0, 0, 0, 9, 18, 9, 1]],
 5: [[1296, 3024, 3168, 1824, 536, 20, 0, 20, 5],
     [0, 1296, 3024, 3168, 1896, 680, 150, 30, 5],
     [0, 0, 648, 1512, 1476, 780, 230, 40, 5],
     [0, 0, 0, 216, 576, 540, 240, 50, 5],
     [0, 0, 0, 0, 36, 180, 180, 60, 5]],
 6: [[1296, 3888, 5400, 4440, 2280, 664, 26, -50, -5, 5, 1],
     [0, 1296, 3888, 5400, 4512, 2472, 904, 214, 36, 7, 1],
     [0, 0, 648, 1944, 2592, 2016, 996, 316, 63, 9, 1],
     [0, 0, 0, 216, 720, 960, 696, 300, 76, 11, 1],
     [0, 0, 0, 0, 36, 204, 306, 210, 75, 13, 1],
     [0, 0, 0, 0, 0, -12, 36, 90, 60, 15, 1]],
}

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def add(a, b):
    c = [0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

DEN[4] = mul([2], mul([3,4,2],[9,12,8,4,1]))
DEN[6] = mul(mul([3,4,2],[36,24,10,4,1]),[12,24,22,12,3])

def evaluate(a, h):
    s = F(0)
    for v in reversed(a): s = s*h + v
    return s

def matmul(a, b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def inverse(a):
    n=len(a)
    c=[[a[i][j] for j in range(n)] + [F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        r=next(i for i in range(k,n) if c[i][k])
        c[k],c[r]=c[r],c[k]
        z=c[k][k]
        c[k]=[v/z for v in c[k]]
        for i in range(n):
            if i==k:continue
            z=c[i][k]
            c[i]=[a-z*b for a,b in zip(c[i],c[k])]
    return [r[n:] for r in c]

def independent_kernel(n,h):
    # Shift P has P_{i,i+1}=1; Q=P-I.
    P=[[F(int((i+1)%n==j)) for j in range(n)] for i in range(n)]
    I=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    Q=[[P[i][j]-I[i][j] for j in range(n)] for i in range(n)]
    Q2=matmul(Q,Q)
    A=[[I[i][j]+h*Q[i][j]/3 for j in range(n)] for i in range(n)]
    B=[[I[i][j]-F(2)*h*Q[i][j]/3+h*h*Q2[i][j]/6 for j in range(n)] for i in range(n)]
    return matmul(A,inverse(B))

count=0
for n in range(2,7):
    den=DEN[n]; polys=NUM[n]
    assert len(polys)==n
    # Exact polynomial identity in Z[h,P]/(P^n-1), independently
    # checking every tabulated rational coefficient.
    left=[[0] for _ in range(n)]
    D=[[6,4,1],[0,-4,-2],[0,0,1]]
    for j,p in enumerate(polys):
        for k,q in enumerate(D):
            left[(j+k)%n]=add(left[(j+k)%n],mul(p,q))
    right=[[0] for _ in range(n)]
    right[0]=mul(den,[6,-2])
    right[1]=add(right[1],mul(den,[0,2]))
    for j in range(n):
        assert trim(left[j]) == trim(right[j]), ('polynomial identity',n,j)
        count+=1
    assert den[0]>0
    for h in (F(1,100), F(1,10), F(1,4), F(1,2), F(1), F(3), F(10)):
        M=independent_kernel(n,h)
        vals=[evaluate(p,h)/evaluate(den,h) for p in polys]
        assert all(M[i][j]==vals[(j-i)%n] for i in range(n) for j in range(n))
        assert all(sum(row)==1 for row in M)
        count+=n*n+n
        if n<=5: assert all(v>0 for v in vals)
        if n==6:
            assert (vals[5]<0) == (evaluate([-12,36,90,60,15,1],h)<0)
        count+=n

# Proof-relevant sign and root bounds, checked with exact fractions.
for n in range(2,6):
    assert all(v>=0 for poly in NUM[n] for v in poly)
assert all(v>0 for poly in NUM[6][1:5] for v in poly if v)
F5 = [-12,36,90,60,15,1]
assert NUM[6][5][:5]==[0]*5 and NUM[6][5][5:]==F5
assert evaluate(F5,F(208608,1000000))<0
assert evaluate(F5,F(208610,1000000))>0
assert evaluate(NUM[6][5],F(1,10))/evaluate(DEN[6],F(1,10)) == -F(743849,19268401151106)
# Positive shifted coefficients for the only sign-indefinite remaining numerator.
p0=NUM[6][0]
shift=[sum((p0[j]*__import__('math').comb(j,k) for j in range(k,len(p0))),0) for k in range(len(p0))]
assert all(v>0 for v in shift)
assert p0[5]+p0[7]+p0[8]>0  # positive on 0<h<=1 after power comparison
print(f'VERIFY_OK {count} exact polynomial/matrix assertions; cycles n=2..6')
