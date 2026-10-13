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

The analytic verification differentiates the two remainder factors used in the proof. For \(0<\theta<1\),
\[
 \frac{d}{ds}\bigl((1+s)^\theta-s^\theta\bigr)<0,
\]
while
\[
 \frac{d}{ds}\bigl((1+s)^{\theta-1}-s^{\theta-1}\bigr)>0.
\]
Together with their respective positive and negative signs, these monotonicities give the stated endpoint bounds on the Lagrange remainder.

The packaged `artifacts/verify.py` was run from the finalized package content. It checks deterministic grids of noninteger exponents and intervals, verifies exactness at integer exponents, and reproduces the source Example 3.7 calculation at \(\alpha=5\). Its successful terminal marker is `VERIFY_OK`.

The numerical checks do not certify the all-parameter theorem; the proof above does. They are intended to detect transcription, sign, coefficient, and normalization errors in the packaged formulas.

No independent audit has been performed.
