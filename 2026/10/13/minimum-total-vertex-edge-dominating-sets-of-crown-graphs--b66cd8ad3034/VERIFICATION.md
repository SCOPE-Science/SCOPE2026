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

The checker constructs
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
for
\[
3\le n\le8.
\]

For each vertex subset \(D\), it tests the total condition by checking that every selected vertex has a selected neighbor. It tests vertex-edge domination using the exact equivalence
\[
D\text{ is vertex-edge dominating}
\quad\Longleftrightarrow\quad
N[D]\text{ is a vertex cover}.
\]

It computes every minimum set and compares the complete family with
\[
\{a_i,a_j,b_k\}
\quad\text{and}\quad
\{a_k,b_i,b_j\},
\]
where \(i,j,k\) are pairwise distinct.

Recorded output:

```text
VERIFY_OK
n=3: gamma_tve=3, minimum_sets=6
n=4: gamma_tve=3, minimum_sets=24
n=5: gamma_tve=3, minimum_sets=60
n=6: gamma_tve=3, minimum_sets=120
n=7: gamma_tve=3, minimum_sets=210
n=8: gamma_tve=3, minimum_sets=336
subsets_checked = 87360
all minimum sets matched the pairwise-distinct-index classification
```

The checker exhausts \(87{,}360\) vertex subsets. The finite computation is corroborative only; the arbitrary-order theorem follows from the closed-neighborhood vertex-cover proof.
