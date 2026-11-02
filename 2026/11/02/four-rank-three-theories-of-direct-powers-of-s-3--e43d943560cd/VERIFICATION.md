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

# Reproduction

Run `python3 s3_orbit_check.py`. The script constructs the six elements of S3, all 70 equality/multiplication atomic bits on a triple of selected elements and identity, the eleven diagonal-conjugation pair orbits, and every pair-orbit multiset through power five. It computes recursively nested rank-three type sets and asserts that the types at powers four and five agree. The canonical hashes are printed and are supplementary, not the comparison criterion. Run `g++ -O3 -std=c++17 s3_direct_check.cpp -o check` followed by `./check` for an independent exhaustive check over every ordered triple of group elements at powers one to three. Both checkers were run successfully, with outputs attached.

The infinite step is proved on paper: coordinatewise duplicator strategies preserve equality, the named identity and the ternary multiplication relation, so equivalence at a fixed rank is preserved by adding a common direct-product factor.

No checker enumerates all infinitely many powers; the algebraic congruence, not extrapolation, proves the tail. No Lean, external independent proof audit or historical priority certification was performed.
