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

# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 interpreter. Expected final line: `VERIFIED four bases; 32 small primes, all primes below 40000 per base, 8770 composite bounds`. The proof itself is in `RESULT.md` and uses no computer output beyond the explicitly enumerated prime candidates below the base-specific length cutoffs. The tests over larger ranges and composite inequalities are auxiliary reproducibility checks and do not certify the infinite theorem independently.

The scientific proof uses the exact base-dependent definition and the arithmetic weight of prime powers. The three primary references explain the previously open base-classification problem and the nearest decimal-only prime theorem. Public-source comparisons found no implication covering all four bases. An external audit has not occurred.
