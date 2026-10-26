"""Exhaustive verification of locally identifying coloring enumeration.

The predicate builds the graph and compares closed-neighborhood color sets;
there is no use of the structural proof inside that predicate.
Run: python check_matching_join.py
"""
from itertools import permutations
from math import comb


def falling(k, r):
    ans=1
    if r<0 or r>k:
        return 0
    for j in range(r):
        ans *= k-j
    return ans


def lid_from_graph(n,t,colors):
    assert 0<=t<=n
    edges=[]
    for base in (0,n):
        edges += [(base+i,base+j) for i in range(n) for j in range(i+1,n)]
    edges += [(i,n+i) for i in range(t)]
    closed=[{i} for i in range(2*n)]
    for a,b in edges:
        closed[a].add(b)
        closed[b].add(a)
        if colors[a]==colors[b]:
            return False
    for a,b in edges:
        if closed[a]!=closed[b] and {colors[x] for x in closed[a]}=={colors[x] for x in closed[b]}:
            return False
    return True


def structural(n,t,top,bottom):
    if len(set(top))!=n or len(set(bottom))!=n:
        return False
    if any(top[i]==bottom[i] for i in range(t)):
        return False
    if t==0:
        return True
    A={c:i for i,c in enumerate(top)}
    B={c:i for i,c in enumerate(bottom)}
    overlap=set(A)&set(B)
    if t==n:
        return len(overlap)<=1
    if any(A[c]<t or B[c]<t for c in overlap):
        return False
    return not (t==1 and len(overlap)==n-1)


def expected_fixed_top(n,t,k):
    d=k-n
    if t==0:
        return falling(k,n)
    if t==n:
        return falling(d,n)+n*(n-1)*falling(d,n-1)
    u=n-t
    rmax=(u-1 if t==1 else u)
    return sum(comb(u,r)**2 * __import__('math').factorial(r)*falling(d,n-r)
               for r in range(rmax+1))


def main():
    cases=0; checked=0
    for n in range(2,6):
        top=tuple(range(n))
        for t in range(n+1):
            for k in range(n,2*n+2):
                accepted=0
                for bottom in permutations(range(k),n):
                    cols=top+bottom
                    brute=lid_from_graph(n,t,cols)
                    classify=structural(n,t,top,bottom)
                    assert brute==classify,(n,t,k,bottom,brute,classify)
                    accepted+=int(brute)
                    checked+=1
                expect=expected_fixed_top(n,t,k)
                assert accepted==expect,(n,t,k,accepted,expect)
                cases+=1
    named_cases=0
    for n in (2,3):
        for t in range(n+1):
            for k in (2*n-1, 2*n):
                brute=0
                for top in permutations(range(k),n):
                    for bot in permutations(range(k),n):
                        brute += int(lid_from_graph(n,t,top+bot))
                expect=falling(k,n)*expected_fixed_top(n,t,k)
                assert brute==expect,('named-count failure',n,t,k,brute,expect)
                named_cases+=1
    print('PASS',cases,'fixed-top cases;',checked,'bottom assignments;',named_cases,
          'full named-color cases tested using the graph definition')

if __name__=='__main__':
    main()
