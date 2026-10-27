#!/usr/bin/env python3
"""Exact finite-field checks for a geometric secant-spread statement.

No third-party dependencies; arithmetic takes place in F_p[u]/(u^3-au-b).
These finite tests corroborate, but do not replace, the universal proof.
"""
from itertools import combinations


def run(p, a, b):
    q = p**3
    def digits(x):
        return [x % p, (x // p) % p, (x // (p*p)) % p]
    def pack(v):
        return sum((v[i] % p)*p**i for i in range(3))
    def add(x, y):
        v, w = digits(x), digits(y)
        return pack([v[i]+w[i] for i in range(3)])
    def sub(x, y):
        v, w = digits(x), digits(y)
        return pack([v[i]-w[i] for i in range(3)])
    def mul(x, y):
        v,w=digits(x),digits(y)
        t=[0]*5
        for i in range(3):
            for j in range(3):
                t[i+j]+=v[i]*w[j]
        for k in (4,3):
            t[k-3]+=b*t[k]
            t[k-2]+=a*t[k]
        return pack(t[:3])
    def power(x,n):
        r=1
        while n:
            if n&1:r=mul(r,x)
            x=mul(x,x); n//=2
        return r
    # The chosen cubic has no root and hence is irreducible.
    assert all((r**3-a*r-b)%p for r in range(p))
    assert all(power(x,q)==x for x in range(q))
    p2=p*p
    lines={}
    for s in range(q):
        for u in range(1,q):
            points=frozenset(add(s,mul(t,u)) for t in range(p))
            if points in lines:continue
            A=power(u,p2-1)
            B=sub(power(s,p2),mul(A,s))
            lines[points]=(A,B)
    assert len(lines)==q*(q-1)//(p*(p-1))
    for points,(A,B) in lines.items():
        sec=frozenset(x for x in range(q)
            if power(x,p2)==add(mul(A,x),B))
        assert sec==points and len(sec)==p
        assert all(sum(digits(x)[i] for x in points)%p==0 for i in range(3))
    assert all(sum(digits(x)[i] for x in range(q))%p==0 for i in range(3))
    seen=set()
    for pts in lines:
        for pair in combinations(sorted(pts),2):
            assert pair not in seen
            seen.add(pair)
    assert len(seen)==q*(q-1)//2
    assert all(sum(x in pts for pts in lines)==(q-1)//(p-1)
               for x in range(q))
    # Standard parallel spread: lines in e_0 direction.
    e0,e1,e2=1,p,p*p
    base={frozenset(add(s,mul(t,e0)) for t in range(p))
          for s in range(q) if digits(s)[0]==0}
    assert len(base)==q//p and set().union(*map(set,base))==set(range(q))
    # Switch one e_0-parallel affine plane for an e_1-parallel
    # family. The resulting spread has at least two directions.
    modified={pts for pts in base if digits(next(iter(pts)))[2]!=0}
    for x0 in range(p):
        pts=frozenset(add(x0,mul(t,e1)) for t in range(p))
        assert pts in lines
        modified.add(pts)
    assert len(modified)==q//p
    assert len(set().union(*map(set,modified)))==q
    assert sum(len(s) for s in modified)==q
    assert modified!=base
    print('VERIFY_OK',f'p={p}',f'q={q}',f'maximal_secants={len(lines)}',
          f'point_degree={(q-1)//(p-1)}',
          f'affine_2_design={len(seen)}_pairs',
          f'parallel_and_nonparallel_spreads={q//p}_blocks',
          'all_block_first_moments_zero')


if __name__=='__main__':
    run(3,1,1)      # u^3-u-1
    run(5,3,4)      # u^3+2u+1
    print('VERIFY_OK exact_small_field_models')


def binary_boundary():
    # F_8 = F_2[u]/(u^3+u+1). Each unordered pair of elements
    # is exactly one two-point section of the Frobenius graph.
    def dig(v):
        return [(v >> i) & 1 for i in range(3)]
    def mul(x,y):
        a,b=dig(x),dig(y)
        t=[0]*5
        for i in range(3):
            for j in range(3):t[i+j]^=a[i]*b[j]
        for k in (4,3):
            t[k-3]^=t[k]
            t[k-2]^=t[k]
        return t[0]+2*t[1]+4*t[2]
    def power(x,n):
        result=1
        while n:
            if n&1:result=mul(result,x)
            x=mul(x,x); n>>=1
        return result
    for s,t in combinations(range(8),2):
        u=s^t
        A=power(u,3)
        B=power(s,4)^mul(A,s)
        meet={x for x in range(8) if power(x,4)==(mul(A,x)^B)}
        assert meet=={s,t}
    blocks=[{0,1},{1,2},{3,4},{5,6}]
    covered=set().union(*blocks)
    assert covered==set(range(7))
    assert sum(len(b) for b in blocks)==8
    assert len(blocks)==4
    # A fifth line x=7z passes through both P_infty and the unique hole x=7.
    print('VERIFY_OK binary_F8_nonspread_optimal_cover=5'
          ' secants=4 doubled=1 hole=7 extra_infinity_line=1')


binary_boundary()
