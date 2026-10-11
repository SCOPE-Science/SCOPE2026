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

For
\[
k(n)=\lfloor\log_2n\rfloor,
\qquad
q_n
=
\frac{2^n}{n}
\left(
\frac{n}{2^{k(n)}}
\right)^\gamma,
\]
the bounded factor
\[
1\le
\left(
\frac{n}{2^{k(n)}}
\right)^\gamma
<2^\gamma
\]
proves
\[
q_n^{1/n}\to2
\]
and
\[
q_n/2^n\to0.
\]

Ordinary dyadic steps satisfy
\[
q_{n+1}/q_n
=
2(1+1/n)^{\gamma-1}\to2,
\]
while reset steps satisfy
\[
q_{n+1}/q_n
\to
2^{1-\gamma}.
\]

For the normalization coefficient
\[
\lambda_n
=
\kappa^{E_n},
\qquad
E_n
=
\sum_{j=1}^nq_j-q_{n+1},
\]
the exact increment is
\[
E_n-E_{n-1}
=
2q_n-q_{n+1}.
\]

If
\[
0<\gamma<1,
\]
these increments are eventually positive and grow at least like
\[
2^n/n^2,
\]
so the normalization series converges and the primary source's simple basin criterion gives
\[
\Omega_\gamma\simeq\mathbb C^2.
\]

If
\[
\gamma=1,
\]
the exponent takes one value
\[
C_k
\]
on exactly
\[
2^k
\]
consecutive indices, with
\[
C_{k+1}-C_k
=
2^{2^{k+1}-k-1}.
\]
Therefore
\[
\sum_n\lambda_n
=
\sum_k2^k\kappa^{C_k}<\infty.
\]
The tail-to-term ratio is at most exponential in
\[
k,
\]
whereas
\[
C_k
\]
is superexponential, so the capture exponent satisfies
\[
\alpha_n\to1.
\]
The stronger primary theorem gives the same biholomorphism conclusion at this endpoint.

If
\[
\gamma>1,
\]
then immediately before a reset,
\[
E_n/q_{n+1}
=
-2(\gamma-1)/n
+O(n^{-2}),
\]
so
\[
E_n\to-\infty
\]
and
\[
\lambda_n\to\infty
\]
along that subsequence. Hence the normalization series diverges.

Finally, the uniform estimate
\[
\sup_{n\gg1}
\frac{\sum_{j<n}q_j}{q_n}
<\infty
\]
verifies the primary source's product condition for every fixed
\[
\gamma>0.
\]
Thus every basin in the family is parabolic.

No numerical experiment is used in these checks.
