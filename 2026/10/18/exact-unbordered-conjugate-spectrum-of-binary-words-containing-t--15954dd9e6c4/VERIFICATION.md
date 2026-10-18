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

Run `python3 verify.py`. Using Python's standard library alone, this script reconstructs every length-\(n\) binary word with precisely three ones for \(3\le n\le23\), directly tests every nonempty proper border of each of its \(n\) rotations, and checks the result against its cyclic zero-gap comparisons. It counts \(10{,}626\) tested words. An independent enumeration of all ordered zero-gap triples for \(3\le n\le120\) verifies the formula coefficients using only integer arithmetic.

The actual packaged script returned `ALL_CHECKS_PASS exhaustive_words 10626 gap_n_max 120`. This finite verification does not prove the all-length theorem; the argument in RESULT.md does. The source-comparison residual risks are described in REVIEW.md and AUDIT.json. No independent audit has been performed.
