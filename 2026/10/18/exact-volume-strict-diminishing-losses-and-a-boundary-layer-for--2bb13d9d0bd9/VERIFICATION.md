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

# Reproducibility and verification

Execute `python check_volume.py` in a directory containing this file and the standalone script. It uses only Python's standard library and performs 15 exact rational comparisons, spanning the single-pair and fully shortened endpoints and mixed contractions in dimensions three, four and five.

The checker forms an integral dilation of each rational-parameter Lipschitz dual polytope, enumerates lattice points at dilations \(0,1,\ldots,n\), and extracts the leading coefficient by finite differences. The signed incidence constraints are totally unimodular, so the Ehrhart polynomial of the integral dilation has leading coefficient equal to the dilated coordinate volume. No floating-point fitting or tolerance is used. All 15 tests passed.

The infinite family is established by the separate minimum-coordinate integration, discrete difference identities, and asymptotic argument in `RESULT.md`; the checker cannot establish those universally. Other vertex-dilation patterns, unequal short spoke weights, the primal unit-ball volume, and independent audit are not verified here.
