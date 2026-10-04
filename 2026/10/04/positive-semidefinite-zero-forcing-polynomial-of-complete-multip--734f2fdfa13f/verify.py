from math import comb

def integer_partitions(n, lo=1, prefix=()):
    if n == 0:
        if len(prefix) >= 2:
            yield list(prefix)
        return
    for k in range(lo, n + 1):
        yield from integer_partitions(n-k, k, prefix+(k,))

def psd_force(parts, mask):
    cls=[]
    for i,n in enumerate(parts): cls += [i]*n
    N=len(cls); blue={v for v in range(N) if (mask>>v)&1}
    while True:
        whites=[v for v in range(N) if v not in blue]
        if not whites: return True
        unseen=set(whites); comps=[]
        while unseen:
            root=unseen.pop(); comp={root}; stack=[root]
            while stack:
                v=stack.pop()
                add=[u for u in list(unseen) if cls[u] != cls[v]]
                for u in add:
                    unseen.remove(u); comp.add(u); stack.append(u)
            comps.append(comp)
        forced=None
        for comp in comps:
            for b in blue:
                nbr=[w for w in comp if cls[w] != cls[b]]
                if len(nbr)==1:
                    forced=nbr[0]; break
            if forced is not None: break
        if forced is None: return False
        blue.add(forced)

def structural(parts, mask):
    cls=[]
    for i,n in enumerate(parts): cls += [i]*n
    w=[0]*len(parts); b=[0]*len(parts)
    for v,i in enumerate(cls):
        if (mask>>v)&1: b[i]+=1
        else: w[i]+=1
    support=[i for i,x in enumerate(w) if x]
    if len(support)<=1: return True
    if len(support)!=2: return False
    i,j=support
    return (w[j]==1 and b[i]>0) or (w[i]==1 and b[j]>0)

def closed_coeffs(parts):
    N=sum(parts); c=[0]*(N+1); c[N]=1
    for n in parts:
        for a in range(1,n+1): c[N-a]+=comb(n,a)
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            ni,nj=parts[i],parts[j]
            for a in range(1,ni): c[N-a-1]+=nj*comb(ni,a)
            for b in range(1,nj): c[N-b-1]+=ni*comb(nj,b)
            if ni>=2 and nj>=2: c[N-2]-=ni*nj
    return c

graph_types=subset_checks=classification_checks=coefficient_checks=0
for N in range(2,11):
    for parts in integer_partitions(N):
        coeff=[0]*(N+1)
        for mask in range(1<<N):
            direct=psd_force(parts,mask)
            structural_ok=structural(parts,mask)
            assert direct==structural_ok,(parts,mask,direct,structural_ok)
            if direct: coeff[mask.bit_count()]+=1
            subset_checks+=1; classification_checks+=1
        expected=closed_coeffs(parts)
        assert coeff==expected,(parts,coeff,expected)
        z=next(k for k,a in enumerate(coeff) if a)
        assert z==N-max(parts),(parts,z,N-max(parts))
        coefficient_checks+=N+1; graph_types+=1
print(f'VERIFY_OK graph_types={graph_types} subset_checks={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} max_order=10')
