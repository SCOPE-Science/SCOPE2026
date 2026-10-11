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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies the stationary second-moment algebra
\[
2\operatorname{Cov}(p,\Delta p)+\operatorname{Var}(\Delta p)=0,
\]
the outgoing covariance
\[
\operatorname{Cov}(P,\Delta p)=\frac12\operatorname{Var}(\Delta p),
\]
and midpoint orthogonality.

It checks the determinant form of
\[
\operatorname{Var}(p)\ge\frac14\operatorname{Var}(\Delta p)
\]
and verifies the equality reflection
\[
P-m=-(p-m).
\]

It verifies the explicit equality two-cycle at \(K=2\pi\) using exact coefficients in units of \(\pi\).

It also checks the trigonometric branch calculation used in the analytic proof: the simultaneous relations
\[
\cos(\theta+m)=0,
\qquad
\cos(\theta+3m)=0
\]
force \(2m\) to be an integer multiple of \(\pi\); the odd branch is incompatible with nonzero kick variance.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure quantifier and the final ergodic period-two classification are analytic arguments in `RESULT.md`, not conclusions from finite orbit sampling.
