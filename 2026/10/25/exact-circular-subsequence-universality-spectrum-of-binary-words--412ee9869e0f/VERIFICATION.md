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

The proof of the all-length statement is contained in `RESULT.md`. The critical steps are: equivalence between binary arches and matchings of unlike adjacent letters; rotation-to-cycle matching; the even-parity reconstruction of transition vectors; the two-state overcount correction for the fully alternating cyclic vector; and coefficient extraction from the weighted transfer matrix.

For finite checks, run `python3 verify.py` using only the Python standard library. The checker independently recomputes circular indexes from every rotation of every nonempty binary word through length 16, compares the entire distribution to the formula, directly checks all possible candidate subsequences for rotations through length 10, independently exhausts edge-subset matchings for cycles through length 10, checks the two exact moment identities, and validates a separate polynomial recurrence through length 80. Observed output: `VERIFY_OK words=131070 direct_rotations=18434 cyclic_matchings=2046 trace_recurrence_n<=80`.

These finite tests do not prove any statement beyond their tested ranges. The infinite assertions are established by the structural matching and transfer-matrix derivation. No external independent audit is claimed.
