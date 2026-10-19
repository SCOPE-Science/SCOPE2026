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

# Verification and limits

The exact-rational `verify.py` is self-contained and checks the disease-free equilibrium, control threshold, right/left critical eigenvectors, demographic center tangent, quadratic infected-mass expansion, sharp global-bound gap, and all five exact asymptotic coefficients for one strictly admissible rational parameter set. Execute with `python3 verify.py`; successful execution prints a single PASS line. The executable is a finite witness check, **not** a proof for all parameters. The general proof is the comparison-plus-positive-mass argument followed by one-dimensional center manifold analysis in `RESULT.md`.

The algebraic proof requires all listed rates strictly positive, \(0<p<1\), and \(g(C)=C/(\kappa+C)\). Its critical asymptotic applies exactly when initial total infection in \((E,I,C)\) is positive. At \(\mathcal R_c>1\), instability excludes global disease-free stability. The reference source's global bound \(\mathcal J_c\le1\) is genuinely more restrictive in the rational witness: \(\mathcal J_c=35/24\) while \(\mathcal R_c=1\).

Computational verification does not constitute independent scientific audit or external certification.
