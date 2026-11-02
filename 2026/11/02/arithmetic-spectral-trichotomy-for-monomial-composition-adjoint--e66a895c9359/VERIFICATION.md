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
# Verification and reproduction

Run `python verify.py` using Python 3. The checker uses only the standard library and tests exact integer indices of finite directed paths under the composition-adjoint product for multiple arithmetic regimes. It is evidence for arithmetic normalization and selected endpoints, not a proof of infinite multiplicities, spectral boundaries, or universal polynomial norm statements.

The analytic verification uses five independent logical steps: (i) adjoint action of isometric monomial composition on the Hardy basis; (ii) reduced-factor divisibility and chain endpoints, including the full family of all finite lengths; (iii) standard shift and finite Jordan point/approximate spectra with weakly null tests; (iv) strong limits of matrix polynomials on increasing finite shifts and infinitely repeated summands; (v) forward-versus-backward strong-power dichotomy. The \(m=n\) boundary is treated separately as a projection. The matrix-polynomial norm is asserted only for finite matrix coefficients. Neither a finite cutoff nor a numerical sample substitutes for the complete proof.

Source comparison: the 2026 Hardy composition-product paper's Theorem 3.24 concerns Schatten membership; the new structural conclusion is not inferred from a failed database search alone. Open priority uncertainty is acknowledged. Independent audit is not performed.
