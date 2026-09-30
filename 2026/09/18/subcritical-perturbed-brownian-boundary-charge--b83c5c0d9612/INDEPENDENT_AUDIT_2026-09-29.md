# Independent Audit — Boundary-charge criterion for subcritical perturbed Brownian reflection

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a081a64ed8446aee68e1f512377e7ba8327265d9`  
**Audited current source tree:** `a081a64ed8446aee68e1f512377e7ba8327265d9`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence; this is a guarded publication-plan payload and is not claimed to be already published.

## Correctness — PASSED

PASS. The orthant Skorokhod reduction is consistent for every ν<1/2 because |ν/(1−ν)|<1. The second coordinate gives V/(1−ν)=M(W)−x, and the first then yields W=(1−ν)x+B+νM(W)+K. Applying Tanaka to X=W−b and using occupation density gives 1/2 L^0(X)=K+νJ−A. For F=M(W)−b≥0 continuous of finite variation, 1_{F=0}dF=0; since dM is supported on W=M, the contact contribution satisfies J=∫1_{X=0,F=0}db. This produces the claimed defect measure. Its weights 1 and 1−ν are positive and bounded away from zero, so it vanishes exactly when |db| charges no contact time. For locally absolutely continuous b, the Brownian quadratic variation makes the zero set of X Lebesgue-null, giving the stated well-posedness corollary.

## Originality — PASSED

PASS, with classical-context qualification. Wang’s 2026 preprint gives existence/uniqueness under the stronger one-sided modulus condition (PB), explicitly splitting ν<1/2 through an orthant Skorokhod problem, and constructs singular rough boundaries with failure. Classical time-dependent Skorokhod literature supplies reflection maps and local-time tools. Targeted searches did not locate the exact model-specific regulator-minus-local-time defect identity, its iff Stieltjes contact-charge criterion, or the corollary covering every locally absolutely continuous boundary in the full subcritical regime. The audit does not claim Tanaka, occupation density, or orthant reflection as new.

## Scientific value — PASSED

PASS. The result identifies the exact obstruction left after the subcritical orthant construction and separates boundary roughness from boundary charge: absolutely continuous t^α boundaries remain well posed even when α≤1/2 and violate Wang’s modulus hypothesis, while singular boundaries can fail by charging the contact set. That substantially clarifies the mechanism in the motivating model.

## Independent checks

- Re-derived the orthant-to-maximum representation and checked the ν<1/2 spectral-radius condition, including negative ν.
- Re-derived the Tanaka identity and justified the zero-level finite-variation restriction 1_{F=0}dF=0.
- Checked support of dM and the exact contact-set reduction for J.
- Checked the signed-measure equivalence with total variation of db on the contact set.
- Checked the locally absolutely continuous corollary using occupation density for quadratic variation t.
- Compared against Wang’s open arXiv statement and classical time-dependent Skorokhod references.
- Verified the current main tree equals the assigned tree and that dated independent-audit files are absent.

## Limitations

- The theorem is restricted to ν<1/2.
- For general singular finite-variation boundaries, the contact-charge criterion is exact but implicit because the contact set is random.
- Broader reflected-semimartingale literature may contain analogous regulator/local-time identities in different notation; novelty is claimed only for this precise perturbed moving-boundary model and consequence.

## Evidence and references

- https://arxiv.org/abs/2609.20491
- https://doi.org/10.1007/978-1-4757-2418-9_7
- https://doi.org/10.1016/j.spa.2008.03.001
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/subcritical-perturbed-brownian-boundary-charge--b83c5c0d9612

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
