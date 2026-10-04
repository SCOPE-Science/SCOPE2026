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

The proof is algebraic. `verify.py` is a dependency-free consistency checker for the nontrivial closed forms. It reconstructs the Lei--Bickel Theorem-2 residual directly from cyclic-shift difference columns using Gram--Schmidt projection, computes the DFT formula independently, and exhaustively compares both with the gcd/parity theorem for every two-one separation for each integer sample size from \(3\) through \(30\).

The checker additionally verifies the global optimizer formula, the power-of-two collapse criterion over the tested range, and the \(n=20\) statement that only separations \(4,8,12,16\) have positive proxy and that their common value is \(\sqrt{80/99}\).

Successful replay prints `VERIFY_OK`.

Limits: finite replay is not the proof for arbitrary \(n\). The all-\(n\) result rests on the circulant Fourier diagonalization, the affine-dependence argument for a missing non-DC frequency, the odd-order secant-square identity, and the divisor optimization given in `RESULT.md`. Independent audit has not been performed.
