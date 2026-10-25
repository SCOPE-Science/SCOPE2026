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

# Reproducibility notes

Run `python verify.py` in a directory containing the extracted file. The program uses only Python 3 standard-library `fractions`, `itertools`, and `math` modules and prints its exact assertion count on success.

The script checks 1,680 exact-rational assertions on explicit finite-support potential-contact laws. It directly computes full terminal-generation distributions, evaluates all integer stop-loss functions (an exhaustive convex-order test for those finite examples), compares all six orders of three specified transmissibility levels, and checks the adjacent-swap variance formula and the two-generation benchmark.

The theorem for arbitrary finite horizon and arbitrary finite-second-moment potential-contact laws is established by the proof in `RESULT.md`, not by enumeration. No claim is made of finite-network, cumulative-incidence, or calendar-time verification. Independent audit has not been performed.
