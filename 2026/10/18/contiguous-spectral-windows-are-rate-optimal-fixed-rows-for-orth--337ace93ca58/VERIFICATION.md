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

# Reproduction

`check_band.py` is self-contained and uses only Python 3 standard library modules. Run `python check_band.py`. It enumerates all active row sets in 1050 randomly generated ordered-spectrum cases, checks the finite-horizon survival identity by exact enumeration of 121 drawing paths, and checks five explicit three-mode parameters. Every check passed in the reported execution.

The unrestricted statement is proved algebraically: each row draw deletes exactly one error coordinate; the worst-case expectation is governed by the least sampled coordinate. The exchange argument is independent of the numerical tests. The three-mode asymptotic follows from elementary logarithmic limits. No external computational certificate or independent review is claimed.
