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
# Reproducing finite verification checks

Run `python3 lens_check.py`. This file uses only the standard library; it checks exact polynomial identities using rational arithmetic, independent conditional radial and angular integrations, agreement with the known three-dimensional distribution, parameter-order inequalities at finitely many radii, direct normalized-Gaussian spherical-quotient samples, and diameter-tail constants. In the completed local run it printed `PASS 951 checks; independent radial/angle quadratures, prior 3D law, exact polynomials, Monte Carlo sphere orbits`.

The analytical proof in RESULT.md is the basis for the all-dimensional statement. The checks do not exhaust all integer dimensions, cyclic orders, or continuous radii, and do not constitute an independent mathematical audit. No external certification has been performed.
