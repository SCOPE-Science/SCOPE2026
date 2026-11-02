"""Separate exact-arithmetic checks for two pinned vertices on a weighted cycle.
Run: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction as Q


def formula(n, a, b, x):
    assert 3 <= n and 1 <= a < b <= n and x > 0
    L = b - a
    m = n - L
    A, B = a - 1, n - b
    assert A+B == m-1
    return (Q(L*L + m*m - 2, 6)
            + (x-1)*Q((m-1)*(2*m-1)-6*A*B, 6*(m-1+x)))


def direct(n, a, b, x):
    """Exact trace of principal grounded Laplacian inverse, no use of formula."""
    F = [i for i in range(1,n+1) if i not in (a,b)]
    k = len(F)
    rows = [[Q(0) for j in range(k)] for i in range(k)]
    where = {v: i for i,v in enumerate(F)}
    for u,v,w in ([(i,i+1,Q(1)) for i in range(1,n)]
                  + [(n,1,1/x)]):
        if u in where: rows[where[u]][where[u]] += w
        if v in where: rows[where[v]][where[v]] += w
        if u in where and v in where:
            rows[where[u]][where[v]] -= w
            rows[where[v]][where[u]] -= w
    M = [rows[i] + [Q(int(i==j)) for j in range(k)] for i in range(k)]
    for col in range(k):
        piv = next(j for j in range(col,k) if M[j][col])
        M[col], M[piv] = M[piv], M[col]
        d = M[col][col]
        M[col] = [v/d for v in M[col]]
        for row in range(k):
            if row == col: continue
            t = M[row][col]
            if t: M[row] = [a-t*b for a,b in zip(M[row],M[col])]
    return sum((M[i][k+i] for i in range(k)),Q(0))


def reduced_candidates(n, x):
    pairs = set()
    for L in range(1,n):
        m=n-L
        if x < 1:
            As = {0,m-1}
        elif x > 1:
            As = {(m-1)//2,m//2}
        else:
            As = set(range(m))
        for A in As:
            a=A+1;b=a+L
            pairs.add((a,b))
    return pairs


def optimizers(n,x):
    vals={(a,b):formula(n,a,b,x)
          for a in range(1,n) for b in range(a+1,n+1)}
    best=min(vals.values())
    return {p for p,v in vals.items() if v==best},best


def main():
    xs=[Q(1,7),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(2),Q(5),Q(20)]
    exact=0; position=0;strong=0
    for n in range(3,11):
        for x in xs:
            opts,v=optimizers(n,x)
            cands=reduced_candidates(n,x)
            assert opts <= cands,(n,x,opts,cands)
            position+=1
            if x<1:
                k=n//2
                expected={(1,1+k),(n-k,n)}
                assert opts == expected,(n,x,opts,expected)
                strong+=1
            for a in range(1,n):
                for b in range(a+1,n+1):
                    z=direct(n,a,b,x)
                    f=formula(n,a,b,x)
                    assert z==f,(n,a,b,x,z,f)
                    exact+=1
    print('exact_grounded_inverse_pairs:',exact)
    print('verified_global_candidate_sets:',position)
    print('verified_strong_edge_closed_cases:',strong)
    print('example_n8_resistance_2:',optimizers(8,Q(2)))
    print('example_n8_resistance_5:',optimizers(8,Q(5)))
    print('example_n10_resistance_100:',optimizers(10,Q(100)))
    print('all_checks_passed')

if __name__=='__main__':main()
