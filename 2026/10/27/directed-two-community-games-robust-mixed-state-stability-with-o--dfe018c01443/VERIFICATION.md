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

The proof derives the physical three-dimensional Jacobian and gives an exact determinant formula for arbitrary admissible rates. Under \(R,\alpha,\beta,u,v,w_{11},w_{22},K>0\) and \(0<p<1\), every term in \(-\operatorname{tr}L\) and \(\det L\) is strictly positive, establishing local exponential stability. No finite experiment is used as a universal proof.

The included `CHECK.py`, using SymPy, was run against the embedded formulae. It verifies \(C(e,f)^{\mathsf T}=0\), \(\det C=0\), the exact trace/determinant identities, the nonlinear model's equilibrium, the full rational Jacobian, the rational characteristic polynomial, and the strictly negative quadratic discriminant \(-6479/1600\). It prints `PASS: general identities and exact oscillatory witness` when successful.

Unproved: global convergence, robustness under arbitrary state-dependent flow or delays, and any classification for three or more communities. No external independent audit has taken place.
