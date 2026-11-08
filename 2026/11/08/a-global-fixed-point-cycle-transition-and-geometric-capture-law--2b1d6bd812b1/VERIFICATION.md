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
# Verification and limits

To rerun the corroborating checks, execute `python3 verify.py`. They use standard-library exact rational arithmetic and seeded reproducible inputs; no external packages are necessary. The script checks all three parameter regimes at selected rational values, the two strict period-four orbits, the exact affine four-step return, eight nested survivor interval lengths, and the critical-square involution.

The proof in `RESULT.md`, not a finite test, establishes the theorem for every positive real parameter. No computer check of finitely many states certifies the global quantifiers; the right-branch square, complete section branch partition and affine inverse law do so analytically. Results about exceptional sets are planar measure statements and should not be confused with an independent stochastic interpretation. Independent audit is not yet performed.
