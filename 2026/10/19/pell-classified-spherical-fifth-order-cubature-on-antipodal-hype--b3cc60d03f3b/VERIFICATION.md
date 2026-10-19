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

# Verification

The supplied `CHECK.py` uses only the Python standard library. It cross-checks rational formulas for the four-index sign correlation and both fourth-tensor coefficients, enumerates uniform subsets in dimensions 4 through 10 for three distinct mean-zero probes, reproduces the first five Pell solutions, and verifies fourth-moment equality for the first four admissible dimensions. It also checks failure of isotropy at one non-Pell parameter.

Actual command: `python CHECK.py`. Actual output: `PASS: 425 exact rational identities, combinatorial moment checks and Pell tests`.

These are finite checks; the universal statements rely on the symbolic coefficient identities, nonconstant quartic power sums, polarization, and Pell classification established in RESULT.md. No independent audit or external certification has been performed.
