# Review: Nine symmetry types and exact click distances for Petersen acyclic orientations

## Correctness

PASS. Exhaustive masks represent every one of the 32768 orientations of the fifteen Petersen edges without quotienting. Two acyclicity tests agree for every mask. Legal single-vertex source/sink moves are computed directly and their endpoints checked. BFS from every one of 16680 acyclic orientations gives all exact click distances, and a mathematically different potential-median calculation agrees for every reachable ordered pair. Component sizes sum to 16680 and non-diagonal pair counts sum to 235080. The complete 120-element symbol-permutation action gives nine component orbits, and global reversal exchanges exactly the two size-21 families. `verify_click_petersen.py` ended in `VERIFY_OK`.

## Originality

PASS for the *refined finite component geometry and symmetry census*, not for general click theory or its Petersen class count. Macauley–Mortveit (2007, 2011) already give the equivalence and class count as a Tutte evaluation. Cameron (2015) already gives the 16680 acyclic orientation count and 168 automorphism orbits **on orientations**. Aichholzer et al. and the later published graph-flex geodesic theorem cover general shortest flip methodology. No inspected source states the nine orbits on click *components*, the size/diameter table or the exceptional reversal pairing. Unindexed prior computations are a remaining risk.

## Value

PASS. A canonical cubic graph serves as a complete, reproducible model of toric click-conjugacy reconfiguration. The nine-orbit refinement and chiral pair contain structure invisible to the Tutte polynomial, classical orientation orbit counts and mere pairwise distance formulas. The complete finite result is motivated without requiring an infinite family generalization.

## Limitations

The graph-specific census does not imply a uniform theorem for larger Kneser graphs. The general distance method and class count are prior knowledge. The program is exhaustive but has not undergone independent mathematical audit. Literature indexing may be incomplete.

Self-review: passed. Independent audit: not yet performed.
