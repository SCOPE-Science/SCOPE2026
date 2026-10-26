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

Run `python3 verify.py` with Python 3. The script uses only standard-library `fractions` and `math`, and it asserts the exact determinant-to-Jacobi leading-constant identity for all permitted angular orders and indices at degrees \(0\leq L\leq8\). It additionally checks the exterior-power product identity, exponent sums, triangular multiplicities, and sharp extremal constants. Execution produced `PASS: 291 exact rational assertions`.

Direct high-precision evaluations of the generalized moment eigenproblem for \(1\leq L\leq4\), all angular orders, and \(\delta=10^{-4}\) agreed with the leading constants to first relative order. Those separate numerical calculations are not claimed as a standalone certificate. The proof of the infinite family depends on the explicitly stated exterior-power asymptotics and classical Jacobi formulas, not on finite examples.

No independent audit, external validation or machine-formal certification has been performed.
