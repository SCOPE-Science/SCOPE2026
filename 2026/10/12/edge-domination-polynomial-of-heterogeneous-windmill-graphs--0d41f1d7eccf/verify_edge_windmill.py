"""Brute-force and algebraic checks for edge domination on clique windmills."""
from itertools import product
from math import comb
from collections import Counter


def double_factorial(n):
    z = 1
    while n > 0:
        z *= n
        n -= 2
    return z


def add_poly(a, b, sign=1):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += sign * v
    while c and c[-1] == 0: c.pop()
    return c


def multiply(a, b):
    if not a or not b: return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c


def power_one_plus(m):
    return [comb(m, i) for i in range(m+1)]


def exact_zero_isolates(m, center):
    p = []
    for j in range(m+1):
        k = m-j
        e = k * (k-1)//2 + (k if center else 0)
        p=add_poly(p, [comb(m,j)*(-1)**j * q for q in power_one_plus(e)])
    return p


def at_most_one_isolate(m, center):
    p = []
    for t in range(min(1,m)+1):
        z = m-t
        a=[]
        for j in range(z+1):
            k=z-j
            e=k*(k-1)//2+(k if center else 0)
            a=add_poly(a, [comb(z,j)*(-1)**j * q for q in power_one_plus(e)])
        p=add_poly(p,[comb(m,t)*q for q in a])
    return p


def polynomial(ms):
    a=[1];b=[1];c=[1]
    for m in ms:
        a=multiply(a,exact_zero_isolates(m,False))
        b=multiply(b,at_most_one_isolate(m,True))
        c=multiply(c,at_most_one_isolate(m,False))
    return add_poly(add_poly(b,c,-1),a)


def edge_list(ms):
    es=[];center=0;off=1
    for m in ms:
        verts=list(range(off,off+m))
        es.extend((0,v) for v in verts)
        es.extend((verts[i],verts[j]) for i in range(m) for j in range(i+1,m))
        off+=m
    return es


def brute(ms):
    es=edge_list(ms)
    E=len(es)
    if E>19: raise ValueError((ms,E))
    # All edges e are dominated iff at least one endpoint has degree>=1 in selected subgraph.
    incidence=[0]*(sum(ms)+1)
    for i,(u,v) in enumerate(es):
        incidence[u]|=1<<i
        incidence[v]|=1<<i
    undominated_edge_masks=[incidence[u]|incidence[v] for u,v in es]
    counts=Counter()
    valid=0
    for mask in range(1<<E):
        if all(mask & bit for bit in undominated_edge_masks):
            counts[mask.bit_count()]+=1
            valid+=1
    return [counts.get(i,0) for i in range(E+1)],valid


def min_closed(ms):
    L=sum(m//2 for m in ms)
    even=[m for m in ms if m%2==0]
    odd=[m for m in ms if m%2==1]
    if even:
        t=1
        for m in odd: t*=m*double_factorial(m-2)
        pq, pe, pp=1,1,1
        for m in even:
            p=double_factorial(m-1)
            e=m*(m-1)*comb(m-2,2)*double_factorial(m-5) if m>=4 else 0
            q=m*(m-1)*double_factorial(m-3)
            pq*=p+e+q
            pe*=p+e
            pp*=p
        return L,t*(pq-pe)+(pp if not odd else 0)
    ts=[m*double_factorial(m-2) for m in ms]
    us=[]
    for m in ms:
        u1=m*double_factorial(m-2)
        u2=m*(m-1)*double_factorial(m-2)
        u3=m*(m-1)*(m-2)*comb(m-3,2)*double_factorial(m-6) if m>=5 else 0
        u4=m*comb(m-1,2)*double_factorial(m-4) if m>=3 else 0
        us.append(u1+u2+u3+u4)
    num=0
    for i,u in enumerate(us):
        p=u
        for j,t in enumerate(ts):
            if j!=i: p*=t
        num+=p
    return L+1,num


def run():
    for m in range(1,8):
        a=exact_zero_isolates(m,False)
        b=at_most_one_isolate(m,True)
        c=at_most_one_isolate(m,False)
        assert all(z>=0 for z in a+b+c),(m,a,b,c)
    count=0;subsets=0;selected=0
    # All 2-blade tuples up to 4 each; 3-blade up to 3; 4-blade up to 2.
    tuples=[]
    for r, maxm in [(2,4),(3,3),(4,2)]:
        for ms in product(range(1,maxm+1),repeat=r):
            if sum(m*(m+1)//2 for m in ms)<=19: tuples.append(ms)
    for ms in tuples:
        poly=polynomial(ms)
        ans,valid=brute(ms)
        assert ans[:len(poly)] == poly and not any(ans[len(poly):]),(ms,poly,ans)
        assert all(v>=0 for v in poly),(ms,poly)
        mn=min(i for i,a in enumerate(ans) if a)
        c,n=min_closed(ms)
        assert (mn,ans[mn]) == (c,n),(ms,(mn,ans[mn]),(c,n))
        count+=1
        subsets+=1<<len(edge_list(ms))
        selected+=valid
    assert polynomial((1,1,1)) == [0,3,3,1]
    assert polynomial((2,2,2)) == multiply(multiply([0,3,3,1],[0,3,3,1]),[0,3,3,1])
    for r in range(2,6):
        for ms in product(range(1,6),repeat=r):
            if r>=4 and max(ms)>=4: continue
            c,n=min_closed(ms)
            poly=polynomial(ms)
            assert next(i for i,a in enumerate(poly) if a)==c,(ms,'minimum',c)
            assert poly[c]==n,(ms,'mincount',n,poly[c])
    print('VERIFY_OK local_sizes=1..7 exhaustive_tuples=%d brute_edge_subsets=%d dominated_sets=%d algebraic_tuples=2..5 blades max_size=5 max_edges=19' % (count,subsets,selected))

if __name__=='__main__': run()
