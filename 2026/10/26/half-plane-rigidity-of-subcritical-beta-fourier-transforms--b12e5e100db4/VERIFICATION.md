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

The two executable Python programs use mpmath. The Kummer-root checker tests 60 nonreal zeros for the specified parameter grid and both orientations with 50-digit precision. The Wronskian/derivative checker uses 55-digit precision to test 16 asymmetric cases, Bessel zeros and first-order movement. Their recorded outputs are packaged as standalone files.

The proof of the infinite claim uses the endpoint asymptotic, the parameter-uniform error argument, and a topological zero-continuation argument, none of which is certified by finite testing. Publication priority against all pre-1973 and subsequent special-function literature remains a genuine limit; independent mathematical audit was not performed.
