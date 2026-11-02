#!/usr/bin/env python3
"""Independent finite checks of neighbor-XOR dynamics on a cycle with one triangular chord.
Uses only the Python standard library. Finite tests corroborate, not prove, all-n claims.
"""
from functools import lru_cache


def matrix(n):
    assert n >= 4
    rows = [0] * n
    for i in range(n):
        rows[i] |= 1 << ((i-1) % n)
        rows[i] |= 1 << ((i+1) % n)
    rows[0] |= 1 << 2
    rows[2] |= 1 << 0
    return rows


def apply(rows, x):
    return sum(((row & x).bit_count() & 1) << i for i,row in enumerate(rows))


def matrix_multiply(a,b):
    n = len(a)
    res = []
    for row in a:
        v=0
        while row:
            bit = row & -row
            v ^= b[bit.bit_length()-1]
            row ^= bit
        res.append(v)
    return res


def matrix_rank(rows):
    pivots={}
    for r in rows:
        while r:
            pos=r.bit_length()-1
            if pos not in pivots:
                pivots[pos]=r
                break
            r ^= pivots[pos]
    return len(pivots)


def matching_polynomial(n):
    # The characteristic polynomial in characteristic two equals the matching polynomial.
    nbr = matrix(n)
    @lru_cache(maxsize=None)
    def count(mask):
        if not mask: return 1
        v=(mask & -mask).bit_length()-1
        rem=mask & ~(1<<v)
        out=count(rem)<<1
        w=rem & nbr[v]
        while w:
            bit=w & -w
            out ^= count(rem ^ bit)
            w ^= bit
        return out
    return count((1<<n)-1)


def path_polynomial(m):
    a,b=1,2   # f_0=1, f_1=x
    if m==0: return a
    for _ in range(2,m+1):
        a,b=b,(b<<1)^a
    return b


def theoretical_z(n):
    if n%2==0:return 2
    d=n-1
    power=1
    while d%2==0:
        d//=2
        power*=2
    return power+1


def test_ranks():
    comparisons=0
    for n in range(4,151):
        A=matrix(n)
        z=theoretical_z(n)
        power=[1<<i for i in range(n)]
        for t in range(1,z+3):
            power=matrix_multiply(A,power)
            deficiency=n-matrix_rank(power)
            expected= min(t,z) if n%2 else 2
            assert deficiency==expected,(n,t,deficiency,expected)
            comparisons+=1
    return comparisons


def test_polynomials():
    checks=0
    for n in range(4,22):
        actual=matching_polynomial(n)
        expected=path_polynomial(n-2)<<2
        assert actual==expected,(n,actual,expected)
        checks+=1
    return checks


def test_complete_dynamics():
    nstates=0
    fulls=0
    for n in range(4,15):
        rows=matrix(n)
        N=1<<n
        # Find every temporal orbit's entry time by memoized traversal.
        T={}
        for start in range(N):
            if start in T:continue
            trail=[]
            seen={}
            state=start
            while state not in T and state not in seen:
                seen[state]=len(trail)
                trail.append(state)
                state=apply(rows,state)
            if state in T:
                next_t=T[state]
                for u in reversed(trail):
                    next_t+=1
                    T[u]=next_t
            else:
                cyc=seen[state]
                for u in trail[cyc:]: T[u]=0
                next_t=0
                for u in reversed(trail[:cyc]):
                    next_t+=1
                    T[u]=next_t
        z=theoretical_z(n)
        shells={}
        for v in T.values():shells[v]=shells.get(v,0)+1
        assert max(shells)==z if n%2 else max(shells)==1,(n,z,shells)
        for t in range(z+1 if n%2 else 2):
            if n%2: expected=1<<(n-z+t-1) if t else 1<<(n-z)
            else: expected=(1<<(n-2)) if t==0 else 3*(1<<(n-2))
            assert shells.get(t,0)==expected,(n,t,shells.get(t,0),expected)
        assert len(T)==N and sum(shells.values())==N
        nstates+=N; fulls+=1
    return nstates,fulls


def main():
    import datetime,json
    polys=test_polynomials()
    ranks=test_ranks()
    states,sizes=test_complete_dynamics()
    print('TRIANGLE_CHORD_XOR_VERIFY_OK')
    print(json.dumps(dict(matching_polynomial_sizes=polys,matrix_power_rank_checks=ranks,exhaustive_graph_sizes=sizes,exhaustive_initial_states=states,scope='4<=n<=150 for ranks; tests are finite corroboration'),sort_keys=True))

if __name__=='__main__':main()
