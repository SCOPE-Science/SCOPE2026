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

# Verification and scientific limits

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The verifier evaluates the exact monotone quadratic transport cost for centered standardized binomial sums by summing Gaussian cell first moments, tests convergence for parameters 0.2, 0.3, 0.5 and 0.7 across three sizes, and confirms the quadratic constant symbolically. The accompanying recorded output reports 21 passed assertions.

The finite verifier cannot establish an asymptotic theorem. The analytic evidence consists of the corrected lattice CDF Edgeworth expansion, inversion at Gaussian-quantile cell boundaries, periodic oscillation averaging and the higher-moment transportation bound for uniform integrability. Results assume a fixed maximal-span finite-support iid law; no general nonlattice result is asserted.
