"""Finite direct check of two-distance visibility in 3-factor Hamming graphs.
Pure Python 3, stdlib only. The infinite theorem rests on the proof, not tests.
"""
from itertools import product, combinations
from collections import Counter


def dist(u,v):
    return sum(a != b for a,b in zip(u,v))


def maximal_diameter_two_cliques(points):
    n=len(points)
    adj=[sum(1<<j for j,y in enumerate(points) if i!=j and dist(x,y)<=2)
         for i,x in enumerate(points)]
    result=[]
    def rec(r,p,x):
        if not(p|x):
            result.append(r)
            return
        union=p|x
        pivot=max((k for k in range(n) if union>>k&1),key=lambda k:(p&adj[k]).bit_count())
        cand=p & ~adj[pivot]
        while cand:
            vbit=cand & -cand
            v=vbit.bit_length()-1
            rec(r|vbit,p&adj[v],x&adj[v])
            p &=~vbit; x|=vbit; cand &=~vbit
    rec(0,(1<<n)-1,0)
    return result


def direct_visible(s):
    for x,y in combinations(s,2):
        d=dist(x,y)
        if d>2: return False
        if d==2:
            i,j=[k for k in range(3) if x[k]!=y[k]]
            u=list(x);u[i]=y[i]
            v=list(x);v[j]=y[j]
            if tuple(u) in s and tuple(v) in s:return False
    return True


def in_classification(s,points):
    for fixed in range(3):
        if len({x[fixed] for x in s})<=1:
            i,j=[k for k in range(3) if k!=fixed]
            for x,y in combinations(s,2):
                if x[i]!=y[i] and x[j]!=y[j]:
                    u=list(x);u[i]=y[i]
                    v=list(x);v[j]=y[j]
                    if tuple(u) in s and tuple(v) in s:return False
            return True
    for center in points:
        if all(dist(x,center)<=1 for x in s):return True
    for a in points:
        for b in points:
            if dist(a,b)!=3:continue
            tetra={x for x in points if
                   all(x[i] in (a[i],b[i]) for i in range(3)) and
                   sum(x[i]==a[i] for i in range(3))%2==1}
            if s<=tetra:return True
    return False


def verify(shape):
    points=list(product(*(range(n) for n in shape)))
    cliques=maximal_diameter_two_cliques(points)
    subsets={0}
    for clique in cliques:
        mask=clique
        while mask:
            subsets.add(mask);mask=(mask-1)&clique
    count=Counter()
    for m in subsets:
        s=frozenset(points[i] for i in range(len(points)) if m>>i&1)
        got=direct_visible(s)
        predicted=in_classification(s,points)
        assert got==predicted,(shape,s,got,predicted)
        if got:count[len(s)]+=1
    maximum=max(count)
    print(shape,'diameter2_candidates',len(subsets),'valid',sum(count.values()),
          'maximum',maximum,'number_of_maxima',count[maximum])
    return maximum,count[maximum]

if __name__=='__main__':
    expected={(2,2,2):(4,10),(2,2,3):(5,12),(2,3,3):(6,30),
              (3,3,3):(7,27),(2,3,4):(7,168),(3,3,4):(8,36)}
    for shape,answer in expected.items():assert verify(shape)==answer
    print('ALL_FINITE_CHECKS_OK')
