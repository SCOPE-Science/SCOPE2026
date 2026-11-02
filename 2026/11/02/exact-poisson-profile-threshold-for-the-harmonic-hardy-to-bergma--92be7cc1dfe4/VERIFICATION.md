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

# Verification scope
The actual embedded `verify_poisson.py` program checks exact symbolic fourth-moment generating functions, the antiderivative, the normalized ratio and its derivative, the logarithmic-series coefficient identity, and the \(5/2\) limiting value. It is not an independent expert certification. Analytical assumptions (absolute convergence for interior parameters, coefficient positivity for all integer indices, normalized area and boundary integration) appear in RESULT.md.

# Limits
The program does not establish global extremality among arbitrary harmonic functions, nor does it check all historical literature. The independent audit is not performed.
