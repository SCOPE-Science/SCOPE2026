# Review
## Correctness
PASS. The exact published constraints were reconstructed and rewritten using \(s=h+v\) and, for the parity obstruction, \(t=h-v\). The proof treats feasibility, both parameter regimes, all four residue classes, boundary values, nonnegativity, and integrality. The finite replay independently enumerates the integer program and matches the formula throughout its test range and on the source tables.

## Originality
PASS. The primary manuscript and the actual companion `toric.py` path were inspected. The source states the integer program, directs optimal computation to an integer solver, and gives only special-case formulas/tables. Targeted searches for the all-parameter optimizer, feasibility threshold, phase transition, and residue-class penalty did not locate a covering result. Closest indexed knot-theory records concern different invariants. Residual risk remains for uncatalogued or differently phrased parallel work.

## Value
PASS. A closed-form optimizer replaces a solver step in a published knot-theory construction, gives explicit witnesses for every feasible parameter pair, and identifies the exact \(q\equiv2\pmod4\) parity penalty. This is a motivated structural simplification of the one-braid construction. It is not presented as the exact toric mosaic number and does not supersede stronger constructions where they apply.

## Closest literature and limitations
The closest source is Heiney--Kipe--Pezzimenti--Pontes--Ta, arXiv:2504.02265v1 / Topology and its Applications 377 (2026), which defines the exact optimization problem. Their companion implementation numerically solves it. The present result should therefore be read as an exact symbolic closure of that optimization problem, not as a new toric-mosaic construction. Other constructions, including the source's full-braid method for part of the \(p=2\) family, can produce smaller mosaics.

Same-model review: passed. Independent audit: not yet performed.
