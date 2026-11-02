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

The geometric proof in `RESULT.md` is the primary certificate. It derives shortest paths using a last-crossing lower bound, resolves the opposite-face minimizer by planar Voronoi sectors, constructs three exact nonoverlapping radial kites, and performs exact polar integration. These steps establish the CDF for every radius and the moment formulas for all real orders greater than \(-2\).

`verify.py` performs a separate reproducible check based on sampling four physical faces, not sampling the derived radial-kite law. With seed `2342809` and 125,000 points per face, the largest twelve-threshold empirical-CDF discrepancy was `0.0006568442373833805`; the sampled mean was `0.7024589696753071` versus `0.7020422297585325`; and the sampled second moment was `0.556058207200719` versus `0.5555555555555556`. The analytic first and second moments agreed with adaptive quadrature to its numerical precision. Three arbitrary-precision perturbations checked the sharp coefficients at both transitions. The checker exited with `all_checks_passed`.

Monte Carlo does not prove a continuum statement, numerical quadrature does not establish exact identities, and the calculation does not establish independent historical priority. The sharp coefficients and normalized endpoints are verified algebraically in `RESULT.md`.
