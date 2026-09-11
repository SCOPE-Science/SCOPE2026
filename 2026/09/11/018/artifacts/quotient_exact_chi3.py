"""Exact ordinary chi=3 of Cay(SL(3,Z),S_gen): LOWER via odd closed walk (length-9
identity word), UPPER via pullback of certified 3-coloring of SL(3,F2) quotient.
Subgroup/surjectivity: the mod-2 images generate the full 168-element SL(3,F2)
by BFS closure (size check), and each generator image is nontrivial (no loops),
so reduction mod 2 is an edge-preserving homomorphism Cayley -> quotient."""
from collections import deque
def mm(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0]+A[0][2]*B[2][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]+A[0][2]*B[2][1], A[0][0]*B[0][2]+A[0][1]*B[1][2]+A[0][2]*B[2][2]),
     (A[1][0]*B[0][0]+A[1][1]*B[1][0]+A[1][2]*B[2][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]+A[1][2]*B[2][1], A[1][0]*B[0][2]+A[1][1]*B[1][2]+A[1][2]*B[2][2]),
     (A[2][0]*B[0][0]+A[2][1]*B[1][0]+A[2][2]*B[2][0], A[2][0]*B[0][1]+A[2][1]*B[1][1]+A[2][2]*B[2][1], A[2][0]*B[0][2]+A[2][1]*B[1][2]+A[2][2]*B[2][2]))
def madj(M):
    a,b,c,d,e,f,g,h,i = M[0][0],M[0][1],M[0][2],M[1][0],M[1][1],M[1][2],M[2][0],M[2][1],M[2][2]
    return ((e*i-f*h,c*h-b*i,b*f-c*e),(f*g-d*i,a*i-c*g,c*d-a*f),(d*h-e*g,b*g-a*h,a*e-b*d))
def EE(i,j,v=1):
    M=[[0]*3 for _ in range(3)]
    for k in range(3): M[k][k]=1
    M[i][j]=v
    return tuple(tuple(r) for r in M)
I=((1,0,0),(0,1,0),(0,0,1))
E12=EE(0,1); E21=EE(1,0); E23=EE(1,2); E32=EE(2,1)
G={'a':E12,'A':madj(E12),'b':E21,'B':madj(E21),'c':E23,'C':madj(E23),'d':E32,'D':madj(E32)}
# LOWER: odd closed walk
w='abAcaBcAC'
M=I
for ch in w: M=mm(M,G[ch])
print("LOWER: word",w,"len",len(w),"evaluates_to_I:",M==I,"-> chi(Cayley)>=3", flush=True)
# UPPER: mod-2 quotient
def mod(M): return tuple(tuple(x%2 for x in row) for row in M)
QI=((1,0,0),(0,1,0),(0,0,1))
Sim={mod(E12),mod(E21),mod(E23),mod(E32)}
print("UPPER: distinct nontrivial gen images:",len(Sim)==4 and QI not in Sim, flush=True)
seen={QI}; q=deque([QI])
while q:
    u=q.popleft()
    for s in Sim:
        v=mod(mm(u,s))
        if v not in seen: seen.add(v); q.append(v)
print("UPPER: subgroup size (expect 168):",len(seen), flush=True)
elems=list(seen); idx={v:i for i,v in enumerate(elems)}; n=len(elems)
N=[set() for _ in range(n)]
for v,i in idx.items():
    for s in Sim: N[i].add(idx[mod(mm(v,s))])
order=sorted(range(n),key=lambda i:-len(N[i]))
color=[-1]*n; nodes=[0]
def bb(t):
    nodes[0]+=1
    if t==n: return True
    best=-1;bs=-1
    for i in order:
        if color[i]<0:
            s=len({color[j] for j in N[i] if color[j]>=0})
            if s>bs: bs=s;best=i
    for cc in range(3):
        if any(color[j]==cc for j in N[best] if color[j]>=0): continue
        color[best]=cc
        if bb(t+1): return True
        color[best]=-1
    return False
ok=bb(0)
print("UPPER: quotient 3-colorable:",ok,"search_nodes:",nodes[0], flush=True)
# verify coloring proper + no loops
prop=all(color[i]!=color[j] for i in range(n) for j in N[i])
print("UPPER: coloring verified proper:",prop,"-> chi(Cayley)<=3", flush=True)
print("EXACT_CHI3_CERTIFIED" if (M==I and ok and prop and len(seen)==168) else "FAIL", flush=True)
