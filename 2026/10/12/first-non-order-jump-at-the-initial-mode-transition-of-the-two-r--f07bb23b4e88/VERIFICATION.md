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

Reproduce the exact finite algebra using `python verify_modes.py` and SymPy. The script derives every mass polynomial from the generating-function recurrence, verifies the algebraic threshold identities and rational brackets, and checks Bernstein derivative coefficients and exact rational tail bounds. The checked positive Bernstein coefficients certify inequalities over full compact parameter intervals by polynomial identities.

The analytic induction begins at count offsets three, six and nine for orders two, three and four respectively, and uses the same uniform upper bounds to control all larger integer offsets. The finite checks do not substitute for this proof. They do not verify independent novelty, historical bibliographic completeness, higher-order behavior, or the later modal transitions.
