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

The proof is analytic. The accompanying checker exhaustively enumerates every mapping
\[
[n]\to[n]
\]
for
\[
1\le n\le7.
\]

It computes indegrees directly and identifies cyclic vertices independently by orbit tracing.

For every \(2\le n\le7\), it verifies the exact mean of the zero-indegree count, the full point-mass Palm identity
\[
\frac{\mathbb E[Z_n\mathbf 1_{\{L_n=t\}}]}{\mathbb E Z_n}
=
\Pr(L_{n-1}=t),
\]
the exact cyclic-point distribution and tails, every threshold covariance, and the exact covariance with \(L_n\).

The finite replay is supplementary. The universal proof is the conditional deletion argument plus the rooted-forest enumeration in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK mappings_checked=873612 distribution_checks=28 tail_checks=28 mean_z_checks=6 palm_checks=27 threshold_covariance_checks=21 covariance_checks=6`.
