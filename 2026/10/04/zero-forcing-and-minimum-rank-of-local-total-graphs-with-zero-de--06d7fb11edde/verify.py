#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1
            continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def zero_forces(S,N):
    blue=set(S)
    while True:
        move=None
        for v in sorted(blue):
            w=N[v]-blue
            if len(w)==1:
                move=next(iter(w))
                break
        if move is None:
            return len(blue)==len(N)
        blue.add(move)

def brute_z(N):
    n=len(N)
    for k in range(n+1):
        cnt=0
        for C in combinations(range(n),k):
            if zero_forces(C,N):
                cnt+=1
        if cnt:
            return k,cnt
    raise RuntimeError

def zpk_graph(p,k):
    n=p**k
    V=list(range(1,n))
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if (x+y)%p==0:
                N[i].add(j); N[j].add(i)
    q=p
    s=p**(k-1)
    return V,N,q,s

def predicted(q,s):
    if s==2:
        return 2,1,(s-1)*(s**(q-1))
    return q*(s-1)-1,q,(s-1)*(s**(q-1))

def component_sizes(N):
    seen=set(); out=[]
    for v in range(len(N)):
        if v in seen: continue
        st=[v]; seen.add(v); c=[]
        while st:
            x=st.pop(); c.append(x)
            for y in N[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        out.append(len(c))
    return sorted(out)

def witness_matrix(q,s,char2):
    blocks=[]
    if s==2:
        # This boundary is necessarily q=2 for a finite local nonfield ring.
        blocks.append([[0]])
        blocks.append([[1,1],[1,1]])
    else:
        blocks.append([[1]*(s-1) for _ in range(s-1)])
        if char2:
            for _ in range(q-1):
                blocks.append([[1]*s for _ in range(s)])
        else:
            for _ in range((q-1)//2):
                t=2*s
                B=[[0]*t for _ in range(t)]
                for i in range(s):
                    for j in range(s,2*s):
                        B[i][j]=B[j][i]=1
                blocks.append(B)
    n=sum(len(B) for B in blocks)
    M=[[0]*n for _ in range(n)]
    a=0
    for B in blocks:
        m=len(B)
        for i in range(m):
            for j in range(m):
                M[a+i][a+j]=B[i][j]
        a+=m
    return M

cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]
for p,k in cases:
    V,N,q,s=zpk_graph(p,k)
    z,mr,count=predicted(q,s)
    sizes=component_sizes(N)
    M=witness_matrix(q,s,p==2)
    assert rank_fraction(M)==mr, (p,k,rank_fraction(M),mr)
    # Verify witness off-diagonal pattern against the direct graph after
    # reordering by residue components is not attempted; rank is checked here,
    # and direct component structure is checked separately below.
    expected = ([s-1]+[s]*(q-1)) if p==2 else ([s-1]+[2*s]*((q-1)//2))
    assert sizes==sorted(expected), (p,k,sizes,expected)
    if len(V)<=15:
        bz,bc=brute_z(N)
        assert bz==z, (p,k,bz,z)
        # Count agrees in the small cases where exhaustive enumeration is used.
        assert bc==count, (p,k,bc,count)
        print(f"Z/{p**k}: |V|={len(V)} components={sizes} exhaustive Z={bz} min_sets={bc} witness_rank={mr}")
    else:
        print(f"Z/{p**k}: |V|={len(V)} components={sizes} structural Z={z} predicted_min_sets={count} witness_rank={mr}")

# A second non-cyclic local ring: F2[x,y]/(x,y)^2.
# Encode a+bx+cy by (a,b,c); units have a=1, zero divisors a=0.
V=[(a,b,c) for a in range(2) for b in range(2) for c in range(2) if (a,b,c)!=(0,0,0)]
N=[set() for _ in V]
for i,x in enumerate(V):
    for j in range(i+1,len(V)):
        y=V[j]
        if (x[0]+y[0])%2==0:
            N[i].add(j); N[j].add(i)
q,s=2,4
z,mr,count=predicted(q,s)
assert component_sizes(N)==[3,4]
bz,bc=brute_z(N)
assert (bz,bc)==(z,count)
assert rank_fraction(witness_matrix(q,s,True))==mr
print(f"F2[x,y]/(x,y)^2: |V|={len(V)} components={component_sizes(N)} exhaustive Z={bz} min_sets={bc} witness_rank={mr}")

print("VERIFY_OK")
