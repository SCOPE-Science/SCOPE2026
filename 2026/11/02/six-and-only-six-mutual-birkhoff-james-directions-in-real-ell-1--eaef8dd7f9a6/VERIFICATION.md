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

The proof directly covers **every** nonzero real vector and every projective clique. Its sole functional-analytic ingredient is the exact subgradient/norming-functional formula for \(\ell_1^3\); no positivity or coordinate discretization is assumed in the final theorem. The upper-bound partition into axes, full support and two support types is exhaustive, and equality forces balanced pairs in all three coordinate planes.

The standalone `CHECK.py` (Python standard library only) checks 13 ternary projective sign patterns, 36 mutual edges, one six-clique, and 15,376 ordered nonzero integer-vector pairs for the directional derivative criterion. Replay from the same directory with `python3 CHECK.py`. These tests establish finite consistency only; the preceding analytic proof handles all real vectors.

Scientific limits: complex scalars and dimension at least four are not covered. Equivalent, unindexed results may exist; one relevant survey was not available in full. Independent audit has not been performed.
