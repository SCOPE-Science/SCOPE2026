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

# Verification of the analytic claim

The proof is self-contained in `RESULT.md`. Execute `python3 verify.py` after extracting this complete package. The verifier uses Python's standard library. In the reference execution it reported successful exact-rational checks that the quartic sign is negative; 21 numerical integration cross-checks for the first three moments on seven radius-height pairs; five reflected normalized-moment comparisons; and 48 independent projected polygonal convex hull computations. These tests corroborate, but do not prove by finite sampling, the full theorem; the analytic moment identities and strict cubic secant inequality prove it for every positive real parameter pair.

Finite discretizations approximate cylindrical rims, so their tolerance is not an exact-arithmetic certificate for projected continuous boundaries. The rational polynomial bounds and all displayed moment formulas do not depend on these polygonal tests. No external or independent assessment is asserted.
