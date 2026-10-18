from math import comb
from itertools import product
from collections import Counter

def partitions(n):
    a=[0]*n
    def rec(i,k):
        if i==n:
            yield a[:]
            return
        for v in range(k+2):
            a[i]=v
            yield from rec(i+1,max(k,v))
    if n:
        a[0]=0
        yield from rec(1,0)
    else:
        yield []

def schur(a,n):
    cmax=max(a)+1
    rows=[[0,0] for _ in range(cmax)]
    cols=[[0]*n for _ in range(cmax)]
    cells=[[] for _ in range(cmax)]
    for idx,cc in enumerate(a):
        row,col=divmod(idx,n)
        rows[cc][row]+=1
        cols[cc][col]+=1
        cells[cc].append((row,col))
    for c in range(cmax):
        for d in range(cmax):
            for E in cells:
                if any(rows[c][row]*cols[d][col] != rows[c][E[0][0]]*cols[d][E[0][1]] for row,col in E):
                    return False
    return True

def check(n):
    count=Counter()
    for p in partitions(2*n):
        if schur(p,n):
            typ='R' if any(sum(1 for v in p[:n] if v==j)!=sum(1 for v in p[n:] if v==j) for j in set(p)) else 'B'
            count[typ]+=1
    return count

def wt(k):return 1+(comb(k,k//2)//2 if k%2==0 else 0)
def weighted(n):
    v=[1]
    for i in range(1,n+1):
        v.append(sum(comb(i-1,k-1)*wt(k)*v[i-k] for k in range(1,i+1)))
    return v[n]
def bells(n):
    b=[1]
    for i in range(1,n+1):b.append(sum(comb(i-1,k-1)*b[i-k] for k in range(1,i+1)))
    return b[n]
if __name__=='__main__':
    for n in range(1,6):
        actual=check(n)
        expected={'R':bells(n),'B':weighted(n)}
        assert actual==expected, (n,actual,expected)
        print(n,actual,'total',sum(actual.values()),'OK',flush=True)

def automorphic_partition_check(p,n):
    # Construct a subgroup of S_2 x S_n via elementary column swaps and a simultaneous row flip.
    cmax=max(p)+1
    balanced=all(p[:n].count(c)==p[n:].count(c) for c in range(cmax))
    parents=list(range(2*n))
    def root(z):
        while parents[z]!=z:
            parents[z]=parents[parents[z]]
            z=parents[z]
        return z
    def union(a,b):parents[root(a)]=root(b)
    def add_action(flipped, perm):
        for r in range(2):
            for j in range(n):
                union(r*n+j,((1-r) if flipped else r)*n+perm[j])
    if not balanced:
        groups={}
        for j in range(n):
            groups.setdefault((p[j],p[n+j]),[]).append(j)
        for js in groups.values():
            for j in js[1:]:
                pm=list(range(n));pm[js[0]],pm[j]=pm[j],pm[js[0]]
                add_action(False,pm)
    else:
        groups={}
        for j in range(n):
            group=tuple(sorted((p[j],p[n+j])))
            orient=0 if p[j]==group[0] else 1
            groups.setdefault((group,orient),[]).append(j)
        for js in groups.values():
            for j in js[1:]:
                pm=list(range(n));pm[js[0]],pm[j]=pm[j],pm[js[0]]
                add_action(False,pm)
        tau=list(range(n))
        for (group,orient),js in groups.items():
            if group[0]!=group[1] and orient==0:
                ks=groups[(group,1)]
                assert len(js)==len(ks)
                for j,k in zip(js,ks):tau[j],tau[k]=k,j
        add_action(True,tau)
    classes={}
    for idx,tag in enumerate(p): classes.setdefault(root(idx),set()).add(tag)
    return all(len(v)==1 for v in classes.values()) and len(classes)==len(set(p))

if __name__ == '__main__':
    for n in range(1,6):
        total=0
        for p in partitions(2*n):
            if schur(p,n):
                assert automorphic_partition_check(p,n),(n,p)
                total+=1
        print('AUTOMORPHIC_OK',n,total,flush=True)
