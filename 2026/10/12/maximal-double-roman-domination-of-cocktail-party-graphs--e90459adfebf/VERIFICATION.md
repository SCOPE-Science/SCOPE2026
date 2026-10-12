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

The checker constructs the cocktail party graph \(CP_n\) directly as a graph on \(2n\) vertices in which each vertex is adjacent to every vertex except itself and its unique partner.

For each labeling
\[
f:V(CP_n)\to\{0,1,2,3\},
\]
it checks the double Roman conditions directly. It then constructs the set dominated by the zero-labeled vertices using closed neighborhoods and accepts the labeling as maximal double Roman exactly when that zero set fails to dominate the graph.

For
\[
2\le n\le5,
\]
the checker exhausts all \(4^{2n}\) labelings, computes the actual minimum weight, and compares the complete minimum-function set with the theorem's predicted family.

Recorded output:

```text
VERIFY_OK
n=2: gamma_m_dR=5, minimum_functions=4
n=3: gamma_m_dR=7, minimum_functions=36
n=4: gamma_m_dR=9, minimum_functions=120
n=5: gamma_m_dR=11, minimum_functions=280
labelings_checked = 1118464
all minimum functions matched the singleton-zero/two-2 classification
```

Thus \(1{,}118{,}464\) labelings are checked in total. The finite computation is exhaustive for the tested orders and corroborative only for the arbitrary-order theorem, which follows from the proof in `RESULT.md`.
