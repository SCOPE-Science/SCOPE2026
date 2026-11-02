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

The complete proof is in `RESULT.md`; `checker.py` is a dependency-free finite test. Running `python3 checker.py` produced:

`ALL_CHECKS_OK (direct forcing n<=3, graph/partition census n<=6)`

The direct small test generates every reflexive symmetric compatibility relation and every binary accessibility relation, tests forcing directly, and separately tests reflexivity, symmetry, and transitivity. The all-size formulas are also checked by complete enumeration of undirected compatibility graphs and set partitions through six points. The asserted all-size and asymptotic results require the mathematical proof; these finite tests do not certify infinitely many cases or historical priority.

Independent audit status: not performed.
