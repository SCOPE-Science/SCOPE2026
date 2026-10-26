# Review of joint nearest-cover multiplicities

## Correctness
**PASS.** For a syndrome matrix, the column space must lie inside the span of its accessed affine parity-check columns. The first-coordinate functional divides the problem into two exact cases. In the nonzero-first-row case, affine bases of the syndrome image give all and only minimal supports; in the zero-first-row case, affine bases in translates of that image do so. The proof verifies that the uniquely determined coefficient matrices use every chosen column, rather than silently counting nonminimal supports. Gaussian rank enumeration gives the populations. Exact independent enumeration covered eight parameter pairs, including every one of 4096 syndromes in the \((m,t)=(3,3)\) case.

## Originality
**PASS with residual risk.** Elimelech–Wei–Schwartz (ISIT 2022, Proposition 11) already proved the *maximum* joint distance for this code family. The result here does not rename that fact: it distinguishes every syndrome's minimum access count and counts *all optimal access sets* with formulas depending on rank, parity, and a factorial quotient. Elimelech–Firer–Schwartz (2021) defines the model, while Li–Shangguan–Wei (2026) proves optimal *asymptotic rates*; neither yields this per-syndrome exact tie spectrum as a stated theorem. The geometric 2026 paper of Alfarano et al. is relevant; only its abstract was accessible, so implicit equivalent coverage there remains possible. Database searches were negative but are not proof of absolute priority.

## Value
**PASS.** The exact number of equally optimal access choices controls redundancy and selection flexibility in joint linear queries. This is not merely another radius bound: two syndromes with the same optimal access count can have one or exponentially many optimum solutions. For fixed \(t\), the deepest \(2^{-t}\) fraction of syndromes in the limit carries \(\Theta(2^m)\) optimal corrections each. This all-parameter profile provides a natural finite-length benchmark for analyzing access ambiguity and tie handling.

## Limitations
The result covers a highly symmetric binary code family, not arbitrary linear codes. It does not bound physical decoder runtime or establish a priority claim beyond the sources examined. The recent geometric framework paper requires further full-text checking in an independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
