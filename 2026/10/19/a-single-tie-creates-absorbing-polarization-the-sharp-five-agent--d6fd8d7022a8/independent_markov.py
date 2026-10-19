"""Independent exact absorbing-chain linear-system check of the 5-agent results.
Standard library only; explicit 32-state transition matrix, no potential ordering assumption.
"""
from fractions import Fraction as F

def solve(A,b):
    n=len(A)
    for col in range(n):
        pivot=next((r for r in range(col,n) if A[r][col]),None)
        assert pivot is not None
        A[col],A[pivot]=A[pivot],A[col];b[col],b[pivot]=b[pivot],b[col]
        d=A[col][col];A[col]=[v/d for v in A[col]];b[col]/=d
        for r in range(n):
            if r==col:continue
            c=A[r][col]
            if c:
                A[r]=[x-c*y for x,y in zip(A[r],A[col])];b[r]-=c*b[col]
    return b

def measure(edges):
    n=5; adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    flips={s:[i for i in range(n) if sum((s>>j&1)!=(s>>i&1) for j in adj[i])*2>len(adj[i])] for s in range(32)}
    absorb={s for s in range(32) if not flips[s]}
    transient=[s for s in range(32) if flips[s]]
    # First-step equations: (I-P_transient)x = P_absorbed, (I-P_transient)t=1.
    A=[];q=[]
    for s in transient:
        row=[F(int(s==t)) for t in transient];rhs=F(0)
        for i in range(n):
            target=(s^(1<<i)) if i in flips[s] else s
            if target in transient:row[transient.index(target)]-=F(1,n)
            elif target not in (0,31):rhs+=F(1,n)
        A.append(row);q.append(rhs)
    psol=solve([a[:] for a in A],q[:]);tsol=solve([a[:] for a in A],[F(1) for _ in transient])
    p=(sum(psol,F(0))+len(absorb-{0,31}))/32
    t=sum(tsol,F(0))/32
    return (p,t,len(absorb),sorted(absorb))

star=[(0,1),(0,2),(0,3),(0,4)]
tri=[(0,1),(0,2),(0,3),(1,2),(1,4)]
for es,e in [(star,(1,2)),(tri,(3,4))]:
    print('before',measure(es))
    print('after ',measure(es+[e]))
