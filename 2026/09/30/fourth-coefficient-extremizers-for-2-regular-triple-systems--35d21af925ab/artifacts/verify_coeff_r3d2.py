from collections import Counter
from itertools import combinations


def enumerate_multigraphs(N):
    pairs=[(i,j) for i in range(N) for j in range(i+1,N)]
    deg=[0]*N; vals=[0]*len(pairs)
    stats=Counter(); eqsig=Counter(); total=0
    def signature():
        adj=[[] for _ in range(N)]; mult={}
        for (i,j),x in zip(pairs,vals):
            if x:
                mult[(i,j)]=x; adj[i].append(j); adj[j].append(i)
        if not all(len(adj[v])==2 for v in range(N)):
            return None
        for v in range(N):
            ds=[u for u in adj[v] if mult[tuple(sorted((u,v)))]==2]
            if len(ds)!=1: return None
        seen=set(); sig=[]
        for s in range(N):
            if s in seen: continue
            stack=[s]; seen.add(s); comp=[]
            while stack:
                v=stack.pop(); comp.append(v)
                for u in adj[v]:
                    if u not in seen:
                        seen.add(u); stack.append(u)
            if len(comp)<4 or len(comp)%2: return None
            sig.append(len(comp)//2)
        return tuple(sorted(sig))
    def rec(k):
        nonlocal total
        if k==len(pairs):
            if all(d==3 for d in deg):
                total += 1
                P=sum(x==2 for x in vals)
                stats[P]+=1
                if P==N//2:
                    eqsig[signature()] += 1
            return
        i,j=pairs[k]
        for x in range(min(2,3-deg[i],3-deg[j])+1):
            deg[i]+=x; deg[j]+=x; vals[k]=x
            ok=True
            for v in range(N):
                need=3-deg[v]
                if need<0:
                    ok=False; break
                cap=0
                for kk in range(k+1,len(pairs)):
                    a,b=pairs[kk]
                    if a==v or b==v: cap += 2
                if need>cap:
                    ok=False; break
            if ok: rec(k+1)
            deg[i]-=x; deg[j]-=x
        vals[k]=0
    rec(0)
    return total,stats,eqsig

for N in (4,6,8):
    total,stats,eqsig=enumerate_multigraphs(N)
    maxP=max(stats)
    assert maxP==N//2
    assert None not in eqsig
    print(f'N={N} labeled_multigraphs={total} max_double_pairs={maxP} equality={sum(eqsig.values())} signatures={dict(eqsig)}')
print('VERIFY_OK')
