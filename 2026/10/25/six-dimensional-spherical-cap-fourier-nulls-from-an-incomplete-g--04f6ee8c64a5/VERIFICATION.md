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

The rational interval checks in `check.py` certify the two signs of the amplitude difference on \(c=0.9\) and \(c=1\), as well as a positive derivative bound exceeding \(0.145\) throughout \([0.9,1]\). The Bessel asymptotic and the uniform finite-tip expansion are analytic proof steps, not covered by numerical checks. High-precision illustrative zeros for indices 10, 20 and 40 are recorded in `checker_output.txt`. To replay: `python check.py` with `mpmath`; no network required. No independent audit has been performed.
