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

The complete proof is in `RESULT.md`; the executable `verify_eop.py` and captured output `verify_output.txt` are included in this package. Run `python verify_eop.py` with Python 3 and SymPy installed.

The direct reference enumerator builds the sunlet as an edge list, declares two chosen edges incompatible only if a third distinct graph edge connects their endpoints, and checks all edge subsets. The reference does **not** use the four-state mask classification or the quartic recurrence. Its 349,504 candidate-subset checks cover every edge subset for \(3\le n\le9\) and compare every coefficient with the recurrence. Symbolic exact-arithmetic checks independently construct the four-state matrix and a 16-state sliding-window matrix and establish the claimed characteristic identities. The sharp degree and maximum-coefficient formulas are checked for all integer \(n\) from 3 through 32.

The proof, rather than these finite tests, establishes the result for all \(n\ge3\). No formal proof-assistant certification, independent assessment, or claim about more general graph classes is made.
