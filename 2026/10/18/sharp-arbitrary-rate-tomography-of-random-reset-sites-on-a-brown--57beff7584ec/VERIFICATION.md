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

Run `python verify.py` from the directory containing the supplied files with Python, `sympy`, and `mpmath` installed. Reconstructed site counts were 2, 3, and 4 by exact symbolic arithmetic; high-precision numerical calculations checked a 3-site case, the forward renewal formula and diffusion boundary-value equation; 15 sampled increasing-node cosh-kernel determinants were positive. The symbolic and numerical checker printed `all checks PASSED`.

These tests are reproducibility evidence for selected cases, not proofs for all site counts, all positive rates, or all unknown measures. Those infinite claims follow from the Cauchy–Binet strict-positivity proof, Vandermonde and Hankel arguments, invariance of domain, and compact moment uniqueness in RESULT.md. Finite-data noise sensitivity is not bounded. Site orientation is provably unidentifiable. An independent audit has not been performed.
