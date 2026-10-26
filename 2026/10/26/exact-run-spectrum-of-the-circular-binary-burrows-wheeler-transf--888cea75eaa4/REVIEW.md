# Scientific assessment

## Correctness: PASS

The circular rotation order admits the explicit gap-layer construction: a row with \(t\) leading zeros is indexed by a gap of length at least \(t\), and its BWT predecessor bit is one precisely at equality. Weak gap rank, unit versus nonunit adjacent rank differences, and a separate zero-constant case exhaust the possibilities. The 365 terms are exact geometric-series counts of all nonnegative quadruples, not finite extrapolations. Standalone integer-polynomial convolution verifies each numerator of the rational generating functions identically, and independent direct sorting agrees on 2401 gap tuples and the entire weight-four word population at lengths 4–19.

## Originality: PASS

The examined 2009 paper introduces circular and bijective BWT context; the 2017 BWT fixed-point paper treats a restricted fixed-point property (even when discussing four ones), and the 2023 BWT-runs paper treats morphism effects and general balanced/two-run results. None gives a general all-weight-four count at every run number, nor a stronger result that yields the presented formulas as an immediate special case. Searches of published records on the exact fixed-weight four cyclic BWT run spectrum and variants likewise surfaced no covering claim; this is evidence of noncoverage among checked records, not proof of absolute historical priority. Possible specialized unindexed equivalences remain a residual risk.

## Value: PASS

The BWT run count is a basic space-complexity statistic in run-length compressed text indexes. The exact all-length distribution at the first nontrivial sparse weight beyond the well-studied three-marker case exhibits the threshold for eight runs (length nine), accounts for periodic inputs without necklace-division errors, and supplies a repeatable structural rank-pattern method instead of a table of small lengths. It is an infinite uniform classification with an inherent coding/indexing motivation.

## Scope and risks

The assertion is limited to binary circular BWT without a sentinel and to Hamming weight four; no direct claims about arbitrary weight or optimal compressors follow. Historical priority could be changed by an unlocated specialized fixed-content BWT-run enumeration. The verifier is deterministic and reproducible but not independent external certification.

Self-review: passed. Independent audit: not yet performed.
