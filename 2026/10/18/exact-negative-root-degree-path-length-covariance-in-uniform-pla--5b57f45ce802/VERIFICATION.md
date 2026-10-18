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
The standalone standard-library checker exhaustively generated all uniform ordered rooted trees of sizes 2 through 9 and computed rational root-degree and total-depth mixed moments from their individual shapes. It compared them with the closed forms, performed independent algebraic moment identities for sizes 2–1200, verified strict binomial comparison for sizes 3–700, and compared leading asymptotic behavior at three large orders. It reported 3837 PASS checks.

The infinite theorem, strict negativity and asymptotic expansion are proved algebraically in RESULT.md; computations do not establish those infinite claims. Reproduce with `python3 verify_plane_tree.py`. No external packages or third-party data files are required. No independent scientific validation is asserted.
