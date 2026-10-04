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

Run `python3 verify_magnitude_heawood.py`. The checker reconstructs the graph and shortest-path metric, independently confirms the relevant chain counts by enumeration and dynamic programming, builds the two boundary maps from the magnitude-chain deletion rule, checks the chain condition, computes each boundary rank in two orientations, and verifies the nongeodetic witness. The accepted numerical checks are \(840\), \(2268\), \(1134\) for the three chain dimensions, boundary ranks \(840\) and \(1092\), and resulting mod-2 homology dimension \(336\).

The computation proves only the stated finite \(\mathbb F_2\) bidegree. It does not establish an integral decomposition, torsion statement, or family theorem.
