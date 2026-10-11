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
# Verification of the mathematical statement

The accompanying `verify_hamming_cech.py` uses no external packages. Run `python3 verify_hamming_cech.py` with Python 3. It builds the entire finite nerve by taking all subsets of every closed Hamming-radius-one neighborhood; no sampled or partial set of faces is used in each tested case. For each prescribed pair, it checks that the lower face has exactly one immediate coface and the upper has none, then deletes the pair. It checks that the entire remaining edge and triangle sets coincide with their predicted descriptions, that no simplex of dimension greater than two survives, and that exact mod-two boundary ranks produce zero first homology and the predicted second Betti number.

Seven checked pairs, in the verifier's order: \((2,3)\): \(14\) spheres; \((2,4)\): \(63\); \((3,2)\): \(7\); \((3,3)\): \(134\); \((4,2)\): \(31\); \((3,4)\): \(783\); \((4,3)\): \(836\). The executable completed with `VERIFY_OK`. Tests with \(n=2\) or \(q=2\) are boundary consistency checks, not extensions of the newness assertion.

All-parameter correctness is established by the intersection classification, the two descending-cardinality free-face lemmas, the two-skeleton description, simple connectivity via coordinate triangles and commuting squares, and integral Hurewicz/Whitehead. Exhaustive finite tests alone cannot prove the universal statement. The prior \((3,3)\) result is expressly acknowledged and not newly asserted. No independent audit has been performed.
