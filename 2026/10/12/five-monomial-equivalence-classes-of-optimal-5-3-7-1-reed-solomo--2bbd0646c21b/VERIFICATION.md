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
# Exact reproducibility record

Running `python3 verify.py` with the standard Python library checks the finite theorem without probabilistic steps. In one replay of this exact package the script printed:

```
DISTINCT_RS_CODES 60
COMPATIBILITY_EDGES 1200
MAXIMAL_CLIQUE_HISTOGRAM {6: 30, 7: 1920, 8: 5070, 9: 1800, 10: 138}
MAXIMUM_FAMILIES 138
COORDINATE_EQUIVALENCE_ORBITS 5
ORBIT_SIZE_STABILIZER [(6, 20), (12, 10), (30, 4), (30, 4), (60, 2)]
STABILIZER_ELEMENT_ORDERS [{1: 1, 2: 5, 4: 10, 5: 4}, {1: 1, 2: 5, 5: 4}, {1: 1, 2: 1, 4: 2}, {1: 1, 2: 1, 4: 2}, {1: 1, 2: 1}]
VERIFY_OK
```

The script also prints complete canonical representatives of all five orbits. All arithmetic is modulo seven; every code, compatibility pair, maximal clique, size-ten clique, and coordinate permutation is enumerated. The script uses two different clique-enumeration recursions as a cross-check. The computed counts are confined to the explicitly defined finite parameter case. This same-package replay is not an independent external audit, and it does not verify any broad field-size statement.
