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

# Reproducibility and limitations

Run `python3 checker.py` with a Python 3 standard-library interpreter. Successful execution prints `VERIFY_OK`.

The checker independently enumerates all increasing partial injections satisfying parity and induced-fence comparisons, compares all coefficients of the recurrence through \(n=9\), tests absence of fixed points against eventual emptiness, verifies the high-rank identities through \(n=20\), and checks explicit defect-five examples for \(7\leq n\leq20\). No third-party packages or downloaded data are required.

The finite tests are **not** certificates of a theorem for all \(n\). The general result rests on the graph-gap bijection, a finite parity-prefix recurrence and the omitted-coordinate argument in the proof. The recurrence measures coefficient arithmetic operations rather than bit complexity, and it is not an enumeration by nilpotency index. A bibliographic full-text gap remains for an older ambient-monoid article. No independent audit has been performed.
