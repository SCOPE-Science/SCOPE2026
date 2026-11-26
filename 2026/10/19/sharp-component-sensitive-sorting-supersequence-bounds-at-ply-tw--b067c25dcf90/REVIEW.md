# Independent mathematical audit

## correctness

PASS

In a two-chain partition, the elements of the second chain below and above any first-chain label bound a consecutive range of insertion slots. Each extension chooses an allowed slot for each such label, and first-chain order within each slot preserves that extension. Counting a label once per allowed slot gives n+i(P), including the one-chain case. At ply two, Helly excludes triangles and a minimum-right-endpoint vertex on a shortest cycle forces its neighbors to meet. The resulting forest has n−c edges, precisely the incomparable pairs of the interval order; every strict realization respects this order, which is the only direction required for the upper bound. For the path construction, the displayed points realize every single adjacent swap as well as the identity. Relative to a fixed identity embedding, each swapped edge requires an early extra occurrence of its right endpoint label or a late extra occurrence of its left endpoint label; no occurrence can be charged twice. Adding isolated labels preserves the path cost and gives equality for every n,c, including c=n. Inspected RESULT.md §§1–3 and VERIFICATION.md, checker.py and checker_output.txt. The frozen output records 364 ply-two cases, 2,090 linear extensions and exact path minima for sizes 2–7; the code was inspected, not run, and this output is not the proof.

## originality

PASS

The same sorting-supersequence framework and a material exact unit-interval overlap are established. The supported distinct content is the sharp worst-case bound over arbitrary ply-two intervals with each component count, and the general width-two-poset construction. Neither inspected primary theorem nor the unit-interval catalogue result gives the non-unit upper bound or the general poset result.

## value

PASS

This determines an exact worst-case preprocessing word length at each component count, including non-unit families for which the unit model is not representative. The two-chain insertion construction is useful beyond interval orders. The theorem neither promises shortest words per arbitrary instance nor transfers a smoothness guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
