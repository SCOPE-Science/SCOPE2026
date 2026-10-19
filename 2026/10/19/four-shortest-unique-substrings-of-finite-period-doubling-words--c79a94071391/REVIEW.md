# Scientific review

**Correctness — PASS.** The proof directly establishes parity recognition for all factors of length at least three, proves exact threefold occurrence of the quarter-length suffix, and constructs multiplicity-preserving desubstitution correspondences. Induction from the explicitly checked eight-letter base word yields the four singleton factors at the claimed length and excludes every smaller length. The standalone checker independently counts factors and suffix occurrences through order thirteen.

**Originality — PASS within examined literature.** Searches for the shortest-unique-factor law and alternative naming conventions found related period-doubling attractor results but no equivalent four-SUS statement. The accessible 2026 period-doubling-attractor manuscript studies *attractor pairs* and proves parity of factor positions, not multiplicities of shortest unique factors. The 2026 packed-string SUS paper concerns generic algorithms and gives no family-specific formula. Unindexed prior work remains a residual risk; absence of a search hit is not claimed as proof of global novelty.

**Value — PASS.** This is a complete infinite-family classification of the exact global shortest-unique substring length, multiplicity and positions for a classical automatic word. It yields an explicit family of algorithmic benchmarks of length \(2^n\) with only four optimal witnesses, and a sharp linear-scale boundary \(2^{n-2}+1\) for uniqueness. It is a structural result, not an isolated numerical tabulation; no unproved downstream theorem is claimed.

**Scientific limitations.** The statements concern complete dyadic morphic iterates, not general prefixes, and do not classify longer minimal unique factors. The originality review cannot exclude differently formulated unindexed results. Computations are corroboration, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
