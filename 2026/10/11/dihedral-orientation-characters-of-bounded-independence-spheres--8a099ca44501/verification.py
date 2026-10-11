#!/usr/bin/env python3
"""Finite checks for dihedral orientation on bounded-independence complexes."""
from itertools import combinations

def admitted(s,n,d):
    return not any(all((a-b)%n not in (1,n-1) for a,b in combinations(t,2)) for t in combinations(s,d))

def sign_of_tuple(vals):
    parity=0
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            parity^=(vals[i]>vals[j])
    return -1 if parity else 1

def cells(n,d):
    return [s for k in range(1,min(n,2*d-2)+1) for s in combinations(range(n),k) if admitted(s,n,d)]

def top_character(n,d,face_set,perm):
    lefschetz=-1  # reduced empty-simplex contribution
    for simplex in face_set:
        im=[perm(x) for x in simplex]
        if set(im)==set(simplex):
            lefschetz+=(-1)**(len(simplex)-1)*sign_of_tuple(im)
    return (-1)**(2*d-3)*lefschetz

def cycmap(steps):
    f=[0]
    for delta in steps[:-1]:
        f.append((f[-1]+delta)%sum(steps))
    assert sum(steps)>0
    return f

def check_swap(n,d,steps,i,fs):
    adj=steps[:]
    adj[i],adj[i+1]=adj[i+1],adj[i]
    a,b=cycmap(steps),cycmap(adj)
    assert sum(a[j]!=b[j] for j in range(n))==1
    for face in fs:
        im=set(a[v] for v in face)|set(b[v] for v in face)
        assert admitted(sorted(im),2*d,d),(n,d,steps,i,face)

N=0
for d in (2,3,4,5):
    for n in range(2*d, min(2*d+7,17)):
        fs=cells(n,d)
        base=(-1)**(d-1)
        for shift in range(n):
            assert top_character(n,d,fs,lambda x,t=shift:(x+t)%n)==1,(n,d,shift)
            assert top_character(n,d,fs,lambda x,t=shift:(t-x)%n)==base,(n,d,shift)
            N+=2
C=0
for d in (2,3,4):
    for n in range(2*d+1,2*d+4):
        fs=cells(n,d)
        for start in range(n):
            steps=[1 if (i-start)%n<2*d else 0 for i in range(n)]
            for j in range(n-1):
                if steps[j]!=steps[j+1]:
                    check_swap(n,d,steps,j,fs)
                    C+=1
print('VERIFY_OK: signed dihedral Lefschetz identities',N,'; adjacent contraction-contiguity pairs',C)
