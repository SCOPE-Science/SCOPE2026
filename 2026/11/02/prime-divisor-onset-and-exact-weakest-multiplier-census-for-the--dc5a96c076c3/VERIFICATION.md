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

# Verification

The proof uses exact symbolic coding of the twisted baker map from Saiki–Takahasi–Yorke; that coding is not inferred from finite enumeration. The Jacobian-cycle claim and the weakest-modulus histogram are reconstructed in `RESULT.md` for all \(M\geq2\) and \(n\geq1\), and the derivation distinguishes eigenvalues from singular values.

Run the standalone, standard-library checker with `python3 check_weakest_spectrum.py`. It computes actual signed monomial products for every non-all-left binary word for \(2\leq M\leq9\), \(1\leq n\leq9\), then checks cycle lengths, signs, weights, histogram equality by right-visit count, global minima, exact extremizer numbers and primitive witnesses. It prints `CHECK_OK 8104 signed-monomial words checked` on success.

The finite test range does not prove the all-dimension statement. The analytic stars-and-bars, smallest-divisor and generating-function arguments supply that proof. No independent external validation or formal certification is claimed.
