# Independent audit — Second-order digital oscillation for distinct substrings of a uniform random word

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** Gheorghiciuc--Ward's uniform fixed-level estimate applies with the number of windows \(N_k=n-k+1\) and has a summable error over all lengths. The exact increment of the occupancy deficit controls replacement of \(N_k\) by \(n\) with total error \(O_d((\log n)^2)\); replacing the binomial term by the exponential occupancy profile contributes bounded total error. Reindexing the geometric profile gives the periodic phase. The Mellin transform \(\Gamma(1-s)/(s(1+s))\) was independently checked numerically with a cancellation-stable integral, and its lattice poles give the stated Fourier coefficients and phase mean. The elementary collision sandwich is also correct because two distinct length-\(k\) windows match with probability exactly \(d^{-k}\), including overlapping windows.

## Originality

**PASS.** Best-of-knowledge originality passes for the all-length second-order periodic correction, its explicit Fourier series, and the finite collision sandwich. The coefficient-one first-order heuristic and the fixed-length occupancy profile are prior input.

### Equivalent formulations

The search explicitly included digital/trie terminology to catch equivalent formulations not using the phrase distinct-substring correction.

Evidence: The archive search returned this record as the exact match; nearby records concern nonuniform first-order corrections or later variance bounds. No inspected older source stated the same all-length periodic function or Fourier coefficients.

### Broader coverage

These sources are strong prior ingredients or same-object comparisons, but no inspected statement dominates the all-length second-order formula.

Evidence: Gheorghiciuc--Ward Corollary 2.2 gives the uniform fixed-level occupancy approximation, with constants uniform in the window count and substring length; it does not sum all lengths. Ahmadi--Ward gives refined \(k=\Theta(\log n)\) fixed-level subword-complexity asymptotics and Mellin/saddle analyses, not the all-length digital phase. Godbole studies the same all-length expectation. The accessible abstract and secondary publication summary describe lower bounds/expectation results but do not expose the claimed second-order periodic expansion; full text was not obtainable in this audit.

### Exact database or table

The exact formula was compared as an analytic theorem rather than as a title match.

Evidence: No prior published archive entry or standard table with the displayed periodic correction or its Fourier coefficients was located.

### Claim versus prior implication

The final claim is a nontrivial analytic consequence of the fixed-level profile, not a restatement of it.

Evidence: The 2007 fixed-level theorem is essential input, but obtaining the global linear term requires uniform summation through the transition scale, control of varying window counts, and Mellin extraction of the lattice phase. An extremal maximum count does not determine the random expectation at linear order. The accessible Godbole material does not state an expansion strong enough to imply the periodic function.

### Source inspections

- **On Correlation Polynomials and Subword Complexity** — ESSENTIAL_PRIOR_NOT_COVERING.
  Identifier: https://doi.org/10.46298/dmtcs.3553
  Material read: complete 18-page paper, including Theorem/Corollary 2.2 and the uniformity statement.
  Evidence: The source gives the uniform fixed-length expectation approximation and explicitly permits the two parameters to vary together; it does not perform the all-length sum.
- **Asymptotic Analysis of the kth Subword Complexity** — RELATED_NOT_COVERING.
  Identifier: https://doi.org/10.3390/e22020207
  Material read: complete 34-page open-access paper, including the logarithmic-length expectation sections.
  Evidence: The paper treats the \(k\)-th subword complexity at logarithmic scales rather than the total across all lengths.
- **The Expected Number of Distinct Substrings in an Alphabet String** — ACCESS_RISK.
  Identifier: https://arxiv.org/abs/2609.19409
  Material read: abstract, bibliographic record, and accessible publication summary; full text could not be retrieved from arXiv/OA, and an authorized institutional retrieval attempt was blocked.
  Evidence: Accessible descriptions confirm the same random variable and expectation problem, but do not expose a second-order digital oscillation theorem. No whole-document noncoverage conclusion is drawn.

### Checked sources

- https://doi.org/10.46298/dmtcs.3553
- https://doi.org/10.3390/e22020207
- https://arxiv.org/abs/2609.19409
- https://doi.org/10.37236/1761
- https://mathoverflow.net/questions/253576/expected-number-of-substring-in-random-string
- Resultary published-finding semantic search

### Residual risks

- The full Godbole paper could not be inspected, so equivalent second-order material there remains a material but unresolved access risk; the accessible descriptions do not by themselves show coverage.
- Older trie/suffix-tree Mellin analyses may contain an implicit equivalent periodic expansion under different terminology.

## Scientific value

**PASS.** The result resolves the complete linear-order correction to a natural all-length random-string statistic, identifies the digital phase and its Fourier spectrum, and quantifies an unusually small binary oscillation. The exact phase is potentially reusable in expectation comparisons and is more informative than the known first-order coefficient.

## Final assessment

The unchanged final claim passes correctness, originality, and scientific value. No research claim or slogan change is required.

This assessment is not formal verification or expert attestation and does not guarantee that no undiscovered prior art exists.
