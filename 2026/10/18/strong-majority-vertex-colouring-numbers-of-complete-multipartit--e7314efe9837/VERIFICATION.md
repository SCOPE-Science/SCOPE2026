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

# Reproduction and limitations

Run `python3 verify_majority.py` in the directory containing the file. The program uses only the Python 3 standard library and tests the defining inequality by constructing vertex neighbourhoods directly, with no invocation of the theorem formula in that predicate. It enumerates named binary and ternary colourings of all 51 unordered connected complete multipartite part profiles on three through eight vertices having minimum degree at least two. It separately builds and directly validates explicit candidate colourings for 9,246 profiles of orders three through 25, plus eight large stress profiles. The run recorded:

```
EXHAUSTIVE: 51 unlabeled multipartite types, sizes 3..8; 51 2-color tests; 51 3-color tests.
CONSTRUCTIVE: 9246 unlabeled multipartite types, sizes 3..25.
LARGE: 8 stress profiles checked. ALL PASSED
```

The exhaustive finite search confirms the exact small-case lower bounds and the constructive generator. The generator's soundness for arbitrary sizes is proved separately by the pair-extension lemma in `RESULT.md`; numerical runs alone cannot certify an infinite family. Bibliographic priority is not independently certified. Independent audit remains unperformed.
