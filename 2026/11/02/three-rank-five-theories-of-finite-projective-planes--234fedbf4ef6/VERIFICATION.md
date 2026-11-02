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

# Verification details

The C++17 source `ef_projective.cpp` generates finite projective planes \(\mathrm{PG}(2,q)\) for \(q=2,3,4,5\) from projective coordinate triples, including the field of order four via \(u^2+u+1=0\). It checks all point and line degrees and uniqueness of joins and intersections. Bottom-up recursive first-order types are computed by taking, at each level, the sorted set of all next-move types and interning these vectors by **exact equality**. Both the rank-four and rank-five roots are compared across planes. The source includes a separate optional `check 4` test that enumerates all atomic fifth extensions at order four and matches the optimized small-incidence-pattern enumeration on every ordered four-tuple (no mismatches).

Build with `g++ -O3 -std=c++17 ef_projective.cpp -o ef_projective`. Run `./ef_projective 2 3 4 5` and `./ef_projective check 4`. The exact recorded output is included as `verification_output.txt` and `fastcheck.txt`. The rank-five computation uses complete direct enumeration of fifth moves for orders two, three, four; at order five it uses the proved empty/singleton/line-intersection reduction. This is an exact finite checker for those instances, not an infinite proof. The mathematical generalization is proved in `RESULT.md` using projective-plane axioms and explicit candidate bounds. All checks are self-review or executable verification; no independent audit is asserted.
