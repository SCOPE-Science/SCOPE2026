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
# Verification details

The exact algebraic calculation is in `RESULT.md`: the \(\{0,1,3\}\) fiber determinant reduces to a polynomial on the full cosine square. Its explicit first partial derivative and the substituted second partial derivative reduce the global maximum to exactly two nonzero algebraic critical values, together with boundary values. The equality orbit and Riesz normalization are proved there.

Run `python checker.py` with NumPy and SymPy installed. The script checks exact critical identities, 2000 seeded direct determinants and Gram eigenvalue products, five perturbations around the candidate optimum, and the matrix Parseval identity. Recorded results are in `checker_output.txt`. The sample tests neither replace the all-angle proof nor establish publication priority. Independent mathematical verification has not been performed.
