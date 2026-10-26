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
# Verification notes

The complete proof is in `RESULT.md`. To reproduce the **finite auxiliary** checks, run `python checker.py` with Python 3.10 or later. The checker uses only `fractions.Fraction` and `math`, evaluates Gegenbauer polynomials by their rational three-term recurrence at exact rational cube inner products, and transforms every degree into each Walsh-size eigenspace. It asserts the exact predicted positive/zero pattern for dimensions \(3\) through \(12\) and degrees \(0\) through \(d+12\), a total of 1825 rational eigenvalues. It also checks the coefficient identities from the three-coordinate null-hyperplane perturbations at odd indices \(1,3,5,7,9,11\).

On this package, the execution passed all assertions and produced `checker_output.txt`. Its finite tests cannot establish any assertion in infinitely many dimensions or unbounded degrees; the formal all-degree claim rests on the symbolic null-hyperplane proof, not numerical extrapolation. There is no claim of independent mathematical validation, publication priority certification, or optimal condition numbers.
