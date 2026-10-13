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

The standalone `verify.py` runs with ordinary Python 3 and standard-library modules only. Run `python verify.py`. Successful replay prints `VERIFY_OK_PARABOLIC_SQUARE_ZERO` followed by the number of exhaustive cases and five rank distributions.

The checker directly enumerates entries in all three rectangular blocks for each tested \((a,b,c,q)\), computes \(AB=0\) with independent finite-field arithmetic, constructs the full matrix, and performs Gaussian elimination to obtain rank. It compares the resulting rank histogram with an independently implemented triple-sum formula. The tested fields are \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) (represented as \(\mathbb F_2[t]/(t^2+t+1)\)), and \(\mathbb F_5\). The test suite includes forty-one parameter tuples with \(a,b,c\) from one to three and at most forty thousand candidate matrices each. It also checks the one-sum total count and that ranks form the predicted complete interval.

In particular, the complete distributions for \((a,b,c)=(2,2,2)\) are \(1+81T+630T^2+216T^3\) over \(\mathbb F_2\) and \(1+608T+19344T^2+13824T^3\) over \(\mathbb F_3\). These cases have respectively \(928\) and \(33777\) valid square-zero matrices.

These finite tests do not prove the formula for arbitrary field size and block dimensions. The proof is the dimension argument and matching construction stated in `RESULT.md`. No external independent audit has been performed.
