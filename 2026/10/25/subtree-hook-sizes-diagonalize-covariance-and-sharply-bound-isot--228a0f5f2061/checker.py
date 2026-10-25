"""Independent exact linear-extension checks of rooted-tree inertia formulas.

Requires only Python 3. Run: python checker.py
"""
from fractions import Fraction as F
from itertools import permutations, product


def descendants(parent):
    s=[1]*len(parent)
    for v in range(len(parent)-1,0,-1):
        s[parent[v]]+=s[v]
    return s


def ancestors(v,parent):
    out=[]
    while v>=0:
        out.append(v)
        v=parent[v]
    return out[::-1]


def direct_moments(parent):
    """Triangulate the order polytope by linear extensions and integrate each simplex."""
    n=len(parent)
    sums=[0]*n
    pairs=[[0]*n for _ in range(n)]
    count=0
    for perm in permutations(range(n)):
        rank=[0]*n
        for i,v in enumerate(perm):rank[v]=i+1
        if any(rank[parent[v]]>rank[v] for v in range(1,n)):continue
        count+=1
        for v in range(n):
            sums[v]+=rank[v]
            for w in range(n):
                a,b=sorted((rank[v],rank[w]))
                pairs[v][w]+=a*(b+1)
    assert count>0
    vol=F(count,1)
    for k in range(1,n+1):vol/=k
    mean=[F(s,count*(n+1)) for s in sums]
    cov=[[F(pairs[v][w],count*(n+1)*(n+2))-mean[v]*mean[w]
          for w in range(n)] for v in range(n)]
    return vol,mean,cov


def predicted_moments(parent):
    n=len(parent);size=descendants(parent)
    anc=[set(ancestors(v,parent)) for v in range(n)]
    def first(k):return F(k,k+1)
    def second(k):return F(k,k+2)
    def prod(seq):
        r=F(1)
        for z in seq:r*=z
        return r
    means=[1-prod(first(size[a]) for a in anc[v]) for v in range(n)]
    cov=[]
    for v in range(n):
        row=[]
        for w in range(n):
            av,aw=anc[v],anc[w]
            double=prod(second(size[a]) for a in av&aw)
            single=prod(first(size[a]) for a in av^aw)
            prodm=prod(first(size[a]) for a in av)*prod(first(size[a]) for a in aw)
            row.append(double*single-prodm)
        cov.append(row)
    return means,cov


def isotropic_factor(k):
    return F(k**(k+2),(k+1)**2*(k+2)**k)


def check_tree(parent):
    n=len(parent); size=descendants(parent)
    vol,mean,cov=direct_moments(parent)
    pvol=F(1)
    for k in size:pvol/=k
    assert vol==pvol
    m,c=predicted_moments(parent)
    assert mean==m and cov==c
    t=[F(0) if p<0 else F(size[v],size[v]+1) for v,p in enumerate(parent)]
    for v in range(n):
        for w in range(n):
            val=cov[v][w]
            if parent[v]>=0:val-=t[v]*cov[parent[v]][w]
            if parent[w]>=0:val-=t[w]*cov[v][parent[w]]
            if parent[v]>=0 and parent[w]>=0:val+=t[v]*t[w]*cov[parent[v]][parent[w]]
            if v==w:
                q=F(1)
                if parent[v]>=0:
                    for a in ancestors(parent[v],parent):q*=F(size[a],size[a]+2)
                expected=q*F(size[v],(size[v]+1)**2*(size[v]+2))
                assert val==expected, (parent,v,val,expected)
            else:
                assert val==0,(parent,v,w,val)
    factors=F(1)
    for k in size:factors*=isotropic_factor(k)
    low=isotropic_factor(n)*isotropic_factor(1)**(n-1)
    high=F(1)
    for k in range(1,n+1):high*=isotropic_factor(k)
    assert low<=factors<=high
    if n>=3:
        if factors==low:assert all(s==1 for s in size[1:])
        if factors==high:assert all(parent[i]==i-1 for i in range(1,n))
    return n*n+2*n+4


if __name__=='__main__':
    checks=0;trees=0
    for n in range(1,7):
        for ps in product(*(range(v) for v in range(1,n))):
            checks+=check_tree([-1,*ps]);trees+=1
    for parent in [[-1,0,1,2,3,4,5],[-1,0,0,0,0,0,0],[-1,0,0,1,1,2,3]]:
        checks+=check_tree(parent);trees+=1
    print('VERIFY_OK exact_rooted_trees=',trees,'rational_equalities=',checks)
