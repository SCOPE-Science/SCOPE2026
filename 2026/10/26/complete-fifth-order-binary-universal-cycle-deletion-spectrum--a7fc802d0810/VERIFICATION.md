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

From the directory holding the two Python programs, run `python3 verify_parity.py` and `python3 verify_mitm.py`. Both are standard-library-only and operate on the explicit 16-vertex/32-edge directed graph whose arcs are the five-bit words. The first computes an exhaustive basis for the rank-15 GF(2) incidence constraints and checks all 131072 parity-feasible subsets. It then requires exact integer degree balance, weak connectivity among active vertices, and at least five remaining edges. The second creates every one of the 65536 choices for each half-edge set, matches opposite 16-component signed divergence vectors, and uses disjoint-set connectivity. Both recompute the full 33 coefficients; neither reads a stored result table as its data source.

Observed script completions:

`PARITY_ORDER5_UNIVERSAL_CYCLE_PASS basis=17 balanced=6600`

`MITM_ORDER5_UNIVERSAL_CYCLE_PASS 6600 balanced`

The complete resulting coefficients are given in `RESULT.md`. Exact finite enumeration establishes this single fixed-order claim; it does not certify a general parameter theorem, uniqueness of the literature result, or independent validation. All integers are exact and no numerical tolerance is involved.
