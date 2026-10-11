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

The exact symbolic replay is in `verify.py`. It derives the logarithmic stationary equations from the printed vector field and verifies
\[
Y-X=\frac{cA}{c^2+ce+e^2},\qquad X-Z=\frac{eA}{c^2+ce+e^2},
\]
and
\[
X+Y+Z=\frac{3+A}{3+c-e}.
\]
It also checks the inward-pointing signs on the upper faces of the biological cube. Running the packaged script produces `VERIFY_OK`, recorded in `verification_output.txt`.

The strict sign \(A>0\) is analytic rather than numerical: the phase marginal is Haar for the continuous phase rotation, compact interior support gives \(x^{-1}-1>0\), and \(\sin^2\theta\) is positive except on a Haar-null set. For a phase-locked periodic orbit, the same equations follow by integrating the three logarithmic derivatives over one full period.

No finite experiment is used as an infinite proof. The verification does not establish existence of any periodic orbit, invariant torus, or strange attractor, and it does not justify logarithmic averaging for invariant measures whose support accumulates on a coordinate plane.
