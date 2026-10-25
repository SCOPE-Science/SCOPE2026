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

The proof and exact rational inequalities appear in `RESULT.md`. Replay the standard-library diagnostics by running `python3 checker.py` in the directory containing the embedded files. On this result the command printed `CHECK_PASS pstar= 0.323267128142707 endpoint_rank= 246 checked_rational_bounds_and_256_characters`. The program reproduces the four exact Krawtchouk vectors, the positivity witnesses obtained from cubed rational bounds, and quotient Walsh eigenvalues over all 256 cosets at five sample exponents. The unrestricted exponent classification and all-bandwidth consequences depend on the analytic proof, not those finitely many samples. No external independent audit was performed.
