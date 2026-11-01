# Scientific review: three-by-nine grid matching complex

## Correctness — PASS
The exact graph and matching-face enumeration are reconstructed in `verify.cpp`. It enumerates all \(7,594,361\) faces, checks \(3,797,088\) Morse pairs and all \(61,837,314\) oriented Hasse covers, and confirms full topological-sort acyclicity. The remaining critical cells are one vertex, \(173\) eight-cells and \(10\) nine-cells. Exact signed gradient-path recursion computes their attaching degrees. The specified ten-column minor is unimodular (determinant \(-1\)), which is enough for the full integral wedge theorem by the Hurewicz theorem and homotopy cell cancellation. The Euler characteristic \(164\) independently agrees with the resulting \(163\) even-dimensional spheres. The computation is exhaustive for this finite complex, not a proof for all widths.

## Originality — PASS, qualified by source-access risk
The current three-row-grid study (Chauhan–Sharma–Shukla, 2026, arXiv:2609.27366) states connectivity and homological results; its Conjecture 4.1 on an all-width sphere wedge is quoted by a public mathematical account. Its homology table through width nine cannot by itself determine the integral homotopy type. The 2021 article claiming an all-width wedge was formally retracted, and its corrigendum explicitly says the nine-column predicted homology was incorrect. Publicly available full results on three-row-grid reflection characters and symmetry quotients do not imply this nonequivariant homotopy classification. Searches of published mathematical records and the accessible comparison ledger revealed no valid covering result. The full 2026 manuscript was unavailable despite attempted lawful access; a hidden specific-width statement cannot be excluded, and novelty has not been independently established.

## Value — PASS
This is the first width at which the retracted earlier analysis explicitly fails, making a rigorous homotopy classification especially motivated. It supplies a complete finite answer in a family whose general wedge question is still posed as a conjecture, and gives a reproducible integral Morse cancellation rather than extrapolating from computer Betti tables. The value lies in closing an actual homotopy gap, not in recomputing the previously tabulated Betti number.

## Closest literature and limitations
The source paper dated 2026-09-23 is the motivating current treatment, but its full text was not available for direct line-by-line comparison. The 2021 predecessor is retracted and cannot supply a valid all-width proof; the 2019 work treats two-row grids only. The finding is restricted to the exact ordinary three-by-nine Cartesian grid and does not prove the all-width conjecture or equivariant refinements.

Self-review: passed. Independent audit: not yet performed.
