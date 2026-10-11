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

# Verification and limits

The proof derives the radial gauge by integrating the product survival function of independent uniform exit coordinates. The singularity estimate relies on the exact short-interval integral between the two competing maximal-coordinate cutoffs; both its exponent and its coefficient are computed analytically. The analytic continuation is used only locally, where its moment is positive.

`verify.py` is standalone and uses only Python standard-library decimal and rational arithmetic. Executing `python3 verify.py` checks the boundary-layer coefficient for \(p=-1/2,0,1,2\), at a generic two-way tie and two distinct triple-way ties, with perturbation sizes decreasing through three scales. It checks rational identities for integer exponents and independently evaluates the strict axial one-sided slope for a zero coordinate. The expected concluding line is `SHARP_RADIAL_JET_CHECKS_OK`.

The finite calculations are sanity checks, not an exhaustive proof of universal quantifiers. The all-dimensional, all-real-exponent statement rests on the polynomial survival identity, the uniform boundary-layer estimate and exact leading-term integration in `RESULT.md`. The classification concerns Peano jets at higher-order ties and does not assert local \(C^m\) for \(m\ge3\). Independent audit: not performed.
