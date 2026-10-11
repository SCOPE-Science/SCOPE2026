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
# Verification of the surface classification

Run `python3 verify_ladder_neighborhood.py` with Python 3 standard library only. The proof for all parameters is in `RESULT.md`, not inferred from these tests. `verification_output.txt` records the expected completed run.

The script independently constructs each graph and its open-neighborhood facets, verifies every link is a path or circle, checks triangles have edge multiplicity at most two, computes connected and boundary components and Euler characteristic, propagates coherent orientations, and uses exact bit-vector elimination on mod-two simplicial boundaries. These tests cover 29 Möbius cases with parameter from 2 through 30 and 28 circular cases with parameter from 3 through 30. The orientations and mod-two ranks agree with the PL types stated for every tested case.

This is a finite computational corroboration of an all-parameter symbolic argument, not an exhaustive proof for all integers or an independent audit. The mathematical proof relies on the explicit simplex and dual-graph descriptions and compact-surface classification.
