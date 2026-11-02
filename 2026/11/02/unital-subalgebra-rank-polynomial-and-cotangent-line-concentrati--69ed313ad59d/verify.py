"""Independent finite enumeration of unital subalgebras of truncated symmetric rings.
Run: python verify.py. No external packages are needed.
"""
from itertools import combinations, product
from collections import Counter

def gauss(n,k,q):
    if k<0 or k>n:return 0
    num=1;den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(i+1)-1
    return num//den

def predicted(d,q):
    D=d*(d+1)//2
    counts=Counter()
    strata=Counter()
    for s in range(d+1):
        e=s*(s+1)//2
        for r in range(e,D+1):
            n=gauss(d,s,q)*gauss(D-e,r-e,q)*q**(s*(D-r))
            counts[1+s+r]+=n;strata[s]+=n
    return counts,strata

def rank(vectors,q):
    arr=[list(x) for x in vectors]
    if not arr:return 0
    n=len(arr[0]); pivot=0
    for j in range(n):
        w=next((i for i in range(pivot,len(arr)) if arr[i][j]%q),None)
        if w is None:continue
        arr[pivot],arr[w]=arr[w],arr[pivot]
        inv=pow(arr[pivot][j]%q,-1,q)
        arr[pivot]=[(a*inv)%q for a in arr[pivot]]
        for i in range(len(arr)):
            if i!=pivot and arr[i][j]:
                a=arr[i][j]
                arr[i]=[(v-a*u)%q for v,u in zip(arr[i],arr[pivot])]
        pivot+=1
        if pivot==len(arr):break
    return pivot

def subspace_bases(n,k,q):
    for pivots in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(pivots[i]+1,n) if j not in pivots]
        for vals in product(range(q),repeat=len(free)):
            mat=[[0]*n for _ in range(k)]
            for i,j in enumerate(pivots):mat[i][j]=1
            for (i,j),x in zip(free,vals):mat[i][j]=x
            yield mat

def verify(d,q):
    assert q in (2,3), "direct RREF enumeration uses prime fields 2 and 3"
    D=d*(d+1)//2;n=d+D
    monoms=list(combinations(range(d),2))
    sq=[(i,i) for i in range(d)] + monoms
    sq.sort()
    predicted_counts,predicted_strata=predicted(d,q)
    found=Counter();fs=Counter();subsp=0
    for k in range(n+1):
        for rows in subspace_bases(n,k,q):
            subsp+=1
            closure=True
            for a in rows:
                for b in rows:
                    w=[0]*d + [(a[i]*b[j] + (a[j]*b[i] if i!=j else 0))%q for i,j in sq]
                    if rank(rows+[w],q)!=k:
                        closure=False;break
                if not closure:break
            if closure:
                found[k+1]+=1
                fs[rank([u[:d] for u in rows],q)]+=1
    assert found==predicted_counts,(d,q,found,predicted_counts)
    assert fs==predicted_strata,(d,q,fs,predicted_strata)
    expected_subspaces=sum(gauss(n,k,q) for k in range(n+1))
    assert subsp==expected_subspaces,(subsp,expected_subspaces)
    print('DIRECT_ENUM_OK',d,q,'subspaces',subsp,'unital_subalgebras',sum(found.values()),'dimension_profile',sorted(found.items()),'cotangent_profile',sorted(fs.items()))

if __name__=='__main__':
    for d,q in [(1,2),(1,3),(2,2),(2,3)]:verify(d,q)
    for d,q in [(3,2),(3,3),(4,2),(5,2)]:
        C,S=predicted(d,q)
        print('FORMULA_PROFILE',d,q,'total',sum(C.values()),'cotangent',sorted(S.items()))
    print('VERIFY_OK')
