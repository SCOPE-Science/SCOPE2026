---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and limits

The exact polar section calculation starts from
\[
h_K(y)-ts\le1,\qquad a h_K(y)+(1-t)s\le1,
\]
with crossover
\[
s_*=\frac{1-a}{1-(1-a)t}.
\]
Integrating the minimum of the two affine section scales to the power \(d-1\) gives
\[
\frac{\operatorname{vol}_{d-1}(K^\circ)}{d\,t(1-t)(1-(1-a)t)^{d-1}}.
\]
The vanishing horizontal centroid of \(K^\circ\) and the axial log-derivative establish the full Santaló center. The centroid inequality is certified analytically by an explicit mixture of \(\mathrm{Beta}(1,k+1)\) laws; strict volume-product monotonicity then follows from a strictly convex Jensen integrand.

Run `python verify.py` with NumPy, SciPy and SymPy available. The program checks symbolic identities and positive polynomials through dimension \(12\), validates parametric values at a grid of intermediate ratios, and constructs polar convex hulls directly for dimension-three frusta over asymmetric triangular and symmetric square bases. It reports `VERIFY_OK` and a worst discrepancy of order \(10^{-15}\). These finite and numerical checks are supplementary; the proof for all dimensions, all positive ratios, and all convex bases is exact in `RESULT.md`.

The 2006 Meyer--Reisner pyramid formula is a known endpoint, not newly certified. No independent audit or independent mathematical validation is asserted.
