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

The verifier constructs \(\operatorname{Cr}_n\) directly from
\[
a_i b_j\in E
\quad\Longleftrightarrow\quad
i\ne j.
\]

For every candidate set \(S\), it checks the super-domination definition directly: each omitted vertex \(u\) must have a selected vertex \(v\) with
\[
N(v)\cap(V\setminus S)=\{u\}.
\]
It independently checks connectivity of the induced selected subgraph.

Every nonempty subset is exhausted for \(3\le n\le7\), totaling \(21{,}819\) subsets. For every exhaustive case \(n\ge4\), the ordinary and connected-super minima agree exactly with the predicted family. The \(n=3\) boundary has fifteen minimum super dominating sets but only six connected minimum sets.

The checker also explicitly tests \(7{,}798\) theorem-predicted minimum constructions: every disjoint omitted-pair choice is checked through \(n=12\), and representative extremal index patterns are checked through \(n=50\).

Recorded output:

```text
VERIFY_OK
n=3: gamma_sp=4, min_sp=15, gamma_csp=4, min_csp=6
n=4: gamma_sp=4, min_sp=6, gamma_csp=4, min_csp=6
n=5: gamma_sp=6, min_sp=30, gamma_csp=6, min_csp=30
n=6: gamma_sp=8, min_sp=90, gamma_csp=8, min_csp=90
n=7: gamma_sp=10, min_sp=210, gamma_csp=10, min_csp=210
subsets_checked = 21819
explicit_minimum_constructions_checked = 7798
exhaustive_parameter_range = 3..7
construction_parameter_range = 4..50
all exhaustive minima for n>=4 matched the disjoint omitted-pair classification
```

Finite computation is corroborative only. The all-order lower bound, equality classification, connectedness, and counting formula follow from the symbolic proof in `RESULT.md`.
