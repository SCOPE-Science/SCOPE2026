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

The `checker.py` program enumerates each partition of a labelled set directly, evaluates the least-cell normality criterion for all ordered tuples in the designated finite test cases, and computes the independent Stirling–Bell census expression. It also explicitly evaluates every two-variable valuation for all partition tuples at the small sizes specified in `RESULT.md`. Running `python checker.py` produces matching counts and the final line `All checks passed.`

These calculations verify the finite cases only. The all-size census is established by the quotient/inclusion–exclusion proof, and the growing-agent Poisson and normality limit by factorial moments, Bell-ratio estimates, and a union bound. No external or independent mathematical audit has been performed. Uniform Bell asymptotics and the Poisson factorial-moment method are invoked as established mathematical results.
