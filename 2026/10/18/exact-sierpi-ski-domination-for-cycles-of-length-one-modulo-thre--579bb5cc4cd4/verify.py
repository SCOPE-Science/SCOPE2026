#!/usr/bin/env python3
"""Exact finite checks of a cyclic Sierpinski-product domination formula.

Python standard library only. The infinite theorem rests on the written proof,
not on these finite tests.
"""
from itertools import combinations, product


def predicted(n, k):
    if k == 1:
        return k*n + int(n % 4 != 0)
    if k == 2:
        return k*n + int(n in (3, 5, 6, 10))
    return k*n + int(n in (3, 6))


def step_set(k):
    return tuple(2 + 3*j for j in range(k))


def walk_steps(length, k):
    m = 3*k + 1
    if length % 2 == 0:
        return [2, m-2]*(length//2)
    if k >= 3 and length >= 5:
        return [3*k-7] + [2]*4 + [2, m-2]*((length-5)//2)
    if k == 2 and length >= 7:
        return [3*k-4]*2 + [2]*5 + [2,m-2]*((length-7)//2)
    return None


def f_from_walks(n,k):
    m = 3*k+1
    f = [None]*n
    seen=set()
    for start in range(n):
        if start in seen:
            continue
        cyc=[]
        v=start
        while v not in seen:
            seen.add(v)
            cyc.append(v)
            v=(v+2)%n
        assert v==start
        steps=walk_steps(len(cyc),k)
        if steps is None:
            return None
        assert all(s in step_set(k) for s in steps)
        assert sum(steps)%m == 0
        pos=0
        for j,i in enumerate(cyc):
            f[i]=pos
            pos=(pos+steps[j])%m
        assert pos==0
    assert len(seen)==n and all((f[(i+2)%n]-f[i])%m in step_set(k) for i in range(n))
    return f


def selected_from_f(n,k,f):
    m=3*k+1
    return {(i,(f[(i-1)%n]+2+3*j)%m)
            for i in range(n) for j in range(k)}


def neighborhoods(n,k,f):
    m=3*k+1
    nbr=[]
    for i in range(n):
        for a in range(m):
            pos={(i,a),(i,(a-1)%m),(i,(a+1)%m)}
            if a==f[(i-1)%n]:
                pos.add(((i-1)%n,f[i]))
            if a==f[(i+1)%n]:
                pos.add(((i+1)%n,f[i]))
            nbr.append(sum(1 << (j*m+b) for j,b in pos))
    return nbr


def uncovered(n,k,f,D):
    m=3*k+1
    nb=neighborhoods(n,k,f)
    covered=0
    for i,a in D:
        covered |= nb[i*m+a]
    universe=(1<<(n*m))-1
    rest=universe & ~covered
    return [(i,a) for i in range(n) for a in range(m) if rest & (1<<(i*m+a))]


def source_upper_witness(n,k):
    m=3*k+1
    f=[0 if i%4 in (0,1) else 2 for i in range(n)]
    D=selected_from_f(n,k,f)
    missing=uncovered(n,k,f,D)
    if len(missing)==1:
        D.add(missing[0])
    elif len(missing)==2:
        assert n%4==2 and set(missing)=={(0,0),(1,0)}
        D.add((0,0))
    else:
        assert len(missing)==0
    assert len(D) <= k*n+1
    assert not uncovered(n,k,f,D)
    return f,D


def possible_by_dp(length,k):
    m=3*k+1
    reachable={0}
    for _ in range(length):
        reachable={(a+b)%m for a in reachable for b in step_set(k)}
    return 0 in reachable


def small_bruteforce(n,k):
    # The global offset of f can be fixed to zero by rotating C_(3k+1).
    m=3*k+1
    full=(1<<(n*m))-1
    found=False
    count=0
    for suffix in product(range(m),repeat=n-1):
        f=(0,)+suffix
        nb=neighborhoods(n,k,f)
        choices=[]
        for layer in range(n):
            choices.append([])
            for idxs in combinations(range(m),k):
                mask=0
                for a in idxs:
                    mask |= nb[layer*m+a]
                choices[-1].append(mask)
        for pieces in product(*choices):
            mask=0
            for p in pieces:
                mask |= p
            if mask==full:
                found=True
                break
        count+=1
        if found:
            break
    return found,count


def main():
    # Explicit seven-by-ten witness for comparing an older draft formula.
    f_seven=[0,4,5,6,0,8,2]
    D_seven=selected_from_f(7,3,f_seven)
    assert len(D_seven)==21 and not uncovered(7,3,f_seven,D_seven)
    tests=0
    for k in range(1,10):
        for n in range(3,61):
            length=n if n%2 else n//2
            possible=possible_by_dp(length,k)
            assert possible==(predicted(n,k)==n*k), (n,k,'dp')
            f=f_from_walks(n,k)
            assert (f is not None)==possible, (n,k,'walk')
            if f is not None:
                D=selected_from_f(n,k,f)
                assert len(D)==k*n and not uncovered(n,k,f,D), (n,k,'witness')
            _,D=source_upper_witness(n,k)
            assert len(D)<=n*k+1
            tests+=1
    brute=[]
    for n,k in [(3,1),(4,1),(5,1),(6,1),(3,2)]:
        obtained,tried=small_bruteforce(n,k)
        assert obtained == (predicted(n,k)==n*k), (n,k,obtained)
        brute.append((n,k,obtained,tried))
    print('VERIFY_OK')
    print('direct construction and cyclic-step DP comparisons:',tests)
    print('all-f small-order searches (n,k,attain_kn,f_values_checked):',brute)

if __name__=='__main__':
    main()
