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

The counterexample sequence is
\[
z_k=\frac1{\log(k+2)}.
\]
The mean-value theorem gives increments of order
\[
\frac1{k(\log k)^2},
\]
so their squares are summable and satisfy the required best-increment \(o(1/k)\) bound, while
\[
kz_k\to\infty.
\]

`artifacts/verify_rate_gap.py` checks representative inequalities and a rigorous integral tail bound. The computation supports, but does not replace, the analytic proof.
