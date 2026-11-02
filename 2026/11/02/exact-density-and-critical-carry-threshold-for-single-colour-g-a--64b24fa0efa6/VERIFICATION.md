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

Run `python3 artifacts/verify.py` with a standard Python 3 interpreter. The script enumerates allowed-digit integers for seven finite digit-position sets in bases two, three, and four. For each case it forms exactly \(g\) positive summands, separately enumerates all independent carry-block coordinates, and verifies their equality after deleting the precisely classified configurations having fewer than \(g\) total block-coordinate units. It also checks the exact number of carry-block words by multiplication of their interval sizes. Finally it directly verifies the prohibited-digit restriction at each smaller summand count.

The observed successful final line was:

`VERIFY_OK finite_cases=7 independent_forms=3 exact_integer_arithmetic=yes`

All operations are exact integer arithmetic; there is no randomized sampling or floating-point tolerance. The proof of the theorem itself rests on the infinite-block decomposition, periodic finite-prefix densities, a uniform tail union bound, and a polynomial-logarithmic bound for zero-summand exceptions. These infinite steps are explained in `RESULT.md` and cannot be inferred from finite enumeration. Historical originality comparisons are literature-based and not independently certified. No independent mathematical audit has been performed.
