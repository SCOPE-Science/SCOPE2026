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

The analytical argument in RESULT.md establishes the scalar two-cycle exhaustion, exact product census, strict Schur stability of every nonzero coordinate orbit, and the sharp spectral plateau; these conclusions are not extrapolated from finite tests. The derivative at the zero-memory boundary is used only to find instability when the coordinate threshold is exceeded; attraction below that threshold has a separate direct contraction proof.

From this directory, run `python verify.py` with Python 3. It uses the standard library only, checks exact return identities and return Jacobian traces/determinants for 40 parameter pairs, enumerates product sign patterns in up to five active coordinates, and checks a curvature-ratio plateau example. Compare with `verify_output.txt`. All computations are finite and therefore cannot certify all-dimensional universality or historical novelty. A repeated quadratic root at a spectral plateau endpoint may have a Jordan block, so the sharp rate is expressed as spectral radius, not a fixed-constant pure power estimate.
