#!/usr/bin/env python3
"""Independent finite-field wedge-product checks for a Grassmann commuting-spectrum formula.

Run: python3 verify.py
Only the Python standard library is used.  The implementation constructs exterior
products from bit-set monomials, rather than assuming any of the counting formulas.
"""
from itertools import combinations, product
from math import comb
from random import Random


def monomials(n, degrees):
    return [sum(1 << i for i in t) for d in degrees for t in combinations(range(n), d)]


def sign_of_wedge(a, b):
    if a & b:
        return 0
    parity = 0
    for i in range(a.bit_length()):
        if (a >> i) & 1:
            parity ^= ((b & ((1 << i) - 1)).bit_count() & 1)
    return -1 if parity else 1


def mat_rank_mod(matrix, prime):
    mat = [row[:] for row in matrix]
    if not mat:
        return 0
    m = len(mat)
    n = len(mat[0])
    p = 0
    for j in range(n):
        k = next((i for i in range(p, m) if mat[i][j] % prime), None)
        if k is None:
            continue
        mat[p], mat[k] = mat[k], mat[p]
        inverse = pow(mat[p][j] % prime, -1, prime)
        mat[p] = [(c * inverse) % prime for c in mat[p]]
        for i in range(p+1,m):
            factor = mat[i][j] % prime
            if factor:
                mat[i] = [(a - factor * b) % prime for a,b in zip(mat[i],mat[p])]
        p += 1
        if p == m:
            break
    return p


def left_wedge_rank(n, x, odd_basis, output_basis, prime):
    """Rank of y -> x wedge y, truncated in total degree <=4."""
    idx = {mask: i for i, mask in enumerate(output_basis)}
    rows = [[0]*len(odd_basis) for _ in output_basis]
    for j, mb in enumerate(odd_basis):
        for ma, coeff in zip(odd_basis,x):
            if coeff == 0:
                continue
            if ma.bit_count() + mb.bit_count() > 4:
                continue
            sgn = sign_of_wedge(ma,mb)
            if sgn:
                rows[idx[ma|mb]][j] = (rows[idx[ma|mb]][j] + sgn*coeff) % prime
    return mat_rank_mod(rows, prime)


def full_commutator_rank(n, coeffs, prime):
    """Direct associative commutator with every full exterior basis monomial."""
    N=1 << n
    rows=[[0]*N for _ in range(N)]
    for a,c in enumerate(coeffs):
        if not c:
            continue
        for b in range(N):
            sign1=sign_of_wedge(a,b)
            sign2=sign_of_wedge(b,a)
            if sign1 != sign2:
                rows[a|b][b]=(rows[a|b][b]+c*(sign1-sign2))%prime
    return mat_rank_mod(rows,prime)


def direct_full_five_checks(q, rounds=120):
    rng=Random(7201+q)
    for j in range(rounds):
        x=[rng.randrange(q) for _ in range(32)]
        if j < rounds//2:
            for i in range(5):
                x[1<<i] = 0
        if j == 0:
            for m in monomials(5,(3,)):
                x[m] = 0
        elif j == 1:
            for m in monomials(5,(3,)):
                x[m] = 0
            x[0b00111] = 1  # a decomposable trivector, wedge-map rank 2
        elif j == 2:
            for m in monomials(5,(3,)):
                x[m] = 0
            x[0b00111] = x[0b11001] = 1  # wedge-map rank 4
        direct=full_commutator_rank(5,x,q)
        if any(x[1<<i] for i in range(5)):
            assert direct==8,(q,j,direct)
        else:
            three=monomials(5,(3,))
            odd=monomials(5,(1,3))
            four=monomials(5,(4,))
            # The rank on cubic data may be read independently by multiplying
            # its coefficients against all 5 linear basis elements.
            cubic=[x[a] for a in three]
            subrows=[[0]*5 for _ in four]
            idx={a:i for i,a in enumerate(four)}
            for k,b in enumerate(monomials(5,(1,))):
                for a,c in zip(three,cubic):
                    sig=sign_of_wedge(a,b)
                    if sig:
                        subrows[idx[a|b]][k]=(subrows[idx[a|b]][k]+c*sig)%q
            indirect=mat_rank_mod(subrows,q)
            assert direct==indirect,(q,j,direct,indirect)


