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

The verifier checks both the graph model and the polynomial formulas.

For \(q=3\), \(q=4\), and \(q=5\), it constructs the actual unit dot-product graph from field arithmetic. The \(q=4\) implementation uses
\[
\mathbb F_2[t]/(t^2+t+1).
\]
It then enumerates every vertex subset, tests domination directly, and tests whether the induced subgraph has a perfect matching by recursive matching search. The resulting paired-domination coefficient vectors are compared with the closed formula.

The component profiles found directly are
\[
K_{2,2},\qquad K_3\sqcup K_{3,3},\qquad 2K_4\sqcup K_{4,4}
\]
for \(q=3,4,5\), respectively. The \(q=5\) graph has \(16\) vertices, so the largest global search checks all \(2^{16}\) subsets.

For \(q\in\{7,8,9,11,13,16\}\), the verifier also checks the minimum exponent, the exact total count
\[
(2^{m-1}-1)^{f(q)}\left(\binom{2m}{m}-1\right)^{(m-f(q))/2},
\]
and the recovery of \(q\) from the degree and leading coefficient of the polynomial.

Exact output:

```text
VERIFY_OK
brute_actual_fields=q3,q4,q5
largest_global_subset_enumeration=2^16
component_profiles=q3:K2,2;q4:K3+K3,3;q5:2K4+K4,4
formula_and_reconstruction_checks=q7,q8,q9,q11,q13,q16
```

These computations are corroborative. The general proof is the slope-involution decomposition together with exact paired-domination counts for \(K_m\) and \(K_{m,m}\).
