#!/usr/bin/env python3
"""Exhaustive and sampled verification of iterative hedged contraction semantics.

The formula being contracted is diamond_a(not p). A state consists of n
successor bitmasks and a truth mask P for p. All operations are exact.
"""
import itertools
import random

def update(rows,p,n):
    U=(1<<n)-1
    A=sum((1<<u) for u in range(n) if not(rows[u] & (U^p)))
    return tuple(row if row&A else row|A for row in rows), A

def test(rows,p,n):
    rows=tuple(rows); orig=rows
    A0=sum((1<<u) for u in range(n) if not(rows[u] & (((1<<n)-1)^p)))
    H=tuple(row&A0 for row in rows)
    count=0; statuses=[]; bound=0
    for step in range(n+2):
        new,A=update(rows,p,n)
        statuses.append(A)
        if A & ~p:
            predicted=sum((1<<u) for u in range(n) if (A&(1<<u)) and (H[u]&A))
            Anew=sum((1<<u) for u in range(n) if not(new[u] & (((1<<n)-1)^p)))
            assert Anew==predicted,(n,orig,p,rows,A,Anew,predicted)
        if new==rows:
            assert count<=n,('too many',n,orig,p,count)
            return count
        count+=1; rows=new
    raise AssertionError(('nonterminating',n,orig,p))

def path(n):
    # world 0 is not p; worlds 1,...,n-1 satisfy p;
    # successor relation is 0->1->...->n-1, with terminal row empty.
    p=((1<<n)-1)^1
    rows=tuple((1<<(i+1)) if i+1<n else 0 for i in range(n))
    count=test(rows,p,n)
    assert count==n,(n,count)
    return count

def multi_update(agents,p,n):
    U=(1<<n)-1
    a_rows=agents[0]
    A=sum((1<<u) for u in range(n) if not(a_rows[u] & (U^p)))
    nxt=tuple(tuple(row if row&A else row|A for row in rs) for rs in agents)
    return nxt,A

def multi_test(agents,p,n):
    original=agents;agents=tuple(tuple(x) for x in agents)
    A0=sum((1<<u) for u in range(n) if not(agents[0][u] & (((1<<n)-1)^p)))
    H=tuple(row&A0 for row in agents[0])
    count=0
    for t in range(n+2):
        nxt,A=multi_update(agents,p,n)
        if A&~p:
            predicted=sum((1<<u) for u in range(n) if A&(1<<u) and H[u]&A)
            newA=sum((1<<u) for u in range(n) if not(nxt[0][u] & (((1<<n)-1)^p)))
            assert predicted==newA,(original,p,n,t)
        if nxt==agents:
            assert count<=n,(n,original,p,count)
            return count
        count+=1;agents=nxt
    raise AssertionError(('multi nonterminating',n,original,p))

def main():
    total=0; maxes={}
    for n in range(1,4):
        N=1<<n; ma=0
        for rows in itertools.product(range(N),repeat=n):
            for p in range(N):
                v=test(rows,p,n);ma=max(ma,v);total+=1
        assert ma==n,(n,ma)
        maxes[n]=ma
    rng=random.Random(20261011)
    for n,k in [(4,20000),(5,20000),(6,10000)]:
        ma=0
        for _ in range(k):
            rows=tuple(rng.randrange(1<<n) for _ in range(n));p=rng.randrange(1<<n)
            ma=max(ma,test(rows,p,n));total+=1
        maxes[n]=ma
    # Multi-agent: exhaustive two-agent models on one and two worlds,
    # then random tests of up to four agents on larger worlds.
    multi_exhaustive=0
    for n in range(1,3):
        N=1<<n
        for r0 in itertools.product(range(N),repeat=n):
            for r1 in itertools.product(range(N),repeat=n):
                for p in range(N):
                    multi_test((r0,r1),p,n);multi_exhaustive+=1
    for n,k in [(3,12000),(4,12000),(5,6000)]:
        for _ in range(k):
            agents=tuple(tuple(rng.randrange(1<<n) for _ in range(n)) for __ in range(4))
            multi_test(agents,rng.randrange(1<<n),n)
    for n in range(1,30):path(n)
    # Depth-zero truth sets are fixed throughout model updates, so there is
    # never a second strict update; enumerate that statement for small n.
    propositional=0
    for n in range(1,4):
        N=1<<n
        for rows in itertools.product(range(N),repeat=n):
            for truth_set in range(N):
                A=(N-1)^truth_set
                one=tuple(row if row&A else row|A for row in rows)
                two=tuple(row if row&A else row|A for row in one)
                assert two==one
                propositional+=1
    print('VERIFY_OK exhaustive_single=%d sampled_single=50000 exhaustive_multi=%d sampled_multi=30000 propositional_cases=%d sharp_paths=29 observed_maxima=%s' % (total-50000,multi_exhaustive,propositional,maxes))

if __name__=='__main__':main()
