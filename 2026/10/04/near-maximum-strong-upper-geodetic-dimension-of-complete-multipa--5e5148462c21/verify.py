import itertools

def partitions(n,r,lo=1):
    if r==0:
        if n==0:
            yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1):
            break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def strong_geodetic(mask, lab):
    n=len(lab)
    selected=[v for v in range(n) if (mask>>v)&1]
    omitted=[v for v in range(n) if not ((mask>>v)&1)]
    if not omitted:
        return True

    # In a complete multipartite graph, only a selected pair from one part
    # has a length-two geodesic, and its internal vertex may be any vertex
    # outside that part. One fixed geodesic can cover at most one omitted
    # vertex. Hence strong geodeticity is exactly a bipartite matching problem
    # between omitted vertices and selected same-part pairs.
    resources=[]
    for a in range(len(selected)):
        for b in range(a+1,len(selected)):
            u,v=selected[a],selected[b]
            if lab[u]==lab[v]:
                resources.append(lab[u])

    match=[-1]*len(resources)
    def augment(oi,seen):
        part=lab[omitted[oi]]
        for j,rpart in enumerate(resources):
            if rpart==part or seen[j]:
                continue
            seen[j]=True
            if match[j] < 0 or augment(match[j],seen):
                match[j]=oi
                return True
        return False

    for oi in range(len(omitted)):
        if not augment(oi,[False]*len(resources)):
            return False
    return True

def minimal_strong(mask,lab):
    if not strong_geodetic(mask,lab):
        return False
    for v in range(len(lab)):
        if (mask>>v)&1 and strong_geodetic(mask & ~(1<<v),lab):
            return False
    return True

def predicted(parts):
    p=tuple(sorted(parts))
    n=sum(p)
    if all(x==1 for x in p):
        return n,1

    # K_{1,m}, m>=2.
    if len(p)==2 and p[0]==1 and p[1]>=2:
        return n-1,1

    # K_{2,m}, m>=2.
    if len(p)==2 and p[0]==2 and p[1]>=2:
        return n-1,(4 if p[1]==2 else p[1])

    # K_{2,1,...,1} with at least two singleton parts.
    if p[-1]==2 and p.count(2)==1 and p.count(1)>=2:
        return n-1,p.count(1)

    # K_{2,2,1,...,1} with at least one singleton part.
    if p.count(2)==2 and p.count(1)>=1 and all(x in (1,2) for x in p):
        t=p.count(1)
        return n-1,(5 if t==1 else 4)

    return n-2,None

types=0
subsets=0
for n in range(2,11):
    for r in range(2,n+1):
        for parts in partitions(n,r):
            lab=labels(parts)
            mins=[]
            for mask in range(1<<n):
                subsets += 1
                if minimal_strong(mask,lab):
                    mins.append(mask)
            upper=max(m.bit_count() for m in mins)
            count=sum(m.bit_count()==upper for m in mins)
            bound,pcount=predicted(parts)
            if pcount is None:
                assert upper <= bound, (parts,upper,bound)
            else:
                assert (upper,count)==(bound,pcount), (parts,upper,count,bound,pcount)
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("strong geodeticity decided by explicit omitted-vertex/same-part-pair matching")
print("all N and N-1 threshold classifications matched")
print("all stated counts of maximum N-1 minimal sets matched")
