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

# Reproduction checks

All operations use exact finite algebra over the binary field. `verify_census.py` runs an exhaustive projective coefficient-orbit enumeration and computes the Macaulay full-rank criteria and the complete rational hyperplane-section histogram, recording `census_output.json` and `orbit_representatives.tsv`. The verifier includes consistency assertions for the 36 smooth orbits and 322,560 equations, the two no-section orbit sizes and point counts, and all histogram bins.

`verify_groebner.py` independently checks the homogeneous gradient ideals on the four standard affine charts of each of 141 surface representatives, then checks every one of the 15 rational hyperplane sections of each of the 36 smooth representatives on three charts. Its saved stdout in `groebner_output.txt` reports zero discrepancies and the matching distribution.

The exact smoothness rank criterion is mathematical, not a bounded finite-field experiment. Both original computations were executed successfully, producing the saved expected records, before packaging. Classification is specific to the stated coefficient space and projective action; non-public earlier work and unindexed priority remain unverified.