def gaussian(n,k,q):
    num=den=1
    for j in range(k):
        num *= q**(n-j)-1
        den *= q**(k-j)-1
    return num//den


def expected_pair_odd(n,q):
    t=comb(n,3) if n>=3 else 0
    R=comb(n-1,3) if n>=4 else 0
    return q**(2*t)+(q**n-1)*(q+1)*q**(2*t-R)


def exhaustive_pair_fibers(n,q):
    odd = monomials(n,(1,3))
    out = monomials(n,(2,4))
    count=0
    dimension_counts={}
    for x in product(range(q),repeat=len(odd)):
        rank=left_wedge_rank(n,x,odd,out,q)
        dimension_counts[len(odd)-rank] = dimension_counts.get(len(odd)-rank,0)+1
        count+=q**(len(odd)-rank)
    assert count == expected_pair_odd(n,q), (n,q,count,expected_pair_odd(n,q))
    assert sum(dimension_counts.values()) == q**len(odd)
    return dimension_counts


def exhaustive_trivector_fibers(q):
    n=5
    one=monomials(n,(1,))
    three=monomials(n,(3,))
    four=monomials(n,(4,))
    counts={}
    for u in product(range(q),repeat=len(three)):
        # Columns of wedge map V -> Lambda^4(V), built directly.
        rows=[[0]*len(one) for _ in four]
        loc={m:i for i,m in enumerate(four)}
        for j,mb in enumerate(one):
            for ma,c in zip(three,u):
                s=sign_of_wedge(ma,mb)
                if s:
                    rows[loc[ma|mb]][j]=(rows[loc[ma|mb]][j]+c*s)%q
        rank=mat_rank_mod(rows,q)
        counts[rank]=counts.get(rank,0)+1
    rank2=(q-1)*gaussian(5,2,q)
    rank4=gaussian(5,1,q)*q*q*(q-1)*(q**3-1)
    assert counts == {0:1,2:rank2,4:rank4}, (q,counts)
    return counts


def random_element_checks(n,q,seed=813,rounds=300):
    rng=Random(seed+n*101+q)
    odd=monomials(n,(1,3))
    out=monomials(n,(2,4))
    t=comb(n,3)
    R=comb(n-1,3)
    # Check the full fiber dimension whenever the linear part is nonzero.
    for i in range(rounds):
        x=[rng.randrange(q) for _ in odd]
        if not any(x[:n]):
            x[0]=1
        actual=left_wedge_rank(n,x,odd,out,q)
        assert actual == (n-1)+R, (n,q,x,actual)


def main():
    total=0
    for n,q in [(2,3),(3,3),(3,5),(4,3)]:
        d=exhaustive_pair_fibers(n,q)
        print('EXHAUSTIVE',n,q,'centralizer-fiber-counts',d)
        total+=1
    for q in [2,3]:
        d=exhaustive_trivector_fibers(q)
        print('TRIVECTOR',q,d)
        total+=1
    for n,q in [(5,3),(5,5),(6,3),(7,3),(7,5)]:
        random_element_checks(n,q)
        total+=1
    for q in (3,5):
        direct_full_five_checks(q)
        total += 1
    # Additional symbolic identity via independent rank strata at rank five.
    for q in (3,5,7):
        r2=(q-1)*gaussian(5,2,q)
        r4=gaussian(5,1,q)*q*q*(q-1)*(q**3-1)
        by_centers=q**49 + r2*q**47 + r4*q**45 + (q**5-1)*q**51
        by_pairs=q**54+(q**5-1)*(q+1)*q**50
        assert by_centers == by_pairs
        total+=1
    print('VERIFY_OK',total,'exhaustive/rank/sampled/symbolic check configurations')

if __name__=='__main__':
    main()
