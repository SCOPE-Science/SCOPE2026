import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def dominates(mask,L):
    n=len(L)
    if mask==0: return False
    for v in range(n):
        if (mask>>v)&1: continue
        if not any(((mask>>u)&1) and L[u]!=L[v] for u in range(n)):
            return False
    return True

def certified(mask,L):
    if not dominates(mask,L): return False
    n=len(L)
    for v in range(n):
        if not ((mask>>v)&1): continue
        outnbr=sum(1 for u in range(n)
                   if not ((mask>>u)&1) and L[u]!=L[v])
        if outnbr==1: return False
    return True

def profile_criterion(mask,parts):
    L=labels(parts)
    d=[0]*len(parts)
    for v,i in enumerate(L):
        if (mask>>v)&1: d[i]+=1
    support=sum(x>0 for x in d)
    dom=(support>=2) or (support==1 and any(d[i]==parts[i] and d[i]>0
                                           for i in range(len(parts))))
    if not dom: return False
    c=[parts[i]-d[i] for i in range(len(parts))]
    q=sum(c)
    return all(q-c[i] != 1 for i,x in enumerate(d) if x>0)

def formula(parts):
    N=sum(parts); r=len(parts)
    coeff=[math.comb(N,k) for k in range(N+1)]
    for ni in parts:
        for k in range(ni+1):
            coeff[k]-=math.comb(ni,k)
    coeff[0]+=r-1
    for ni in parts:
        coeff[ni]+=1

    coeff[N-1]-=N

    for ni in parts:
        outside=N-ni
        if outside>=2:
            for k in range(1,ni):
                coeff[N-k-1]-=outside*math.comb(ni,k)

    for i in range(r):
        for j in range(i+1,r):
            if parts[i]>=2 and parts[j]>=2:
                coeff[N-2]+=parts[i]*parts[j]
    return coeff

def paper_K3n(n):
    N=n+3
    c=[0]*(N+1)
    c[2]=3*n
    for i in range(3,n):
        c[i]=3*math.comb(n,i-1)+math.comb(n,i-3)
    c[n]=math.comb(n,n-3)+1
    c[n+1]=math.comb(n,n-2)+3
    c[n+3]=1
    return c

types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            L=labels(parts)
            actual=[0]*(N+1)
            for mask in range(1<<N):
                subsets+=1
                got=certified(mask,L)
                assert got==profile_criterion(mask,parts)
                if got:
                    actual[mask.bit_count()]+=1
            assert actual==formula(parts)
            types+=1

for n in range(3,11):
    assert formula((3,n))==paper_K3n(n)

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("all-set profile criterion matched")
print("all polynomial coefficients matched")
print("K_{3,n} specialization matched the 2025 theorem for n = 3..10")
