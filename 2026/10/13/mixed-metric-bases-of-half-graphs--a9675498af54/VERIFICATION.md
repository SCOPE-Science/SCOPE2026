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

The verifier constructs the half graph \(H_n\) directly for every \(2\le n\le8\). It computes all-pairs vertex distances with breadth-first search and forms each edge distance by taking the minimum distance to its two endpoints.

For each \(n\), every pair of distinct elements of \(V(H_n)\cup E(H_n)\) is converted into the bit mask of landmarks that distinguish that pair. The checker then exhausts every vertex subset of size at most \(n\). It verifies that no subset of size less than \(n\) intersects every separator mask, and that the size-\(n\) solutions are exactly \(\{a_n,b_1\}\) together with one choice from every internal diagonal pair.

Recorded output:

```text
n=2: order=4, edges=3, elements=7, subsets_size_le_n=11, bases=1
n=3: order=6, edges=6, elements=12, subsets_size_le_n=42, bases=2
n=4: order=8, edges=10, elements=18, subsets_size_le_n=163, bases=4
n=5: order=10, edges=15, elements=25, subsets_size_le_n=638, bases=8
n=6: order=12, edges=21, elements=33, subsets_size_le_n=2510, bases=16
n=7: order=14, edges=28, elements=42, subsets_size_le_n=9908, bases=32
n=8: order=16, edges=36, elements=52, subsets_size_le_n=39203, bases=64
VERIFY_OK
n_range = 2..8
subsets_checked_size_at_most_n = 52475
minimum_bases_checked = 127
all smaller subsets failed mixed resolution
all size-n mixed bases matched the forced-endpoint diagonal-transversal classification
```

The finite computation is corroborative only. The theorem for arbitrary \(n\) follows from the forced endpoint landmarks, the prefix and suffix class-count inequalities, and the explicit sufficiency argument in the proof.
