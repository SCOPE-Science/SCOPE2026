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

# Reproducibility

Run `python3 verify_duad.py` and `python3 verify_conflict.py` in the directory containing the source files and the two CSVs. Both programs require only Python 3's standard library and raise an exception if any claimed count or certificate differs.

`verify_duad.py` exhaustively examines 32768 sets of duads; each private syntheme choice yields exactly one induced matching. It computes the full polynomial, inclusion-maximal spectrum and extensions, then verifies the ten geometric optima against `maxima.csv` and all coefficients against `spectrum.csv`.

`verify_conflict.py` independently constructs the 45 incidence flags and their complete compatibility relation; it enumerates all induced matchings by increasing edge indices, counts legal extensions against all 45 possible edges, and checks both CSVs.

Observed successful output:

```
VERIFY_POINT_OK duads=15 synthemes=15 flags=45 subsets=32768
VERIFY_POINT_OK polynomial=1,45,720,5160,16920,22680,8520,720,90,10 total=54866
VERIFY_POINT_OK inclusion_maximal=5:3060,6:5520,7:360,9:10
VERIFY_POINT_OK size8=90 all_uniquely_extend_to_size9=true
VERIFY_POINT_OK all_10_maxima_are_3plus3_partitions_of_six=true
VERIFY_CONFLICT_OK flags=45 enumerated_induced_matchings=54866 polynomial=1,45,720,5160,16920,22680,8520,720,90,10
VERIFY_CONFLICT_OK inclusion_maximal=5:3060,6:5520,7:360,9:10
VERIFY_CONFLICT_OK size8_unique_extension=90/90 size9=10
```

These computations are exhaustive only for the single 30-vertex graph. The separate analytical proof of the maximum matching classification appears in `RESULT.md`. No independent external validation has been performed.
