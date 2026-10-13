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

The checker constructs the half graph directly from
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

For each labeling, it forms the zero set \(B_0\). Every zero vertex is required to have a neighbor \(w\) satisfying
\[
f(w)\ge2
\]
and
\[
f(w)\ge1+\left\lceil\frac{|N(w)\cap B_0|}{2}\right\rceil.
\]

For every
\[
3\le n\le7,
\]
the checker exhausts all labelings of total weight at most the claimed optimum. It rejects every lower-weight labeling, confirms the endpoint optimum, confirms uniqueness for the odd orders, and confirms the explicit distinct optimum for each even order tested.

Recorded output:

```text
VERIFY_OK
n=3: gamma_StR=4, minimum_functions=1, unique
n=4: gamma_StR=6, minimum_functions=28, nonunique
n=5: gamma_StR=6, minimum_functions=1, unique
n=6: gamma_StR=8, minimum_functions=49, nonunique
n=7: gamma_StR=8, minimum_functions=1, unique
bounded_labelings_checked = 449345
odd minima matched the unique endpoint labeling; every tested even order had the explicit alternate optimum
```

The finite computation is exhaustive for all labelings relevant to the minimum claim in the tested range. It is corroborative only; the theorem for arbitrary \(n\) follows from the symbolic lower-bound and equality analysis in `RESULT.md`.
