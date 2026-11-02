"""Exact finite checks for a uniform binary-search-tree record/leaf theorem."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

def rank_code(values):
    return [sum(x <= values[j] for x in values[:j+1]) for j in range(len(values))]

def actual_bst(values):
    """Insert key indices in order of increasing priority, then inspect depth and leaves."""
    n = len(values)
    left=[-1]*n
    right=[-1]*n
    root=min(range(n),key=lambda k:values[k])
    for j in sorted(range(n),key=lambda k:values[k]):
        if j==root:continue
        k=root
        while True:
            arr=left if j<k else right
            if arr[k]<0:
                arr[k]=j
                break
            k=arr[k]
    dep=0
    k=root
    while k!=0:
        k=left[k]
        assert k>=0
        dep+=1
    leaf=[int(left[k]<0 and right[k]<0) for k in range(n)]
    return dep,leaf

def vectors(values):
    n=len(values)
    a=[0]+[int(values[k]==min(values[:k+1])) for k in range(1,n)]
    b=[int(values[0]>values[1])]+[int(values[i]>values[i-1] and values[i]>values[i+1]) for i in range(1,n-1)]+[int(values[-1]>values[-2])]
    ranks=rank_code(values)
    b_from_rank=[int(ranks[1]==1)]+[int(ranks[i]>ranks[i-1] and ranks[i+1]<=ranks[i]) for i in range(1,n-1)]+[int(ranks[-1]>ranks[-2])]
    assert b==b_from_rank
    assert actual_bst(values)==(sum(a),b)
    return sum(a),b

def covariance_expected(n,i):
    if i==1:return F(1,4)
    if i==2:return F(-1,9)
    if i==n:return F(-1,2*n*(n-1))
    return F(-2,3*i*(i-1)*(i+1))

def exhaust(n):
    count=factorial(n)
    freqs=[{} for i in range(n)]
    allhist={}
    nsum=[0]*n
    dsum=0
    joint=[0]*n
    for values in permutations(range(n)):
        d,b=vectors(values)
        dsum+=d
        allhist[d]=allhist.get(d,0)+1
        for i,flag in enumerate(b):
            if flag:
                nsum[i]+=1
                joint[i]+=d
                f=freqs[i];f[d]=f.get(d,0)+1
    for i in range(1,n+1):
        cov=F(joint[i-1],count)-F(dsum*nsum[i-1],count*count)
        assert cov==covariance_expected(n,i),(n,i,cov,covariance_expected(n,i))
        # All integer upper-tail thresholds, with strictness in at least one
        direction=1 if i==1 else -1
        strict=False
        for threshold in range(n):
            c_tail=F(sum(v for k,v in freqs[i-1].items() if k>=threshold),nsum[i-1])
            u_tail=F(sum(v for k,v in allhist.items() if k>=threshold),count)
            assert direction*(c_tail-u_tail)>=0,(n,i,threshold,c_tail,u_tail)
            strict|=direction*(c_tail-u_tail)>0
        assert strict
    global_cov=sum((covariance_expected(n,i) for i in range(1,n+1)),F(0))
    assert global_cov==F((n-2)*(n+1),12*n*(n-1))
    return len(list(range(n)))*n

def local_moment_checks():
    for i in range(3,81):
        denom=(i-1)*i*(i+1)
        mass=F(0)
        pprev=F(0);pnext=F(0);pboth=F(0)
        for a in range(1,i):
            for b in range(1,i+1):
                if b<=a:continue
                for c in range(1,i+2):
                    if c>b:continue
                    weight=F(1,denom)
                    mass+=weight
                    pprev+=weight*(a==1)
                    pnext+=weight*(c==1)
                    pboth+=weight*(a==1 and c==1)
        assert mass==F(1,3)
        assert pprev/mass+pnext/mass-pboth/mass==F(3,i+1)
        assert pboth/mass==F(3,i*(i+1))
        assert F(3*i-2,i*(i-1)*(i+1))-F(3,i*(i+1))==F(1,i*(i-1)*(i+1))
    for n in range(3,200):
        assert sum((covariance_expected(n,i) for i in range(1,n+1)),F())==F((n-2)*(n+1),12*n*(n-1))

if __name__=='__main__':
    local_moment_checks()
    for n in range(3,9):
        exhaust(n)
    print('PASS: n=3..8 all insertion permutations, every leaf-position covariance, every conditional upper tail, direct BST construction, rank-coded identities; n=3..199 exact global identities; i=3..80 exact local factorial enumerations.')
