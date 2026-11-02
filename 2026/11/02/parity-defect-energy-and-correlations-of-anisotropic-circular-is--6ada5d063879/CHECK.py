"""Exact finite-size checks of an anisotropic circular-ladder Ising formula.

All positions and loops are labelled; requires Python 3.9+ and standard library.
Finite enumeration is a consistency test, not an infinite-family proof.
"""

from collections import Counter


def leg_rung_edges(n):
    leg = [(a*n+i, a*n+(i+1)%n) for a in range(2) for i in range(n)]
    rung = [(i, n+i) for i in range(n)]
    return leg, rung


def bond_cut(mask, edges):
    return sum(((mask >> u) ^ (mask >> v)) & 1 for u, v in edges)


def expected_exchange(n, J, K, minority):
    return 2*n*J+n*K-2*(2*J+K)*minority+(4*J if n%2 and minority==n else 0)


def exact_independent_set_count(n):
    leg, rung = leg_rung_edges(n)
    return sum(1 for mask in range(1 << (2*n))
               if all(not (mask>>u&1 and mask>>v&1) for u,v in leg+rung))


def pell_lucas(n):
    # Integer recurrence for (1+sqrt(2))^n+(1-sqrt(2))^n.
    a, b = 2, 2
    for _ in range(n):
        a, b = b, 2*b+a
    return a+(-1)**n


def spin(mask, i):
    return 1 if mask >> i & 1 else -1


def run():
    sector_tests = 0
    field_tests = 0
    correlation_tests = 0
    lines = []
    for n in range(3, 10):
        leg, rung = leg_rung_edges(n)
        size = 1 << (2*n)
        configurations = []
        for mask in range(size):
            plus = mask.bit_count()
            k = min(plus, 2*n-plus)
            M = 2*plus-2*n
            bl = bond_cut(mask, leg)
            br = bond_cut(mask, rung)
            configurations.append((mask, k, M, 2*n-2*bl, n-2*br))
        independent = sum(1 for mask,_,_,_,_ in configurations
                          if all(not ((mask>>u&1) and (mask>>v&1))
                                 for u,v in leg+rung))
        assert independent == pell_lucas(n), (n,independent,pell_lucas(n))
        for J, K in [(1,1), (1,3), (2,1)]:
            energies = [J*ls+K*rs for _,_,_,ls,rs in configurations]
            sector_min = {k: min(energies[i] for i,c in enumerate(configurations)
                                 if c[1]==k) for k in range(n+1)}
            for k in range(n+1):
                assert sector_min[k]==expected_exchange(n,J,K,k),(n,J,K,k,sector_min[k])
                sector_tests += 1
            # Work with twice the field so every total energy is integral.
            field2_values=sorted(set([0,K,2*K,2*(K+J),2*(K+2*J),2*(K+2*J)+2]))
            for h2 in field2_values:
                vals=[2*energies[i]-h2*c[2] for i,c in enumerate(configurations)]
                minimum=min(vals)
                gs=[configurations[i] for i,e in enumerate(vals) if e==minimum]
                counts=Counter(c[2] for c in gs)
                if n%2:
                    if h2<2*K: exp={0:2*n}
                    elif h2==2*K: exp={0:2*n,2:2*n}
                    elif h2<2*(K+2*J): exp={2:2*n}
                    elif h2==2*(K+2*J): exp=None
                    else: exp={2*n:1}
                else:
                    if h2<2*(K+2*J): exp={0:2}
                    elif h2==2*(K+2*J): exp=None
                    else: exp={2*n:1}
                if exp is not None:
                    assert counts==exp,(n,J,K,h2,counts,exp)
                else:
                    assert len(gs)==independent,(n,J,K,h2,len(gs),independent)
                    lowM=2 if n%2 else 0
                    assert set(counts)==set(range(lowM,2*n+1,2))
                field_tests+=1
                if n%2 and n<=7 and h2 in [K,2*K,2*(K+J)]:
                    # Same-leg and across-leg correlations, including the lower crossing.
                    for r in range(n):
                        row=sum(spin(c[0],0)*spin(c[0],r) for c in gs)
                        expected_row=(-1)**r*(n-2*r)
                        assert row*n==expected_row*len(gs),(n,J,K,h2,'row',r)
                        correlation_tests+=1
                        cross=sum(spin(c[0],0)*spin(c[0],n+r) for c in gs)
                        if r>0:
                            assert cross==-row,(n,J,K,h2,'cross',r)
                        else:
                            correction=0 if h2<2*K else (1 if h2==2*K else 2)
                            assert cross*n==(-n+correction)*len(gs),(n,J,K,h2,'rung')
                        correlation_tests+=1
        lines.append(f'n={n}: {size} labelled configurations, independent sets={independent}')
    print('EXHAUSTIVE EXACT CHECKS PASSED')
    print('\n'.join(lines))
    print(f'fixed-magnetization sector comparisons: {sector_tests}')
    print(f'ground-state field/degeneracy comparisons: {field_tests}')
    print(f'exact rational correlation comparisons: {correlation_tests}')
    print('All formulas tested at J,K=(1,1),(1,3),(2,1).')
    print('Scope: n=3,...,9. Infinite-family theorem requires the analytic proof.')


if __name__=='__main__':
    run()
