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

# Exact finite-range verification

The reproducible files are `verify.py` (standard-library Python 3) and `coefficients.csv` (every rational coefficient of each of \(252\) canonical parameter classes). Run `python3 verify.py` alongside the CSV. The program independently regenerates and overwrites the CSV from the defining formula, verifies strict positivity in all \(203\) classes of ambient dimension at most \(13\), and checks the exact five exceptions among the \(49\) classes of ambient dimension \(14\). It additionally cross-checks \(503\) integer lattice point counts with an independent coordinate dynamic program, verifies the published \(-687323/79200\) quadratic coefficient, and prints `EXACT_OK`.

The certificate's SHA-256 before packaging was `deee2e21b08b82d9aa37f55163e45f75c68b2800075e85b894f0c89e309a1108` and its byte length was `37909`. These describe the regenerated text. Every rational coefficient is printed in unreduced or reduced exact `Fraction` form by the verifier as appropriate; the file stores reduced exact fractions. There is no use of machine floating-point in the classification.

The mathematical proof that these finitely many values determine the claimed Ehrhart polynomials is the membership/counting lemma and the degree bound proved in `RESULT.md`. Finite numerical confirmations beyond the exact exhaustion are not extrapolated to untested dimensions or mathematical families. The human historical-priority question remains open pending independent assessment.
