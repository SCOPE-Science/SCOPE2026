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

# Reproduction and scope

The complete finite claim concerns exactly two sixteen-vertex graphs and two neighborhood conventions. `verify_coverage.py` computes all legal completed sequence polynomials using covered-neighborhood subsets; `verify_selected_sets.cpp` independently computes the same counts using selected-vertex subsets. `check_certificate.py` checks every recurrence row in `coverage_certificate.json`, all graph parameters, exact four-clique counts, terminal polynomials and longest-sequence witnesses. For reproducibility, use Python 3 and a C++17 compiler; the recorded full outputs are in `coverage_output.txt`, `selected_output.txt`, and `certificate_output.txt`.

State-space sizes for covered neighborhoods are \(198,654,398,654\); nonzero selected-state counts in the independent enumeration are \(11169,10137,17129,10137\). Both programs agree on all four full distributions, including their vanishing coefficients beyond maximal length. This finite computation does not prove analogous results for other strongly regular graphs. Literature novelty remains susceptible to unindexed material. There has been no independent external audit.
