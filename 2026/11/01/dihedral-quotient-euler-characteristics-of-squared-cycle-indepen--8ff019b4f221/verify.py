#!/usr/bin/env python3
"""Independent verification of a quotient Euler characteristic formula."""
from math import gcd

def A(m):
    if m <= 0: return 1
    values={0:1,1:0,2:-1}
    for k in range(3,m+1):values[k]=values[k-1]-values[k-3]
    return values[m]

def W(d):
    if d<3:return 1
    if d==3:return -2
    if d==4:return -3
    if d==5:return -4
    v={3:-2,4:-3,5:-4}
    for k in range(6,d+1):v[k]=v[k-1]-v[k-3]
    return v[d]

def predicted_orbit_sum(n,reflection=False,k=0):
    if not reflection:
        return W(gcd(n,k))
    if n%2:
        h=(n-1)//2
        m=h-2
        return A(m)-A(m-1)
    h=n//2
    if k%2 ==0:
        m=h-3
        return A(m)-2*A(m-1)+A(m-2)
    return A(h-2)

def direct_orbit_sum(n,reflection,k):
    # A stable simplex is a union of permitted orbits.
    perm=lambda i: ((k-i)%n if reflection else (k+i)%n)
    unseen=set(range(n));orbits=[]
    while unseen:
        i=min(unseen);o=[];v=i
        while v not in o:
            o.append(v);unseen.remove(v);v=perm(v)
        orbits.append(set(o))
    allowed=[]
    for orbit in orbits:
        if all(min(abs(x-y),n-abs(x-y))>2 for x in orbit for y in orbit if x!=y):
            allowed.append(orbit)
    # orientation of group on a selected union of orbits is accounted for
    # by the alternating sign (-1)^number_of_selected_orbits.
    from itertools import combinations
    total=0
    for m in range(len(allowed)+1):
        for tup in combinations(range(len(allowed)),m):
            verts=set()
            for t in tup:verts.update(allowed[t])
            if all(min(abs(x-y),n-abs(x-y))>2 for x in verts for y in verts if x<y):
                total+=(-1)**m
    return total

def euler(n):
    return -sum(predicted_orbit_sum(n,False,k)+predicted_orbit_sum(n,True,k) for k in range(n))//(2*n)

if __name__=='__main__':
    for n in range(6,23):
        for ref in (False,True):
            for k in range(n):
                got=direct_orbit_sum(n,ref,k)
                want=predicted_orbit_sum(n,ref,k)
                assert got==want,(n,ref,k,got,want)
        total=-sum(predicted_orbit_sum(n,False,k)+predicted_orbit_sum(n,True,k) for k in range(n))
        assert total%(2*n)==0,(n,total)
        print('N',n,'reduced_quotient_euler',total//(2*n))
    for n in range(23,501):
        total=-sum(predicted_orbit_sum(n,False,k)+predicted_orbit_sum(n,True,k) for k in range(n))
        assert total%(2*n)==0,(n,total)
    print('CHECKS_OK')
