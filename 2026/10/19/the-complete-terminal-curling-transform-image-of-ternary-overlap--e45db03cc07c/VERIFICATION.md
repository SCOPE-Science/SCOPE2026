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

# Reproducibility

The attached `verify_profile.py` enumerates all canonical representative pairs up to length 85 and verifies the terminal transform image, fiber cardinalities, and parent branching. It has no external dependencies. Run `python3 verify_profile.py`.

The attached `crosscheck_full.cpp` independently enumerates every labeled candidate without symmetry reduction, using explicit period comparisons. Compile with `c++ -std=c++17 -O2 crosscheck_full.cpp -o check_full` and run `./check_full`. Both executables were run with all assertions enabled, with successful outputs recorded verbatim in `computation_output.txt`.

The finite reasoning is exhaustive because both source and transformed-prefix overlap-freeness are hereditary and because the next curling number in an overlap-free source is exactly the square-suffix indicator plus one. No probabilistic extrapolation, external proof checker, or unverifiable search cutoff is used. The source paper's terminal count is independently reproduced, not assumed.

Scientific limitations: no classification beyond the specified 84-letter family; no full historical-priority guarantee; independent mathematical audit has not been performed.
