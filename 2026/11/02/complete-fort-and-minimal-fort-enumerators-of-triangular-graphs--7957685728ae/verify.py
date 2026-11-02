#!/usr/bin/env python3
"""Direct finite checks for the fort enumerator of triangular graphs.

Uses direct edge-adjacency tests, separate from the proof's degree criterion.
"""
from math import comb, factorial
from collections import Counter

def mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): C[i+j]+=a*b
    return C

def add(A,B,fac=1):
    N=max(len(A),len(B));return [(A[i] if i<len(A) else 0)+fac*(B[i] if i<len(B) else 0) for i in range(N)]

def binomial_pow(k):return [comb(k,j) for j in range(k+1)]

def no_degree_one(n):
    out=[0]*(comb(n,2)+1)
    for s in range(n+1):
        r=n-s; P=binomial_pow(comb(r,2))
        for k in range(s//2+1):
            t=s-2*k
            if r==0 and t>0:continue
            coeff=(-1)**s*comb(n,s)*factorial(s)//(2**k*factorial(k)*factorial(t))*(r**t)
            for j,p in enumerate(P):out[s-k+j]+=coeff*p
    return out

def no_isolates(n):
    out=[0]*(comb(n,2)+1)
    for i in range(n+1):
        c=(-1)**i*comb(n,i)
        for j,p in enumerate(binomial_pow(comb(n-i,2))):out[j]+=c*p
    return out

def predicted(n):
    f=no_degree_one(n);g=no_isolates(n);h=[0]*len(f)
    for i in range(n+1):
        c=(-1)**i*comb(n,i)
        for j,x in enumerate(no_degree_one(n-i)):h[j]+=c*x
    ret=[f[j]+g[j]-h[j] for j in range(len(f))];ret[0]-=1
    return ret

def predicted_minimal(n):
    sf=[[1]]
    for N in range(1,n+1):
        out=[0]*(comb(N,2)+1)
        for j in range(2,N+1):
            multiplicity=1 if j==2 else j
            factor=comb(N-1,j-1)*multiplicity
            for k,val in enumerate(sf[N-j]):out[k+j-1]+=factor*val
        sf.append(out)
    ans=sf[n][:]
    for ell in range(3,n):
        ans[ell]+=comb(n,ell)*factorial(ell-1)//2
    return ans

def brute(n):
    root=[(i,j) for i in range(n) for j in range(i+1,n)]
    m=len(root); neighbors=[]
    for i,(a,b) in enumerate(root):
        neighbors.append(sum(1<<j for j,(c,d) in enumerate(root) if i!=j and (a==c or a==d or b==c or b==d)))
    fort=bytearray(1<<m); counts=Counter(); min_counts=Counter(); classfails=0
    for mask in range(1,1<<m):
        good=True
        for j in range(m):
            if mask>>j&1:continue
            if (neighbors[j]&mask).bit_count()==1:
                good=False;break
        if not good:continue
        fort[mask]=True; k=mask.bit_count();counts[k]+=1
        deg=[0]*n
        for j,(a,b) in enumerate(root):
            if mask>>j&1:deg[a]+=1;deg[b]+=1
        # Independently test the structural degree criterion on every fort.
        if not (0 not in deg or 1 not in deg):raise AssertionError(('criterion',n,mask,deg))
    has_fort_sub=bytearray(1<<m)
    for mask in range(1,1<<m):
        leastbit=mask&-mask
        prev=mask^leastbit
        has_fort_sub[mask]=int(bool(fort[prev] or has_fort_sub[prev]))
        # Also propagate through all other immediate submasks to avoid missing a fort.
        t=prev
        while t and not has_fort_sub[mask]:
            bit=t&-t
            sub=mask^bit
            if fort[sub] or has_fort_sub[sub]:has_fort_sub[mask]=1
            t-=bit
    for mask in range(1,1<<m):
        if not fort[mask] or has_fort_sub[mask]:continue
        k=mask.bit_count();min_counts[k]+=1
        deg=[0]*n
        for j,(a,b) in enumerate(root):
            if mask>>j&1:deg[a]+=1;deg[b]+=1
        if min(deg)>=1:
            if any(min(deg[a],deg[b])!=1 for j,(a,b) in enumerate(root) if mask>>j&1):classfails+=1
        else:
            used=[v for v in range(n) if deg[v]>0]
            if 1 in deg or len(used)<3 or len(used)!=k or any(deg[v]!=2 for v in used):classfails+=1
    if classfails:raise AssertionError(('classification',n,classfails))
    return counts,min_counts

for n in range(2,8):
    expected=predicted(n); counts, min_counts=brute(n)
    actual=[counts[i] for i in range(len(expected))]
    minimal_predicted=predicted_minimal(n)
    minimal_actual=[min_counts[i] for i in range(len(minimal_predicted))]
    assert minimal_predicted==minimal_actual, ('minimal polynomial mismatch',n,minimal_predicted,minimal_actual)
    assert actual==expected, ('polynomial mismatch',n,actual,expected)
    least=min(min_counts)
    expected_least={2:(1,1),3:(2,3),4:(2,3),5:(3,40),6:(3,35)}
    if n>=7:expected_least[n]=(3,comb(n,3))
    assert (least,min_counts[least])==expected_least[n], (n,least,min_counts)
    print(f'n={n} vertices={comb(n,2)} forts={sum(counts.values())} min_size={least} min_count={min_counts[least]} support={[(k,c) for k,c in counts.items() if c and k<=4]}',flush=True)
print('VERIFY_OK')
