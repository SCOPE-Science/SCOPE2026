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

def dominates(mask,L):
    n=len(L)
    for v in range(n):
        if (mask>>v)&1:
            continue
        if not any(((mask>>u)&1) and L[u]!=L[v] for u in range(n)):
            return False
    return True

def two_secure(mask,L):
    n=len(L)
    S=[v for v in range(n) if (mask>>v)&1]
    if len(S)<2 or not dominates(mask,L):
        return False
    for u1 in range(n):
        for u2 in range(u1+1,n):
            ok=False
            for v1 in S:
                if not (v1==u1 or L[v1]!=L[u1]):
                    continue
                for v2 in S:
                    if v2==v1:
                        continue
                    if not (v2==u2 or L[v2]!=L[u2]):
                        continue
                    moved=(mask & ~(1<<v1) & ~(1<<v2)) | (1<<u1) | (1<<u2)
                    if dominates(moved,L):
                        ok=True
                        break
                if ok:
                    break
            if not ok:
                return False
    return True

def criterion(mask,parts,L):
    k=mask.bit_count()
    if k<2:
        return False
    selected=[0]*len(parts)
    for v,i in enumerate(L):
        if (mask>>v)&1:
            selected[i]+=1
    return all(k-s >= min(n-s,3) for n,s in zip(parts,selected))

def coeff_formula(parts):
    N=sum(parts)
    a=[0]*(N+1)

    if max(parts)<=2:
        a[2]=math.comb(N,2)

    M=sum(n for n in parts if n<=3)
    if N>=3:
        a[3]=math.comb(M,3)

    if N>=4:
        H=[n for n in parts if n>=5]
        bad=sum(
            math.comb(n,4)
            +(N-n)*math.comb(n,3)
            +math.comb(N-n,2)*math.comb(n,2)
            for n in H
        )
        overlap=sum(
            math.comb(H[i],2)*math.comb(H[j],2)
            for i in range(len(H))
            for j in range(i+1,len(H))
        )
        a[4]=math.comb(N,4)-bad+overlap

    for k in range(5,N+1):
        bad=0
        for n in parts:
            if n>=k+1:
                bad += (
                    math.comb(n,k)
                    +(N-n)*math.comb(n,k-1)
                    +math.comb(N-n,2)*math.comb(n,k-2)
                )
        a[k]=math.comb(N,k)-bad
    return a

types=subsets=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            L=labels(parts)
            actual=[0]*(N+1)
            for mask in range(1<<N):
                subsets += 1
                got=two_secure(mask,L)
                assert got==criterion(mask,parts,L), (parts,mask)
                if got:
                    actual[mask.bit_count()] += 1
            assert actual==coeff_formula(parts), (parts,actual,coeff_formula(parts))
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("definition-level two-attack test matched the structural criterion")
print("all enumerator coefficients matched")
