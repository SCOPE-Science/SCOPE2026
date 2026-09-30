# Independent audit — Zero-residual false positives in projected certification of constrained extremal eigenpairs

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/17/projected-eigenpair-certification-false-positive--dc23fa36a6e4`
**Audited tree:** `506798f281edcea5b0893549fc72147f27b94116`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

For H=diag(0,0,M) and A=[1,0,0], the feasible target is M on e3 while e2 is feasible with penalized eigen-residual, projected feasibility residual, projected KKT residual, and consecutive projected-value change all exactly zero. The scaled inner operator leaves e2 as a positive-eigenvalue non-dominant eigenvector. The nearby feasible family u_delta has residual M delta sqrt(1-delta^2) tending to zero while value error tends to M. Direct inspection of Wang–Xia’s public Algorithm 1 confirms that it requires only a unit initial vector, uses residual-based inner acceptance, warm-starts continuation, and accepts via precisely the four projected tests. The proposed extremality bracket follows immediately from Rayleigh–Ritz and the penalty duality.

### Independent checks

- Verified algebraically that lambda^c=M and M_rho=diag(-rho,0,M) for every rho>0.
- Verified e2 makes all three same-level residuals zero and warm-started continuation makes the outer change zero.
- Verified independently at M=7, rho=0.3 and for the nearby u_delta family that residual tends to zero while global value error remains near 7.
- Inspected the public arXiv Algorithm 1 and stopping-rule text: unit initialization only, residual-based Split–Merge acceptance, projection/KKT tests, outer-change test, and warm starting.

## Originality

The general fact that small Ritz/eigenpair residual does not identify the requested extreme eigenvalue is classical and is not counted as novel. The audited contribution is the exact PSM-specific zero-residual counterexample, the explicit interface gap between unrestricted PSM initialization and the Split–Merge dominant-overlap hypothesis, the robust residual/error family, and a penalty-duality value bracket. Fresh searches through 2026-09-29 located no public erratum, comment, or independent source giving this PSM-specific construction.

### Literature checked

- https://arxiv.org/abs/2609.18538 — Wang–Xia, Projected Hessian Quantification Theorem; source PSM algorithm and projected-certification rule.
- https://arxiv.org/abs/2501.15131 — Liu–Xia, Split–Merge; dominant-eigenvector convergence context and overlap hypothesis.
- https://doi.org/10.1137/S0895479800366859 — van Dorsselaer–Hochstenbach–van der Vorst; classical extreme-Ritz residual versus extremality context.

## Scientific value

This identifies a deterministic certification failure in a newly proposed matrix-free extremal eigensolver without attacking its valid penalty duality. It cleanly separates stationarity/feasibility from spectral-index certification and supplies a direct way to repair the acceptance semantics with a validated upper enclosure.

## Limitations

- The exact bad initialization is orthogonal to the target and has probability zero under an absolutely continuous random start; the result is about deterministic a posteriori certification, not a positive-probability random-start failure claim.
- The audit does not dispute Wang–Xia’s penalty duality, finite-attainment theorem, or asymptotic penalty expansion.
- A useful repaired certificate requires an independently validated dominant-eigenvalue upper enclosure; the crude lambda_max(H) bound may be loose.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
