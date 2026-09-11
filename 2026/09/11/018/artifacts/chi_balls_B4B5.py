"""Exact 3-colorings of Cayley balls B_4 (n=1729) and B_5 (n=8409) in Cay(SL(3,Z),S_gen).
Backtracking with saturation ordering; prints search-node certificates.
B_4 solves in <1s; B_5 in ~5-60s. Run: python3 chi_balls_B4B5.py [4|5] (default both)."""
from collections import deque
import sys, time
sys.setrecursionlimit(1000000)
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
g=[EE(0,1),EE(1,0),EE(1,2),EE(2,1)]
S=[]
for x in g: S += [x, madj(x)]

def run(R, cap):
    dist={I:0}; q=deque([I])
    while q:
        u=q.popleft()
        if dist[u]==R: continue
        for s in S:
            v=mm(u,s)
            if v not in dist: dist[v]=dist[u]+1; q.append(v)
    elems=list(dist); idx={v:i for i,v in enumerate(elems)}
    n=len(elems); N=[set() for _ in range(n)]
    for v,i in idx.items():
        for s in S:
            j=idx.get(mm(v,s))
            if j is not None: N[i].add(j)
    order=sorted(range(n), key=lambda i:-len(N[i]))
    color=[-1]*n; nodes=[0]
    def bb(t):
        nodes[0]+=1
        if nodes[0]>cap: return None
        if t==n: return True
        best=-1;bs=-1
        for i in order:
            if color[i]<0:
                s=len({color[j] for j in N[i] if color[j]>=0})
                if s>bs: bs=s; best=i
        for cc in range(3):
            if any(color[j]==cc for j in N[best] if color[j]>=0): continue
            color[best]=cc
            r=bb(t+1)
            if r: return True
            if r is None: return None
            color[best]=-1
        return False
    t0=time.time()
    r=bb(0)
    used=max(color)+1 if r else None
    print(f"B{R}: n={n} 3-colorable={r} colors_used={used} nodes={nodes[0]} time={round(time.time()-t0,1)}s", flush=True)
    return r

radii = [int(a) for a in sys.argv[1:]] or [4,5]
ok = True
for R in radii:
    ok = run(R, 8000000) and ok
print("BALLS_CERTIFIED" if ok else "BALLS_FAIL", flush=True)
