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

`verify.py` performs only reproducibility and algebra checks. It evaluates the positive Kummer series for even modes, reconstructs \(\lambda_k\), checks representative Hessian coefficients, verifies the analytic all-mode margin \(2-8(\sqrt e-1)<0\), checks the second-order support-to-radial expansion numerically, and cross-checks the zero-mode normalization against the exact radial-ball second derivative.

The mathematical proof of the infinite statement does not depend on a finite enumeration. It uses the exact inequality \(\lambda_k>k\) for every \(k\ge1\), which follows from the positive-coefficient hypergeometric representation. For the centrally symmetric fixed-perimeter tangent space, only even \(k\ge2\) occur, and then \(k^2+2\lambda_k>8\).

The only general analytic input not reproved from first principles is standard smooth dependence of the Dirichlet solution of a uniformly elliptic equation with smooth coefficients under a smooth boundary perturbation. The proof states this dependency and derives all resulting boundary and integral coefficients explicitly.
