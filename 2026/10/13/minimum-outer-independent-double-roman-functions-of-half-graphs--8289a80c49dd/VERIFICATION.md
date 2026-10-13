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

The verifier constructs \(H_n\) for
\[
2\le n\le5.
\]
For every map
\[
f:V(H_n)\to\{0,1,2,3\},
\]
it directly checks outer independence, the zero-defense rule, and the label-\(1\) support rule. It then computes the minimum weight and compares the complete minimum-function set with the theorem.

Recorded output:

```text
VERIFY_OK
n=2: gamma_oidR=5, minimum_functions=4
n=3: gamma_oidR=7, minimum_functions=8
n=4: gamma_oidR=8, minimum_functions=5
n=5: gamma_oidR=9, minimum_functions=6
quaternary_labelings_checked = 1118464
all minimum functions matched the piecewise classification
```

The verifier examines \(1{,}118{,}464\) quaternary labelings. The computation is exhaustive for \(H_2\) and \(H_3\), and corroborative for the infinite family. The arbitrary-\(n\) theorem follows from the analytic proof.
