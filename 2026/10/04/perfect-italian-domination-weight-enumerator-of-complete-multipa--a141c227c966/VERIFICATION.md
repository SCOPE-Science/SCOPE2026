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

The symbolic proof uses only the neighborhood structure of complete multipartite graphs. For a zero-labeled vertex in part \(X_i\), the neighbor-label sum is exactly the global weight minus the weight inside \(X_i\). Summing the resulting equalities over zero-containing parts gives the finite case split used in the enumerator.

The included checker independently evaluates the original definition. For every ternary labeling of every complete multipartite isomorphism type of orders two through nine, it explicitly sums labels over vertices in different parts for each zero-labeled vertex. It then compares the result with the stated profile criterion and with every coefficient of the closed formula.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
orders = 2..9
all-set profile criterion matched
all weight-enumerator coefficients matched
published all-parts-at-least-3 minimum specializations checked = 7
```

The checker also compares the minimum nonzero coefficient degree against the published all-parts-at-least-three theorem on every tested specialization where that theorem applies. The finite computation is corroborative only; the all-orders statement follows from the proof.
