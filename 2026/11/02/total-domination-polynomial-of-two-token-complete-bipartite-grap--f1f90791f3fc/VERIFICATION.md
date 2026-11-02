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

# Verification information

The complete polynomial and minimum-set formulas are proved in `RESULT.md`. The standalone standard-library Python program `verify.py` checks the underlying token graph from its literal edge definition, independent of the inclusion–exclusion formulas, and then compares all cardinality coefficients.

Run `python3 verify.py` from the directory containing this file. The observed output includes:

```text
GRAPH_ENUM_OK 2 2 minimum 2 min_sets 8
GRAPH_ENUM_OK 2 3 minimum 3 min_sets 12
GRAPH_ENUM_OK 2 4 minimum 4 min_sets 32
GRAPH_ENUM_OK 2 5 minimum 5 min_sets 80
GRAPH_ENUM_OK 3 3 minimum 4 min_sets 108
GRAPH_ENUM_OK 3 4 minimum 5 min_sets 576
COMPONENT_ENUM_OK 3 5 minimum 6 min_sets 1170
COMPONENT_ENUM_OK 4 4 minimum 5 min_sets 576
COMPONENT_ENUM_OK 4 5 minimum 6 min_sets 2520
ALL_FORMULA_BOUNDARY_OK 56
GRAPH_MASKS_TESTED 4260928
VERIFY_OK
```

The six literal graph enumerations inspect all \(4,260,928\) possible initial vertex subsets across their respective cases. The three component enumerations generate mixed and pure selected-vertex subsets independently. The 56 additional parameter checks compare the minimum degree and minimum coefficient against the closed formulas, not against direct token-graph enumeration. Tests are finite and are not claimed to prove the result for all parameters; the universal proof is the four-part argument in `RESULT.md`.

Scientific priority and the correctness of the proof have not been independently assessed. No external proof certification has been performed.
