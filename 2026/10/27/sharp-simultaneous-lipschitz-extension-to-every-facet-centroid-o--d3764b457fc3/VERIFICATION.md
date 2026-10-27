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

The analytical proof reduces unrestricted linear interpolation to a two-weight family through signed-permutation averaging and checks the exact finite transportation norms of each pair type.

Run `python3 verify_crossfacet_stdlib.py` with Python 3 standard library. Actual execution passed all vertex--facet pairs (1,264) and all facet--facet pairs (2,660) in dimensions 3--6, checking every assignment matching in the latter pairs (68,364 assignment permutations across the four dimensions). A separate SciPy transportation-linear-program verifier, run on dimensions 3--5, also passed all target-point pairs.

Finite checks cannot prove the all-dimensional theorem. The infinite statement relies on the explicit source--sink distance classification, the derangement matching for each \(k\ge2\), the two dual 1-Lipschitz witnesses, and the comparison \(B(0)\le A(0)\) for \(d\ge3\). Verification is not independent mathematical certification.
