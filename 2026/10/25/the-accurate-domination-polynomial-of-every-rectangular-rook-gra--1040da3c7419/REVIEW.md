# Scientific review: accurate domination on rectangular rook graphs

## Correctness — PASS

The claim is proved at the stated quantifiers \(2\le p\le q\), \(0\le k\le pq\). The domination criterion follows from the undominated intersection of an empty row and an empty column. For \(2k\le pq\), any complement meeting all rows supplies a dominating \(p\)-subset that extends to a \(k\)-subset, while after a full selected row is forced any complement meeting all columns supplies a dominating \(q\)-subset. This proves the two simultaneous full-row/full-column obstructions. At \(2k>pq\), no disjoint \(k\)-subset can exist. The two displayed inclusion–exclusion sums count precisely those cases, and the relation \(2(p+q-2)\le pq\) completes the sharp minimum argument. The separate \(p=2\) and \((p,q)=(3,3)\) boundary cases are correctly normalized. Finite testing replays the original definition and coefficients on actual labeled boards; it is not substituted for proof.

## Originality — PASS, with explicit residual risk

The closest full-text primary sources are Cyman–Henning–Topp (arXiv:1710.03308v1, 2017), which treats accurate domination structurally, chiefly for trees and coronas, and Alikhani–Safazadeh–Ghanbari (arXiv:2101.10185v1, 2021), which enumerates accurate dominating sets for paths, cycles and other specified graph classes. The latter's half-order observation already covers the high-cardinality half of the present polynomial, so only the complete rook-graph low-half classification, its resulting coefficients, the minimum formula and exceptional multiplicities are claimed as new. The line-graph translation to edge domination is an equivalent formulation rather than an independent novelty claim. Search comparisons of titles, parameters and implications found no indexed result covering these additional conclusions.

The full text of the 2022 paper *Accurate and Connected Accurate Domination Polynomials of Graphs*, DOI:10.22457/apam.v25n2a02861, was not obtained. Its available abstract mentions standard graph classes without identifying the rook family; it remains an explicit possible priority risk. The small-graph atlas of the same period may contain isolated small rook graphs, which cannot supply this two-parameter result by itself. Negative database searches alone are not treated as proof of absolute novelty.

## Value — PASS

Accurate domination is a natural nonlocal constraint: it requires excluding *all* equally large disjoint dominating rivals. The complete characterization shows that this quantifier collapses to a sharp size threshold and two geometric full-line obstructions in a natural line-graph family. The exact polynomial counts every size, while the minimum solution space changes from all \(\binom{2q}{q+1}\) sets in width two to only \(pq\) cross-shaped sets in the generic range, with a separate \(3\)-by-\(3\) exception. These structural and enumerative results are not consequences of the known numerical minimum for ordinary domination or of the general high-half observation alone. No downstream theorem or uniqueness beyond the inspected record is asserted.

## Scope and outstanding limitations

The statement is limited to two-factor rectangular rook graphs; it makes no assertion about arbitrary graphs, higher Hamming products, or independent certification. The exhaustive program covers finitely many parameter pairs; it provides consistency checks but not a proof of the infinite claim. The incomplete 2022 full-text comparison and potentially unindexed equivalent publications are bibliographic risks.

Self-review: passed. Independent audit: not yet performed.
