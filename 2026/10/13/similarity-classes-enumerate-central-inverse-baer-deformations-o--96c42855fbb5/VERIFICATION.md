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

Using Python 3 with only its standard library, run `python3 verify.py` in the directory containing this report and `verify.py`. The script prints `VERIFY_OK` after exhaustive checks of all 729 alternating bilinear laws on \(\mathbb F_3^4\) under the symplectic transvection action, and all three parameter values of the two-dimensional central law on 27-element groups. Expected orbit sizes are 1,1,1,72,72,72,80,80,80,90,90,90. The rank-stratum counts are 1,3,8 at ranks 0,2,4 respectively. The symbolic proof addresses the infinite range of primes and dimensions; these are finite consistency tests only.

The proof, full source citations, and current scientific limits are in `RESULT.md`. An independent audit has not been performed.
