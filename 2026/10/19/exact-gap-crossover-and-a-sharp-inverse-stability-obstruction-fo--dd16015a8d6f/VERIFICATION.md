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

**Exact identities.** The four-tent equality and squared \(L^2\) norm follow analytically by Plancherel and direct tent-overlap integration. The power data are squared Fourier magnitudes, not Fourier magnitudes themselves. The quotient geometric metric minimizes symmetric-difference mass under translations and reflections; the reference equal-length set is reflection invariant.

**Executable check.** Run `python3 verification/covariogram_check.py` with Python 3 standard library only. The program evaluates eight cases by exact rational endpoint and covariogram integration, including ratios below one, between one and two, and at or above two; it also independently compares forty nonzero-frequency Fourier integrals with the closed identity. Successful output: `PASS: 8 exact rational covariogram integrals; 40 direct Fourier checks.`

**Limits.** Finite checks are not exhaustive. The universal validity rests on the displayed elementary analytic identities. The printed Lipschitz conclusion of Xia–Xu (Theorem 1.3(ii)) conflicts with this explicit family under its stated lower-bound assumptions; the contradiction should be independently assessed before drawing conclusions about the other results of that paper. No independent audit or external validation is claimed.
