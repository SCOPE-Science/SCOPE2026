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
The analytic verification uses the exact formulas of arXiv:2207.03713v1.

1. Substitute \(\gamma=0\) into equations (4.6a)–(4.6b). The radical is \(|\alpha\beta-4|\), yielding the unordered pair \(\{\sqrt2/\alpha,\beta/(2\sqrt2)\}\).
2. Apply Theorem 6.2 channel by channel and Theorem 6.3 for the union and multiplicities.
3. In the subcritical rectangle, apply Theorem 7.2 to compare \(N_-(1/2,H)\) with the sum of the two Jacobi counts.
4. Use \(N_+(\mu,J_0)\sim[4\sqrt2\sqrt{\mu-1}]^{-1}\), as invoked in Theorem 7.3, together with
\[
\frac{\sqrt2}{\alpha}-1=\frac{\sqrt2-\alpha}{\alpha},\qquad
\frac{\beta}{2\sqrt2}-1=\frac{\beta-2\sqrt2}{2\sqrt2}.
\]
This gives the two displayed coefficients. Because both coordinate distances tend to zero, their positive sum diverges and the bounded comparison error is \(o\) of the sum.

`verify.py` independently evaluates the original and factorized channel formulas on representative points on both sides of \(\alpha\beta=4\), checks the channel ordering swap, and checks the two conversion constants. These computations are checks of algebra only; they are not substitutes for the analytic proof.

Unproved limits: no statement is made for \(\gamma\ne0\), for opposite-sign \(\alpha,\beta\), or about sharpening the finite comparison error in Theorem 7.2.
