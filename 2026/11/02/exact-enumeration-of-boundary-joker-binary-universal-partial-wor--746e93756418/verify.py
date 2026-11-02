#!/usr/bin/env python3
"""Exact arithmetic checks for boundary-wildcard universal-word enumeration.
All checks are finite; the all-length proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
from math import factorial


def binary(n):
    return [''.join(p) for p in product('01', repeat=n)]


def full_edges(n):
    return binary(n)


def removed_edges(n, prefix, k):
    assert len(prefix) == k + n - 1 and prefix.count('*') == 1
    return [prefix.replace('*', z)[i:i+n] for i in range(k) for z in '01']


def brute_upword_count(n, k):
    length = 2**n + n - k - 1
    if length > 18:
        raise ValueError('not intended for longer exhaustive enumeration')
    count = 0
    for rest in product('01', repeat=length-1):
        s = ''.join(rest[:k-1]) + '*' + ''.join(rest[k-1:])
        seen = set()
        ok = True
        for i in range(length-n+1):
            sub = s[i:i+n]
            for word in ([sub.replace('*','0'), sub.replace('*','1')]
                         if '*' in sub else [sub]):
                if word in seen:
                    ok = False
                    break
                seen.add(word)
            if not ok:
                break
        if ok and len(seen) == 2**n:
            count += 1
    return count


def euler_trail_count(n, prefix, k):
    """Independent directed-edge subset DP, not using matrix-tree formula."""
    m = n-1
    rem = removed_edges(n, prefix, k)
    assert len(set(rem)) == 2*k
    remaining = [e for e in full_edges(n) if e not in set(rem)]
    outgoing = {v: [] for v in binary(m)}
    dest = []
    for j,e in enumerate(remaining):
        outgoing[e[:-1]].append(j)
        dest.append(e[1:])
    balance = {v: 0 for v in binary(m)}
    for e in remaining:
        balance[e[:-1]] += 1
        balance[e[1:]] -= 1
    start = prefix[k:k+m]
    end = [v for v,d in balance.items() if d == -1]
    assert balance[start] == 1 and len(end) == 1
    end = end[0]
    mask_all = (1 << len(remaining))-1

    @lru_cache(None)
    def rec(v,mask):
        if mask == mask_all:
            return int(v == end)
        return sum(rec(dest[j], mask | (1 << j)) for j in outgoing[v]
                   if not (mask & (1 << j)))
    return rec(start,0)


def bareiss(matrix):
    """Integer-only fraction-free exact determinant."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    den = 1
    for k in range(n-1):
        if a[k][k] == 0:
            for i in range(k+1,n):
                if a[i][k] != 0:
                    a[k],a[i] = a[i],a[k]
                    sign = -sign
                    break
            else:
                return 0
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top = a[i][j]*pivot - a[i][k]*a[k][j]
                assert top % den == 0
                a[i][j] = top // den
        for i in range(k+1,n):
            a[i][k] = 0
        den = pivot
    return sign*a[-1][-1]


def cofactor_tree_count(n, rem, root):
    m = n-1
    v = binary(m)
    ix = {s:i for i,s in enumerate(v)}
    mat = [[0]*len(v) for _ in v]
    for e in full_edges(n):
        if e in rem:
            continue
        i,j = ix[e[:-1]], ix[e[1:]]
        mat[i][i] += 1
        mat[i][j] -= 1
    r = ix[root]
    reduced = [[mat[i][j] for j in range(len(v)) if j!=r]
               for i in range(len(v)) if i!=r]
    return bareiss(reduced)


def pstep(x, y, j):
    m = len(x)
    return Q(1,2**j) if x[j:] == y[:m-j] else Q(0)


def k_matrix(n):
    """Green-function rank-three update for penultimate boundary case."""
    assert n>=4
    m=n-1
    s=('01'*m)[:m]
    b=('10'*m)[:m]
    t='00'+s[:m-2]
    c='00'+b[:m-2]
    E=[(s,b),(c,s),(b,s)]
    out=[]
    for u,v in E:
        row=[]
        for w,_ in E:
            z=Q(0)
            for j in range(m):
                z += pstep(u,w,j)-pstep(v,w,j)-pstep(u,t,j)+pstep(v,t,j)
            row.append(z/2)
        out.append(row)
    return out


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def target1(n):
    return 1 << (2**(n-1) - n + 1)


def target2(n):
    if n==2:
        return 0
    if n==3:
        return 2
    t=1 << (2**(n-1)-n)
    result = Q(t,3) * (1 - Q(-1,2)**(n-2))
    assert result.denominator == 1
    return int(result)


def verify():
    # Independent brute-force enumeration of all candidate partial strings.
    for (n,k) in [(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(4,3)]:
        if k==2 and n==2:
            # At n=2 the two wildcard windows cannot be four distinct words.
            assert brute_upword_count(2,2) == 0
        elif k<=2:
            assert brute_upword_count(n,k) == (target1(n) if k==1 else target2(n))
        else:
            assert brute_upword_count(n,k) == 4
    # Direct edge-subset enumeration at five bits: no matrix tree or determinant.
    for n in (2,3,4,5):
        s='0'*(n-1)
        prefix='*'+s
        expected=target1(n)//2
        assert euler_trail_count(n,prefix,1)==expected
    for n in (3,4,5):
        s=('01'*n)[:n-1]
        prefix='0*'+s
        assert euler_trail_count(n,prefix,2)==target2(n)//2
    # Independent exact integer Laplacian cofactor calculations.
    for n in (2,3,4,5,6):
        m=n-1
        expected = 1 << (2**m-n)
        root='1'+'0'*(m-1)
        assert cofactor_tree_count(n,set(),root)==expected
        r1=set(removed_edges(n,'*'+'0'*m,1))
        assert cofactor_tree_count(n,r1,root)==expected
        if n>=4:
            s=('01'*n)[:m]
            root2='00'+s[:m-2]
            r2=set(removed_edges(n,'0*'+s,2))
            expected2=target2(n)//2
            assert cofactor_tree_count(n,r2,root2)==expected2
    # Exact rational overlap identity for several additional sizes.
    for n in range(4,41):
        r=Q(-1,2)**(n-2)
        alpha=(1-r)/3
        beta=(1+2*r)/3
        K=k_matrix(n)
        assert K[0][0] == alpha
        assert K[0][1] == 0
        assert K[0][2] == -beta
        assert K[1][1] == Q(1,2)
        assert K[2][0] == -alpha
        assert K[2][1] == 0
        assert K[2][2] == beta
        B=[[Q(int(i==j)) - K[i][j] for j in range(3)] for i in range(3)]
        assert det3(B) == alpha/2
    # Small cases of final formula and its structural parity adjustment.
    assert [target1(n) for n in range(2,7)] == [2,4,32,4096,134217728]
    assert [target2(n) for n in range(2,7)] == [0,2,4,768,20971520]
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
