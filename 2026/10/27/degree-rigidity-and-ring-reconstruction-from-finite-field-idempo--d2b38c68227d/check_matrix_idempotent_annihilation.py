#!/usr/bin/env python3
"""Independent finite enumerator for idempotent annihilation in matrix rings.

No external packages, network access, or input files are required.
The field of order 4 uses F_2[x]/(x^2+x+1).
"""
from itertools import product
from collections import Counter, defaultdict


def field_tables(q):
    if q == 4:
        add = [[a ^ b for b in range(q)] for a in range(q)]
        def multiply(a, b):
            poly = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        poly ^= (1 << (i+j))
            if poly & 8:
                poly ^= 0b1100   # x^3 = x^2 + x
            if poly & 4:
                poly ^= 0b111    # x^2 = x + 1
            return poly
        mul = [[multiply(a,b) for b in range(q)] for a in range(q)]
    else:
        assert q in (2,3,5)
        add = [[(a+b)%q for b in range(q)] for a in range(q)]
        mul = [[(a*b)%q for b in range(q)] for a in range(q)]
    return add,mul


def gaussian(n,k,q):
    if k<0 or k>n:
        return 0
    a=b=1
    for i in range(k):
        a *= q**(n-i)-1
        b *= q**(k-i)-1
    return a//b


def gl(k,q):
    z=1
    for i in range(k): z*=q**k-q**i
    return z


def matrix_rank(rows,n,q,add,mul):
    a=[list(row) for row in rows]
    inv=[0]*q
    for x in range(1,q):
        inv[x]=next(y for y in range(1,q) if mul[x][y]==1)
    rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if a[i][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        a[rank]=[mul[inv[a[rank][col]]][v] for v in a[rank]]
        for i in range(n):
            if i!=rank and a[i][col]:
                c=a[i][col]
                a[i]=[add[a[i][j]][mul[c][a[rank][j]]] if q==4 else
                      add[a[i][j]][mul[(q-c)%q][a[rank][j]]] for j in range(n)]
        rank+=1
    return rank


def make_matrix(entries,n,q,add,mul):
    rows=tuple(tuple(entries[i*n:(i+1)*n]) for i in range(n))
    row_codes=tuple(sum(v*q**j for j,v in enumerate(row)) for row in rows)
    lookup=[]
    for coeff in product(range(q),repeat=n):
        out=[0]*n
        for i,v in enumerate(coeff):
            for j in range(n): out[j]=add[out[j]][mul[v][rows[i][j]]]
        lookup.append(sum(v*q**j for j,v in enumerate(out)))
    # product enumerates least-significant digit LAST: reorder lookup to base-q code.
    row_map=[0]*(q**n)
    for coeff,outcode in zip(product(range(q),repeat=n),lookup):
        row_map[sum(v*q**j for j,v in enumerate(coeff))]=outcode
    return rows,row_codes,row_map


def idempotents(n,q,add,mul):
    ans=[]
    for entries in product(range(q), repeat=n*n):
        rows,row_codes,row_map=make_matrix(entries,n,q,add,mul)
        if all(row_map[c]==c for c in row_codes):
            ans.append((rows,row_codes,row_map,matrix_rank(rows,n,q,add,mul)))
    return ans


def rank_product(E,F,n,q,add,mul):
    rows = []
    for c in E[1]:
        outcode=F[2][c]
        rows.append(tuple((outcode//(q**i))%q for i in range(n)))
    return matrix_rank(rows,n,q,add,mul)


def rank_matrix_count(a,b,t,q):
    return gaussian(a,t,q)*gaussian(b,t,q)*gl(t,q)


def predicted(n,r,s,q):
    if s>n-r:return 0
    return gaussian(n-r,s,q)*(2*q**(s*(n-s)) - q**(s*(n-r-s)))


def run(n,q):
    add,mul=field_tables(q)
    e=idempotents(n,q,add,mul)
    expected_total=sum(gaussian(n,r,q)*q**(r*(n-r)) for r in range(n+1))
    assert len(e)==expected_total,(n,q,len(e),expected_total)
    counts=Counter(x[3] for x in e)
    assert all(counts[r] == gaussian(n,r,q)*q**(r*(n-r)) for r in range(n+1))
    graph=[a for a in e if 0<a[3]<n]
    observed_degrees=Counter()
    checked_pairs=0
    for E in graph:
        r=E[3]
        per_s=Counter()
        for F in graph:
            ef=all(F[2][row]==0 for row in E[1])
            fe=all(E[2][row]==0 for row in F[1])
            if ef or fe:
                assert E is not F
                per_s[F[3]]+=1
            checked_pairs+=1
        for s in range(1,n):
            assert per_s[s]==predicted(n,r,s,q),(n,q,r,s,per_s[s],predicted(n,r,s,q))
        d=sum(per_s.values())
        observed_degrees[(r,d)]+=1
    for r in range(1,n):
        degree=sum(predicted(n,r,s,q) for s in range(1,n))
        assert observed_degrees[(r,degree)] == counts[r]
    # Independent reverse-rank distribution conditional on E F = 0.
    conditional=0
    for r in range(1,n):
        E=next(v for v in graph if v[3]==r and
               all(v[0][i][j]==(1 if i==j and i<r else 0)
                   for i in range(n) for j in range(n)))
        for s in range(1,n-r+1):
            reverse=Counter()
            for F in graph:
                if F[3]==s and all(F[2][row]==0 for row in E[1]):
                    reverse[rank_product(F,E,n,q,add,mul)]+=1
            for u in range(min(r,s)+1):
                expected=(gaussian(n-r,s,q)*q**(s*(n-r-s)) *
                          rank_matrix_count(s,r,u,q))
                assert reverse[u]==expected,(n,q,r,s,u,reverse[u],expected)
                conditional+=1
    deg_seq=[sum(predicted(n,r,s,q) for s in range(1,n)) for r in range(1,n)]
    assert all(deg_seq[i]>deg_seq[i+1] for i in range(len(deg_seq)-1))
    if n>=2:
        delta=min(deg_seq)
        Q=(delta+1)//2
        M=observed_degrees[(n-1,delta)]
        A=M//Q
        recovered_q=(A-1)//(A-Q)
        assert (A-1)%(A-Q)==0 and recovered_q==q
        found_n=2
        while recovered_q**(found_n-1)<Q:found_n+=1
        assert found_n==n
    print(f'n={n} q={q} idempotents={len(e)} graph_vertices={len(graph)} '
          f'ordered_tested={checked_pairs} degrees={deg_seq} '
          f'conditional_cells={conditional} status=PASS')
    return checked_pairs


def main():
    total=0
    for n,q in ((2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)):
        total+=run(n,q)
    print(f'ALL_MATRIX_IDEMPOTENT_ANNIHILATION_TESTS_PASSED cases=7 ordered_pairs={total}')

if __name__=='__main__': main()
