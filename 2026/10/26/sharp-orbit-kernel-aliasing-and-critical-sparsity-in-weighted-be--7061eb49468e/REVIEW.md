# Scientific review: sharp orbit-kernel aliasing and critical sparsity

## Correctness
**PASS.** Fourier-sector orthogonality reconstructs the exact projection coefficient, with all normalizations specified. Strict variance monotonicity proves the unique finite optimizing radius when \(m\le N\). Uniform Riemann sums, dominated series comparisons and a two-leading-alias AM–GM bound establish the three density regimes and the sharp near-degree square-root deficit. The supplied checker passed 630 independently reconstructed finite numerical assertions. It does not replace the analytical asymptotic proof.

## Originality
**PASS (best-knowledge, not independent priority certification).** The closest literature covers broad existence of weighted Bergman best-kernel approximants, RKHS kernel-approximation criteria and older sampling by Bergman kernels. The closest public orbit-kernel finding concerns Szegő frame determinants, not monomial energy capture. Searches included aliases using congruence residues, root-of-unity Gram matrices, negative-binomial weights and sampling density; no inspected mathematical statement implied the optimized all-regime theorem. A plausible 2021/2022 primary paper was available only through its abstract and first page, so hidden equivalence remains possible.

## Mathematical value
**PASS.** The rotationally symmetric kernel dictionary is a natural reproducible sparse approximation benchmark. The theorem gives a precise obstruction when sampling density stays below one and a sharp square-root recovery rate at the critical density, across all \(\alpha>-1\). The result has a mathematically motivated scope; it is not an unrestricted best-node theorem.

## Limitations
The optimized configurations are restricted to common-radius regular polygons. Endpoint Hardy behavior is not claimed. The density-dependent macroscopic constant has a convergent series characterization and unique variational optimizer, not an elementary expression. Full-text priority comparison for one source and independent scientific validation remain open.

Self-review: passed. Independent audit: not yet performed.
