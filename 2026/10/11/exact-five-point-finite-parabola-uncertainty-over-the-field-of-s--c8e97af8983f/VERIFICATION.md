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

Run `python3 verify_parabola_7.py`. The embedded standalone program uses only the Python standard library and exact integer arithmetic. It enumerates all 194580 five-row frequency subsets containing the origin for fixed support 2,3,4,5,6, computes exact cyclotomic determinants and kernel cofactors, and evaluates all remaining frequencies in rank-four full-support cases. Expected leading output: `EXACT_CERTIFICATE_PASS`. The supporting mathematical reductions prove coverage of every five-point support, every nonzero complex coefficient vector, and the orbit and ray counts. A finite certificate is sufficient here because the underlying space of rank patterns is finite; no claim about arbitrary larger fields is inferred. The source version first posted in September 2026 could not be inspected in full, leaving a literature-coverage limitation. Independent audit has not been performed.
