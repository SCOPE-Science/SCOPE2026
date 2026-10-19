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

# Verification evidence

The proof in `RESULT.md` supplies a characteristic-free (within characteristic two) coordinate reduction and exact factor-composition identities. The key equations are verified by direct multiplication of \(2\times2\) matrices, and nondegeneracy of the alternating form on \(K^2\) proves the surjectivity required for all normal-form cases.

The standalone program `verify.py` uses only Python's standard library. Run it as `python verify.py`. It directly implements genuine binary finite fields using the irreducible polynomials \(x+1\), \(x^2+x+1\), and \(x^3+x+1\); constructs the original endomorphism matrices; enumerates all generators and all ordered products of two generators; constructs each announced normal-form stratum independently; checks set equality and exact cardinalities; checks closure against further generators over \(\mathbb F_2\) and \(\mathbb F_4\); and directly computes \(AX+XA\) on the original \(2\times2\) matrix arguments. The latter direct check uses every matrix input for the two smaller fields and a deterministic sample over \(\mathbb F_8\).

The expected and reproduced counts, as `(field order, generators, two-factor products, total semigroup)`, are `(2,8,30,33)`, `(4,64,892,907)`, and `(8,512,29688,29751)`. Execution terminates with `VERIFY_OK`. The checks cover all two-factor products over the three indicated finite fields, but they are not an exhaustive test over every field or matrix dimension. The normal-form and factor-length theorem is established by the written proof, not by extrapolation.

No independent scientific audit or external formal certification has been performed.
