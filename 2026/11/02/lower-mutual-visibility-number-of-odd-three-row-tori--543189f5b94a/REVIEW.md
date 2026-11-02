# Scientific review: odd three-row toroidal lower mutual visibility

## Correctness

PASS. All quantifiers are over odd \(n=2k+1\) with integer \(k\ge2\). Every geodesic in \(K_3\square C_n\) has at most one row change, and odd-cycle column geodesics are unique. The lower-bound extension argument handles empty rows and occupancy patterns \((1,1,1)\), \((2,1,1)\). The upper bound checks all ten pairs of the proposed five-set and uses six exhaustive ranges of unselected vertices to show no sixth vertex can be added. The standalone graph-BFS verifier checks the construction at twelve odd lengths through \(n=51\) and exhaustively rules out all smaller maximal sets through \(n=9\). Computation is not substituted for the infinite proof.

## Originality

PASS on the evidence reviewed, with an unindexed-prior-result risk. Brešar and Yero (arXiv:2307.02951, Sections 2 and 6) explicitly give the lower-visibility formulas for two path factors and two complete factors and pose the toroidal case as a problem; for \(n\ge5\), \(C_3\square C_n\) is neither of those two factor families. Cicerone et al. (arXiv:2304.00864, Section 4) establish maximum, total, dual and outer visibility values of tori, not the inclusion-minimal maximal ordinary-visibility parameter. Cicerone, Di Stefano and Klavžar (arXiv:2112.13024, Section 3) address maximum visibility in Cartesian products. The corresponding mathematical-record searches and recoverable previously available claims revealed no covering theorem. An undiscovered stronger source remains possible; publication priority is not independently certified.

## Mathematical value

PASS. The previously articulated toroidal-grid problem motivates this exact natural invariant. The sharp constant value for every odd length is counterintuitive in an arbitrarily long torus and follows from a constructive arrangement whose maximality requires a six-case global geodesic obstruction. It gives a genuine infinite subfamily rather than an unmotivated finite computation. This does not purport to solve even-length or all-width tori.

## Validation scope and limitations

The proof is complete for the stated family; the verifier is finite and does not constitute an independent audit. The available literature comparisons reduce but cannot eliminate priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
