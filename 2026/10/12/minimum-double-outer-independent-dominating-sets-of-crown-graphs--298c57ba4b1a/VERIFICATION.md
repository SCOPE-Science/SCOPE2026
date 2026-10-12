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
For every vertex subset \(D\), it checks that the complement is independent and that
\[
|N[v]\cap D|\ge2
\]
for every vertex \(v\). The minimum cardinality and complete minimum-set family are compared with the theorem.

Recorded output:

```text
VERIFY_OK
n=3: gamma_doi=4, minimum_sets=3
n=4: gamma_doi=6, minimum_sets=16
n=5: gamma_doi=7, minimum_sets=20
n=6: gamma_doi=8, minimum_sets=30
n=7: gamma_doi=9, minimum_sets=42
n=8: gamma_doi=10, minimum_sets=56
subsets_checked = 87360
all minimum sets matched the piecewise classification
```

The checker exhausts \(87{,}360\) subsets. The finite computation is corroborative; the arbitrary-order theorem follows from the independent-complement proof.
