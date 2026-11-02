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

# Reproducibility and scope

Execute `python verify_hessian3.py` with `sympy==1.14.0`. The actual successful output is included as `verify_hessian3.out`, terminating in `VERIFY_OK`.

The verifier checks the exact characteristic-three polynomial Hessian identity, the two local singularity-orbit Hessian determinants, the explicit fifteen singular representatives, exhaustive point counts over the projective hyperplane in \(\mathbb F_3\) and \(\mathbb F_9\), and the numerical traces forced by resolving fifteen split nodes. These are exact finite calculations, not floating-point experiments.

The geometric classification of singular points over an algebraic closure is proved through the common additive cubic equation and cannot be concluded just by the list of rational points. The all-extension zeta formula uses the standard K3 Betti number and absolute-value bounds for Frobenius, plus equality in the triangle inequality. The Picard-rank conclusions use the odd-characteristic K3 Tate theorem. No proof of historical priority or independent assessment is claimed.
