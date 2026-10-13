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

The checker enumerates every connected canonical chain graph with
\[
|X|,|Y|\in\{3,4\}.
\]
A canonical type is represented by a nondecreasing positive degree sequence on one side whose maximum equals the opposite-side size.

For every type, the checker enumerates all labelings
\[
f:V(G)\to\{0,1,2,3\},
\]
tests the two double Roman conditions and the no-isolated-positive condition directly, computes the minimum weight, and compares every minimum function with the universal-pair classification.

Recorded output:

```text
VERIFY_OK
chain_types_checked = 46
quaternary_labelings_checked = 1662976
minimum_functions_checked = 156
all minima were exactly universal opposite-side pairs labeled 3
```

The checker covers \(46\) canonical chain types and \(1{,}662{,}976\) quaternary labelings. This finite verification is corroborative only; the arbitrary-size theorem follows from the analytic proof.
