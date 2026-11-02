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

# Reproducible exact checks

Run `python3 verify_chord_order.py`. The program requires only the Python standard library (`fractions`, `math`, `collections`), with no input data or external files. It prints `PASS: 119211 independent exact assertions` on successful completion. The tests enumerate all pairings of the remaining endpoints for \(3\le n\le8\), independently count crossing degrees for each admissible \(a\), and compare to the counting formula. They then verify normalization, conditional moments, likelihood-ratio quotients, their exact signs, strict upper-tail comparisons and the sharp opposite-parity counterexample over explicitly bounded ranges. Arithmetic is exact (integer and `Fraction`), not floating point.

The proof for all \(n\ge3\) is the combinatorial counting argument and elementary strict monotonicity of the mass quotient in `RESULT.md`. Finite tests are consistency checks rather than a proof for infinitely many cases. No independent external audit has been performed.
