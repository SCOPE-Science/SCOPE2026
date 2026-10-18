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

# Exact verification procedure

Run `python3 petersen_edge_toric_check.py` under Python 3.10 or newer. The program uses only integers, exact rational arithmetic, and the Python standard library. Its terminal output ends with `VERIFY_OK` on success.

The computation checks the full affine lattice via a unit minor; enumerates all 5,005 nine-vertex facet witnesses; obtains 25 distinct valid primitive facet inequalities; obtains 5,734 faces including empty and full via exact facet-mask intersections; determines every face's dimension and incident facet normals; verifies 4,087 simplicial cones have lattice-unit minors; and identifies 1,645 nonsimplicial cones, whose 115 minimal elements have exactly one primitive \(\pm1\) ray relation each. Classification frequencies are 60 for \((2,3)\), 45 for \((2,4)\), and 10 for \((3,3)\); the complete \(S_5\) orbit multisets are \((10,20,30)\), \((15,30)\), \((10)\). Every vertex's incident-facet count is 18.

The implication from saturated one-relation toric cones to rank-one determinantal cones and their Segre multiplicities is a mathematical argument detailed in `RESULT.md`, not itself tested by polynomial ideal arithmetic. The verification makes no assertion of independent auditing or of historical-literature completeness.
