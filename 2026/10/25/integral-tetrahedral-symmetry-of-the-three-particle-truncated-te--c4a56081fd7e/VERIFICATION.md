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
# Reproducibility and verification

Run `python3 verify.py` with Python 3.9 or later. The script imports only the Python standard library. Expected final marker: `TRUNCATED_TETRAHEDRON_B3_Z4_S4_PERMUTATION_VERIFIED`.

The checker independently constructs all 12 vertices and 18 edges of the truncated tetrahedral graph; confirms valence three; enumerates the entire weight-three degree-three and degree-two reduced Świątkowski chain bases of respective sizes 1,760 and 4,752; and constructs all 1,760 signed differential columns. It computes the full rank as 1,756 over both \(\mathbb F_2\) and \(\mathbb F_{32003}\), using exact arithmetic with no approximation. Each of four explicitly constructed three-triangle product cycles has integral boundary zero, disjoint support from other cycles, and only unit coefficients. For each of the 24 graph symmetries, it transforms each of these four integral chains and confirms 96 **signed coefficient-wise** equalities with the appropriate permuted basis cycle.

The code's finite field ranks alone neither prove integral homology nor an infinite theorem. The accompanying written proof uses the established natural integral chain-model comparison, four rationally independent cycles to force equality in characteristic zero, and disjoint unit-coefficient supports to establish primitive saturation over the integers. Because weight three permits no chain degree exceeding three, there are no higher boundaries at degree three.

This verification does not calculate lower-degree homology, fundamental groups, or spaces of four or more particles. Independent mathematical audit has not been performed.
