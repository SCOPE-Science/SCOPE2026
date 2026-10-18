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

The standalone `verify_hardy_commutator.py` was executed against the actual packaged script. It verifies integer-exponent kernel identities, exact rank-two cross-block matrices and the rational Hilbert--Schmidt integral formula. These computations are finite checks only. Infinite-dimensional correctness rests on the independent analytical argument in `RESULT.md`, including the beam spectrum for double integration, \(H^3\) smoothing of the regular remainder, Ky Fan interlacing and geometric summation of singular-value counts.

The Weyl limit is pointwise in the parameter \(\alpha>0\); no error bound uniform down to \(\alpha=0\) is asserted. The 1996 and 1988 full papers were inaccessible and were not used as proof of originality. The status of independent validation is not_performed.
