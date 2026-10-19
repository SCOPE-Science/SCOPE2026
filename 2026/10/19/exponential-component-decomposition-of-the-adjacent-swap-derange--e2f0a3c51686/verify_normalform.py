"""Independent constructive check of component normal forms and isolated states."""
from itertools import permutations
from collections import defaultdict


def normal_form(w):
    n=len(w)
    inv={v:j for j,v in enumerate(w,1)}
    L=tuple(sorted(v for v in range(1,n+1) if inv[v]<v))
    R=tuple(sorted(v for v in range(1,n+1) if inv[v]>v))
    return L+R


def bubble_to_front(arr,start,value,trace):
    p=arr.index(value)
    while p>start:
        arr[p-1],arr[p]=arr[p],arr[p-1]
        assert all(arr[j]!=j+1 for j in range(len(arr)))
        trace.append(tuple(arr))
        p-=1


def canonical_path(w):
    n=len(w)
    arr=list(w);path=[w]
    inv={v:j for j,v in enumerate(w,1)}
    L=sorted(v for v in range(1,n+1) if inv[v]<v)
    R=sorted(v for v in range(1,n+1) if inv[v]>v)
    for j,v in enumerate(L+R):
        bubble_to_front(arr,j,v,path)
    assert tuple(arr)==normal_form(w)
    return path


def moves(w):
    for k in range(len(w)-1):
        a=list(w)
        a[k],a[k+1]=a[k+1],a[k]
        if all(a[j]!=j+1 for j in range(len(w))):
            yield tuple(a)

if __name__=='__main__':
    for n in range(2,9):
        groups=defaultdict(set);vertices=0;frozen=[];longest=0
        for w in permutations(range(1,n+1)):
            if any(v==j+1 for j,v in enumerate(w)):continue
            vertices+=1
            path=canonical_path(w)
            assert all(normal_form(v)==normal_form(w) for v in path)
            longest=max(longest,len(path)-1)
            groups[normal_form(w)].add(w)
            if not any(moves(w)):frozen.append(w)
        assert len(groups)==2**(n-2)
        for canon,member in groups.items():
            assert canon in member
            assert all(canonical_path(w)[-1]==canon for w in member)
        expect={tuple(range(2,n+1))+(1,), (n,)+tuple(range(1,n))}
        assert set(frozen)==expect
        print('n',n,'derangements',vertices,'normal_forms',len(groups),'frozen',len(frozen),'max_bubble_swaps',longest)
    print('VERIFY_OK')
