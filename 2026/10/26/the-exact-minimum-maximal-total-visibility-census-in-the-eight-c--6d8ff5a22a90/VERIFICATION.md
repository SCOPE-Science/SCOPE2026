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

Compile and execute `enumerate.cpp` using a standards-compliant C++17 compiler. The program checks every independent subset of each size \(5\le k\le8\) in the even-weight 128-vertex half cube, after normalizing one codeword to zero. It prints and checks these anchored pairs of counts (candidates, dominating): (611100,0), (2984625,0), (7490595,0), and (9234285,142380). It also prints the three observed distance-six degree-and-component profiles of the 142,380 anchored extremal codes. Expected terminal line: `VERIFY_OK`.

Execute `python3 verify.py` to check an even-parity code of size eight and its odd translate, their radius-two covering property and pairwise minimum distance four. It then independently tests the shortest-path definition of total mutual visibility for all 32,640 unordered pairs of the 256 vertices, using breadth-first search with internal selected vertices forbidden. It checks no additional cube vertex can be selected and verifies the exact unanchored count arithmetic. Expected terminal line: `WITNESS_OK total=16; half_count=2278080; min_maximal_total=5189648486400`.

The translation and vertex-incidence double-counting argument upgrades the normalized finite enumeration to the complete count. Enumeration cannot certify any unbounded-dimension conjecture, and the Python witness test alone is not a complete cardinality census.
