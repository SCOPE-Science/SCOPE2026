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
The bundled checker enumerates every weak composition of \(d\) into \(n+1\) parts for
\[
1\le n\le5,\qquad 1\le d\le10,\qquad 0\le k<d.
\]

For each triple it verifies:
- direct fixed-monomial membership by the condition
  \[
  \max_i a_i\ge d-k;
  \]
- the exact inclusion-exclusion count
  \[
  \sum_j(-1)^{j+1}\binom{n+1}{j}\binom{n+d-j(d-k)}{n};
  \]
- the stable simplification
  \[
  (n+1)\binom{n+k}{n}
  \]
  whenever
  \[
  d>2k;
  \]
- pairwise separation of all degree-\(d\) monomial weights for base-\((d+1)\) variable weights.

Finite checks are regression evidence only. The all-parameter proof is the unique-factorization and Euler-localization argument in `RESULT.md`.
