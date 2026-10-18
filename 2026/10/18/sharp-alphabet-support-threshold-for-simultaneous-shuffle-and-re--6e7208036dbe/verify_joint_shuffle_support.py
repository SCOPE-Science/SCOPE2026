"""Finite checks for the common-support theorem for shuffle squares and reverse shuffle squares.

Run: python verify_joint_shuffle_support.py
Requires Python 3.9+ standard library only. No external data.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def nonnest(n):
    """All non-nesting perfect matchings, by a FIFO arch sweep."""
    queue, arcs = [], []
    def walk(t):
        if t == 2*n:
            if not queue:
                yield tuple(arcs)
            return
        if len(queue) < n:
            queue.append(t)
            yield from walk(t+1)
            queue.pop()
        if queue:
            a = queue.pop(0)
            arcs.append((a,t))
            yield from walk(t+1)
            arcs.pop()
            queue.insert(0,a)
    yield from walk(0)


def avoid123(n):
    """All permutations having no increasing subsequence of length three."""
    def walk(a, remaining):
        if not remaining:
            yield tuple(a)
            return
        for x in remaining:
            if any(a[i] < a[j] < x for i in range(len(a)) for j in range(i+1,len(a))):
                continue
            yield from walk(a+[x],[v for v in remaining if v!=x])
    yield from walk([],list(range(n)))


def components(n, first, second):
    parent=list(range(2*n))
    def root(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,j in first+second:
        a,b=root(i),root(j)
        if a!=b:parent[b]=a
    return len({root(i) for i in range(2*n)})


def witnesses(w):
    n=len(w)//2
    for a in combinations(range(2*n),n):
        I=set(a)
        u=tuple(w[i] for i in a)
        v=tuple(w[i] for i in range(2*n) if i not in I)
        yield u==v, u==v[::-1]


def example(n):
    # a new initial letter 0, followed by a palindrome using 1,2,...
    half=(n-1)//2
    left=tuple(range(1,half+1))
    p=left + ((half+1,) if (n-1)%2 else ()) + left[::-1]
    assert len(p)==n-1
    return (0,)+p+(0,)+p


def check():
    target={1: {1:1},2:{1:3,2:1},3:{1:15,2:10},
            4:{1:98,2:85,3:13},5:{1:804,2:763,3:197},
            6:{1:7126,2:7557,3:2518,4:223},
            7:{1:69233,2:79757,3:30795,4:4256},
            8:{1:709795,2:875677,3:384117,4:71061,5:4250}}
    total=0
    for n in range(1,9):
        ss=list(nonnest(n))
        rr=[tuple((i,n+p[i]) for i in range(n)) for p in avoid123(n)]
        assert len(ss)==len(rr)==comb(2*n,n)//(n+1)
        assert all(all(not(i<k<ell<j) for i,j in S for k,ell in S if (i,j)!=(k,ell)) for S in ss)
        assert all(all(not(i<j<k and x<y<z) for i,x in R for j,y in R for k,z in R) for R in rr)
        hist=Counter()
        for S in ss:
            for R in rr:
                common=set(S)&set(R)
                assert len(common)<=2
                c=components(n,S,R)
                assert c <= (n+len(common))//2
                hist[c]+=1
        assert hist==target[n],(n,hist)
        assert max(hist)==n//2+1
        w=example(n)
        assert len(w)==2*n
        assert len(set(w))==n//2+1
        if n<=7:
            obs=list(witnesses(w))
            assert any(x for x,y in obs) and any(y for x,y in obs)
        total+=len(ss)*len(rr)
    direct=0
    for n in range(1,5):
        for q in (2,3):
            max_s=0
            for w in product(range(q),repeat=2*n):
                # First filter necessary that each letter occur an even number of times.
                if any(w.count(x)%2 for x in range(q)):
                    continue
                obs=list(witnesses(w))
                if any(x for x,y in obs) and any(y for x,y in obs):
                    max_s=max(max_s,len(set(w)))
                    assert len(set(w))<=n//2+1
                direct+=1
            assert max_s==min(q,n//2+1),(n,q,max_s)
    print('JOINT_SHUFFLE_SUPPORT_PASS matching_pairs=',total,'direct_even_words=',direct,
          'n_matching=1..8','direct_n=1..4_q=2,3')


if __name__=='__main__':
    check()
