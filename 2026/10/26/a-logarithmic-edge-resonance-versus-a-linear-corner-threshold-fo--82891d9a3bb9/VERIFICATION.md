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

# Reproduction and limits

The mathematical argument is in `RESULT.md`. Run `python3 verify.py` using Python 3 (standard library only) to reproduce independent midpoint numerical checks of the first edge and quadrant sites. The script prints `NUMERICAL_CHECKS_OK` upon successful finite checks. Its midpoint approximations are not certified enclosures and do not establish spectrum, asymptotic limits, or originality; those depend on the proof and literature assessment.

For the critical half-plane state, the momentum-space function is locally \(O(|k|^{-1})\) and fails to be square-integrable; for the quadrant it is locally \(O(1)\) and is square-integrable. The scalar spectral equation is \(1=\lambda F(\varepsilon)\), with \(F(0)-F(\varepsilon)\) of order \(\varepsilon\log(1/\varepsilon)\) or \(\varepsilon\) respectively. In the first case the exact logarithmic coefficient is \(j^2/(4\pi)\); in the second the coefficient is the explicit positive Brillouin-zone integral \(B_{a,b}\). Both checks hold for any fixed positive integer site coordinates. This package does not include an external audit or computer-assisted certificate of infinite-dimensional statements.
