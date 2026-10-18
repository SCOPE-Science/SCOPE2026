# Scientific review

## Correctness
PASS. Independent sampling and orthogonality give the exact finite-horizon expected squared-error identity. An exchange argument proves the all-cardinality consecutive-band classification, and exact algebra proves the three-mode divergence. The standalone checker passed 1050 exhaustive random-spectrum subset comparisons, 121 enumerated-path checks and five analytic parameter checks; the infinite family follows from proof rather than tests.

## Originality
PASS with residual bibliographic uncertainty. Searches covered the spectral-band optimization, aliases such as fixed-row subspace constraints, diagonal sampling, and the Frobenius row-ID surrogate. The 2026 source supplies the general rate and surrogate, but not a statement selecting the exact minimizing fixed subset over all diagonal spectra, nor a sharp unbounded separation from that surrogate. Relevant sections of two earlier Lok–Rebrova primary manuscripts similarly supply subspace-constrained frameworks and rates without the optimization result. The exact minimax set comparison, rather than a re-labeling of the original convergence formula, is the assessed increment; a previously published equivalent combinatorial optimization cannot be excluded absolutely.

## Value
PASS. Fixed row selection is a substantive algorithm-design problem, and the exact all-horizon classification provides a complete benchmark for the orthogonal-row specialization. The diverging exponent ratio proves that minimizing the residual Frobenius norm can misalign badly with expected-error convergence optimization, even for consistent diagonal problems. This is a structural limitation of a natural proxy, not a claim that every instance or implementation is inefficient.

## Limits
The model is diagonal and uses exact norm-proportional Kaczmarz draws. The analysis excludes correlated rows, initialization work, and alternative sampling distributions. Bibliographic coverage, while targeted, is not exhaustive.

Self-review: passed. Independent audit: not yet performed.
