#!/usr/bin/env python3
"""Independent finite-orbit proxy for equivalence relations on ordered rational atoms."""
from math import comb

def bell(n):
    out=[1]
    for m in range(1,n+1):
        out.append(sum(comb(m-1,j)*out[j] for j in range(m)))
    return out

def formula(k,b):
    return sum(comb(k+1,j)*b[k+j] for j in range(k+2))

def partitions(n):
    a=[0]*n
    def rec(pos,largest):
        if pos==n:
            yield tuple(a)
        else:
            for j in range(largest+2):
                a[pos]=j
                yield from rec(pos+1,max(j,largest))
    yield from rec(1,0)

def canonical(seq):
    d={};a=[]
    for i in seq:
        if i not in d: d[i]=len(d)
        a.append(d[i])
    return tuple(a)

def swapped_stable(p, l, r):
    q=list(p); q[l],q[r]=q[r],q[l]
    return canonical(q)==p

def proxy(k):
    # k singled-out points and k+1 gaps, 2 proxy points in each gap
    gaps=[(3*i,3*i+1) for i in range(k+1)]
    n=3*k+2
    count=0
    essential=0
    for p in partitions(n):
        if not all(swapped_stable(p,l,r) for l,r in gaps):
            continue
        count+=1
        all_essential=True
        for i in range(k):
            # With s_i forgotten, the neighboring gaps coalesce with s_i.
            merged=[3*i,3*i+1,3*i+2,3*i+3,3*i+4]
            pivot=merged[0]
            if all(swapped_stable(p,pivot,j) for j in merged[1:]):
                all_essential=False
                break
        essential+=all_essential
    return count,essential

def main():
    b=bell(26)
    f=[formula(k,b) for k in range(10)]
    expected=[2,10,114,2066,52922,1788850]
    assert f[:6]==expected
    p=[proxy(k) for k in range(4)]
    assert [c for c,e in p]==f[:4],(p,f[:4])
    print('EXHAUSTIVE_TWO_POINT_PER_GAP_PROXY',[c for c,e in p])
    g=[sum((-1)**(k-t)*comb(k,t)*f[t] for t in range(k+1)) for k in range(10)]
    assert g[:6]==[2,8,96,1752,45304,1543808]
    assert [e for c,e in p]==g[:4], (p,g[:4])
    print('EXHAUSTIVE_MINIMAL_SUPPORT_PROXY',[e for c,e in p])
    for k in range(1,10):
        assert 0<=g[k]<=f[k]
        assert f[k]-g[k] <= k*f[k-1] # inclusion-exclusion agrees with union bound
    print('SUPPORT_ESSENTIAL_COUNTS',g[:7])
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
