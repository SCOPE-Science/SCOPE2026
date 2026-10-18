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

Run `python3 verify_refinement.py` and `python3 verify_orbits.py` from this directory. The refinement verifier constructs actual adjacency lists and compares 1-WL partitions at rounds zero, one and two to the predicted orbit partition for all marker subsets up to size three in boards from \(2	imes2\) through \(4	imes5\), and additional seeded tests through \(9	imes11\). It also directly checks a nonsquare and a square sharpness witness. The automorphism verifier independently enumerates row and column permutations, with coordinate swaps for square boards, filters by pointwise-mark fixation and compares group orbits to the category formula.

Observed exact program outputs are in `verification_output.txt`:

- `VERIFY_REFINEMENT_OK cases=6413 vertex_instances=208470 sharp_examples=2`
- `VERIFY_ORBITS_OK explicit_group_instances=1276`

These are finite consistency checks, not proof for arbitrary dimensions or all marker subsets. The general mathematical proof appears in `RESULT.md`. The external independent scientific audit has not been performed.
