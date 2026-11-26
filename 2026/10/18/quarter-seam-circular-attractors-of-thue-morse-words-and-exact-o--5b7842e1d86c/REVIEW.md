# Independent mathematical audit

## correctness

PASS

The transport induction is valid: a factor crossing the internal boundary of U_{r+1}(a) sees the same ordered pair of r-blocks at the seam between two U_{r+1}(1-a) blocks; one inside a single r-block can be transported first at scale r, then embedded at a scale-(r+1) seam with those last and first r-blocks. The cyclic quarter-block pattern 0110 realizes 01, 11, 10 and 00; complementing the last-letter map when r is odd still gives seams with equal letters of each kind. Thus either endpoint at each seam suffices, also for singleton factors, and the four pairs are disjoint. A direct substitution and linear window count gave 40 length-13 factors in the 64-letter t_6; the prefix survives for all n >= 6 and three positions can cover at most 39 such factors. A fresh exact cyclic enumerator confirmed minima 2,2,4,4,4,4,4 and counts 2,2,151,96,96,80,80 at n=2..8, and exact set equality with all five endpoint families at n=7 and 8. Each constraint is the union over all occurrences of one factor, and branching over all positions of a missed constraint is exhaustive; dropping supersets and merging identical states preserves solutions. Replay: python3 /workspace/branches/cb805c78-968b-4328-8202-1fa26276691a/independent_check.py 8 (output full_run.txt in the same directory). For the 40-factor count, apply 0->01 and 1->10 six times to 0 and count {w[i:i+13] for i in range(52)}. No classification beyond n=8 is certified or claimed.

## originality

PASS

The inspected work establishes important linear and circular antecedents, but not the specific circular quarter-seam theorem or the order-7/8 enumeration. Credit the linear optimum and seam-based methods as prior; the distinct result is the endpoint-robust cyclic construction and the exact cyclic families, not the numeral four in isolation.

## value

PASS

Gives the exact optimum of an established circular compression invariant on a canonical substitution family, and a uniform construction robust to the choice of left or right endpoint at every quarter seam. The complete 80-set descriptions at consecutive larger dyadic orders are useful exact examples that distinguish cyclic from linear coverage and can test lifting conjectures; two equal counts do not establish stabilization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
