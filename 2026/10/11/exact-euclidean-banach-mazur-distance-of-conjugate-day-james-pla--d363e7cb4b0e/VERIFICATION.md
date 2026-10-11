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
# Verification

The quantified theorem is established by the analytic proof in `RESULT.md`; no finite enumeration or numerical solver is used as a substitute for proof.

Checks performed on the final claim:

- The Day–James norm and its conjugate exponent range were reconstructed from the primary definitions.
- Hölder duality was applied directly to both sign regimes to verify that the determinant antinorm equals the original norm.
- The antinorm of \(H_\rho\) was recomputed from the inverse of its \(2\times2\) quadratic-form matrix, giving the factor \((1-\rho^2)^{-1/2}\).
- The derivatives controlling \(f_p\), \(G_p\), and the positive-quadrant distortion branch were algebraically reduced to expressions with explicit sign.
- The endpoint regimes \(\rho\ge0\) and \(\rho\le-\alpha\) were checked separately, so the interior balance is not accepted merely as a stationary point.
- Direct numerical grid sanity checks at \(p=2.1,2.5,3,4,6,10\) matched the closed formula to floating-point precision. These checks are corroborative only.
- The symbolic specialization \(p=3\) gives \(d_{\mathrm{BM}}^2=2^{5/3}/3\); the specialization \(p=4\) gives \(d_{\mathrm{BM}}^2=6-2\sqrt6\).

Limits: the proof does not address nonconjugate exponent pairs, complex scalars, or higher-dimensional analogues. General \(s_p\) is characterized uniquely by a scalar equation rather than by elementary radicals.
