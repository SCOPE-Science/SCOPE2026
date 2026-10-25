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
# Verification of the sharp two-term local fourth moment

Run `python3 verify.py` in the same directory. The checker uses only the Python standard library and evaluates both exclusion polynomial identities by exact rational coefficient arithmetic, determines the unique positive critical point by bisection, and compares six independent midpoint quadratures with the proved sharp bound. During preparation, the execution printed:

`VERIFY_OK algebraic_identities=2 independent_quadratures=6 root=0.444104063969434 constant=1.607669326088568`

The proof does not rely on the finite six-case quadrature; it covers every pair of positive integer frequencies and every complex amplitude. The exact proof and strict exclusion arguments are in RESULT.md. The 2026 motivating full manuscript was inaccessible, so historical priority remains uncertain. Independent mathematical audit is not performed.
