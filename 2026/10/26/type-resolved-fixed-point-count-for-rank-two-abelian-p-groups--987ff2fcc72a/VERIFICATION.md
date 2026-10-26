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

The standalone checker `verify.py` was run from the exact source content embedded in this ledger. It exhaustively enumerates the parameterized automorphisms and compares the fixed-point set directly with \(A[p]\) for eight finite parameter pairs. All eight matched the formula and the script ended with `ALL_CHECKS_PASSED`.

The finite enumerations are consistency checks only. The general statement is proved in RESULT.md by an exhaustive valuation split for \(\delta=d-1\). The result is limited to \(A=C_p\oplus C_{p^b}\), \(b\ge2\); no claim is made about other invariant-factor types or a complete distribution over all fixed subgroups.
