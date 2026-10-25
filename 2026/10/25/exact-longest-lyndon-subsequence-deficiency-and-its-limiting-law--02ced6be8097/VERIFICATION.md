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

The self-contained `verify.py` uses only the Python standard library. It independently generates **all distinct scattered subsequences** of each of 625 small four-run binary words, tests the strict proper-suffix definition of a Lyndon word, and computes each maximum without using the claimed run formula. It also exhaustively enumerates 91,390 positive four-part compositions at total lengths 4–40 and compares all tail-distribution coefficients and extrema with the claimed generating function.

Command: `python3 verify.py`

Observed output:

`VERIFY_OK direct_subsequence_sets=625 complete_compositions=91390 lengths=4..40 tail_distributions=true sharp_extrema=true`

The finite search does not prove the formula, the generating functions, or the limiting distribution for arbitrary lengths. Proofs of those claims are given in `RESULT.md`. This package does not contain an independent audit or externally issued certificate.
