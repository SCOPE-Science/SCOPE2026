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

The symbolic proof uses two exact facts: the positive support is a vertex cover exactly when the zero set is independent, and every independent set of a complete multipartite graph lies in one part. For a zero in \(X_i\), its neighborhood-label sum is exactly the total weight outside \(X_i\).

The included checker does not use the theorem when testing a labeling. It builds each graph from its part labels, tests independence of the zero set directly, computes each zero vertex's neighborhood-label sum, and records the weight of every valid map to \(\{0,1,2\}\). It then compares every coefficient with the closed formula and checks the minimum weight.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
orders = 2..9
all weight-enumerator coefficients matched
minimum-weight formula matched
published complete-bipartite minimum matched for 1 <= q <= p <= 10
```

The checker also verifies the published complete-bipartite minimum formula for \(1\le q\le p\le10\). The exhaustive computation is finite corroboration only; the theorem for arbitrary part sizes follows from the proof.
