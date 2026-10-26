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

## Reproducible checks

The file `verify.py` independently builds every graph's adjacency from the Cartesian-product edge rule and tests that each vertex (including every selected one) has a selected *neighbor*, not merely itself. Every nonempty subset of each of the nine graphs with \(2\le n\le10\) is tested for total domination and deletion-minimality. The resulting exact set of vertex subsets is compared, element by element, with the three structural families; then multiplicities and the claimed gap are checked. `verify_output.txt` is the output of executing this exact file's contents with Python 3. The verification is finite corroboration, not a substitute for the unlimited proof in `RESULT.md`.

## Limits

The test does not prove statements for \(n>10\), certify bibliographic originality, or constitute independent external validation.
