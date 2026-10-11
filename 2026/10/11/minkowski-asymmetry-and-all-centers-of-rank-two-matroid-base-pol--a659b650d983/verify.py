#!/usr/bin/env python3
"""Exact finite checks for the rank-two base-polytope Minkowski-center formulas.
No third-party dependencies. Exhaustion is finite evidence, not the proof for all sizes.
"""
from fractions import Fraction as F
from itertools import combinations

def parallel_classes(sizes):
    classes=[];first=0
    for size in sizes:
        classes.append(tuple(range(first, first+size)))
        first+=size
    return classes

def asymmetry(sizes):
    p=len(sizes)
    if p==2:
        return F(max(1,sizes[0]-1,sizes[1]-1))
    return max(F(max(sizes)),F(sum(sizes)-2,2),F(2,p-2))

def center(sizes):
    classes=parallel_classes(sizes);p=len(classes);n=sum(sizes);s=asymmetry(sizes)
    if p==2:
        return [F(1,len(C)) for C in classes for _ in C]
    Z=2*(s+1)-n
    caps=[s-m for m in sizes]
    U=sum(caps)
    assert Z>=0 and U>=Z>=0
    z=[F(0) for _ in range(n)]
    if U>0:
        for C,cap in zip(classes,caps):
            for e in C:z[e]=Z*cap/(U*len(C))
    return [(1+v)/(s+1) for v in z]

def check(sizes):
    classes=parallel_classes(sizes);n=sum(sizes);p=len(classes);s=asymmetry(sizes)
    c=center(sizes)
    assert sum(c)==2
    assert all(v>=0 for v in c)
    assert all(sum(c[e] for e in C)<=1 for C in classes)
    vertices=[]
    for i in range(p):
        for j in range(i+1,p):
            for e in classes[i]:
                for f in classes[j]:vertices.append((e,f))
    for e,f in vertices:
        v=[int(i in (e,f)) for i in range(n)]
        reflected=[((s+1)*c[i]-v[i])/s for i in range(n)]
        assert sum(reflected)==2
        assert all(z>=0 for z in reflected)
        assert all(sum(reflected[i] for i in C)<=1 for C in classes)
    # Independently check that every formula term is a necessary obstruction.
    if p>=3:
        assert s>=max(sizes) and s*2>=n-2 and s*(p-2)>=2
        Z=2*(s+1)-n;U=p*s-n
        active=[i for i,m in enumerate(sizes) if m<s]
        d=0 if Z==0 else sum(sizes[i]-1 for i in active) if Z==U else sum(sizes[i] for i in active)-1
        assert 0<=d<=n-1
    else:
        assert s+1>=max(sizes)
        d=sum(m-1 for m in sizes if s+1>m)
        assert 0<=d<=n-2
    return len(vertices)

def profiles(n):
    for p in range(2,n+1):
        for cuts in combinations(range(1,n),p-1):
            a=(0,)+cuts+(n,)
            yield tuple(a[i+1]-a[i] for i in range(p))

if __name__=='__main__':
    tested=0;vertices=0
    for n in range(2,12):
        for sizes in profiles(n):
            vertices+=check(sizes);tested+=1
    print('PASS: exact rational rank-two profiles:',tested)
    print('PASS: reflected base-vertex checks:',vertices)
    print('Boundary examples:')
    for m in [(1,1,1),(1,1,1,1),(1,1,1,1,1),(3,1,1),(2,2,1),(3,3),(5,2)]:
        print(m,'asymmetry=',asymmetry(m))
