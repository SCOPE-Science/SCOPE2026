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

# Exact check reproducibility

Run `python3 verify.py` from the directory containing the bundled files. The program requires only the Python standard library. Expected output starts with `VERIFY_OK` and reports completed exact integer and rational checks.

The program independently calculates central trinomial numbers via a three-term recurrence and exact binomial sums through index 260, then compares their residues to independent base-five digit products. It exhaustively counts every ordered residue pair over \(0\le n<5^L\) for \(0\le L\le7\) and matches the sixteen closed formulas; it also checks both carry parity maps and computes total variation with exact `Fraction` arithmetic.

The infinite theorem is justified by the digit-factorization argument, multiplicative character orthogonality, and the exhaustive symbolic partition into trailing-four suffixes, all supplied in RESULT.md. Numerical checks have no authority beyond their finite ranges. A publicly available exact theorem for the same two-point distribution could negate novelty; independent priority and mathematical audit have not been performed.
