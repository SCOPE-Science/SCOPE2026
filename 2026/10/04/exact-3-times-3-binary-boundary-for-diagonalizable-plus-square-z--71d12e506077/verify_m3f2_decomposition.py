#!/usr/bin/env python3
# Exact stdlib verifier for the 3x3 F2 diagonalizable-plus-square-zero classification.
N = 3
TOTAL = 1 << (N*N)
I = sum(1 << (i*N+i) for i in range(N))

def mm(A,B):
    C=0
    for i in range(N):
        for j in range(N):
            s=0
            for k in range(N):
                s ^= ((A>>(i*N+k))&1) & ((B>>(k*N+j))&1)
            C |= s << (i*N+j)
    return C

def inv(A):
    rows=[]
    for i in range(N):
        left=sum(((A>>(i*N+j))&1)<<j for j in range(N))
        rows.append(left | (1 << (N+i)))
    r=0
    for c in range(N):
        p=next((i for i in range(r,N) if (rows[i]>>c)&1),None)
        if p is None:
            return None
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(N):
            if i != r and ((rows[i]>>c)&1):
                rows[i] ^= rows[r]
        r += 1
    B=0
    for i,row in enumerate(rows):
        for j in range(N):
            B |= ((row>>(N+j))&1) << (i*N+j)
    return B

def enc(M):
    return sum((M[i][j]&1) << (i*N+j) for i in range(N) for j in range(N))

def conj(P,A,Pinv):
    return mm(mm(P,A),Pinv)

idempotents=[A for A in range(TOTAL) if mm(A,A)==A]
sqzero=[A for A in range(TOTAL) if mm(A,A)==0]
decomposable={D^Z for D in idempotents for Z in sqzero}
assert len(idempotents)==58
assert len(sqzero)==22
assert len(decomposable)==380

GL=[A for A in range(TOTAL) if inv(A) is not None]
assert len(GL)==168
GLinv={P:inv(P) for P in GL}
J3=enc([[0,1,0],[0,0,1],[0,0,0]])
C1=enc([[0,0,1],[1,0,1],[0,1,0]]) # x^3+x+1
C2=enc([[0,0,1],[1,0,0],[0,1,1]]) # x^3+x^2+1
bad_reps=[J3, I^J3, C1, C2]
bad_orbits=[]
for A in bad_reps:
    orb={conj(P,A,GLinv[P]) for P in GL}
    bad_orbits.append(orb)
assert [len(x) for x in bad_orbits]==[42,42,24,24]
bad=set().union(*bad_orbits)
assert len(bad)==132
assert bad == set(range(TOTAL)) - decomposable

# Independently check the ten good rational-canonical types by explicit D+N witnesses.
E12=enc([[0,1,0],[0,0,0],[0,0,0]])
Q0=enc([[0,1,0],[1,1,0],[0,0,0]])
Q1=enc([[0,1,0],[1,1,0],[0,0,1]])
W=enc([[1,1,0],[1,1,0],[0,0,0]])
examples=[
    (0,0,0),
    (I,I,0),
    (enc([[1,0,0],[0,0,0],[0,0,0]]),enc([[1,0,0],[0,0,0],[0,0,0]]),0),
    (enc([[1,0,0],[0,1,0],[0,0,0]]),enc([[1,0,0],[0,1,0],[0,0,0]]),0),
    (E12,0,E12),
    (I^E12,I,E12),
    (enc([[0,1,0],[0,0,0],[0,0,1]]),enc([[0,0,0],[0,0,0],[0,0,1]]),E12),
    (enc([[1,1,0],[0,1,0],[0,0,0]]),enc([[1,0,0],[0,1,0],[0,0,0]]),E12),
    (Q0,enc([[1,0,0],[0,0,0],[0,0,0]]),W),
    (Q1,enc([[1,0,0],[0,0,0],[0,0,1]]),W),
]
for A,D,Z in examples:
    assert A == (D^Z)
    assert mm(D,D)==D
    assert mm(Z,Z)==0

print('VERIFY_OK')
print('idempotents=58 square_zero=22 decomposable=380 nondecomposable=132')
print('bad_class_sizes=42,42,24,24')
