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

Run `python3 verify.py` in a directory containing the attached verifier. It independently tests scattered-subsequence membership with an iterator rather than reusing the run-cost theorem. For \(1\le k\le8\), it enumerates all binary candidates with lengths 1 through \(2k+1\), checks each of the single-letter deletion conditions, compares each outcome against the theorem's run-cost classification, totals all MAS and shortest absent subsequences, then checks the claimed rational-coefficient recurrence for the first 100 indices.

Recorded output for the enclosed exact script: `VERIFY_OK hosts=8 candidates= 349504 formula_checks=100 counts= [3, 5, 9, 16, 28, 49, 86, 151, 265]`.

Verification does not replace a proof for unbounded \(k\). The proof in `RESULT.md` derives the infinite theorem analytically; checking finitely many hosts is an independent reproducibility sanity check. No independent audit has been performed.
