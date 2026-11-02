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

# Verification details

The accompanying `CHECK.py` evaluates a symbolic cubic reciprocal resultant over four independent algebraic parameters, checks its factored identity and the two boundary frequencies, and tests the Zak Fourier formula against direct convergent series for three asymmetric pole pairs. The theorem's strict inequalities were checked separately by differentiating \(x\coth x\), \(x\tanh x\), and \(x/\sinh(x/2)\), as written in the proof. The latter parameter-uniform analytic steps cannot be certified by finitely sampled calculations.

The critical spectral-domain boundaries are \(0<a<b\), \(0<\xi<1\), and the edge \(\xi=0\); the case \(a=b\), larger pole sets, and arbitrary lattice densities are not asserted. The mathematical review is not independent.
