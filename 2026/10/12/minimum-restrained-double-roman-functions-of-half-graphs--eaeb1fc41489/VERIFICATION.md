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

For every map
\[
f:V(H_n)\to\{0,1,2,3\},
\]
it checks directly that every zero has either one label-\(3\) neighbor or two label-\(2\) neighbors, every label-\(1\) vertex has a neighbor labeled at least \(2\), and the zero-induced subgraph has no isolated vertex.

The minimum weight and the complete minimum-function set are compared with the theorem.

Recorded output:

```text
VERIFY_OK
n=2: gamma_rdR=6, minimum_functions=5
n=3: gamma_rdR=8, minimum_functions=9
n=4: gamma_rdR=8, minimum_functions=1
n=5: gamma_rdR=8, minimum_functions=1
quaternary_labelings_checked = 1118464
all minimum functions matched the piecewise classification
```

The verifier examines \(1{,}118{,}464\) quaternary labelings. The finite computation is exhaustive for \(H_2,H_3,H_4,H_5\). It is corroborative only for the arbitrary-\(n\) statement, which follows from the end-block proof.
