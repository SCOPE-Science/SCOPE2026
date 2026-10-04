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

The standalone checker constructs \(W_{n,m}\) directly from an adjacency list. For every tested vertex subset, it computes the induced degree of every selected vertex and decides dissociation without using the theorem's structural classification.

It separately compares the direct decision with the center/blade criterion, accumulates the full coefficient sequence, tests inclusion-maximality by all one-vertex extensions, and checks the total count, maximum size, and both maximal-set multiplicities.

Recorded output:

```text
VERIFY_OK
windmill_parameter_pairs_checked = 16
vertex_subsets_checked = 334112
dissociation_sets_checked = 62554
maximal_dissociation_sets_checked = 3408
parameters n,m>=2 with 1+n*m<=18
all direct degree tests matched the structural classification
all dissociation-polynomial coefficients matched
all total counts, maximum sizes, and maximal-set multiplicities matched
```

The finite exhaustive computation is corroborative only. The theorem for arbitrary \(n,m\ge2\) follows from the proof.
