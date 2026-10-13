# Scientific review: quantitative three-edge cumulant positivity

## Correctness — PASS
The normalized rational transform in Wästlund (2026, equations (36)–(38)) has a defect \(t^2/P_J(t)\) whose coefficients are dominated uniformly in the rectangular dimensions. The comparison logarithm has coefficients no larger than \(1/(2p)\), proved by an explicit recurrence valid at every order. Three matched pole-zero pairs leave at least one unpaired pole contribution \(1/p\) to the comparison cumulant series. Subtraction proves the stated positive bound for all \(p\geq1\), with no asymptotic restrictions. All endpoints \(m,n=3\) are covered. The standalone checker passes 11,500 exact checks, including independent normalization and mean tests; finite tests are not the universal proof.

## Originality — PASS
The primary source, Wästlund (arXiv:2602.07563v1), explicitly asks in Conjecture 10 for positive cumulants and proves only the zero-free property for three-edge matching in Proposition 15. A zero-free disk does not imply coefficientwise positivity of the logarithm. Alm and Sorkin (2002) supply earlier Laplace transforms and variance calculations, but their full text remained inaccessible; their accessible abstract does not state the all-order positivity theorem. The 2026 central limit theorem of Mordant is about a different limit and edge distribution. Targeted literature and published-record searches did not reveal an equivalent result. Residual priority risk is recorded in `AUDIT.json`, not concealed.

## Value — PASS
This establishes the entire first nontrivial cardinality case of a motivated published conjecture: all rectangular dimensions and all cumulant orders simultaneously, with an explicit lower bound. The first nonreal numerator zeros occur in the three-matching regime, so mere real-rootedness arguments no longer work. No claim is made for matchings of four or more edges, nor for arbitrary edge-cost distributions.

Self-review: passed. Independent audit: not yet performed.
