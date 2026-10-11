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

For odd \(n\ge3\), normalize \(R=1\) and put \(t=\pi/(2n)\). The proof's exact ingredients are the optimal arc bound
\[
\operatorname{arcLength}(\overline B(c,r)\cap S^1)\le2\arcsin r
\]
for \(r<1\), the majority run's diameter \(2\cos t\), the cutpoint coordinates
\[
q_\pm=(0,\pm\cos(2t)/\cos t),
\]
and the exact difference
\[
\cos^2t-\big(\sin^2t+\cos^2(2t)/\cos^2t\big)=\cos(2t)\tan^2t.
\]
The source file `verify.py` independently checks symbolic algebra for these formulas and finite vertex/edge configurations for every odd \(n\) from \(3\) through \(201\).

Finite checks show the construction behaves as stated in a substantial regression range. The analytic proof in `RESULT.md`, especially the arc-count lower bound and the half-polygon convexity argument, is what establishes the theorem for **all** odd integers and every positive circumradius. No experiment or timeout is treated as an infinite proof.
