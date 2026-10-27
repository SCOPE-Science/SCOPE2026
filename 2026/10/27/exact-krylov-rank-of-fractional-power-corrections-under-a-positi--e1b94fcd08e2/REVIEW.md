# Scientific review

## Correctness — PASS
The universal proof is based on valid scalar-to-matrix Stieltjes representations for \(0<s<1\), the exact Sherman–Morrison resolvent identity, strictly positive scalar integration weights, and independence of distinct simple-pole resolvent functions. The common kernel equals the orthogonal complement of the active spectral projections; polynomial spectral interpolation identifies that span with the full Krylov subspace. All endpoint and support qualifications are explicit. The nonzero exact determinant in the two-dimensional square-root witness and the deterministic standalone consistency checks corroborate but do not replace the proof.

## Originality — PASS
The closest inspected source, Shmueli–Drineas–Avron (arXiv:2201.13156, §§1, 3–4, 7), proves numerical low-rank approximability via eigenvalue decay and observes generic full rank without the exact active-spectrum formula. Beckermann–Kressner–Schweitzer (arXiv:1707.03045, §§1–3, 5) and Beckermann–Cortinovis–Kressner–Schweitzer (arXiv:2008.11501, §§1–4) analyze Krylov compression and approximate corrections, not the simultaneous exact kernel and all-exponents rank classification. Rational-function rank bounds and scaled-identity corrections cover different or strict special cases. Searches of the available mathematical-record index and accessible preceding findings did not identify a statement implying the claim. This is a best-knowledge originality assessment, not a guarantee of publication priority; a more general operator-monotone strictness theorem remains a residual risk.

## Mathematical value — PASS
The exact rank is a natural missing structural invariant in algorithms that explicitly approximate low-rank matrix-function corrections. The theorem completely classifies exact rank, range, kernel, and degenerate repeated-spectrum cases for two families of practically relevant fractional powers. It explains why low-rank **approximation** and exact low-rank **structure** differ, and gives the exact Krylov subspace necessary to contain any correction. The same theorem characterizes the sharp integer-exponent rank collapse and supplies an exact smallest-dimensional witness. No claim of new numerical convergence rates or singular-value decay is made.

Self-review: passed. Independent audit: not yet performed.
