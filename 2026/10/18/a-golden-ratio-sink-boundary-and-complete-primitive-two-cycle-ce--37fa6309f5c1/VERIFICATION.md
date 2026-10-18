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

With Python 3 and SymPy available, execute `python checker.py` from the directory containing the program and `RESULT.md`. The executed program returned `PASS: 164 exact algebraic/radical identities; ten rational phase representatives.` Its identities verify the derivation of the scalar cycle equations, point lifts, return Jacobian determinant and the symmetry-matrix characteristic cubic. The parameter representatives cover orbit-count thresholds, two interior sink values, the saddle regime, and the repeller regime. This is not an exhaustive real-parameter check. The proof of exhaustive cycle classification and the all-real spectral boundary is in `RESULT.md`.

No numerical solver approximations, finite grids or asymptotic sampling are used to justify nonexistence or the exact threshold. Independent validation of this research has not been performed. Historical priority remains subject to further literature comparison.
