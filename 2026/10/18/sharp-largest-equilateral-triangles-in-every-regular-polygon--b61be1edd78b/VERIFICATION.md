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

# Verification and boundaries

Run `python verify.py` after extracting it from the package. The standard-library checker independently enumerates the vertices of the orientation-specific three-variable linear program in small regular polygons. It also checks witness feasibility and the strict angular inequality for the integers 4 through 300 that are not multiples of three. The expected final line is:

`VERIFY_OK analytic_witness_cases=198 independent_LP_orientations=80`

A finite check does not certify all dimensions, all integers, or all continuous orientations. Those follow from the explicit analytic proof, including the balanced support-normal bound, direct witness containment, and rigidity of active contacts. Historical mathematical priority remains uncertain where a highly relevant older primary source was inaccessible.
