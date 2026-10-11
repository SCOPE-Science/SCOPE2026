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

# Verification of the mathematical claim

The proof uses the exact finite-dimensional spectral identities for the swap and maximally entangled rank-one tensor, and exact weighted Hölder optimization. The extracted standalone `verify_brauer.py` was run using Python 3 and returned `BRAUER_SCHATTEN_EXACT_BLOCK_CHECK_OK`. Tests check the partial transpose identity, integer matrix relations, quartic Schatten trace expressions, endpoint-compatible scalar formulas and witness ratios for \(2\le n\le5\), but do not prove arbitrary \(n\) or continuous \(p\). The universal proof is in RESULT.md.

The p-dependent formula is restricted to the canonical invariant plane. Only the full two-level endpoint norms and Hilbert–Schmidt norm are claimed. The published motivating qualitative example and inaccessible older comparison source are identified in the scientific discussion. Same-model review is not independent validation.
