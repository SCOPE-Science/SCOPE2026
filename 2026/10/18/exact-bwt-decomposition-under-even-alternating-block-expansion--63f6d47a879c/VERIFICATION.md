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
# Computational verification

Execute `python3 verify.py` with Python 3 and the standard library. The program checks the explicit alternating-expansion BWT block formula by brute-force cyclic-rotation sorting for all mixed binary parents of lengths 2 to 9 and expansion factors 2, 3 and 4 (3012 combinations). It also checks 180 seeded larger cases, for parent lengths up to 305, against a separately implemented cyclic suffix-doubling algorithm and validates the factor-1 counterexample.

The expected output is `VERIFY_OK exhaustive_two_symbol_inputs_n_2_to_9_cases=3012 independent_suffix_doubling_cases=180 h1_sharp_counterexample=001`. No additional files or dependencies are required. Tests are finite and cannot replace the general proof. The theorem is not asserted for the endmarked BWT, unary parent words or h=1.
