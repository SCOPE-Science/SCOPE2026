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
The universal theorem is analytic; the embedded script is an exact finite replay of its lattice inequalities.

For integer supports with
\[
1\le L<U\le7
\]
and rational probability denominators through \(8\), the verifier enumerates every distribution and computes its exact mean. At each of
\[
z\in\left\{\frac12,\frac23,\frac32,2\right\},
\]
it verifies
\[
\mathbb E_{q_{\min}}[z^A]
\le
\mathbb E_q[z^A]
\le
\mathbb E_{q_{\max}}[z^A].
\]
Because \(z^x\) is strictly convex for \(z\ne1\), these are the expectation inequalities used in the proof.

The replay performs \(76{,}416\) exact expectation comparisons and \(19{,}104\) strictness checks.

For the worked case
\[
R_0=2,
\qquad
L=1,
\qquad
U=4,
\qquad
\mu=\frac52,
\]
it certifies by exact rational polynomial signs that the adjacent-age root obeys
\[
1.3247<\lambda_{\min}<1.3248
\]
and the endpoint root obeys
\[
1.3802<\lambda_{\max}<1.3803.
\]

Run:

`python3 verify_euler_lotka_lattice_bounds.py`

The first output line must be:

`VERIFY_OK`

The finite replay is not used as a substitute for the convex-order proof or for the universal equality conditions.
