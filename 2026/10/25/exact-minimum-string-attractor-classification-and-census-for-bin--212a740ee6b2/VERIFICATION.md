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

# Verification of the mathematical claim

The theorem's infinite quantifiers are proved in `RESULT.md` by an exhaustive inequality-case partition, explicit attractor witnesses, two disjoint forced-factor obstructions, and symbolic generating-function calculations. The proof requires no machine assistance for its universal statements.

The complete standalone program `verify.py` uses Python's standard library. Execute with `python3 verify.py`; success prints:

`FOUR_RUN_ATTRACTORS_PASS brute_parameter_tuples=2401 max_run_length=7 exact_length_coefficients=4..22`

The program independently generates all distinct contiguous factors of each four-run test word and merges the position masks of all their occurrences. It then checks all choices of one, two, and three positions for a hitting set, compares the mathematical classification, checks constructive witnesses, and verifies integer coefficients of the proposed generating function. It tests all positive \(a,b,c,d\le7\) and independently checks \(4\le n\le22\) for the integer enumeration.

Finite verification is not a proof for larger parameters. No independent mathematical audit has yet been performed.
