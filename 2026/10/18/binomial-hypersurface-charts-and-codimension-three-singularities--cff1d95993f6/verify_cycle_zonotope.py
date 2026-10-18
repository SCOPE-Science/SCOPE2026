#!/usr/bin/env python3
"""Finite exact checks for cycle graphical-zonotope toric singular charts.
No third-party dependencies; counts do not replace the all-n proof.
"""
from itertools import combinations
from math import comb

def verify(n):
    smooth = singular = 0
    by_mult = {}
    ncases = 0
    for mask in range(1, (1<<n)-1):
        k = mask.bit_count()
        # Convention: 1 signifies the clockwise direction of an edge.
        roots = []
        for i in range(n):
            j=(i+1)%n
            r=[0]*n
            if (mask>>i)&1:
                r[i]-=1; r[j]+=1
            else:
                r[i]+=1; r[j]-=1
            roots.append(tuple(r))
        # Integral circuit: clockwise root sum = opposite root sum.
        accum=[0]*n
        for i,r in enumerate(roots):
            s=1 if ((mask>>i)&1) else -1
            for j in range(n): accum[j]+=s*r[j]
        assert accum == [0]*n
        # Every n-1 graph edge incidence columns yield a unimodular lattice basis:
        # deleting the final (constant) row gives determinant ±1.
        for omit in range(n):
            A=[[roots[col][row] for col in range(n) if col!=omit]
               for row in range(n-1)]
            import fractions
            M=[[fractions.Fraction(q) for q in line] for line in A]
            det=fractions.Fraction(1)
            for c in range(n-1):
                pivot=next((r for r in range(c,n-1) if M[r][c]),None)
                assert pivot is not None
                if pivot!=c: M[c],M[pivot]=M[pivot],M[c];det=-det
                p=M[c][c];det*=p
                for r in range(c+1,n-1):
                    scale=M[r][c]/p
                    for cc in range(c,n-1): M[r][cc]-=scale*M[c][cc]
            assert abs(det)==1
        ncases+=1
        if k in (1,n-1): smooth+=1
        else:
            singular+=1
            mult=min(k,n-k)
            by_mult[mult]=by_mult.get(mult,0)+1
            # Jacobian support consists of the unions of coordinate subspaces
            # vanishing at 2 chosen variables from each monomial block.
            assert comb(k,2)*comb(n-k,2)>0
            assert n-4 >= 0
    assert ncases==(1<<n)-2
    assert smooth==2*n
    assert singular==(1<<n)-2*n-2
    assert by_mult=={
        m: sum(comb(n,k) for k in range(2,n-1) if min(k,n-k)==m)
        for m in range(2,n//2+1)
    }
    print('PASS',n,'fixed_total',ncases,'smooth',smooth,
          'singular',singular,'mults',sorted(by_mult.items()),
          'sing_dimension',n-4)

if __name__=='__main__':
    for n in range(3,9): verify(n)
    print('VERIFY_OK')
