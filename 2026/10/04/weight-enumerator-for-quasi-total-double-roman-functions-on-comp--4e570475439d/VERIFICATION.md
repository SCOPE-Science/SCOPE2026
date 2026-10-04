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

The checker constructs each complete multipartite graph from its part labels and tests the quasi-total double Roman definition directly on every map to \(\{0,1,2,3\}\). For a vertex labeled \(0\), it counts neighboring labels \(2\) and \(3\); for a vertex labeled \(1\), it tests for a neighboring label at least \(2\); and for every positive vertex it tests isolation inside the induced positive support.

A separate polynomial routine evaluates the closed formula using integer coefficient arrays. It does not call the structural classifier to decide validity.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 58
labelings_checked = 1653904
valid_functions_counted = 1311046
orders = 2..8
every weight-enumerator coefficient matched
minimum-weight corollary matched
```

The exhaustive computation is finite corroboration only. The theorem for arbitrary part sizes follows from the proof.
