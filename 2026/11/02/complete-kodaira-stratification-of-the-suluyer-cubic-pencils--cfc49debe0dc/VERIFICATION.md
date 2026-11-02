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

# Reproducibility notes

Run `python verify.py` in an environment with Python 3 and SymPy. Successful completion prints `VERIFY_OK exact discriminant, all exceptional valuations, nodal basepoint`.

The script reconstructs the binary quartic \(H=LG\) directly from the two defining cubics, forms the classical invariants \(I,J\), expands and checks \(4I^3-J^2\), checks the discriminant of \(Q_a\), and tests the seven collision classes in their exact algebraic quotient rings. The special ordinary nodal point at the nontransverse base parameter is checked using the gradient and local Hessian. The classification additionally uses the classical characteristic-zero Kodaira table, relative minimality and Shioda–Tate; those geometric theorems are established in the mathematical proof rather than replaced by code.

The calculation was executed from this standalone artifact with no external datasets. It requires SymPy, and it does not independently certify historical originality or constitute an independent mathematical review.
