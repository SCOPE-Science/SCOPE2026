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

# Exact finite checks

Execute `python3 verify.py` from the directory containing this file and `verify.py`. The verification code enumerates complete Prüfer words, retains precisely the trees whose edges join distinct multipartite classes, and computes exact rational moments for twenty graph types. The expected output is `VERIFY_OK trees=348528 assertions=22795 cases=20`.

The separate code paths for direct enumeration versus the analytic product formula were checked for one-vertex leaves, cross-part two-vertex leaves, and covariance of the entire class leaf counts. A larger finite sweep checks the sign boundaries. These checks are not an exhaustive proof over all graph orders. The mathematical proof depends on the multipartite matrix-tree enumerator and the leaf-deletion bijections; no external certification has taken place.
