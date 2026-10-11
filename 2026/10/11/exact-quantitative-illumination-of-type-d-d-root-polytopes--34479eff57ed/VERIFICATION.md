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
# Reproducible proof checks

The supplied file `verify_root_illumination.py` runs under Python 3 without external packages. Run `python3 verify_root_illumination.py` in the directory containing the embedded files. An executed exact-integer sweep with magnitudes \(0,1/2,1,3/2,2,3,4\) in dimensions \(3\) through \(6\) returned:

```
EXACT_DIAGNOSTIC_OK cases=137200 illuminated_pairs=68296 max_single_source_count=3
```

This checks the complete active-facet inequality for each signed coordinate pair against a separately computed compressed criterion, the strict efficiency obstruction on those cases, and absence of disjoint illuminated edges. It is a finite test, not an exhaustive argument for all magnitudes/dimensions.

The universal proof is independent of enumeration: the exact coordinate-halfspace polytope identity; the active-facet source illumination equivalence; pairwise edge intersection; star/triangle graph classification; strict weighted inequalities; and near-vertex upper sources appear explicitly in `RESULT.md`. For \(d\ge3\), their combination proves the stated infimum. The prior-work evaluation was a same-model scientific comparison and is not an independent audit. Earlier unindexed publication remains possible.
