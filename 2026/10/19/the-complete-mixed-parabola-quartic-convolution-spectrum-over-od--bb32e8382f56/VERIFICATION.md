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

# Reproducible checks and limits

Execute `python3 verify.py` in the directory containing the distributed files. The checker uses only the Python 3 standard library, constructs prime fields and degree-two finite-field extensions via an irreducible quadratic polynomial, and independently enumerates all ordered mixed sums. For each of 16 fields it checks the displayed five-level counts, the total target count, the first and second factorial moments, and the mixed energy identity. `verification_output.txt` contains the exact replay output ending with `ALL PASS: 16 fields, including three quadratic extensions`.

The script was run successfully against its own distributed `verify.py` source. It checks fields of orders 5 through 47 (thirteen primes listed in the result) and 25, 49, 121. These finite computations are diagnostic and do not certify infinitely many fields. The complete mathematical proof is the quadratic Gauss sum formula, the 3-root Vieta reduction, the exhaustive equality-partition inclusion–exclusion, and factorial-moment inversion given in `RESULT.md`. No external independent validation has been performed.
