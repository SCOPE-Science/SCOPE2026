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

# Verification notes

Execute `python3 verify_noncrossing.py` with Python 3 and no external dependencies. It enumerates all \(C_n\) noncrossing matchings for \(2\le n\le8\) and compares exact integer counts for every ordered pair of eligible edge coordinates with the two-chord Catalan formula. All 8,771 comparisons pass. The checker also constructs both noncrossing completions for all 714 alternating four-vertex choices in those sizes, and obtains the predicted rank over the finite field of order 1,000,003 in each of seven sizes.

These tests check finite examples and the concrete geometry of the principal local move. The theorem for arbitrary \(n\) rests on the proof that alternating checkerboards generate every standard integer zero-marginal basis element. A modular computation is not used to infer the universal integer saturation. Exact individual nonzero covariance eigenvalues and conditioning are not claimed. Independent external validation and historical priority review remain unperformed.
