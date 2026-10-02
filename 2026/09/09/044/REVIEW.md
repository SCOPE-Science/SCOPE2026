# Review status

Independent mathematical audit date: 2026-09-30 UTC.

Disposition: **passed**.

Correctness: PASS. A fresh Murnaghan-Nakayama implementation independently rebuilt the S6, S7 and S8 character tables, re-derived all 155 rows, and reproduced the unique global family maximum |s-a|=5 at lambda=(4,3,1), nu=(4,2,2) with (s,a,g,m)=(6,1,7,5). It also confirmed that the (3,2,1) square has g>0 and s>0 for all 11 irreducibles. The character identities s=(g+m)/2 and a=(g-m)/2 are standard, and the package's second recursion checks column orthogonality, transpose symmetry, exact divisibility and the stored table.

Originality: PASS. The closest primary splitting paper gives broad formulas for hooks, several two-part families and selected shallow constituents, while explicitly treating the splitting problem as sparse and more difficult beyond those regimes. No inspected source supplied the complete nine-square non-hook three-row S6-S8 table, its 155 (s,a,g,m) rows, or the stated family extremum. The exact census is not implied by the cited general unsplit-positivity results.

Scientific value: PASS. The nine squares form the complete non-hook three-row family for n=6,7,8, so the cutoff is a natural finite classification rather than an arbitrary slice. The split data refine ordinary Kronecker coefficients, identify an extremal symmetric/alternating imbalance, and record a complete symmetric-part containment phenomenon for the S6 staircase. The result is finite, but it is a reusable reference table for a motivated unresolved splitting regime.

Evidence: `INDEPENDENT_AUDIT_2026-09-30.md` and `INDEPENDENT_AUDIT_2026-09-30.json`.
