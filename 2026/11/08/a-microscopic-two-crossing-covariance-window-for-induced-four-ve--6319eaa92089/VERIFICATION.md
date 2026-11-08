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

The reproducible file `verify.py` contains 74 exact checks. It directly enumerates all graph realizations on up to six labeled vertices at three rational edge densities and uses rational-arithmetic coefficient interpolation to certify each of the three local projection polynomials. Run with `python verify.py` using Python 3 without installing third-party packages.

The exact covariance formula and the asymptotic scalings are derived in `RESULT.md`. The leading \(n^4\) covariance law follows from exact finite polynomial terms; the variance \(n^5\) terms follow from the disjoint triangle and wedge projections. The simple-root expansions use the implicit function theorem on the exact polynomial near \(p=1/2\). The finite enumeration is an independent check of the finite identity, not a substitute for the asymptotic proof.

No independent mathematical audit has been performed. Historical priority is not conclusively settled, particularly for a relevant inaccessible 1990 paper.
