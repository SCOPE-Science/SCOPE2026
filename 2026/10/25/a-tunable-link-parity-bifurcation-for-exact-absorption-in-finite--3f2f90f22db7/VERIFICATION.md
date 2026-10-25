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

The complete proof is in `RESULT.md`. Run `python verify_bridge_absorption.py` with Python 3 and NumPy. The program prints `PASS: 813 checks; direct linear equations, flux, roots and large-n scaling` when successful. It checks the resolvent fraction and its hyperbolic representation, solves full stationary scattering linear systems for 18 segment sizes with varied loss and interface strength, verifies flux conservation, computes the root patterns on both sides of each even critical coupling for lengths through 18, and checks the leading finite-size asymptotics through length 1000.

The analytical argument—not this finite computation—proves all positive-parameter and all-length assertions. The quartic coefficient follows from cancellation of the critical logarithmic-curvature terms, giving exactly \(2n+1\). No interval or continuum exhaustive numerical certificate is asserted.

Known literature establishes the homogeneous-bond even/odd obstruction and the one-site absorption condition. The separately tuned joining-bond threshold, pair creation, quartic loss response, and large-length asymptotics are the precise content assessed here. There is no independent audit or experimental verification of this theorem.
