"""Exact finite-state certificate for minimum forts of C4 Cartesian Cn.
Run: python3 verify.py   (Python standard library only).
The mathematical argument relating the certificate to all n is in RESULT.md.
"""
from collections import defaultdict, deque
from itertools import combinations

WIDTH = 4
MASKS = range(1 << WIDTH)
STATES = [(a,b) for a in MASKS for b in MASKS if a or b]
IDS = {s:i for i,s in enumerate(STATES)}
NEGATIVE_POTENTIAL = {
 (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
 (0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),
 (1,10),(1,11),(2,5),(2,7),(4,10),(4,14),(8,5),(8,13)
}

def admissible(a,b,c):
    for r in range(4):
        if not ((b >> r)&1):
            k = ((a >> r)&1) + ((c >> r)&1)
            k += ((b >> ((r+1)%4))&1) + ((b >> ((r-1)%4))&1)
            if k == 1:
                return False
    return True


def components(n, arcs):
    adj=[[] for _ in range(n)]
    rev=[[] for _ in range(n)]
    for a,b in arcs:
        adj[a].append(b)
        rev[b].append(a)
    seen=set(); order=[]
    def visit(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:visit(w)
        order.append(v)
    for v in range(n):
        if v not in seen:visit(v)
    seen=set(); groups=[]
    def revisit(v,g):
        seen.add(v);g.append(v)
        for w in rev[v]:
            if w not in seen:revisit(w,g)
    for v in reversed(order):
        if v not in seen:
            g=[];revisit(v,g);groups.append(g)
    return groups


def matrix_multiply(A,B):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    out[i][j]+=A[i][k]*B[k][j]
    return out


def charpoly(A):
    n=len(A); X=[[int(i==j) for j in range(n)] for i in range(n)]
    coef=[]
    for k in range(1,n+1):
        X=matrix_multiply(A,X)
        trace=sum(X[i][i] for i in range(n))
        assert trace % k==0
        c=-trace//k
        coef.append(c)
        for i in range(n): X[i][i]+=c
    assert all(z==0 for row in X for z in row)
    return coef


def direct_count(n):
    N=4*n
    adj=[]
    for j in range(n):
        for r in range(4):
            neighbors=[(j,(r+1)%4),(j,(r-1)%4),((j+1)%n,r),((j-1)%n,r)]
            adj.append(sum(1 << (4*c+s) for c,s in neighbors))
    def is_fort(bitset):
        return all((bitset>>v)&1 or (bitset&adj[v]).bit_count()!=1 for v in range(N))
    for k in range(1,2*((n+1)//2)+1):
        count=0
        for choices in combinations(range(N),k):
            mask=sum(1<<v for v in choices)
            if is_fort(mask):count+=1
        if count:
            return k,count
    raise AssertionError('no fort found')


def main():
    edges=[]; tight=[]; defect=[]
    for a,b in STATES:
        for c in MASKS:
            if admissible(a,b,c):
                # Two consecutive empty columns cannot occur in any nonempty fort.
                assert b or a==c
                assert (b,c)!=(0,0)
                u=IDS[a,b];v=IDS[b,c]
                w=b.bit_count()-1
                p=-int((a,b) in NEGATIVE_POTENTIAL)
                q=-int((b,c) in NEGATIVE_POTENTIAL)
                reduced=w+p-q
                assert reduced >= 0,(a,b,c,reduced)
                edges.append((u,v))
                if reduced==0:tight.append((u,v))
                if reduced==1:defect.append((u,v))
    assert len(STATES)==255 and len(edges)==2671
    parts=components(len(STATES),tight)
    recurrent=[g for g in parts if len(g)>1 or (g[0],g[0]) in tight]
    assert sorted(len(g) for g in recurrent)==[4,4,10,10]
    for g in recurrent:
        S=set(g); und=defaultdict(set)
        for u,v in tight:
            if u in S and v in S:
                und[u].add(v);und[v].add(u)
        color={}
        for u in g:
            if u not in color:
                color[u]=0;que=deque([u])
                while que:
                    z=que.popleft()
                    for v in und[z]:
                        assert v!=z
                        if v not in color:
                            color[v]=1-color[z];que.append(v)
                        else:assert color[v]!=color[z]
        verts=sorted(g); position={v:i for i,v in enumerate(verts)}
        A=[[0]*len(g) for _ in g]
        for u,v in tight:
            if u in S and v in S:A[position[u]][position[v]]+=1
        polynomial=charpoly(A)
        if len(g)==4: assert polynomial==[0,0,0,-1] # t^4-1
        if len(g)==10: assert polynomial==[0,-1,0,-2,0,0,0,0,0,0] # t^10-t^8-2t^6
    # T is the 255 x 255 tight adjacency and B the defect-one adjacency.
    T=[[] for _ in STATES]
    for u,v in tight:T[u].append(v)
    # Sparse row representation for successive exact integer matrix powers of T.
    M=[{i:1} for i in range(len(STATES))]
    def advance(P):
        Q=[defaultdict(int) for _ in STATES]
        for i,row in enumerate(P):
            dest=Q[i]
            for j,ways in row.items():
                for k in T[j]:dest[k]+=ways
        return Q
    # h_m=trace(B T^(2m)); values up to 257 suffice for a
    # 255-dimensional Cayley--Hamilton recurrence certificate.
    h=[]
    for m in range(258):
        h.append(sum(M[v].get(u,0) for u,v in defect))
        M=advance(advance(M))
    assert (h[0],h[1],h[2],h[3],h[4])==(2,6,10,22,42)
    for m in range(1,256):
        assert h[m+2]==h[m+1]+2*h[m],(m,h[m:m+3])
    for m in range(1,26):
        expected=(8*(2**m)-2*((-1)**m))//3
        assert h[m]==expected
    for n in range(3,8):
        k,c=direct_count(n)
        predicted_k=2*((n+1)//2)
        if n%2==0:
            predicted_c=4*(2**(n//2)+(-1)**(n//2))+8*int(n%4==0)
        else:
            m=(n-1)//2
            predicted_c=n*(8*2**m-2*(-1)**m)//3
        assert (k,c)==(predicted_k,predicted_c),(n,k,c,predicted_k,predicted_c)
    print('VERIFY_OK states=255 edges=2671 recurrent_scc=[4,4,10,10]')
    print('VERIFY_OK exact_characteristic_polynomials=4 Cayley_Hamilton_residuals=255')
    print('VERIFY_OK direct_fort_census_n=3..7; minima_and_counts=correct')
    print('samples',[(n,2*((n+1)//2), (4*(2**(n//2)+(-1)**(n//2))+8*int(n%4==0)) if n%2==0 else n*(8*2**((n-1)//2)-2*(-1)**((n-1)//2))//3) for n in range(3,13)])

if __name__=='__main__':main()
