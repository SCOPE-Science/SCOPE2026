import itertools, math


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


def edges_for(L):
    n=len(L)
    return [(u,v) for u in range(n) for v in range(u+1,n) if L[u]!=L[v]]


def direct_mixed_generator(mask,L,edges):
    S=[s for s in range(len(L)) if (mask>>s)&1]
    sigs=[]
    # vertex signatures
    for v in range(len(L)):
        sigs.append(tuple(0 if s==v else (2 if L[s]==L[v] else 1) for s in S))
    # edge signatures: in a complete multipartite graph, a landmark has distance 0 to
    # an edge exactly when it is an endpoint, and distance 1 otherwise.
    for u,v in edges:
        sigs.append(tuple(0 if s==u or s==v else 1 for s in S))
    return len(set(sigs))==len(sigs)


def criterion(mask,parts,L):
    N=sum(parts)
    omitted=[v for v in range(N) if not ((mask>>v)&1)]
    if len(omitted)==0:
        return True
    if len(omitted)==1:
        x=omitted[0]
        i=L[x]
        return all(parts[j]>=2 for j in range(len(parts)) if j!=i)
    if len(omitted)==2:
        x,y=omitted
        return len(parts)==2 and L[x]!=L[y] and min(parts)>=3
    return False


def coeff_formula(parts):
    N=sum(parts)
    q=sum(n==1 for n in parts)
    A=N if q==0 else (1 if q==1 else 0)
    B=parts[0]*parts[1] if len(parts)==2 and min(parts)>=3 else 0
    c=[0]*(N+1)
    c[N]=1
    if N-1>=0: c[N-1]+=A
    if N-2>=0: c[N-2]+=B
    return c


def mixed_dimension_direct(parts):
    L=labels(parts); E=edges_for(L); N=sum(parts)
    for k in range(N+1):
        for comb in itertools.combinations(range(N),k):
            mask=sum(1<<v for v in comb)
            if direct_mixed_generator(mask,L,E):
                return k
    raise AssertionError('no mixed generator')


types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            L=labels(parts)
            E=edges_for(L)
            actual=[0]*(N+1)
            for mask in range(1<<N):
                subsets += 1
                got=direct_mixed_generator(mask,L,E)
                assert got==criterion(mask,parts,L), (parts,mask,got)
                if got:
                    actual[mask.bit_count()]+=1
            pred=coeff_formula(parts)
            assert actual==pred, (parts,actual,pred)
            q=sum(n==1 for n in parts)
            expected=(N-2 if len(parts)==2 and min(parts)>=3 else (N if q>=2 else N-1))
            observed=min(k for k,c in enumerate(actual) if c)
            assert observed==expected, (parts,observed,expected)
            types += 1

# Explicitly replay the published K_{3,3,5} example domain.
parts=(3,3,5)
actual_k335=mixed_dimension_direct(parts)
assert actual_k335==10

print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('vertex_subsets_checked =',subsets)
print('orders = 2..10')
print('definition-level mixed codes matched the complement classification')
print('all enumerator coefficients matched')
print('K_{3,3,5} direct mixed metric dimension =',actual_k335)
print('2022 Theorem 5 claimed value for K_{3,3,5} =',sum(parts)-len(parts))
