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

# Verification record

The included `verify.py` uses only the Python standard library and exact rational arithmetic to check the derivative recurrence for three example distributions, the mean-zero constraints, the variance bound on those examples, and a finite first-derivative ratio sanity check. The analytic proof in `RESULT.md` establishes the asymptotic; finite checks are not used as proof.

Limits: fixed \(m\), \(k\), and \(q\); no independent audit or independent validation is claimed.
