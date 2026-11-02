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

Run `python verify_support.py` with Python 3 and the standard library. The exact checker tests all specified construction cases for even \(n\leq20\) and odd \(n\leq19\), verifies each marginal and every ordered-pair envy probability with rational arithmetic, and performs rational Gaussian elimination for all three-agent marginal and envy constraints. Its expected printed outcome is PASS with six pivots giving the unique three-agent uniform weight \(1/6\).

The proof, rather than the finite checks, establishes the universal support bounds. Step 2 requires distinct, strictly positive supported permutations; allowing redundant copies cannot reduce the distinct support. The exact value for odd \(n\geq5\) remains open here. Independent verification has not been performed.
