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

# Verification instructions

Run `python3 verify.py` with the standard Python library. The script independently enumerates all binary scattered subsequences of the finite word `01` repeated \(k\) times, for \(1\leq k\leq12\). Candidate absent words are tested by deleting each of their letters and rerunning the actual finite-word subsequence matcher. Their complete length histograms are compared against the closed binomial formula; the first 12 totals and the recurrence through \(k=50\) are checked separately.

The successful execution prints `VERIFY_OK binary_repeated_permutation k=1..12 recurrence=1..50`. The returned finite results support but cannot prove the theorem for unbounded \(k\). The infinite proof is in `RESULT.md`, using the greedy-position identity, exact deletion-cost classification, run-composition counts, and binomial generating function. No external certification is claimed.
