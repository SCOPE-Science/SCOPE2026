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

The proof is symbolic and uses only the defining conditions. Positive-support independence forces all positive labels into one part; direct neighborhood constraints then force that whole part to use only labels \(2\) and \(3\).

The included checker does not use the classification to decide feasibility. It reconstructs each complete multipartite graph, tests pairwise independence of the positive support, and tests the double Roman conditions separately at every vertex for every map to \(\{0,1,2,3\}\). It compares the resulting complete weight distribution with the closed formula and checks the minimum weight and minimum-function multiplicity.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
quaternary_labelings_checked = 9256080
orders = 2..9
all-function classification matched
all weight-enumerator coefficients matched
minimum weight and minimum-function count matched
```

The exhaustive computation is finite corroboration only; the theorem for arbitrary part sizes follows from the proof.
