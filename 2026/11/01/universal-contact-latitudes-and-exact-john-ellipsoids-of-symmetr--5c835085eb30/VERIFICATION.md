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

The proof is analytic. The key exact checks are the positive root of the semiaxis quadratic, the squared-distance identity on the unit sphere, tangency of normalized ball-supporting gradients, and the weighted contact relations \(\sum_i\omega_i u_i=0\) and \(\sum_i\omega_i u_i u_i^{\mathsf T}=I_d\). Together with the standard sufficient form of John's theorem, these establish global unique optimality for all permitted dimensions and overlaps.

Run `python3 verify.py` with NumPy and SciPy. It tests finite examples in dimensions from \(2\) through \(100\) and overlap parameters between \(0.001\) and \(0.99\), numerically checks the exact identities and finite contact certificate, and compares solutions with continuous constrained axisymmetric optimization for selected parameters. It also checks a fixed-separation, large-dimension limit.

Numerical optimization and grid testing do not prove the theorem for all real parameters or certify an independent audit. The analytic proof requires the established John contact theorem. An equivalent calculation in older literature has not been conclusively ruled out.
