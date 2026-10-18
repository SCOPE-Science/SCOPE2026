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

Run `python3 verify.py` using the Python standard library from the directory containing this document. It exhaustively enumerates all permutations for \(2\le n\le8\), tests covers by actual transpositions and inversion-number changes, records inversion ranks separately for each position gap, and compares integer polynomial coefficients after cross multiplication. It does not use floating point q evaluations.

The shipped `verification_output.txt` was produced by running the shipped `verify.py` before this package was assembled. It reports all seven checked dimensions, 1,246,964 candidate position pairs, and PASS for the polynomial identities, reciprocity, uniform expectation, and covariance consistency. The exact verification procedure uses independent cover detection, while the proof uses conditional Mallows weight enumeration.

No finite enumeration proves the all-dimensional theorem. The proof of consecutive-block q-projectivity and the endpoint-rank classification supplies that infinite step; the verification checks the arithmetic and small boundaries. No independent external audit or external certificate has been performed.
