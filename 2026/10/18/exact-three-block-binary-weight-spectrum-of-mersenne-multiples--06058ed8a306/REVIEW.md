# Review of the three-block Mersenne multiple spectrum

## Correctness — PASS
The claimed domain is all integers \(m\ge2\). Three \(m\)-bit blocks reduce divisibility by \(2^m-1\) to four possible block sums; zero is excluded and the all-one case is treated separately. The other two sums are complementary, and a two-carry-state transfer matrix exactly enumerates one of them. Explicit carry excursions establish every attainable weight and exclude the gap. The first next-minimum multiplier follows from a complete two-block obstruction and two exact boundary calculations. Cayley–Hamilton proves the recurrence. An independent exact-arithmetic checker compares all \(87898\) multiples in the test intervals for \(m=1,\ldots,8\). Finite tests supplement rather than replace the proof.

## Originality — PASS (best-knowledge comparison)
Elsholtz (arXiv:1602.05974v1) treats low-weight multiples of primes and references the global minimum-weight phenomenon. Clokie et al. (arXiv:2002.02731v1), notably Theorem 4 and Section 3, address unrestricted multiple weights, minimum weights and decision algorithms, not the uniformly parameterized three-block polynomial or sharp finite-window gap. Searches on equivalent three-block carry enumeration and Mersenne Hamming-weight spectra in published-result records did not identify a covering claim. Stolarsky (1980) is a relevant inaccessible original and remains an explicit residual risk, not assumed absent or read. The published-source comparison does not amount to independent validation or an absolute novelty guarantee.

## Value — PASS
The shortest nontrivial three-block window of multiples of \(2^m-1\) has a non-obvious **complete** weight spectrum with a long forbidden terminal interval, an explicit all-degree enumerator, exact boundary multiplicities, and the first occurrence of the next-to-minimal weight. This connects a classical digit-sparsity extremal problem to an explicit two-state carry combinatorics and is substantially stronger than recomputing minima or running a finite table.

## Scope and remaining risks
The restriction \(m\ge2\) prevents overlap of the boundary-coefficient formulas at the degenerate length. The exclusion interval is a finite-cutoff statement. The full 1980 Stolarsky paper was not accessible, and obscurer equivalent formulations may exist. An independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
