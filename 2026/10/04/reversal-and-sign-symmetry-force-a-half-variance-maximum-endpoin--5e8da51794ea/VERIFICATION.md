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

The theorem is analytic. The accompanying checker uses exact rational arithmetic.

It constructs dependent, nonexchangeable increment laws by taking mixtures of deterministic increment vectors and closing each support only under reversal and global sign change. For several odd polynomial transforms it verifies
\[
\mathbb E[M g(S)]
=
\frac12\mathbb E[Sg(S)],
\]
the drawdown companion, and zero covariance of the range with \(g(S)\).

It separately enumerates iid symmetric two-point and three-point walks and verifies
\[
\operatorname{Cov}(M,S)
=
\frac12\operatorname{Var}(S)
\]
exactly.

A dynamic program for the simple symmetric walk computes the exact finite-\(n\) correlation for increasing \(n\) and checks approach toward the Brownian-limit constant.

Finite replay is supplementary. The universal result is the reversal/sign proof in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK orbit_identity_checks=36 nonexchangeable_checks=3 iid_cov_checks=38 asymptotic_checks=12`.
