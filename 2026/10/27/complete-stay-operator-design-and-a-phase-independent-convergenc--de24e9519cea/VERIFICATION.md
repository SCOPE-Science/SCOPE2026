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

# Reproducibility

Run `python verify.py` with NumPy and SymPy available. In the checked rational example the program independently constructs \(L,R,C,B\), establishes \(L^*L+R^*R+B^*B=I\) exactly, verifies \(\eta=209/224\), propagates the complementary population for small integer times using exact symbolic matrices, and checks 12 non-real phase choices and phase-independent rates numerically. The actual run printed `PASS: exact Kraus identities, unique-ray population rate, and 12 complex phase completions; eta=209/224`.

The proof of the universal assertion is the finite-dimensional algebra in `RESULT.md`; finitely many script checks neither establish the all-parameter theorem nor establish originality. The recurrence inference invokes the published unique-invariant-state criterion in Loebens, Theorem 3.8. Independent audit has not been performed.
