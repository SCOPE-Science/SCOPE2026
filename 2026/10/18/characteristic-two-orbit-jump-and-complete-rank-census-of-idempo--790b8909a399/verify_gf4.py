"""Independent exhaustive GF(4) check for idempotent derivations on the rank-two free class-two Lie algebra.
GF(4)=F_2[u]/(u^2+u+1). Run with Python 3: python verify_gf4.py.
"""
from collections import Counter
from itertools import product

def mul(a,b):
    x=0
    if b&1: x^=a
    if b&2: x^=(a<<1)
    if x&8: x^=0b1100 # reduce u^3+u^2+u (u^2=u+1)
    if x&4: x^=0b111
    return x

def rank(M):
    A=[list(row) for row in M]
    r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][j]), None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=next(a for a in (1,2,3) if mul(a,A[r][j])==1)
        A[r]=[mul(x,inv) for x in A[r]]
        for i in range(len(A)):
            if i!=r:
                c=A[i][j]
                A[i]=[u^mul(c,v) for u,v in zip(A[i],A[r])]
        r+=1
    return r

def mmul(A,B):
    return [[mul(A[i][0],B[0][j]) ^ mul(A[i][1],B[1][j]) ^ mul(A[i][2],B[2][j]) for j in range(3)] for i in range(3)]

observed=Counter()
for a,b,c,d,e,f in product(range(4),repeat=6):
    A=((a,b),(c,d))
    tr=a^d # action on exterior square in char2 is trace
    D=[[a,b,0],[c,d,0],[e,f,tr]]
    if mmul(D,D)==D: observed[rank(D)]+=1
expected={0:1,2:(4+1)*4**2+4**2}
assert observed==expected, (observed,expected)
print('GF4:',dict(sorted(observed.items())))
print('VERIFY_OK_IDEMPOTENT_FREE_CLASS2_GF4')
