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

# Reproducibility

Execute `python3 verify.py` with `sympy` available. The script checks the rank-six and rank-four normal forms by exact matrix ranks, tests the splitting discriminator \(h^0(E(-1)|_L)\) on jumping and nonjumping lines, and verifies that the fourteen exterior-Koszul columns printed in [1] annihilate a rank-six bivector, then tests the rank-four limit. Over \(\mathbb F_3\), it enumerates all \(130\) two-dimensional subspaces of a fixed four-dimensional support and counts \(40\) exceptional isotropic planes.

The linear algebra is exact, but this is a finite consistency test. The universal conclusions over \(\mathbb C\), the Lagrangian-quadric identification, and the line-splitting classification follow from the argument in RESULT.md. A separate independent mathematical audit has not been performed.
