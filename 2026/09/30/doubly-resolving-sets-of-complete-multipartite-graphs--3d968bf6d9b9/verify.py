from itertools import combinations

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n+1):
        for rest in partitions(n-a, a):
            yield (a,)+rest

def structure(sizes):
    parts=[]; part_of={}; v=0
    for i,n in enumerate(sizes):
        P=list(range(v,v+n)); parts.append(P)
        for x in P: part_of[x]=i
        v += n
    return parts,part_of

def d(u,v,part_of):
    if u==v: return 0
    return 2 if part_of[u]==part_of[v] else 1

def direct_drs(mask,sizes):
    N=sum(sizes); parts,part_of=structure(sizes)
    W=[v for v in range(N) if mask>>v & 1]
    if len(W)<2: return False
    for u in range(N):
        for v in range(u+1,N):
            vals={d(u,w,part_of)-d(v,w,part_of) for w in W}
            if len(vals)<2: return False
    return True

def classified_drs(mask,sizes):
    N=sum(sizes); parts,_=structure(sizes)
    W={v for v in range(N) if mask>>v & 1}
    if len(W)<2: return False
    m=[sum(v in W for v in P) for P in parts]
    for n_i,m_i in zip(sizes,m):
        if n_i>=2 and m_i<n_i-1:
            return False
    support=[i for i,x in enumerate(m) if x>0]
    t=len(support)
    if t>=3:
        return len(sizes)-t <= 1
    if t==2:
        i,j=support
        if len(sizes)-t>1: return False
        if m[i]<sizes[i] and m[j]<2: return False
        if m[j]<sizes[j] and m[i]<2: return False
        return True
    if t==1:
        i=support[0]
        if len(sizes)!=2: return False
        j=1-i
        return sizes[j]==1 and m[j]==0 and m[i]==sizes[i] and m[i]>=2
    return False

def psi_formula(sizes):
    N=sum(sizes)
    nons=[n for n in sizes if n>=2]
    p=len(nons); s=len(sizes)-p
    if p==0: return max(N-1,2)
    if p==1:
        return N-2 if s>=3 else N-1
    if p==2:
        a,b=nons
        if s>=2: return N-3
        if s==1: return N-3 if min(a,b)>=3 else N-2
        return N-2 if min(a,b)>=3 else N-1
    return N-p-(1 if s else 0)

def basis_count_formula(sizes):
    N=sum(sizes)
    nons=[n for n in sizes if n>=2]
    p=len(nons); s=len(sizes)-p
    if p==0: return 1 if N==2 else N
    if p==1:
        a=nons[0]
        if s==1: return 1
        if s==2: return N
        return a*s
    if p==2:
        a,b=nons
        if s==0: return N if min(a,b)==2 else a*b
        if s==1: return a*b+a+b if min(a,b)==2 else a*b
        return a*b*s
    prod=1
    for n in nons: prod*=n
    return prod*(s if s else 1)

types=subsets=class_checks=min_checks=count_checks=0
for N in range(2,9):
    for sizes in partitions(N):
        if len(sizes)<2: continue
        types += 1
        direct=[]
        for mask in range(1<<N):
            a=direct_drs(mask,sizes)
            b=classified_drs(mask,sizes)
            subsets += 1; class_checks += 1
            assert a==b, (sizes,mask,a,b)
            if a: direct.append(mask)
        optimum=min(mask.bit_count() for mask in direct)
        bases=sum(mask.bit_count()==optimum for mask in direct)
        assert optimum==psi_formula(sizes), (sizes,optimum,psi_formula(sizes))
        assert bases==basis_count_formula(sizes), (sizes,bases,basis_count_formula(sizes))
        min_checks += 1; count_checks += 1
print(f'TYPES={types}')
print(f'SUBSETS={subsets}')
print(f'CLASSIFICATION_CHECKS={class_checks}')
print(f'MINIMUM_CHECKS={min_checks}')
print(f'BASIS_COUNT_CHECKS={count_checks}')
print('VERIFY_OK')
