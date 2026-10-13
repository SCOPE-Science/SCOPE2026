from itertools import combinations
from math import comb


def edges_barbell(n):
    # vertices 0..n-1 and n..2n-1; bridge 0--n
    E=set()
    for base in (0,n):
        for i in range(n):
            for j in range(i+1,n):
                E.add((base+i,base+j))
    E.add((0,n))
    return E

def adj_from_edges(N,E):
    A=[set() for _ in range(N)]
    for u,v in E:
        A[u].add(v); A[v].add(u)
    return A

def restrained(n,S):
    N=2*n; A=adj_from_edges(N,edges_barbell(n)); S=set(S); T=set(range(N))-S
    for v in T:
        if not (A[v]&S): return False
        if not (A[v]&T): return False
    return True

def structural(n,S):
    S=set(S); X=set(range(n))-S; Y=set(range(n,2*n))-S
    if len(X)==n or len(Y)==n: return False
    def no_iso_side(X,other,bridge_here,bridge_other):
        if not X: return True
        if len(X)>=2: return True
        v=next(iter(X))
        return v==bridge_here and bridge_other in other
    return no_iso_side(X,Y,0,n) and no_iso_side(Y,X,n,0)

def formula_coeffs(n):
    # A(z)=(1+z)^n-n z^(n-1)-1
    A=[0]*(n+1)
    for k in range(n+1): A[k]=comb(n,k)
    A[0]-=1; A[n-1]-=n
    out=[0]*(2*n+1)
    for i,a in enumerate(A):
        for j,b in enumerate(A): out[i+j]+=a*b
    # +2 z^(n-1)((1+z)^(n-1)-1)-z^(2n-2)
    for k in range(1,n): out[n-1+k]+=2*comb(n-1,k)
    out[2*n-2]-=1
    return out

def brute_coeffs(n):
    N=2*n; out=[0]*(N+1); struct=0
    for mask in range(1<<N):
        S=[v for v in range(N) if mask>>v&1]
        r=restrained(n,S); s=structural(n,S)
        if r!=s:
            raise AssertionError((n,mask,r,s))
        if r: out[len(S)]+=1
        struct+=1
    return out,struct

total_masks=0; valid_sets=0; coeff_checks=0
for n in range(3,9):
    b,checks=brute_coeffs(n); f=formula_coeffs(n)
    assert b==f,(n,b,f)
    total_masks+=checks; valid_sets+=sum(b); coeff_checks+=len(b)
    nz=[k for k,c in enumerate(b) if c]
    assert nz[0]==2
    assert b[2]==n*n
    assert sum(b)==(2**n-n-1)**2+2**n-3
b2,_=brute_coeffs(2); assert b2==formula_coeffs(2) and b2[2]==1
print(f"VERIFY_OK n_range=3..8 subset_checks={total_masks} valid_sets={valid_sets} coefficient_checks={coeff_checks} boundary_n2=P4_checked max_order=16")
