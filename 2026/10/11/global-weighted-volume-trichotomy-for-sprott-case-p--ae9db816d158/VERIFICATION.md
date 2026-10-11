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

# Verification and boundaries

The accompanying exact-symbolic checker (`checks/check_sprott_p.py`) uses Python 3 and SymPy to verify all polynomial, divergence, equilibrium and variance identities for arbitrary symbolic parameters; it also checks exact specializations. Run from the extracted package root with `python checks/check_sprott_p.py`. Exit status zero verifies these finite algebraic checks.

The global measure-zero proof is not a computer-assisted finite search. Its critical step is the weighted finite-time change-of-variables formula applied to a measurable bounded forward-invariant set. Strict weighted expansion for negative \(b\) contradicts inclusion of that set into itself when it has positive volume. This theorem allows exceptional bounded trajectories and makes no claim of complete escape rates. The critical case follows by monotone-function limit sets, including complete-orbit backward limits.

Historical comparisons used the complete 1994 introducing article, the 2013 case-P technical parameter note, and the accessible primary 2021 comparison paper. The novelty comparison is limited to inspected text and listed searches. The review is not independent validation.
