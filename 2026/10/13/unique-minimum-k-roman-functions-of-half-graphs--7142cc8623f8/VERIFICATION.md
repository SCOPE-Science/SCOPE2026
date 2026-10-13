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

The checker constructs the half graph
\[
H_n
\]
directly from
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

For every tested labeling it applies the defining \([k]\)-Roman condition directly: if \(f(v)<k\), it computes the active neighbors of \(v\), the closed-neighborhood label sum, and checks
\[
f(N[v])\ge k+|AN(v)|.
\]

It exhausts all labelings of total weight at most
\[
2(k+1)
\]
for
\[
2\le k\le5,\qquad 3\le n\le5.
\]

Recorded output:

```text
VERIFY_OK
k=2, n=3: gamma_[kR]=6, minimum_functions=1
k=2, n=4: gamma_[kR]=6, minimum_functions=1
k=2, n=5: gamma_[kR]=6, minimum_functions=1
k=3, n=3: gamma_[kR]=8, minimum_functions=1
k=3, n=4: gamma_[kR]=8, minimum_functions=1
k=3, n=5: gamma_[kR]=8, minimum_functions=1
k=4, n=3: gamma_[kR]=10, minimum_functions=1
k=4, n=4: gamma_[kR]=10, minimum_functions=1
k=4, n=5: gamma_[kR]=10, minimum_functions=1
k=5, n=3: gamma_[kR]=12, minimum_functions=1
k=5, n=4: gamma_[kR]=12, minimum_functions=1
k=5, n=5: gamma_[kR]=12, minimum_functions=1
bounded_labelings_checked = 1035068
all minima matched the unique endpoint labeling
```

Thus the computation is exhaustive for every labeling relevant to the minimum and minimum-function claims in the tested parameter range. It is finite corroboration only; the arbitrary-\(k\), arbitrary-\(n\) theorem is established by the symbolic proof in `RESULT.md`.
