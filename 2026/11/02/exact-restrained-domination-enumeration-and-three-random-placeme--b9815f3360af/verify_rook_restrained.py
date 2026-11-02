"""Independent finite checks for restrained domination on rook graphs.

No graph-theoretic characterization is assumed by the direct exhaustive predicate.
Usage: python verify_rook_restrained.py
"""
from collections import Counter
from math import comb, factorial


def polynomial_from_formula(m, n):
    # Counts complements U, with t marking |U|.
    coeff = [0] * (m*n+1)
    for a in range(min(m, n)+1):
        factor = (-1)**a * comb(m,a) * comb(n,a) * factorial(a)
        forced = a
        remaining = (m-a)*(n-a)
        for k in range(remaining+1):
            coeff[forced+k] += factor*comb(remaining,k)
    for a in range(1,m+1):
        for b in range(1,n+1):
            factor = (-1)**(a+b) * comb(m,a)*comb(n,b)
            forced = a*n + b*m-a*b
            remaining = (m-a)*(n-b)
            for k in range(remaining+1):
                coeff[forced+k] -= factor*comb(remaining,k)
    return coeff


def direct_predicate(m, n, selected_mask):
    total = m*n
    for v in range(total):
        if (selected_mask>>v)&1:
            continue
        r,c=divmod(v,n)
        yes_selected = False
        yes_unselected = False
        for w in range(total):
            if w == v:
                continue
            rr,cc=divmod(w,n)
            if rr == r or cc == c:
                if (selected_mask>>w)&1:
                    yes_selected = True
                else:
                    yes_unselected = True
        if not (yes_selected and yes_unselected):
            return False
    return True


def structural_predicate(m,n,selected_mask):
    outside = [[not(bool((selected_mask>>(i*n+j))&1)) for j in range(n)] for i in range(m)]
    all_u_rows = any(all(row) for row in outside)
    all_u_cols = any(all(outside[i][j] for i in range(m)) for j in range(n))
    if all_u_rows and all_u_cols:
        return False
    for i in range(m):
        for j in range(n):
            if outside[i][j] and sum(outside[i]) == 1 and sum(outside[ii][j] for ii in range(m)) == 1:
                return False
    return True


def verify():
    subsets = 0
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        raw=Counter()
        for s in range(1<<(m*n)):
            p=direct_predicate(m,n,s)
            q=structural_predicate(m,n,s)
            assert p==q, (m,n,s,'structural disagreement')
            if p:
                raw[m*n-s.bit_count()]+=1
            subsets +=1
        formula=polynomial_from_formula(m,n)
        assert formula == [raw[i] for i in range(m*n+1)], (m,n,formula,raw)
        print(f'{m}x{n}: {1<<(m*n)} subsets; {sum(raw.values())} restrained dominating sets; polynomial OK')
    print(f'TOTAL: {subsets} direct-subset and structural comparisons; all passed')
    # Exact factorial moments of isolated U-edges for the near-all-selected critical window.
    # These are identities, not a numerical substitute for the asymptotic proof.
    import math
    for nn in (100,1000,10000):
        qq=(math.log(nn)+math.log(math.log(nn)))/(2*nn)
        mu=nn*nn*qq*(1-qq)**(2*nn-2)
        pair=(nn*(nn-1))**2*qq**2*(1-qq)**(4*nn-6)
        print(f'n={nn}: E[Z]={mu:.6f}, E[(Z)_2]/E[Z]^2={pair/mu**2:.6f}')


if __name__ == '__main__':
    verify()
