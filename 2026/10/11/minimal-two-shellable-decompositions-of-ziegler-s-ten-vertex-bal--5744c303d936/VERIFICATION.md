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

The standalone `verify.py` uses only the Python standard library and the twenty-one tetrahedra stated in the result. It reconstructs the complete face set and checks the face vector \( (10,38,50,21)\).

For every nonempty tetrahedron subset, it decides shellability by the exact recursive last-facet criterion. The dynamic program covers all \(2^{21}-1\) nonempty subsets. It then examines every unordered nontrivial complementary partition, retains only pairs whose two generated pure \(3\)-complexes are shellable, reconstructs their intersection from all cross-facet intersections, requires that the maximal intersection faces are triangles, and independently applies the shellability recurrence to that \(2\)-complex.

The verification therefore exhausts the complete finite domain of the claim. It also checks that the full ball itself is not shellable, that exactly \(247\) partitions survive, that their block-size distribution is \(3,10,23,40,74,97\), and that the minimum block size is five with exactly the three displayed witnesses and four interface triangles each.

Successful replay prints:

`VERIFY_OK f=10,38,50,21 shellable_full=no two_shellable_splits=247 size_distribution=5+16:3,6+15:10,7+14:23,8+13:40,9+12:74,10+11:97 minimum_block=5 minimal_splits=3 interface_triangles=4_each`

The computation is exact integer/set logic. It makes no claim about arbitrary recursive constructibility trees beyond the explicitly defined two-shellable decompositions.
