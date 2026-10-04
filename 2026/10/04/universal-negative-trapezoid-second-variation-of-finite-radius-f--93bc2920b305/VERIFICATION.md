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

The proof is analytic. The bundled script `artifacts/verify.py` performs an independent numerical replay of the exact one-dimensional integral near the affine-parallelogram point. For several values of \(\lambda\), it compares finite-difference second derivatives with
\[
V_{ss}(0,0)=\frac{16\lambda\operatorname{artanh}\lambda}{(1+\lambda)^2},
\]
\[
V_{\delta s}(0,0)=\frac{8\left(\lambda-(1+\lambda)\operatorname{artanh}\lambda\right)}{(1+\lambda)^2},
\]
and
\[
V_{\delta\delta}(0,0)=\frac{16\left(\lambda-\operatorname{artanh}\lambda\right)}{(1+\lambda)^2}.
\]
It also checks the optimized Schur-complement formula and the inequalities \(r_+<\lambda<\operatorname{artanh}\lambda\) that make the curvature strictly negative.

The numerical checks are finite corroborations only. The universal quantifier over all \(R>0\) is justified by the exact root comparison in `RESULT.md`, not by sampled computation.
