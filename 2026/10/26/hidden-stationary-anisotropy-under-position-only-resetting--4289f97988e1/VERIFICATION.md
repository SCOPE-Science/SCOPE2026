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

# Mathematical verification

The proof derives stationary generator equations for the projected second moment, projected–angular mixed moment, and projected fourth moment. The independent last-reset calculation averages the squared conditional Gaussian variance using the exact angular correlation \(\mathbb E[\cos(2\Theta_s)\cos(2\Theta_t)]=\tfrac12 e^{-4q|t-s|}\).

Run `python VERIFY.py` in an environment with Python 3, `sympy` and `mpmath` (and optionally `scipy` for transient ODE cross-checks). In the tested environment, the standalone script returned `PASS 984 mathematical checks`. These include 240 independent positive rational parameter quadruples, symbolic generator identities, numerical Laplace-age angular integrations, and finite-time ODE stabilization from distinct initial orientations. The script does not check priority and numerical samples are not an infinite proof.

At \((D_{\parallel},D_{\perp},r,q)=(3,1,2,1/2)\), the generator and renewal calculations independently give \(\mathbb E[Z^2]=2\), \(\mathbb E[Z^4]=51/2\), and excess kurtosis \(27/8\). The corresponding isotropic Brownian-reset stationary law has the same variance but fourth moment \(24\), demonstrating inequivalence.

The stationary theory requires strictly positive angular and translational diffusivities and strictly positive Poisson-reset rate. It does not establish a full exact non-Gaussian density or a finite-sample shape estimate.
