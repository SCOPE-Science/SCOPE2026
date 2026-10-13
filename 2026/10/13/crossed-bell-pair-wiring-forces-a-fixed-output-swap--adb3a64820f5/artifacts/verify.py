#!/usr/bin/env python3
from itertools import product

# Exact integer verification for the crossed Bell-pair wiring in arXiv:2610.01684v1.
# Unnormalised Bell states are sufficient because only conditional maps up to nonzero scalar/global sign are compared.

def bell_amp(x,z,i,j):
    return (1 if j == (i ^ x) else 0) * ((-1) ** (z*i))

def chain_map(x,z,u,v):
    # Mentor projects m,n onto beta_{x,z}; sender projects s,B onto beta_{u,v};
    # resources are Phi+ on m-A and n-B. Return map s -> A.
    M = [[0,0],[0,0]]
    for a in (0,1):
        for s in (0,1):
            M[a][s] = sum(bell_amp(x,z,a,n)*bell_amp(u,v,s,n) for n in (0,1))
    return M

I=((1,0),(0,1)); X=((0,1),(1,0)); Z=((1,0),(0,-1))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mpow(A,n): return I if n==0 else A

def scale(A,c): return tuple(tuple(c*A[i][j] for j in range(2)) for i in range(2))

def expected(x,z,u,v):
    # X^(x xor u) Z^(z xor v), up to global sign.
    return mm(mpow(X,x^u), mpow(Z,z^v))

for bits in product((0,1), repeat=4):
    M=tuple(tuple(r) for r in chain_map(*bits))
    P=expected(*bits)
    assert M == P or M == scale(P,-1), (bits,M,P)

# Source resource basis terms: order m1 m2 m3 A1 A2 A3 and m4 m5 m6 B1 B2 B3.
omega1={"000000","001100","010010","011110","100001","101101","110011","111111"}
omega2={"000000","001001","010010","011011","100100","101101","110110","111111"}
calc1=set(); calc2=set()
for m1,m2,m3 in product((0,1), repeat=3):
    calc1.add(f"{m1}{m2}{m3}{m3}{m2}{m1}")  # A1=m3,A2=m2,A3=m1
for m4,m5,m6 in product((0,1), repeat=3):
    calc2.add(f"{m4}{m5}{m6}{m4}{m5}{m6}")  # B1=m4,B2=m5,B3=m6
assert omega1 == calc1
assert omega2 == calc2

# In ordered physical output A2,A3, chain 2 carries input qubit b2 and chain 1 carries b1.
# Hence all-plus branch is exactly SWAP on computational basis.
S=((1,0,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1))
e01=(0,1,0,0)
def mv(A,v): return tuple(sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A)))
assert mv(S,e01)==(0,0,1,0)  # |01> -> |10>
assert mv(S,e01)!=e01

print('VERIFY_OK')
