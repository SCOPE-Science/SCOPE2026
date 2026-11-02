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

# Reproduction and verification

Run `python3 check_wheel.py` in a standard Python 3 environment. It uses only `fractions.Fraction` and `itertools.combinations`, with no external dependencies. The script directly enumerates acyclic edge sets of wheels with three through seven rim vertices and independently recomputes all forced spoke-subset weights at three rational fugacities. It also verifies strict negativity and increasing pair coincidence with circular distance. Its separate determinant routine checks all index subsets of sizes one through five in a nine-point window for three rational exponential bases.

Expected result:

`PASS 822 exact wheel-forest inclusion and covariance tests; 1143 exact Toeplitz determinant tests`

These finite checks replay the formulas at enumerated sizes only. The analytic proof of universal finite-size identities and the infinite-volume stationary renewal/determinantal law is in `RESULT.md`, Sections 1–5. Historical overlap with the full multivariate wheel-forest paper remains an unresolved research-priority question; prior unit-fugacity results are not claimed as new. Independent validation has not been performed.
