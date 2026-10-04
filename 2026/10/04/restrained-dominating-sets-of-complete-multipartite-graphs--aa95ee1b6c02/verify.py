import math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def restrained(mask,lab):
    n=len(lab)
    for v in range(n):
        if mask>>v & 1: continue
        if not any((mask>>u & 1) and lab[u]!=lab[v] for u in range(n)):
            return False
        if not any((not (mask>>u & 1)) and u!=v and lab[u]!=lab[v] for u in range(n)):
            return False
    return True

def profile(mask,parts):
    lab=labels(parts); s=[0]*len(parts); c=[0]*len(parts)
    for v,p in enumerate(lab):
        if mask>>v & 1: s[p]+=1
        else: c[p]+=1
    return s,c

def criterion(mask,parts):
    n=sum(parts)
    if mask==(1<<n)-1: return True
    s,c=profile(mask,parts)
    ss=sum(x>0 for x in s); cs=sum(x>0 for x in c)
    if cs<2: return False
    if ss>=2: return True
    if ss==1:
        i=next(i for i,x in enumerate(s) if x>0)
        return s[i]==parts[i]
    return False

def formula(parts):
    N=sum(parts); r=len(parts)
    C=[0]*(N+1)
    if r==2:
        a,b=parts
        C[N]=1
        A=[0]*(a+1); B=[0]*(b+1)
        for j in range(1,a): A[j]=math.comb(a,j)
        for j in range(1,b): B[j]=math.comb(b,j)
        for i,x in enumerate(A):
            for j,y in enumerate(B):
                C[i+j]+=x*y
        return C
    for k in range(N+1): C[k]+=math.comb(N,k)
    for ni in parts:
        for k in range(ni+1): C[k]-=math.comb(ni,k)
    C[0]+=r-1
    for ni in parts:
        off=N-ni
        for k in range(ni):
            C[off+k]-=math.comb(ni,k)
    for ni in parts: C[ni]+=1
    return C

def min_formula(parts):
    r=len(parts); N=sum(parts)
    if r==2:
        if min(parts)>=2: return 2,parts[0]*parts[1]
        return N,1
    s=sum(n==1 for n in parts)
    if s: return 1,s
    e=sum(parts[i]*parts[j] for i in range(r) for j in range(i+1,r))
    return 2,e+sum(n==2 for n in parts)

types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts); actual=[0]*(N+1); valid=[]
            for mask in range(1<<N):
                subsets+=1
                got=restrained(mask,lab)
                assert got==criterion(mask,parts)
                if got:
                    actual[mask.bit_count()]+=1
                    valid.append(mask)
            assert actual==formula(parts)
            g=min(m.bit_count() for m in valid)
            cnt=sum(m.bit_count()==g for m in valid)
            assert (g,cnt)==min_formula(parts)
            types+=1
print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("all-set criterion matched direct restrained-domination test")
print("all polynomial coefficients matched")
print("all minimum values and minimum-set counts matched")
