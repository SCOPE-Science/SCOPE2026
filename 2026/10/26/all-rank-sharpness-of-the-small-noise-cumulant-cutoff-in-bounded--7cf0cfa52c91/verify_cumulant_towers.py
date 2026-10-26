"""Exact rational truncated-cumulant versus labelled-tree verification."""
from fractions import Fraction as Q
from itertools import combinations,product
from math import factorial

def partitions(items):
    if not items:
        yield ()
        return
    h,*tail=items
    for p in partitions(tail):
        yield ((h,),)+p
        for j in range(len(p)):
            yield p[:j]+(tuple(sorted((h,)+p[j])),)+p[j+1:]

def epoly(a,d):
    return [Q(a**k, factorial(k)) for k in range(d+1)]

def mul(a,b,d):
    out=[Q(0)]*(d+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=d:out[i+j]+=x*y
    return out

def exact_coeff(indices,C):
    r=len(indices); d=r-1
    answer=Q(0)
    for part in partitions(list(range(r))):
        weight=Q((-1)**(len(part)-1)*factorial(len(part)-1))
        f=[Q(1)]+[Q(0)]*d
        for block in part:
            pair_cov=sum((C[indices[a]][indices[b]] for a,b in combinations(block,2)),0)
            f=mul(f,epoly(pair_cov,d),d)
        answer+=weight*f[d]
    return answer

def connected_tree_coeff(indices,C):
    r=len(indices)
    if r==2:return Q(C[indices[0]][indices[1]])
    ans=Q(0)
    # Prufer sequences generate every labelled tree exactly once.
    for seq in product(range(r),repeat=r-2):
        deg=[1]*r
        for v in seq:deg[v]+=1
        prodw=Q(1)
        for v in seq:
            leaf=next(i for i in range(r) if deg[i]==1)
            prodw*=C[indices[leaf]][indices[v]]
            deg[leaf]-=1;deg[v]-=1
        a,b=[i for i in range(r) if deg[i]==1]
        prodw*=C[indices[a]][indices[b]]
        ans+=prodw
    return ans

def run():
    matrices=[[[1]],[[1,1],[1,2]],[[2,1,1],[1,3,1],[1,1,4]],[[2,-1],[-1,2]]]
    tests=0
    for C in matrices:
        n=len(C)
        for r in range(2,7 if n<3 else 6):
            for v in combinations(range(n+r-1),r):
                # nondecreasing multi-indices (avoid permutations)
                ind=tuple(x-i for i,x in enumerate(v))
                a=exact_coeff(ind,C);b=connected_tree_coeff(ind,C)
                assert a==b,(C,r,ind,a,b)
                if n==1: assert a == Q(r**(r-2))
                if n>1 and all(C[i][j]>0 for i in range(n) for j in range(n)):assert a>0
                tests+=1
    print(f'PASS {tests} exact scalar/multivariate coefficient comparisons; Cayley coefficients all ranks checked')
if __name__=='__main__':run()
