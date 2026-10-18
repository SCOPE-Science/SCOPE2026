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

# Verification instructions and boundaries

Compile `verify_greedy_binary4.cpp` with a C++17 compiler and run it with no command-line arguments. It constructs a complete 16-input overlap table from the four-bit words, computes all shortest-superstring optima by subset dynamic programming, and recursively considers every maximum-overlap greedy merge on every nonempty input subset. The entire comparison uses integer arithmetic and outputs an exact maximizing numerator, denominator, count and mask list. Cache resets every 128 input masks only bound memory usage; they do not drop an input subset. The complete transcript is in `verification_output.txt`.

Run `python3 verify_witness.py` to check the explicit eight-string witness using literal substring comparisons at every merge and exhaustive enumeration of all \(8!\) input orders for the optimum. The lower witness check is independent of the endpoint-state implementation.

The endpoint lemma and finite recurrence in `RESULT.md` justify extrapolation from checked software to **all 65,535 inputs in the stated domain**. Neither checker proves statements for larger alphabets or input lengths, and neither constitutes independent external scientific validation. Compiler/runtime failures are not treated as mathematical impossibility.
