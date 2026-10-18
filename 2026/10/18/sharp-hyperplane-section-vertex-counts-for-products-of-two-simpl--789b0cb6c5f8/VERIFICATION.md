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

# Reproduction and limits

Execute `python3 check_simplotopes.py` in a directory containing the extracted standalone file. It requires Python 3 and its standard library; no network or optional package is needed. Successful execution prints these records:

```
EXHAUSTIVE_PARTITIONS_OK 76792
RATIONAL_HYPERPLANE_INTERSECTIONS_OK 823
UNRESTRICTED_CUT_GAP_OK 9
SIMPLOTOPE_SECTION_THEOREM_CHECKS_OK
```

The checker enumerates all Ferrers diagrams within the specified finite ranges, without extrapolating from that enumeration to all \(m,n\). It separately constructs affine coordinates for products of simplices, intersects rook-graph edges with exact-rational hyperplanes, and compares distinct intersection vertices to the graph cut count. For every dimension, the proof in `RESULT.md` supplies the required general argument.

The source-date anchor is Seacrest and Su, arXiv:0910.1134v1, first posted 6 October 2009. This is the date of a motivating public source, **not a publication date for the present theorem**. Historical-priority uncertainty remains in the alternate terminology of ordered sign matrices and threshold cuts. The result does not establish higher-codimension or multifactor analogues. No independent mathematical audit has been carried out.
