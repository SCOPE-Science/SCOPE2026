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
The main theorem is analytic.

For two cumulative outputs \(C_1,C_2\) with the same fixed-window incidence,
\[
C_1(t)-C_1(t-h)=C_2(t)-C_2(t-h),
\]
their difference \(D=C_1-C_2\) satisfies
\[
D(t+h)=D(t).
\]
Because
\[
C(t)=C(0)+S(0)-S(t)
\]
and \(S(t)\) is nonincreasing and nonnegative, each \(C(t)\) converges. Therefore \(D\) is both periodic and convergent and must be constant.

The bundled checker verifies that the cumulative-incidence ambiguity reported in the source,
\[
T(\alpha,\beta,\gamma)
=
\left(\frac{\alpha\gamma}{\beta},\gamma,\beta\right),
\]
is an involution and preserves
\[
\alpha\gamma,\qquad \beta\gamma,\qquad \beta+\gamma.
\]

The checker does not prove the infinite-time periodicity argument; that proof is given explicitly above.
