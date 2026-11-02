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
# Verification of exact finite non-contingency laws

Run `python3 checker.py` using the ordinary Python 3 standard library. The program exhaustively enumerates uniform colour assignments for selected small combinations of the number of Boolean colours, block size, and number of blocks. For each assignment, it computes every colour support and the non-contingency images of each propositional-colour singleton. It checks that the resulting pointed truth-value signatures have the claimed number of Boolean atoms, and it exhaustively applies the non-contingency operator to **every union** of those signature cells to verify closure. Independently, it constructs the exact rational distribution from the independent support-category probabilities using a dynamic program and compares all atom-count probabilities and first moments.

The executed program returned `ALL_CHECKS_OK exhaustive_assignments= 9502`. No numerical approximation or random seeds are needed. The asymptotic assertions are mathematically justified in RESULT.md by exact multinomial factorial moments, exponential-scale separation and sequential compactness; a finite exhaustive run cannot certify statements for all increasing sizes. The theorem makes no claim about unspecified nonuniform or dependent colour laws. Independent audit: not performed.
