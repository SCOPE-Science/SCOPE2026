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

# Verification record

The analytic derivation uses the polygonal mixed-area edge-support identity, a gcd reduction to an evenly spaced angular grid, and the finite trigonometric sum. The proof itself treats every pair of integers \(n,m\ge3\) and every angle; the brute-force program is illustrative only.

The standalone `verify_polygon_sum.py` checker uses only the Python standard library, constructs the hull of all pairwise vertex sums, and independently measures its area by the shoelace identity. It was run for each pair \(3\le n,m\le18\), with two positive unequal radii, 15 noncritical rotations and both critical extrema, comparing 4352 cases and extremal hull side counts. Its recorded output was `VERIFY_OK pair_counts= 256 cases= 4352`. Floating tolerance was \(10^{-9}\); this does not certify the continuous claim. The 2011 motivating preprint's full text was inaccessible, and the historical novelty comparison is necessarily limited.
