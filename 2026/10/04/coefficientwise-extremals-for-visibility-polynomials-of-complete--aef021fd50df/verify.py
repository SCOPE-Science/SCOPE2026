import itertools, math
from collections import deque

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for q in partitions(n-a, a):
            yield (a,) + q

def labels(parts):
    L=[]
    for i,a in enumerate(parts):
        L += [i]*a
    return L

def graph(parts):
    L=labels(parts); n=len(L)
    adj=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if L[i] != L[j]:
                adj[i].append(j); adj[j].append(i)
    return L,adj

def all_dist(adj):
    n=len(adj); out=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w] < 0:
                    d[w]=d[v]+1; q.append(w)
        out.append(d)
    return out

def direct_mv(mask, adj, D):
    verts=[v for v in range(len(adj)) if (mask>>v)&1]
    for ia,u in enumerate(verts):
        for v in verts[ia+1:]:
            banned=set(verts)-{u,v}
            dd={u:0}; q=deque([u])
            while q:
                x=q.popleft()
                if x==v: break
                for y in adj[x]:
                    if y in banned or y in dd: continue
                    dd[y]=dd[x]+1; q.append(y)
            if dd.get(v,-1) != D[u][v]:
                return False
    return True

def structural(mask, parts, L):
    cnt=[0]*len(parts)
    for v in range(len(L)):
        if (mask>>v)&1:
            cnt[L[v]] += 1
    for i,s in enumerate(cnt):
        if s>=2 and sum(parts[j]-cnt[j] for j in range(len(parts)) if j!=i)==0:
            return False
    return True

def formula(parts):
    N=sum(parts)
    c=[math.comb(N,k) for k in range(N+1)]
    p=sum(a>=2 for a in parts)
    for a in parts:
        if a>=2:
            sh=N-a
            for j in range(2,a+1):
                c[sh+j] -= math.comb(a,j)
    if p>=1:
        c[N] += p-1
    return c

def complement_formula(parts,t):
    N=sum(parts)
    return math.comb(N,t)-sum(math.comb(a,t) for a in parts if a>=t+2)

types=subsets=0
for N in range(2,11):
    for parts in partitions(N):
        if len(parts)<2:
            continue
        L,adj=graph(parts); D=all_dist(adj)
        actual=[0]*(N+1)
        for mask in range(1<<N):
            subsets += 1
            a=direct_mv(mask,adj,D)
            b=structural(mask,parts,L)
            assert a==b, (parts,mask,a,b)
            if a: actual[mask.bit_count()] += 1
        pred=formula(parts)
        assert actual==pred, (parts,actual,pred)
        if any(x>=2 for x in parts):
            assert actual[N]==0
            for t in range(1,N):
                assert actual[N-t]==complement_formula(parts,t)
        types += 1

for N in range(3,31):
    family=[]
    for parts in partitions(N):
        if len(parts)<2 or all(a==1 for a in parts):
            continue
        family.append((parts,formula(parts)))
    assert family

    # Coefficientwise maximum: exactly the multipartite graphs with every part <=2.
    maxvec=[max(c[k] for _,c in family) for k in range(N+1)]
    max_parts=sorted(p for p,c in family if c==maxvec)
    expected=sorted(p for p,c in family if max(p)<=2)
    assert max_parts==expected, (N,max_parts,expected)
    assert maxvec == [math.comb(N,k) for k in range(N)] + [0]

    # The star uniquely minimizes the cubic coefficient.
    star=(1,N-1)
    sc=formula(star)
    m3=min(c[3] for _,c in family)
    assert [p for p,c in family if c[3]==m3] == [star]
    assert m3 == math.comb(N-1,3)

    if N<=5:
        minvec=[min(c[k] for _,c in family) for k in range(N+1)]
        assert sc==minvec
        assert [p for p,c in family if c==minvec] == [star]
    else:
        witness=tuple(sorted((3,N-3)))
        wc=formula(witness)
        assert sc[3] < wc[3]
        assert wc[N-1] == 0 < sc[N-1] == 1
        # Any coefficientwise minimum would need the unique smallest cubic
        # coefficient, hence would have to be the star; the witness defeats it.

print("VERIFY_OK")
print("multipartite_types_definition_checked =",types)
print("vertex_subsets_definition_checked =",subsets)
print("definition_orders = 2..10")
print("extremal_partition_orders = 3..30")
print("all-set criterion and polynomial matched")
print("coefficientwise maxima classification matched")
print("minimum-existence threshold N=6 matched")
