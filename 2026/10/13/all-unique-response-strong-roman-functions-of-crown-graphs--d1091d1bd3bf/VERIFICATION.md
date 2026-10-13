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

The verifier constructs every crown graph
\[
\operatorname{Cr}_n
\]
for
\[
3\le n\le5.
\]

For each permitted labeling, it directly checks both components of the definition: the unique-response restrictions on the number of strong neighbors, and the strong Roman defender inequality for every zero-labeled vertex.

The direct result is compared with the three-family classification. It also independently compares the complete weight histogram with
\[
z^{2n}+2n z^{n+h}+n z^{2h},
\qquad
h=1+\left\lceil\frac{n-1}{2}\right\rceil.
\]

Recorded output:

```text
VERIFY_OK
n=3: h=2, weight_counts={4: 3, 5: 6, 6: 1}, total_functions=10
n=4: h=3, weight_counts={6: 4, 7: 8, 8: 1}, total_functions=13
n=5: h=3, weight_counts={6: 5, 8: 10, 10: 1}, total_functions=16
labelings_checked = 1114841
URStRDFs_checked = 39
all feasible functions matched the three-family classification and exact weight enumerator
```

The finite enumeration is corroborative only. The theorem for all \(n\ge3\) follows from the crown \(2\)-packing classification and the forced-label argument in the proof.
