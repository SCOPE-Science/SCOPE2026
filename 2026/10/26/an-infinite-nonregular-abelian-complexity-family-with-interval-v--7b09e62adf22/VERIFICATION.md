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

Run `python3 verify_cyclic_abelian.py` with Python 3.9 or later; no third-party packages are required. The checker constructs each substituted word directly, independently counts its letters and all sliding factor counts on the nine ordered adjacent block pairs, then compares with the exact recurrence. It checks the adjacent-pair completeness prerequisite in finite substitution iterates and uses only integer equality assertions. The complete expected terminal output is stored in `verify_cyclic_abelian_output.txt`, and the final PASS line attests to 30 comparisons across six values of the parameter and five lengths each.

The proof of the infinite result is the explicit weighted-factor induction, spectral inversion, irrational rotation, and C-finite/Fourier contradiction in `RESULT.md`. Empirical checks cannot by themselves imply any assertion for infinitely many exponents or factor lengths. Neither the computations nor this note constitute independent scientific validation.
