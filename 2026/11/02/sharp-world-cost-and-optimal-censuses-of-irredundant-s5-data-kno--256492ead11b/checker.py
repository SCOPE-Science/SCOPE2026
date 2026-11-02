"""Independent finite checks of irredundant finite S5 value knowledge.
Run: python checker.py
"""
from itertools import combinations, product
from math import comb, factorial, ceil


def bell(n):
    b=[1]
    for m in range(n):
        b.append(sum(comb(m,j)*b[j] for j in range(m+1)))
    return b[n]


def local_count(q,r,s):
    universe=set(range(q))
    options=[frozenset(c) for c in combinations(range(q),s)]
    count=0
    for tup in product(options,repeat=r):
        if set.intersection(*(set(z) for z in tup)): continue
        if not all(set.intersection(*(set(tup[j]) for j in range(r) if j!=i)) for i in range(r)):
            continue
        count+=1
    return count


def threshold(r,s):
    return ceil(r*s/(r-1))

for r,maxs in [(2,4),(3,5),(4,4),(5,4)]:
    for s in range(r-1,maxs+1):
        q=threshold(r,s)
        assert q>=r
        assert local_count(q-1,r,s)==0,(r,s,q)
        val=local_count(q,r,s)
        assert val>0,(r,s,q)
        # At all optimal models, deficit in the omission multiplicities is <r-1.
        deficit=(r-1)*q-r*s
        assert 0<=deficit<=r-2
        if s%(r-1)==0:
            b=s//(r-1)
            assert q==r*b
            assert val==factorial(q)//factorial(b)**r,(r,s,q,val)
        if r==3:
            b=q-s
            if s%2==0:
                expected=factorial(q)//factorial(b)**3
            else:
                expected=3*factorial(q)//(factorial(b-1)**2*factorial(b))
            assert val==expected,(r,s,q,val,expected)
        print('r,s,q,local_count,global_S5_count=',r,s,q,val,val*bell(q-s)**r)

# Independently enumerate partitions, rather than only subsets, at the smallest 3-agent instance.
def partitions(seq):
    if not seq:
        yield ()
        return
    first,tail=seq[0],seq[1:]
    for p in partitions(tail):
        yield (frozenset((first,)),)+p
        for i in range(len(p)):
            yield p[:i]+(p[i]|{first},)+p[i+1:]

for n,r,k in [(4,3,3),(5,3,4),(4,2,3)]:
    ps=list(partitions(list(range(n))))
    good=[]
    for p in ps:
        c=next(z for z in p if 0 in z)
        if len(c)==k:good.append(c)
    actual=0
    for cells in product(good,repeat=r):
        if len(set.intersection(*(set(c) for c in cells)))!=1:continue
        if any(len(set.intersection(*(set(cells[j]) for j in range(r) if j!=i)))==1 for i in range(r)):
            continue
        actual+=1
    expected=local_count(n-1,r,k-1)*bell(n-k)**r
    assert actual==expected,(n,r,k,actual,expected)
    print('partitions check',n,r,k,actual)
# A separate multivariate coefficient dynamic program checks the general formula.
def coefficient_count(q,r,s):
    b=q-s
    answer=0
    for omit in range(1<<r):
        allowed=[t for t in range(1,1<<r) if not (t.bit_count()==1 and (t&omit))]
        states={(0,)*r:1}
        for _ in range(q):
            nxt={}
            for exp,ways in states.items():
                for t in allowed:
                    e=tuple(exp[i]+((t>>i)&1) for i in range(r))
                    if all(x<=b for x in e):nxt[e]=nxt.get(e,0)+ways
            states=nxt
        sign=-1 if omit.bit_count()%2 else 1
        answer+=sign*states.get((b,)*r,0)
    return answer
for r,s in [(2,1),(2,2),(3,2),(3,3),(4,3)]:
    q=threshold(r,s)
    assert coefficient_count(q,r,s)==local_count(q,r,s),(r,s)
    print('coefficient check',r,s,q)
print('ALL_CHECKS_OK')
