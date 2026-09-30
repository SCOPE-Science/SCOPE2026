# Independent Audit — Sharp large-noise asymptotics for variance-gamma medians

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a68824f59a0a547e8859bd3dd5cb7b871b62663b`  
**Audited current source tree:** `a68824f59a0a547e8859bd3dd5cb7b871b62663b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. After scaling theta=1, the normal-gamma representation Y_kappa=2G_s+sqrt(2kappa G_s)N with s=r/2 gives the submitted CDF integral. Differentiating and evaluating the standard Bessel-K integral reproduces the exact density D_{s,kappa}(q). The center deficit is a Student-t probability, giving the kappa^{-1/2} leading term. The small-q Bessel regimes change precisely at nu=s-1/2=0 and nu=1, i.e. r=1 and r=3, and the submitted constants follow from matching the deficit with the integrated density. I independently recomputed the constants, including the exact r=2 expansion M=1+(2sqrt(kappa))^{-1}+o(kappa^{-1/2}), the critical r=1 inverse-log denominator with the 2 log log term, the r=3 (2/3)(log kappa)/kappa correction, and the r>3 coefficient 2(r-1)/(3(r-3)). Direct numerical mixture/Bessel integration at r=1/2,1,2,3,4 converges to the stated leading laws.

## Originality — PASSED

PASS. Gaunt--Ouimet's July 2026 preprint proves sharp median bounds and monotonicity and determines the limiting floor—0 for r<=1 and (r-1)theta for r>1—but its public statement does not give the submitted five large-noise asymptotic regimes or the logarithmic critical laws at r=1 and r=3. The earlier Gaunt--Merkle work treated median bounds/conjectures, and the 2024 variance-gamma review surveys the median literature without these phase-transition formulas. Targeted searches for the r=1 inverse-log law, the r=3 log/kappa law, and the displayed constants found no covering prior result.

## Scientific value — PASSED

PASS. The theorem refines a qualitative limiting-median result into a complete sharp asymptotic phase diagram with two genuine critical shapes and explicit constants. The five regimes expose how endpoint singularity and inverse-moment integrability change the convergence scale, which is useful information not captured by the existing bounds alone.

## Independent checks

- Re-derived the normalized normal-gamma mixture CDF and the exact Bessel-K formula for its q-derivative.
- Recomputed the Student-t center deficit and its kappa^{-1/2} expansion.
- Matched the Bessel small-argument regimes for 0<r<1, r=1, 1<r<3, r=3, and r>3 and independently simplified every displayed coefficient.
- Checked the r=2 special case against its exact elementary formula.
- Numerically solved the median equation using both the mixture CDF and the integrated Bessel density; for r=1/2,1,2,3,4 the normalized correction approaches the submitted asymptotic prediction.
- Compared the result with Gaunt--Ouimet 2026, Gaunt--Merkle 2021, and the modern variance-gamma review; targeted searches found no prior matching critical asymptotics.
- Verified that the assigned record path did not change between the dispatcher source-check commit and current main and that the dated audit markers are absent.

## Limitations

- The asymptotics are for fixed shape r and theta>0 as sigma/theta tends to infinity; they are not uniform across the critical shapes r=1 or r=3.
- The 2001 Laplace/generalized-Laplace monograph was located bibliographically but no specific matching large-noise median asymptotic was found in lawful open-access search; no claim is made to have read inaccessible book sections.
- The proof relies on standard Bessel-K and Student-t asymptotics; those analytic ingredients are not claimed as new.

## Evidence and references

- https://arxiv.org/abs/2609.20212
- https://arxiv.org/abs/2002.01884
- https://arxiv.org/abs/2303.05615
- https://doi.org/10.1007/978-1-4612-0173-1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
