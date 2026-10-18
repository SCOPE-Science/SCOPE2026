#!/usr/bin/env python3
"""Exact finite-state and independently enumerated checks for Möbius-ladder 1-limited domination.
No nonstandard Python packages are required. Run: python3 verify.py
"""
from collections import Counter
from itertools import product

# Polynomial operations over Z[u], represented by lists of coefficients.
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def plus(a,b):
    out=[0]*max(len(a),len(b))
    for i,c in enumerate(a):out[i]+=c
    for i,c in enumerate(b):out[i]+=c
    return trim(out)

def minus(a,b):
    return plus(a,[-v for v in b])

def mul(a,b):
    if a==[0] or b==[0]:return [0]
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return trim(out)

def times(a,k):return trim([k*x for x in a])

def mon(k,c=1):return [0]*k+[c]

def matmul(A,B):
    r=len(A); c=len(B[0]); k=len(B)
    C=[[[0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for q in range(k):
            a=A[i][q]
            if a!=[0]:
                for j in range(c):
                    if B[q][j]!=[0]:C[i][j]=plus(C[i][j],mul(a,B[q][j]))
    return C

def trace(A):
    z=[0]
    for i in range(len(A)):z=plus(z,A[i][i])
    return z

def det_identity_coefficients(A):
    """Newton identities compute det(I-t A) in Z[u][t], exactly."""
    n=len(A); powers=[]; power=A
    for k in range(1,n+1):
        powers.append(trace(power))
        if k<n:power=matmul(power,A)
    e=[[1]]
    for k in range(1,n+1):
        v=[0]
        for j in range(1,k+1):v=plus(v,mul(e[k-j],powers[j-1]))
        assert all(x%k==0 for x in v), ('Newton division',k)
        e.append(trim([-x//k for x in v]))
    return e

def flip(a):return ((a&1)<<1)|((a&2)>>1)

def admissible(a,b,c):
    return all(((a>>r)&1)+((c>>r)&1)+((b>>(1-r))&1)<=1+((b>>r)&1) for r in (0,1))

STATES=list(product(range(4),repeat=2))
JUMP={s:i for i,s in enumerate(STATES)}
SWAP=[JUMP[flip(a),flip(b)] for a,b in STATES]
M=[[[0] for _ in range(16)] for _ in range(16)]
for i,(a,b) in enumerate(STATES):
    for c in range(4):
        if admissible(a,b,c): M[i][JUMP[b,c]]=mon(b.bit_count())
assert all(M[i][j]==M[SWAP[i]][SWAP[j]] for i in range(16) for j in range(16))

# Bases e_i+e_swap(i) (including the fixed vectors), and e_i-e_swap(i).
seen=set(); plus_basis=[]; minus_basis=[]
for i in range(16):
    if i in seen:continue
    j=SWAP[i];seen|={i,j}
    v={i:1}
    if j!=i:
        v[j]=1;minus_basis.append({i:1,j:-1})
    plus_basis.append(v)

def action_block(basis):
    out=[[[0] for _ in basis] for _ in basis]
    for col,v in enumerate(basis):
        W=[[0] for _ in range(16)]
        for ii in range(16):
            for j,sgn in v.items():W[ii]=plus(W[ii],times(M[ii][j],sgn))
        for row,u in enumerate(basis):
            representative=next(iter(u))
            out[row][col]=times(W[representative],u[representative])
        for i in range(16):
            check=[0]
            for row,u in enumerate(basis):
                if i in u:check=plus(check,times(out[row][col],u[i]))
            assert check==W[i],('basis decomposition',i,col)
    return out

P=action_block(plus_basis);N=action_block(minus_basis)
assert len(P)==10 and len(N)==6
DP=det_identity_coefficients(P)
DN=det_identity_coefficients(N)
for coeffs in (DP,DN):
    while len(coeffs)>1 and coeffs[-1]==[0]:coeffs.pop()
# Exact symbolic target products in Z[u][t].
A={0:mon(0,-1),1:mon(0),2:mon(1),3:plus(mon(1),times(mon(2),2)),
   4:plus(plus(mon(2),mon(3)),mon(4)),5:mon(4)}
expected_plus=[[0] for _ in range(11)]
for tdeg,poly in A.items():
    expected_plus[tdeg]=minus(expected_plus[tdeg],poly)
    expected_plus[tdeg+1]=plus(expected_plus[tdeg+1],mul(mon(1),poly))
while len(expected_plus)>1 and expected_plus[-1]==[0]:expected_plus.pop()
# (tu-1)*A(t,u): coeff k = u*A[k-1]-A[k]
assert DP==expected_plus,('plus determinant',DP,expected_plus)
expected_minus=[[1],mon(1,-1),mon(1)]
assert DN==expected_minus,('minus determinant',DN,expected_minus)
print('EXACT determinants: plus and minus blocks match the displayed factors.')

# Independent direct enumeration on C_{2n} with antipodal rungs.
def brute(n):
    v=2*n
    nbr=[(1<<((i-1)%v))|(1<<((i+1)%v))|(1<<((i+n)%v)) for i in range(v)]
    out=Counter()
    for T in range(1<<v):
        good=True
        for i in range(v):
            if (T&nbr[i]).bit_count()>1+((T>>i)&1):
                good=False;break
        if good:out[v-T.bit_count()]+=1
    return out

def trace_twist_poly(n):
    # Weighted paths on the original 16-state automaton, independent of its block factorization.
    ans=[0]
    for initial in range(16):
        d={(initial,0):1}
        for _ in range(n):
            nd={}
            for (state,k),count in d.items():
                a,b=STATES[state]
                for c in range(4):
                    if admissible(a,b,c):
                        key=(JUMP[b,c],k+b.bit_count())
                        nd[key]=nd.get(key,0)+count
            d=nd
        for (state,k),count in d.items():
            if state==SWAP[initial]:
                if k>=len(ans):ans += [0]*(k+1-len(ans))
                ans[k]+=count
    return trim(ans)

for n in range(3,10):
    poly=trace_twist_poly(n)
    direct=brute(n)
    assert {2*n-k:c for k,c in enumerate(poly) if c}==dict(direct),(n,poly,direct)
    opt=min(direct)
    predicted_n=n if n%4==0 else n+1
    predicted_count=4 if n%4==0 else (3*n if n%2 else 2*n)
    assert (opt,direct[opt])==(predicted_n,predicted_count)
    print(f'n={n}: independent exhaustive subsets={1<<(2*n)}; min={opt}; count={direct[opt]}; coefficients match.')

# Factorization implies the following coefficient formula at the two lowest degrees.
# [z^0] Q(t,z) = 4t^4/(1-t^4).
# [z^1] Q(t,z) = t(1+4t+7t^2-2t^4)/(1-t^2)^2.
# The two series give the minimum and its number for EVERY n>=3.
# Recheck longer cases using the full transfer automaton, not a finite proof substitute.
for n in range(10,31):
    poly=trace_twist_poly(n)
    maxT=len(poly)-1
    count=poly[maxT]
    assert (2*n-maxT,count)==(n if n%4==0 else n+1,
            4 if n%4==0 else (3*n if n%2 else 2*n))
print('Exact symbolic transfer determinants and all n=3..30 transfer counts passed.')
