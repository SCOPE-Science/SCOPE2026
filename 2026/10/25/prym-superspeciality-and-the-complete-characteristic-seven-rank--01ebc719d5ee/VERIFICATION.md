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

The attached `check.py` was executed with Python 3, returning `ALL_CHECKS_PASSED`. Its checks reconstruct each polynomial cube over \(\mathbb F_7\), compare every matrix entry with the proposed diagonal identities for all seven prime-field parameters, check the genus-two quotient matrix and the even/odd eigenspace split, and verify the two quadratic-field roots \(a^2=-1\) in \(\mathbb F_{49}\).

The algebraic proof, not finite tests, establishes all statements for algebraically closed \(k\). The program does not classify arbitrary curves, prove comprehensive literature novelty, or provide independent mathematical review. The smoothness restriction \(a^2\ne4\) is essential. Computations use only the provided standalone checker, with no external packages.
