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

The analytic proof reduces the arithmetic upper bound and geometric lower bound to exact polynomial identities after the substitutions \(x=k\pi/(2N)\), \(z=x^2\), and \(y=\sin^2x\). `verify.py` checks those identities with exact rational polynomial arithmetic and rechecks the endpoint sign estimates. It also samples every lower-half mode for \(2\le N\le400\) as a regression check.

The finite sweep is not a proof for all \(N\). The proof for all admissible modes is the alternating-series control of \(\sin x\), monotonicity of the reduced functions, and the exact polynomial sign bounds stated in `RESULT.md`.

The asymptotic coefficients were obtained by expansion of the closed-form consistent and lumped eigenvalues at \(\theta=0\). The shared \(-\theta^8/6048\) term in the two postprocessed errors explains why the bracket-width expansion skips the \(N^{-6}\) term.
