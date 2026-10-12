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
The checker enumerates coordinate fixed-point tuples for dimension vectors with
\[
1\le d_i\le4
\]
and lengths up to five arrows, subject to a finite enumeration cap.

A coordinate arrow from \(V_{i-1}\) to \(V_i\) is represented by a pair
\[
(s_i,t_i),
\]
where \(s_i\) is its source basis index and \(t_i\) its target basis index. Consecutive coordinate matrix units compose to zero exactly when
\[
s_{i+1}\ne t_i.
\]

The checker counts all tuples satisfying these inequalities and compares the answer with
\[
d_0d_n\prod_{i=1}^{n-1}d_i(d_i-1).
\]

It separately verifies the ambient-product Euler characteristic and the vanishing formula whenever an intermediate dimension is one.

These finite checks are regression evidence only. The all-parameter theorem is the symbolic torus-fixed-point argument in `RESULT.md`.
