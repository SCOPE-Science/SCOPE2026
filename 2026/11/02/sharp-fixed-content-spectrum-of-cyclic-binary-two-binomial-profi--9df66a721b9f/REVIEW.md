# Scientific review

## Correctness — PASS

The fixed-content reduction of the complete two-binomial profile to the scattered `01` statistic follows from partitioning all mixed ordered position pairs. The rotation update is precisely \(-q\) for a moved zero and \(+p\) for a moved one, yielding the integer height walk \(h_i=NB_i-qi\). Collision congruences give the lower bound and its exact periodicity equality case. A length-\(N/d\) balanced window exists by integer averaging and unit-step sliding; removing it preserves the outside heights, so induction on the content gcd proves the upper bound. The two-run word attains it by direct intersection counting of two arithmetic progressions. Adjacent swaps change at most one height and fixed-composition strings form a connected swap graph, giving the entire integer range. Boundary cases \(d=1\), \(p=1\), \(q=1\), repeated rotations and cyclic arcs are covered. Independent implementation of literal `01`-pair counting confirms the theorem across 32,738 mixed binary words through length 14 and 9,801 witness parameter pairs. All unbounded conclusions follow from the proof.

## Originality — PASS with significant historical risk

Rigo–Salimov (2013) supplies the two-binomial context; Lejeune–Rigo–Rosenfeld (2020) gives general equivalence via Parikh matrices. Neither inspected full text proves a universal exact fixed-composition spectrum over cyclic rotations. Richomme (2025) studies geometry of the same scattered coefficient, without a stated circular spectrum in its inspected text. Relevant published mathematical-record queries found nearby read-multispectrum and bracelet-orbit results but no dominating theorem. Chuan (2004) is especially close because its conjugacy-class moments are **exactly affinely equivalent** to the rotation `01` statistic. Its accessible abstract concerns spreads and Christoffel words, not the present range of cardinalities; its unavailable complete text means historical priority cannot be established conclusively, and coverage might be found there. This is a substantive explicit residual risk rather than a claim of exhaustive novelty.

## Mathematical value — PASS

For every prescribed nondegenerate binary content, the theorem completely classifies the attainable numbers of distinct scattered-subsequence profiles on cyclic rotations, identifies all minimizers and an extremal maximizer, and supplies an exact balanced-arc collision test. The all-parameter no-gaps result uses a nontrivial removal induction and swap continuity; it is a structural answer to a natural family of circular binomial-equivalence counting questions, not a small computed case or trivial normalization.

## Limits

The exact historical relation to the inaccessible original Chuan (2004) paper deserves independent investigation. The claim concerns only length-at-most-two scattered binomial equivalence over a binary alphabet. The finite checker is corroborative, not an infinite proof. Independent mathematical assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
