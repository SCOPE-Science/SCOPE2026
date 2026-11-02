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

# Reproducible checks and scope

The argument in `RESULT.md` is analytical: the map is a degree-three proper half-plane covering, the component count follows from planar Riemann–Hurwitz, and the critical heights are obtained from a cubic discriminant. These facts are proved there, not inferred from numerical tests.

For supplementary reproducibility, install `requirements.txt` and run `python check.py`. The checker tests the symbolic derivative, the exact discriminant and its factorization, samples interior critical points for seven specified positive rational masses (including both sides of the symmetric value), verifies the critical-height formulas, and checks the algebraic cusp coefficient. Successful output is:

`CHECK_OK: derivative, cubic discriminant, critical heights, symmetry and cusp coefficient`

The finite checker does not exhaust all masses, all thresholds, or all component topologies. No independent audit or third-party certification has been performed.
