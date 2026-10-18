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

# Reproduction and scope

Run `python attention_flip_check.py` with Python 3.9+ and no third-party dependencies. This checks the normalized full-softmax map itself, evaluates tangent derivatives by centered differences for 32 parameter/configuration cases, checks the two exact sign-flipping orbits, and verifies two 240-step locally attracting sample trajectories. The analytic theorem covers all stated real parameters; the finite computation is corroborative rather than a proof of all-parameter claims.

For arbitrary positive \(a<b\), \(\alpha>0\), and \(\eta>0\), the mathematical proof computes the derivative of every query/key dot product on the tangent circle at the two collinear states and shows it vanishes; the remaining normalization derivative gives the exact Jacobian. The hyperbolic stability test is the strict spectral-radius criterion for the second iterate. Equality endpoints and global basins have not been resolved or computed. Independent audit has not been performed.
