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

# Verification record

The accompanying `checker.py` implements the precisely stated recurrence for contraction on \(\Diamond p\). It recomputes modal truth after each update rather than freezing the initial truth set. The script exhaustively checks all \(1{,}052{,}740\) pairs consisting of an accessibility relation and an atom valuation on every labelled nonempty carrier of size at most four, establishes first stationarity by the claimed \(n\) bound, checks the complete counts by first fixed stage, and checks the explicit sharpness family for carrier sizes one through 24.

Command: `python3 checker.py`. Expected final output: `ALL_CHECKS_OK`.

The theorem for arbitrary finite \(n\) is proved in `RESULT.md` by a monotonicity and terminal-step lemma, together with an all-size induction for sharpness. The computation tests only finite instances and is not an independent mathematical audit.
