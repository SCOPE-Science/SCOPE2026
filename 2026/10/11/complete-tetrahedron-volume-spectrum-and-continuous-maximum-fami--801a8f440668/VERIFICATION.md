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

# Verification and scope

The `verify.py` program accompanies this result as a standalone Python 3 standard-library certificate. It checks all \(\binom{12}{4}=495\) unordered four-vertex selections, compares two algebraically independent exact determinant expressions, computes exact positive/negative signs in \(\mathbb Z[\varphi]\), and establishes the five-volume histogram. It independently enumerates and tests the 20 supporting facets of the regular icosahedron; all 220 base triples and their allowed maximizing apex sets; all 20 base-to-facet correspondences; the same oriented maximum determinant across each associated facet; and the absence of all forbidden two-by-two grids. It also checks that all 30 vertex-supported maximizers are present in precisely two families.

Run with `python3 verify.py`. Success prints `VERIFY_OK vertex_sets=495 volume_levels=5 histogram=75,30,180,180,30 maxsets=30 families=20 facets=20 grids=0 witness=(0, 1, 4, 11)`. This is an exact **finite exhaustive enumeration** over a fully specified vertex set; the 60-digit comparison is redundant numerical diagnostics.

The argument for tetrahedra having arbitrary points in the polytope is the multiaffinity/convex-average reasoning in `RESULT.md`, together with the precisely enumerated equality conditions. The checker by itself does not prove statements about arbitrary continuum sets; the written mathematical reduction does. Historical priority and external scientific validation are not established.
