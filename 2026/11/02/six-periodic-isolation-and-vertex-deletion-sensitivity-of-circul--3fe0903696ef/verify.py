#!/usr/bin/env python3
"""Direct checks for isolation in cycle prisms and their vertex deletions.

Run: python3 verify.py. The program uses only Python's standard library.
"""
from itertools import combinations

def edges(n, deleted=None):
    assert n >= 3
    e=set()
    def add(x,y):
        if x != deleted and y != deleted:
            e.add(tuple(sorted((x,y))))
    for i in range(n):
        for r in (0,1):
            add(2*i+r,2*((i+1)%n)+r)
        add(2*i,2*i+1)
    return sorted(e)

def is_isolating(n, selected, deleted=None):
    e=edges(n,deleted)
    assert len(set(selected)) == len(selected)
    assert all(0 <= x < 2*n and x != deleted for x in selected)
    N=set(selected)
    for x,y in e:
        if x in selected:N.add(y)
        if y in selected:N.add(x)
    return all(x in N or y in N for x,y in e)

def full_formula(n):
    return (n+2)//3+(n%6==3)

def removed_formula(n):
    return (n+2)//3-(n%6==4)

def full_witness(n):
    if n%3:
        return [2*c+(j%2) for j,c in enumerate(range(0,n,3))]
    k=n//3
    if k%2==0:
        return [2*(3*j)+(j%2) for j in range(k)]
    cols=[0,1]+list(range(3,n,3))
    return [2*c+(0 if c==0 or c==1 or ((c//3)%2==1) else 1) for c in cols]

def removed_witness(n):
    if n%6==3:
        return [2*(1+3*j)+(1-j%2) for j in range(n//3)]
    if n%6==4:
        return [2*c+(1-j%2) for j,c in enumerate(range(2,n-1,3))]
    # Switch the two layers globally when needed to avoid vertex (0,0).
    a=full_witness(n)
    if 0 in a:a=[x^1 for x in a]
    assert 0 not in a
    return a

def exact_min_and_count(n,deleted=None):
    e=edges(n,deleted)
    verts=[x for x in range(2*n) if x!=deleted]
    masks=[]
    for v in verts:
        ne={v}
        ne.update(y if x==v else x for x,y in e if x==v or y==v)
        masks.append(sum(1<<t for t,(x,y) in enumerate(e) if x in ne or y in ne))
    universe=(1<<len(e))-1
    for k in range(len(verts)+1):
        count=0
        for ids in combinations(range(len(verts)),k):
            m=0
            for i in ids:m|=masks[i]
            if m==universe:count+=1
        if count:return k,count
    raise AssertionError

def main():
    for n in range(3,11):
        a,c=exact_min_and_count(n)
        b,d=exact_min_and_count(n,0)
        assert a==full_formula(n) and b==removed_formula(n),(n,a,b)
        print('DIRECT_EXHAUSTIVE',n,'full',a,'minima',c,'deleted',b,'minima',d)
    for n in range(3,601):
        a=full_witness(n)
        b=removed_witness(n)
        assert len(a)==full_formula(n),(n,'full size',len(a))
        assert len(b)==removed_formula(n),(n,'delete size',len(b))
        assert is_isolating(n,a),('full witness',n,a)
        assert is_isolating(n,b,deleted=0),('removed witness',n,b)
    print('WITNESS_DIRECT_GRAPH_CHECKS_OK 598 full and 598 deleted')
    print('VERIFY_OK')
if __name__=='__main__':main()
