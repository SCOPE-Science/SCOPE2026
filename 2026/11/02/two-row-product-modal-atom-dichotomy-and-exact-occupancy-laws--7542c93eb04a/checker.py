"""Direct finite enumerator for two-row grid modal algebras.
Run: python3 checker.py. No third-party packages required.
"""
from collections import Counter
from itertools import product
from math import comb, factorial

def partitions(pattern, q):
    m = len(pattern)
    colors = [pattern[j][i] for i in (0, 1) for j in range(m)]
    def cid(keys):
        names = {x:i for i,x in enumerate(sorted(set(keys)))}
        return tuple(names[x] for x in keys)
    states = cid(colors)
    out = [len(set(states))]
    for d in range(5):
        keys=[]
        for i in (0,1):
            horiz=tuple(sorted({states[i*m+j] for j in range(m)}))
            for j in range(m):
                vert=tuple(sorted({states[j],states[m+j]}))
                keys.append((states[i*m+j],horiz,vert))
        new=cid(keys)
        out.append(len(set(new)))
        if new==states: break
        states=new
    return out

def prediction(pattern):
    E=set(pattern)
    symmetric=E=={(b,a) for a,b in E}
    p0={a for a,b in E};p1={b for a,b in E}
    final = len(E) if symmetric else 2*len(E)
    if final==len(p0|p1): depth=0
    elif symmetric or p0!=p1 or not (E & {(b,a) for a,b in E}): depth=1
    else: depth=2
    return final,depth

def stirling2(n,k):
    if n==0: return int(k==0)
    if k==0: return 0
    if k>n: return 0
    t=[[0]*(k+1) for _ in range(n+1)];t[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1): t[i][j]=j*t[i-1][j]+t[i-1][j-1]
    return t[n][k]

def exact_predicted(q,m):
    N=q*q
    symcounts=[0]*(N+1)
    for diagonal in range(q+1):
        for pairs in range(q*(q-1)//2+1):
            symcounts[diagonal+2*pairs] += comb(q,diagonal)*comb(q*(q-1)//2,pairs)
    dist=Counter()
    for t in range(1,min(N,m)+1):
        surj = factorial(t)*stirling2(m,t)
        dist[t]+=symcounts[t]*surj
        dist[2*t]+=(comb(N,t)-symcounts[t])*surj
    assert sum(dist.values())==N**m
    return dist

tests=0
for q,maxm in [(2,6),(3,4),(4,3)]:
    for m in range(1,maxm+1):
        dist=Counter()
        for word in product(range(q*q),repeat=m):
            pat=tuple(divmod(x,q) for x in word)
            vals=partitions(pat,q)
            end=vals[-1]
            target,depth=prediction(pat)
            assert end==target,(q,m,pat,vals,target)
            # earliest rank at which partition is stable: atom counts strictly refine until stable
            seen=next(i for i,num in enumerate(vals) if num==end)
            assert seen==depth,(q,m,pat,vals,depth)
            dist[end]+=1
            tests+=1
        assert dist==exact_predicted(q,m),(q,m,dist,exact_predicted(q,m))
print('ALL_CHECKS_OK', 'complete_coloured_models=',tests)

# Each nonempty ordered-pair support can be represented by one copy of each
# occupied column type; repetitions do not alter modal distinguishability.
support_cases=0
for q in (3,4):
    for mask in range(1,1 << (q*q)):
        pat=tuple(divmod(j,q) for j in range(q*q) if mask & (1 << j))
        vals=partitions(pat,q)
        predicted,depth=prediction(pat)
        assert vals[-1]==predicted,(q,mask,vals,predicted)
        assert next(i for i,v in enumerate(vals) if v==vals[-1])==depth,(q,mask,vals,depth)
        support_cases+=1
print('SUPPORT_CHECKS_OK',support_cases)
