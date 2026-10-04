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

The symbolic proof reduces certified domination to the exact outside-neighbor count \(q-c_i\) for each selected part and then performs inclusion-exclusion over half-shadowed-part events.

The included checker does not use the theorem to decide whether a tested set is certified. It constructs the graph from part labels, tests domination directly, counts outside neighbors of every selected vertex, and compares the resulting accepted sets with the profile criterion and the closed polynomial.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
all-set profile criterion matched
all polynomial coefficients matched
K_{3,n} specialization matched the 2025 theorem for n = 3..10
```

The checker also compares the specialization to \(K_{3,n}\) with the published 2025 piecewise coefficient formula for \(3\le n\le10\). The finite checks are corroborative only; the all-orders result is established by the proof.
