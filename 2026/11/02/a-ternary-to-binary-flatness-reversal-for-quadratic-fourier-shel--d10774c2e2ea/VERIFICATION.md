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

# Exact certificate and scope

Run `python3 checker.py` on Python 3.9 or newer. The checker has no third-party dependencies and computes only exact integers and Eisenstein-integer pairs. No approximating trigonometric values, numerical tolerances, or random choices enter the exhaustive result.

The complete six-variable ternary search fixes the five edge phases incident with the first vertex by the proved vertex-gauge symmetry and traverses the remaining ten exponents, each in \(\{0,1,2\}\). It checks all \(59049\) configurations and the full nineteen-value histogram of aggregate four-vertex matching defects, whose least value is \(27\) with \(360\) normalized minimizers. Using \(B_6=255\), this certifies the sharp fourth moment \(363\). The checker also reconstructs a minimizing coefficient array and evaluates its moment by two different exact formulas: character-product matching sums and row correlations of its symmetric coefficient matrix. As further cross-checks it verifies the same identity for every normalized binary configuration in dimensions four through six, and checks the displayed six-by-six real conference matrix directly.

The proof of the universal lower bounds, the five-variable optimal constructions, and the impossibility of a six-variable conference matrix over odd phase alphabets is analytical and appears in `RESULT.md`. Finite enumeration by itself does not prove any additional claim outside the enumerated discrete domain. Independent validation has not been performed.
