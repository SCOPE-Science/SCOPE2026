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

The analytic proof and the standalone script `verification/check.py` are the evidence for this package. The script executes without third-party dependencies using Python 3 and checks diagonal eigenvalue identities for 25 parameter choices, exact beta-CDF instances in dimensions two and three, the critical three-dimensional half-probability example, finite independent-sphere simulations, exact tail constants for the critical regime, and a high-dimensional chi-square approximation.

Run: `python3 verification/check.py` from the package root.

Observed output: `VERIFY_OK exact_spectral_cases=25 beta_cdf_cases=5 finite_probe_checks=4 high_dimension=1`.

Random simulations have fixed seeds and specified finite sample counts. They verify finite comparisons within numerical tolerance but do not prove beta-law identities, tail equivalences, integrability boundaries, or the order-of-limits statements; those are established in `RESULT.md`. No external audit or independent validation is claimed.
