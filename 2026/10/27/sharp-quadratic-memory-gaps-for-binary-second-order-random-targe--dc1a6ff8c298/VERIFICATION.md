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

# Verification and boundaries

The analytical evidence consists of a direct stationary flux solution, eight finite first-step systems, two exact factorizations, and positivity of the denominators. The proof covers every point of the strictly positive four-parameter transition cube; the program checks only a finite subset and cannot prove a universal or historical claim by itself.

`check_binary_second_order.py` independently constructs the lifted four-state transition law and solves the stationary and target-hitting linear equations using `fractions.Fraction`, without substituting the claimed analytic hitting-time expressions into those solves. Its assertions then compare independently solved values to both quadratic deficit formulas. The checks comprise 268 rational parameter tuples, include edge-near-positive examples, and explicitly verify the witness with marginal \((1/2,1/2)\).

Reproduction: run `python check_binary_second_order.py` in the folder holding the supplied source; the program needs only Python's standard library and prints its exact outputs to standard output. The included `check_output.txt` records its successful output. The command was performed again on the complete supplied source file before packaging.

Limitations: strict positivity is needed for the asserted stationary uniqueness, finite positive-hitting means, and denominator positivity. First passage is at a strictly *positive* time, including when the current state equals the target. The theorem concerns hitting a one-symbol target, not any of the four history states. No independent audit, external mathematical certification, or exhaustive historical-priority determination is asserted.
