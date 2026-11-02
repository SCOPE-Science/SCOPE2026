# Scientific review

## Correctness — PASS
For every integer \(n\ge2\), \(1\le d<n\), the jump-counter identity \(x+B+dK_x\pmod n\) proves the minimum required number of effective idempotent actions, and the return time from \(d\) to \(0\) proves the independent rotation-letter lower bound. The explicit map \(ab^{n-d}\) gives equality; its exact action on the \(d\)-indexed cycle is proved in `RESULT.md`. Equality of each lower-bound term forces the literal unique optimum. Noncoprime cases are separately impossible by invariant residues. A standalone BFS verifier tested the finite range; no infinite claim relies on enumeration.

## Originality — PASS, subject to priority risks
Don (2015), Proposition 2, already proves the coprimality synchronization criterion and a general \((n-1)^2\) bound; neither is presented as new. Rystsov (2022) gives the regular-group simple-idempotent uniform upper bound, and Rystsov–Szykuła (2023), Theorems 22–23, gives broader structural synchronization criteria. The exact parameter-sensitive minimum and uniqueness of the shortest reset word have not been identified in the inspected primary texts or in semantically ranked research records. Classical \(d=1\) is acknowledged as a known extremal case. The older Rystsov (2000) article and some related complete texts were not inspected; unlocated equivalent specializations remain a genuine risk.

## Value — PASS
This resolves a natural explicit family at every size, including noncoprime impossibility, interpolating between the quadratic Černý threshold and linear reset lengths. The extremal instruction sequence is rigid rather than merely bounded. The exact classification gives useful information about synchronization cost and optimal-word multiplicity beyond previously available general estimates.

## Scientific limits
No independent validation was performed. The proof assumes exactly the two specified input maps, and computational experiments cover finite parameters only. Research priority remains subject to deeper bibliographic checking of older idempotent-automata literature.

Self-review: passed. Independent audit: not yet performed.
