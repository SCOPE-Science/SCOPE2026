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

The verifier constructs the half graph
\[
H_n
\]
for
\[
2\le n\le5.
\]

It exhausts every map
\[
f:V(H_n)\to\{0,1,2,3\},
\]
tests positive-support independence, and checks the double Roman requirements directly.

The direct result is compared with the theorem's \(n+1\) support families. The verifier also computes the exact weight histogram and compares it with
\[
2z^{2n+1}(1+z)^{n-1}
+
(n-1)z^{2n+2}(1+z)^{n-2}.
\]

Recorded output:

```text
VERIFY_OK
n=2: i_dR=5, minimum_functions=2, total_IDRDFs=5, histogram={5: 2, 6: 3}
n=3: i_dR=7, minimum_functions=2, total_IDRDFs=12, histogram={7: 2, 8: 6, 9: 4}
n=4: i_dR=9, minimum_functions=2, total_IDRDFs=28, histogram={9: 2, 10: 9, 11: 12, 12: 5}
n=5: i_dR=11, minimum_functions=2, total_IDRDFs=64, histogram={11: 2, 12: 12, 13: 24, 14: 20, 15: 6}
quaternary_labelings_checked = 1118464
feasible_IDRDFs_checked = 109
all feasible functions matched the n+1 support-family classification
```

The computation checks \(1{,}118{,}464\) quaternary labelings and \(109\) feasible functions. It is corroborative only; the arbitrary-\(n\) theorem follows from the independent-dominating-support classification and the forced boundary labels.
