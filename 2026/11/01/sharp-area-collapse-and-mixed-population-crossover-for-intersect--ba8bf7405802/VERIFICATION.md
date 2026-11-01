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

# Reproducible checks

Run `python check_intersection.py` with SciPy available. The completed execution printed:

`INTERSECTION_CHECK_OK: 25 independent numerical/algebraic checks; mixed crossover and two pure second-order expansions`

The checks independently evaluate radial CDFs from the original Gaussian/arcsine and Rayleigh/uniform mixtures and from the Bessel integrals at four nonzero radii of each type, compare both two-term small-radius expansions at two radii, verify symbolic identities for both asymptotic constants, calculate finite-population expected intersection-area integrals, evaluate three mixed critical-window cases, and check four limiting crossover integrals.

The samples are deterministic numerical evaluations and do not certify any infinite sequence or historical priority. The proof in RESULT.md gives the uniform-tail and asymptotic justifications. No external or independent mathematical audit was performed.
