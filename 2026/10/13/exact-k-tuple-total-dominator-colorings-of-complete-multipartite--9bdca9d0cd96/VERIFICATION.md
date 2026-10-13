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

The theorem is analytic. The executable checker performs finite, independent stress tests.

It first enumerates every color-count vector for complete multipartite profiles with two through four parts and each part size at most five. For every tested \(k\), it compares the direct minimum of \(\sum_i c_i\) subject to \(\sum_j c_j-c_i\ge k\) against the stated \(k+\tau\) formula, including infeasible cases.

It then enumerates labeled vertex colorings for every ordered complete multipartite profile of total order at most six. For each feasible \(k\), it checks that no coloring with one fewer color exists and that the exact number of optimal labeled colorings agrees with
\[
(k+\tau)!\sum_{\substack{1\le c_i\le\min\{n_i,\tau\}\\\sum_i c_i=k+\tau}}\prod_i {n_i\brace c_i}.
\]
Finally it checks the complete-bipartite specialization \(\chi_{k,d}^t(K_{m,n})=2k\) for every \(1\le m\le n\le50\) and every \(1\le k\le m\).

The finite computations do not establish the infinite theorem; correctness for arbitrary part sizes and arbitrary feasible \(k\) rests on the proof in `RESULT.md`.

Replay output from the packaged checker:

```text
ALL CHECKS PASSED; vector_cases=9550; assignment_cases=124; assignment_checks=847396; labeled_count_checks=124; bipartite_cases=22100; small_total_order<=6; vector_part_sizes<=5; bipartite_range=1<=m<=n<=50
```
