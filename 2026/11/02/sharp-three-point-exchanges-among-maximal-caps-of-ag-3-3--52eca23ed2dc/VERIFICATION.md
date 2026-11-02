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

# Reproduction and claim-to-evidence mapping

The result concerns only \(27\) affine points and their \(117\) ternary three-point lines. Both complete programs are included as standalone files. They do not need downloaded data, external packages, or previously saved enumeration outputs.

Run:

```
python3 verify.py
g++ -O3 -std=c++17 -Wall -Wextra verify_alt.cpp -o verify_alt
./verify_alt
```

The first program builds all caps recursively using forbidden third points, verifies that exactly \(2106\) size-nine caps and no size-ten caps occur, compares every pair of size-nine caps, and constructs the \(3\)-exchange adjacency when the intersection size is six. It checks the full pair-intersection census, regularity, connectivity, and the complete joint intersection/distance table by breadth-first search from every vertex. Its final marker is `ALL_VERIFY_OK`.

The second program independently scans every one of the \(\binom{27}{9}=4686825\) size-nine bitmasks against \(117\) generated line masks, checks no size-nine cap extends to size ten, and generates each edge by explicitly choosing three removals and three insertions. All exchanges are rechecked for symmetry. It independently searches from all \(2106\) vertices and asserts every joint distance/intersection bin. Its final marker is `INDEPENDENT_VERIFY_OK`.

These exhaustive finite certificates establish the maximum size and number of caps, minimum nonzero exchange cardinality, \(72\)-regularity, \(75816\) edges, connectedness, diameter four, and the stated distance layers. The interpretation of disjoint distance-four partners as the unique complementary cap partition uses the independently published Proposition 2.2 of Follett et al. No result for larger affine dimensions follows from these checks. The reported checks are same-authority computational reproductions; independent scholarly audit is not performed.
