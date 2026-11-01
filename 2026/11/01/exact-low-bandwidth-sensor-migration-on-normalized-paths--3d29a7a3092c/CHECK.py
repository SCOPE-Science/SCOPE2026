#!/usr/bin/env python3
"""Independent finite checks for low-pass normalized-path sensor placement.
Uses Python's standard library only. Numerical checks are supplementary;
the all-order statements follow from the proof in RESULT.md.
"""
import math

assertions = 0

def ck(cond, msg):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)

def ratio(n, m, j):
    d = 1 if j == 0 or j == n-1 else 2
    v = float(d**m)
    for k in range(1, m):
        v *= math.cos(math.pi*k*j/(n-1))**2
    return v

def predicted(n, m):
    if m == 2:
        if n == 3: return {0, 2}
        if n == 4: return set(range(4))
        return {1, n-2}
    if m == 3:
        if n <= 6: return {0, n-1}
        return {1, n-2}
    if m == 4:
        if n == 4: return set(range(4))
        if n == 7: return {0, 2, 4, 6}
        if n == 9: return {0, 1, 3, 5, 7, 8}
        if n <= 8: return {0, n-1}
        return {1, n-2}
    raise ValueError(m)

# All sensor positions, all paths through 300 sites and first 2--4 modes.
for n in range(3, 301):
    for m in range(2, min(4, n)+1):
        vals = [ratio(n, m, j) for j in range(n)]
        peak = max(vals)
        winners = {j for j,v in enumerate(vals) if abs(v-peak) < 2e-9*max(1,peak)}
        ck(winners == predicted(n, m), ('classifier', n, m, winners))
        ck(abs(vals[0]-1) < 1e-9, ('endpoint',n,m))
        ck(abs(vals[-1]-1) < 1e-9, ('mirror endpoint',n,m))

# General all-bandwidth sufficient condition, N >= ceil(3 m^{3/2}).
for m in range(2, 19):
    start = math.ceil(3*m**1.5)
    for n in [start, start+1, start+9, start+31]:
        vals = [ratio(n,m,j) for j in range(n)]
        peak = max(vals)
        winners = {j for j,v in enumerate(vals) if abs(v-peak) < 1e-7*max(1,peak)}
        ck(winners == {1,n-2}, ('large-path',n,m,winners,peak))

# Independent construction: symmetric normalized adjacency, and its
# spectral modes, then calculate iterates by matrix multiplication.
def matvec(H, x):
    return [sum(hij*xj for hij,xj in zip(row,x)) for row in H]

def determinant(A):
    n=len(A)
    B=[row[:] for row in A]
    sign=1.0
    for k in range(n):
        r=max(range(k,n),key=lambda i:abs(B[i][k]))
        if abs(B[r][k])<1e-14:return 0.0
        if r!=k: B[k],B[r]=B[r],B[k]; sign=-sign
        pivot=B[k][k]
        sign*=pivot
        for i in range(k+1,n):
            z=B[i][k]/pivot
            for l in range(k+1,n): B[i][l]-=z*B[k][l]
    return sign

for n in range(3, 30):
    deg=[1 if j in (0,n-1) else 2 for j in range(n)]
    H=[[0.0]*n for _ in range(n)]
    for j in range(n-1):
        H[j][j+1]=H[j+1][j]=1/math.sqrt(deg[j]*deg[j+1])
    for m in range(2, min(4,n)+1):
        modes=[]
        for k in range(m):
            norm=math.sqrt(2*(n-1)) if k in (0,n-1) else math.sqrt(n-1)
            v=[math.sqrt(deg[j])*math.cos(math.pi*k*j/(n-1))/norm for j in range(n)]
            ck(abs(sum(x*x for x in v)-1)<2e-12, ('norm',n,m,k))
            y=matvec(H,v)
            ev=math.cos(math.pi*k/(n-1))
            ck(max(abs(y[j]-ev*v[j]) for j in range(n))<2e-12, ('eig',n,k))
            modes.append(v)
        data=[]
        for k in range(m):
            z=modes[k]
            sequence=[]
            for t in range(m):
                sequence.append(z[:]); z=matvec(H,z)
            data.append(sequence)
        # ratio of direct determinants, not from trigonometric formula
        base=abs(determinant([[data[k][t][0] for k in range(m)] for t in range(m)]))
        ck(base>1e-15, ('base nonzero',n,m,base))
        for j in range(n):
            cur=abs(determinant([[data[k][t][j] for k in range(m)] for t in range(m)]))
            actual=(cur/base)**2
            ck(abs(actual-ratio(n,m,j))<4e-8*max(1,ratio(n,m,j)),('direct',n,m,j,actual,ratio(n,m,j)))
        # alternative diffusion: each mode has multiplier exp(-tau(1-lambda))
        rates=[math.exp(-0.23*(1-math.cos(math.pi*k/(n-1)))) for k in range(m)]
        base=abs(determinant([[modes[k][0]*rates[k]**t for k in range(m)] for t in range(m)]))
        ck(base>1e-18, ('diff base',n,m))
        for j in range(n):
            cur=abs(determinant([[modes[k][j]*rates[k]**t for k in range(m)] for t in range(m)]))
            if base>1e-12:
                ck(abs((cur/base)**2-ratio(n,m,j))<1e-6*max(1,ratio(n,m,j)), ('heat',n,m,j))
print('CHECK_OK assertions=%d' % assertions)
