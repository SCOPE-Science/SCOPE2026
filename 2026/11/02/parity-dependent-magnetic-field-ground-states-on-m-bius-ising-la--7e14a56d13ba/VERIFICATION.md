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

Run `python3 check_mobius.py` using a standard Python 3 installation; no external packages or downloaded input are required. `CHECK_OUTPUT.txt` contains the exact output from this program executed on the complete local source. Its two independently implemented checks are direct bit-enumeration of the graph's edge cuts for \(3\le n\le10\) and a four-rung-state twisted transfer recursion for \(3\le n\le64\). Both include the two critical fields, positive and negative noncritical fields, and the \(h=0\) spin-reversal point. The checker uses the integer field \(q=2h/J\), with \(J\) normalized to one, so it never relies on a floating-point equality for ground-state multiplicity.

Passing finite computations **does not certify all sizes**. The proof of the infinite-family statement is the cut identity and rung-parity argument in `RESULT.md`. The independent-set trace identity yields the critical-field count. Historical priority and physical measurements remain outside these calculations.
