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

The displayed co-detection covariance identity was checked by an independent labeled-subset enumeration for every feasible incidence-overlap parameter triple and every sample depth for populations of two through ten units. The code in `verify_incidence_covariance.py` executes using Python's standard library (`fractions`, `itertools`, `math`, `json`); no third-party dependencies or external data are needed. It made 3,774 exact covariance comparisons across 460 parameter triples, tested the closed criterion, and verified the special-family polynomial and sign pattern in 5,040 additional exact calculations for populations of five through one hundred units.

Reproduce by running `python3 verify_incidence_covariance.py` from the package directory; its JSON output should equal `verification_certificate.json`. All stated computation checks were executed successfully. The unrestricted theorem is based on the ratio-factor proof in `RESULT.md`, which is independent of finite enumeration. The computation does not certify untested sampling schemes or literature uniqueness.
