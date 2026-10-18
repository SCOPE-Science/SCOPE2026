# Scientific review: three-shell quadratic Walsh sampling

## Correctness — PASS

The complete claimed domain is integer dimension \(n\ge4\), permutation-invariant strictly positive sampling on exactly three complete Hamming layers, and all characters of degree at most two. The key equivalence converts their entire Gram matrix to degree-four moments of the coordinate sum, using the triangular Krawtchouk basis. The division-of-polynomials argument proves that the two cubic orthogonality relations are both necessary and sufficient; positivity follows from evaluating squared Lagrange polynomials against the full-support binomial measure. This independently checks the potentially non-obvious positivity condition. The single-root discriminant enumerator is algebraically exhaustive, with the excluded zero denominator proved impossible. Endpoint, symmetric, interior, and Pell identities are derived symbolically. The first nonunique dimension is a finite claim, supported by two independent exact enumerators and actual standalone rational verification from the submitted paths, not by extrapolation. Further independent testing would be useful, but no material mathematical gap was found in the specified claims.

## Originality — PASS, best knowledge

The first public eligible source, Bannai–Bannai–Tanaka–Zhu (2020-06-03), develops two-shell relative designs; inspected full text and theorem sections do not supply the full three-shell quadratic Walsh Parseval classification. Gavrilyuk–Suda–Vidali address unweighted tight binary strength-four orthogonal arrays; Carlet–Kiss–Nagy address unweighted binary orthogonal-array simplicity. The closest specific published overlap, *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, calculates one-shell compression eigenvalues and an arithmetic square-dimension resonance. It does not give the weighted three-shell Gram identity, unique positive shell masses, enumeration, first multiple orbit, or Pell coexistence, and the spectral resonance alone does not logically imply them. The earlier linear-band two-shell classification requires only degree-two moments and does not subsume the four-moment problem here. Genuine remaining risk: a classical Krawtchouk/quadrature enumeration or a relative-design appendix under other terminology might contain an equivalent classification. A partially inaccessible related binary-design treatment cannot be assessed beyond its indexed statement; neither its mere inaccessibility nor search failure is treated as novelty proof.

## Mathematical value — PASS

The question is a natural exact Parseval sampling design problem for the complete quadratic Walsh band. Its positive three-shell minimum, all-dimension arithmetic decision rule, complete weight specification, and explicit first and infinite nonuniqueness phenomenon describe structural constraints beyond routine moment fitting. Unlike isolated small samples or arbitrary parameter slices, it classifies an infinite canonical family and identifies the first genuine ambiguity in shell geometry. These facts inform sparse-layer Fourier measurement design without claiming optimality among arbitrary point samplers.

## Evidence and limitations

The formal proof, reproducible `verify.py`, and its actual recorded output establish the precise scope described in `RESULT.md`. Verification in finite dimensions is not substituted for the infinite theorem. General Lagrange quadrature, binomial moments and single-shell Johnson decompositions are prior mathematical methods. No exhaustive search of every unindexed historical quadrature source is possible, and no independent verification is asserted.

Self-review: passed. Independent audit: not yet performed.
