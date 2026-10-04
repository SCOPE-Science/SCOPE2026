from itertools import combinations
from collections import deque
from math import comb

def double_star(a,b):
    # centers 0,1; A-leaves 2..a+1; B-leaves a+2..a+b+1
    n=a+b+2
    adj=[set() for _ in range(n)]
    u,v=0,1
    adj[u].add(v); adj[v].add(u)
    A=list(range(2,2+a))
    B=list(range(2+a,n))
    for x in A:
        adj[u].add(x); adj[x].add(u)
    for y in B:
        adj[v].add(y); adj[y].add(v)
    return adj,u,v,A,B

def distances(adj):
    n=len(adj)
    D=[[10**9]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0
        q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if D[s][y]==10**9:
                    D[s][y]=D[s][x]+1
                    q.append(y)
    return D

def is_general_position(D,mask):
    verts=[v for v in range(len(D)) if (mask>>v)&1]
    for x,y,z in combinations(verts,3):
        if D[x][y]+D[y][z]==D[x][z]:
            return False
        if D[x][z]+D[z][y]==D[x][y]:
            return False
        if D[y][x]+D[x][z]==D[y][z]:
            return False
    return True

def structural(a,b,u,v,A,B,mask):
    cu=(mask>>u)&1
    cv=(mask>>v)&1
    xa=sum((mask>>x)&1 for x in A)
    xb=sum((mask>>x)&1 for x in B)

    if not cu and not cv:
        return True
    if cu and cv:
        return xa==0 and xb==0
    if cu:
        return (xa==0) or (xb==0 and xa<=1)
    return (xb==0) or (xa==0 and xb<=1)

def predicted_coeffs(a,b):
    m=a+b
    out=[0]*(m+1)
    # neither center
    for k in range(m+1):
        out[k]+=comb(m,k)
    # u only: x(1+x)^b + a x^2
    for j in range(b+1):
        out[j+1]+=comb(b,j)
    out[2]+=a
    # v only: x(1+x)^a + b x^2
    for j in range(a+1):
        out[j+1]+=comb(a,j)
    out[2]+=b
    # both centers only
    out[2]+=1
    return out

def maximal_gp(D,mask):
    if not is_general_position(D,mask):
        return False
    n=len(D)
    for v in range(n):
        if not ((mask>>v)&1):
            if is_general_position(D,mask|(1<<v)):
                return False
    return True

graphs=subsets=gp_sets=maximal_sets=0
for a in range(2,8):
    for b in range(2,8):
        adj,u,v,A,B=double_star(a,b)
        D=distances(adj)
        n=len(adj)
        coeff=[0]*(n+1)
        facets=[]
        for mask in range(1<<n):
            subsets += 1
            actual=is_general_position(D,mask)
            pred=structural(a,b,u,v,A,B,mask)
            assert actual==pred,(a,b,mask,actual,pred)
            if actual:
                gp_sets += 1
                coeff[mask.bit_count()]+=1
                if maximal_gp(D,mask):
                    facets.append(mask)
                    maximal_sets += 1

        while coeff and coeff[-1]==0:
            coeff.pop()
        assert coeff==predicted_coeffs(a,b),(a,b,coeff,predicted_coeffs(a,b))

        expected_facets=[]
        # all leaves
        mask=sum(1<<x for x in A+B)
        expected_facets.append(mask)
        # u plus all B, v plus all A
        expected_facets.append((1<<u)+sum(1<<x for x in B))
        expected_facets.append((1<<v)+sum(1<<x for x in A))
        # u with one A; v with one B; and u,v
        expected_facets += [(1<<u)|(1<<x) for x in A]
        expected_facets += [(1<<v)|(1<<y) for y in B]
        expected_facets.append((1<<u)|(1<<v))
        assert set(facets)==set(expected_facets),(a,b,len(facets),len(expected_facets))

        assert max(i for i,c in enumerate(coeff) if c)==a+b
        assert coeff[a+b]==1
        assert sum(coeff)==2**(a+b)+2**a+2**b+a+b+1
        graphs += 1

print("VERIFY_OK")
print("double_star_parameter_pairs_checked =",graphs)
print("vertex_subsets_checked =",subsets)
print("general_position_sets_checked =",gp_sets)
print("maximal_general_position_sets_checked =",maximal_sets)
print("parameters a,b = 2..7")
print("all direct geodesic tests matched the structural classification")
print("all polynomial coefficients matched the closed formula")
print("all maximal-set classifications matched")
print("all general-position numbers, unique maximum-set counts, and total counts matched")
