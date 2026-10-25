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

The accompanying `verify.py` uses only Python's standard library. Execute `python3 verify.py` from the directory with the seven extracted files. A completed successful execution prints `ALL_PROJECTED_OCTAHEDRON_DIAMETER_CHECKS_OK`.

The program reconstructs the six projected vertex positions and the full set of pairwise distances for 400 integer normal triples, compares the exact Gauss--Bonnet CDF against independently parameterized spherical-area quadrature, checks the CDF's derivative against its stated density, checks both endpoint constants and the exact tangent-triangle area, and compares 260,000 seeded Gaussian-spherical samples against the distribution at five thresholds.

These are finite precision consistency checks and not an independent proof. The density identity, Gauss--Bonnet area evaluation, conditional tangent-triangle convergence and limiting coefficient computations are proved analytically in `RESULT.md`. Numerical sampling cannot establish that the result is historically new or that its asymptotic statements hold for all parameters.
