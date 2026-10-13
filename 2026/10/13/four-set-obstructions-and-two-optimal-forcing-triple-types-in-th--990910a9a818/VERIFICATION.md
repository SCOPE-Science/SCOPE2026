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

# Reproduction and verification

Run `python3 verify.py` with Python 3.8 or later. No packages or external inputs are required. The verifier constructs the 14-vertex cyclic Heawood graph, enumerates every allowed permutation matching (seven rows, three candidate neighbours per row), and independently computes the exact permanent using Ryser inclusion-exclusion. It also reconstructs the Fano incidence relation using seven nonzero binary vectors and checks the same matching set in that second model.

For every one of the 24 matchings, the verifier directly evaluates each of its 128 edge subsets by counting how many complete perfect matchings extend that subset; it agrees exactly with the proposed polynomial and, for the reference matching, with the seven-block criterion. For symmetry, it enumerates all 168 invertible linear maps of the 3-dimensional binary vector space, adds point-line duality, and applies all 336 graph automorphisms to the matching and forcing subsets, verifying the claimed full orbits.

Expected successful output:

```text
VERIFY_OK fano_incidence=7points_7lines heawood_edges=21
VERIFY_OK matchings_permutation=24 ryser_permanent=24 geometric_matchings=24
VERIFY_OK overlap_histogram=0:2,1:7,2:7,4:7,7:1
VERIFY_OK seven_maximal_nonforcing_4sets=rotations_of_{0,1,3,5}
VERIFY_OK all_128_subsets_per_matching=24_matching_checks
VERIFY_OK per_matching_forcing_polynomial=14z3+28z4+21z5+7z6+z7
VERIFY_OK minimum_local_forcing_sets=14 cyclic_types=7+7
VERIFY_OK automorphisms=336 matching_orbit=24 stabilizer=14
VERIFY_OK across_matchings_minimum_triplets=336 orbit_sizes=168+168
```

The assertions cover exactly the stated finite graph and finite matching universe. This is reproducible computation and internal review only, not external or independent validation. The count of all perfect matchings is essential: checking just the seven four-edge competitors, without exhausting the remaining matchings, would be insufficient to prove the obstruction criterion.
