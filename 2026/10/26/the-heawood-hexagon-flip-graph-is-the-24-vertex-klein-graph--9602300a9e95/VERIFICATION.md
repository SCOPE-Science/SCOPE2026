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

# Reproducibility and checked limits

Run `python3 verify_permutations.py` and `python3 verify_cycles.py` from the directory containing the scripts and `klein_reference.am`. Both are standalone Python 3 standard-library programs. Their captured actual outputs are `verify_permutations.out` and `verify_cycles.out`.

The first program checks all 5040 permutation possibilities, identifies all 24 admissible perfect matchings, constructs every Hamming-three transition, checks connectivity and all 576 ordered-pair intersection-number conditions, enumerates eight perfect one-factorizations, and tests each of 576 adjacency-matrix entries against the published Klein matrix under an explicit vertex permutation. The second independently enumerates matching assignments, all 28 hexagons, and the alternating six-cycle flips, then reproduces the same graph fingerprint and graph invariants. The second method does not derive flip adjacency from Hamming distance.

The shared canonical SHA-256 fingerprint of the lexicographically ordered matchings and sorted flip edges is `d24c03e5de28643a1ab7271df299b66de1fc6d3e71d1ad151bfa2ce71911f04a`. The 24-line comparison matrix is reproduced from https://www.math.mun.ca/distanceregular/graphdata/klein.am ; its standalone file SHA-256 is `6302f118d7c7fe0cf6a3a8de2f56a8959c02b45c930cafebcbb596efd9a8e673`.

The finite domain is all matchings on exactly 14 vertices of the specified Fano incidence graph. No inference is made about arbitrary cubic graphs, higher-order projective planes, or longer alternating-cycle flips. Literature priority is not formally certified. No independent external audit has been performed.
