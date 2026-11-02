# Scientific review

## Correctness — PASS

The claim covers every integer alphabet size \(q\ge2\). In a nonconstant cyclic edge-label sequence, \(t\) appearances of one edge label produce at most \(t-1\) adjacent equal-label pairs. The two oppositely centered palindromes on each distinct symbol pair therefore force three edge traversals, while every constant palindrome forces two loops. Closed-walk vertex degree parity forces at least \(q/2\) additional nonloop traversals when the alphabet is even. A connected Eulerian multigraph with one loop per symbol and one intersymbol edge per pair (plus a perfect matching for even alphabets) expands to a cover meeting this bound; the equality case enforces all asserted profile conditions. The actual standalone verifier constructs and checks covers for \(2\le q\le30\) and independently computes exact minima for \(q=2,3,4\).

## Originality — PASS, residual risk acknowledged

The initial 2019 Chen–Kitaev–Sun universal-cycle paper and the 2020 full-text article address exact-once factor covers after deleting a few words; their quantified existence probabilities and de Bruijn-graph constructions do not give shortest **at-least-once** covers for the family of all three-letter palindromes or the mandatory adjacency profiles. Searches for cyclic palindrome covers, palindrome superstrings, Eulerian parity corrections, and the exact formula found no equivalent statement in accessible scientific records. General shortest-superstring literature supplies an algorithmic setting, not an explicit value for this family. A hidden older graph-walk or superstring specialization remains the main novelty risk; absence from searches does not prove historical uniqueness.

## Value — PASS

All three-letter palindromes are a natural reversal-symmetric test family, and the minimum cyclic covering length gives an exact unavoidable observation budget. The optimum changes by a sharp \(q/2\) parity correction, and every optimum has an explicit constrained adjacency spectrum: a complete characterization at the level of pair counts. The construction applies uniformly to arbitrary alphabet size and shows that the parity obstruction, not an algorithmic search artifact, is the only excess needed. The assertion is an infinite structural optimum rather than a small-census calculation.

## Scientific boundaries

No theorem is claimed for longer palindromes or non-cyclic covers; no independence or external certification has occurred. Exhaustive BFS covers only \(q\le4\), while the proof applies to all \(q\ge2\). The source comparison remains subject to independently reviewing further historical shortest-superstring literature.

Self-review: passed. Independent audit: not yet performed.
