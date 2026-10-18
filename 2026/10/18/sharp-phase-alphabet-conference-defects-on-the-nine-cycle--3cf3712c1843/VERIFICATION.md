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

# Reproducibility and limits

Run `python3 verify_phase_energy.py` in a standard Python 3 environment; no third-party libraries or data files are required. The executable includes all four cyclotomic polynomial reductions, exact zero-mean tests for each of the \(q^7\) normalized exponent tuples, exact integer / quadratic-field norm calculations, and exact pair comparisons. It prints the qualifying-sequence and optimizer counts and fails with an assertion if any prescribed result differs.

Completed checks: the qualifying normalized counts are respectively 35, 1225, 9135, and 23765 for alphabets of sizes 2, 4, 6, and 8; the four minimum-energy pairs are respectively (16,0), (16,0), (4,0), and (24,-16); optimizer counts are 12, 84, 6, and 6. For eight phases, the program additionally certifies all six listed normalized exponent patterns and the strict next minimum pair (40,-24). An independent floating-point direct DFT and autocorrelation calculation on one optimizer checks the normalization; it is not used in any exhaustive comparison.

The finite exhaustive loops are the proof of numerical optimality and completeness *only for the explicitly stated finite alphabets*. The cyclotomic-ring and Parseval identities, plus a global-phase normalization argument, justify the translation of the finite calculation into the theorem. Independent audit of the theorem, code, and historical priority has not been performed. The exact minima do not imply analogous statements for unrestricted phases, nonzero means, or other cyclic lengths.
