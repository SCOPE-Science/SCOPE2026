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

# Verification and reproducibility

Run `python3 checker.py` from the extracted standalone files. The script uses only Python's standard library. Successful execution prints `VERIFY_OK`.

The checker enumerates every ordered pair of six-coordinate matrices over \(\mathbf F_2\) and \(\mathbf F_3\), calculates both the additive commutator and the asserted group target, and checks all \(q^3\) target counts against the three formulas. The group calculation is additionally compared against direct \(4\times4\) matrix multiplication and geometric-series inversion for every binary pair and a deterministic sample of ternary pairs. The six-variable determinant counting lemma and its exceptional cases are independently checked over \(\mathbf F_4\) using arithmetic modulo \(t^2+t+1\). The exact total-mass and commuting-probability identities are checked at several integer field sizes.

The finite checks do not prove the theorem for every field. The universal proof is the algebraic fiber count: rank-one versus rank-zero dichotomy for the last coordinate, the two determinant maps sharing one coordinate pair, and the exact group-commutator shift. The paper explicitly distinguishes the previously determined zero-target count from its full nonidentity-fiber distribution. No independent mathematical audit or external certification is asserted.
