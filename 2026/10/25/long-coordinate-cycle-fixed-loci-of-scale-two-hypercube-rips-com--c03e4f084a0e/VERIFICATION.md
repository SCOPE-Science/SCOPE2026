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

# Verification and reproducibility

Run `python3 verify_fixed_rotation.py` from the package directory; Python 3.8 or later is sufficient and no third-party libraries are required. The standalone script reconstructs all cyclic vertex orbits of the rotated Hamming cube, tests whether each orbit spans a scale-two Rips simplex, directly checks every pair of admissible orbits, and verifies that the proposed simplicial map preserves edges and is contiguous to the identity. Because both the orbit complex and its proposed target are flag complexes, checking all pairwise relations confirms all simplices for each tested finite parameter pair.

Actual execution of the packaged source produced `CASE_COUNT=19 ALLOWED_ORBITS_TOTAL=300 PAIRS_TOTAL=4274` followed by `VERIFY_OK`; the per-instance output is included in `verify.log`. Finite cases cover k=4 with m from 0 through 4, k=5 and 6 with m from 0 through 3, and k=7 and 8 with m from 0 through 2. These computations demonstrate finite consistency, not an infinite theorem. The proof in RESULT.md supplies the all-parameter orbit-weight bound and explicit strong retraction; the cited Adamaszek–Adams theorem supplies the integral component classification.

No external or independent audit has been performed, and these checks do not assess research priority.
