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

# Verification and reproducibility

The mathematical result is proved in `RESULT.md`; the executable test uses only the Python standard library. Run `python3 checker.py`, which should report `PASS 6089 exact-rational parameter sets and 16 absorbing levels; integer scaling, geometric law, and nonmonotone example verified`. `check_output.txt` contains the output observed in the recorded run.

The checker evaluates transition probabilities with `fractions.Fraction`; it compares the Markov formulas to direct rounded affine steps, verifies the full trap classification across a finite integer window, tests exact seven-step probabilities and detailed balance, and enumerates the integer-resonance examples. The range tests are finite and cannot independently certify every integer, every stepsize, or an infinite-time limit; those follow from the displayed proof. Other rounding modes or intermediate-precision implementations are outside its scope.
