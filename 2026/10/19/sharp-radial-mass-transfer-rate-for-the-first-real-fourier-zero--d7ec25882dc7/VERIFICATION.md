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

The primary proof is the decreasing-energy identity for the radial sphere kernel; it is valid in every integer dimension at least two and forces the two shell-location extrema. Uniform radial mass bounds, the intermediate-value argument, and simple-root perturbation establish matching upper and lower first-order bounds. Standard Bessel differentiation gives the coefficient in the theorem.

Run `python check.py` with Python 3, NumPy and SciPy. It computes the first two positive Bessel zeros (integer or half-integer order), the normalized unit-ball Fourier transform, the explicit two-component perturbation Fourier profile, and the first positive zero near the original one. It compares the observed displacement against the analytic coefficient at two mass fractions for each dimension two through seven. The script reports its numerical tolerances. The proof does not depend on numerical experiments, and no independent validation has been performed.
