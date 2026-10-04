# Same-model review

## Correctness
**PASS.** The proof was reconstructed from the source definition rather than inferred from experiments. In the scalar saturated regime, Theorem 2 identifies \(O^*\) with a projection residual. Rewriting that residual as a cyclic-orbit altitude and diagonalizing the circulant orbit matrix gives the reciprocal-Fourier formula, with an explicit affine-dependence proof when a non-DC Fourier coefficient vanishes. The binary two-point spectrum then reduces the calculation to a secant-square sum, and divisor optimization proves the global row-ordering statement. The bundled checker independently reconstructs the residual and verifies every separation for \(3\le n\le30\). Risk: the claim is only about the source proxy; the files consistently avoid equating proxy collapse with universal absence of statistical power.

## Originality
**PASS.** The closest source is Lei--Bickel, arXiv:1907.06133 / DOI 10.1093/biomet/asaa079. It gives the general residual formula for \(O^*\), states that row order matters, and poses the general ordering optimization as a nonlinear traveling-salesman problem. The inspected full text does not state a Fourier altitude law, a two-active-row binary theorem, a gcd/parity collapse criterion, or the exact optimizer. Alias searches covered CPT terminology, cyclic-shift/simplex terminology, Fourier/harmonic-mean terminology, sparse binary predictors, power-of-two sample sizes, and later permutation-power work. Classical circulant theory supplies only the DFT diagonalization ingredient. Residual risk: generic cyclic-orbit geometry may contain the altitude identity under another name, but no checked source covers the CPT arithmetic row-ordering theorem itself.

## Value
**PASS.** The result addresses a design sensitivity explicitly emphasized by the source. A predictor with exactly two active rows is a natural sparse binary covariate. Rather than merely recomputing \(O^*\), the theorem exactly solves all row orderings, shows when every ordering necessarily collapses, and identifies all optimizers when noncollapse is possible. The \(n=20\), \(5\%\) saturated case is especially concrete: only four of nineteen oriented spacings produce positive proxy. The limitation to the proxy, saturated group, and two active rows is scientifically material and disclosed.

### Closest literature and limitations
- Lei and Bickel, arXiv:1907.06133 / DOI 10.1093/biomet/asaa079: direct CPT source; Theorem 2 and equation (17) are the closest prior statements.
- Gray, DOI 10.1561/0100000006: classical circulant DFT diagonalization, used only as a linear-algebra ingredient.
- Koning and Hemerik, arXiv:2202.00967 / DOI 10.1093/biomet/asad050: broader transformation-subgroup power analysis, but not the CPT row-ordering object.
- The theorem does not give a full alternative rejection probability and does not extend here to nonsaturated groups, more than two active rows, or nuisance covariates.

Same-model review: passed. Independent audit: not yet performed.
