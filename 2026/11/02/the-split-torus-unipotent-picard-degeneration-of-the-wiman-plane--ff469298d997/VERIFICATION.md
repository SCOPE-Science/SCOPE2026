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

Run `python3 verify_wiman3.py` with Python 3 (standard library only). The verifier computes the characteristic-three polynomial identity, four tangent locations, all six ordinary intersections of the four lines, the weighted incidence arithmetic, and exhaustive projective point counts over three finite fields.

Observed output:

```
CHARACTERISTIC3_FACTORIZATION_OK
FOUR_RATIONAL_DISTINCT_TANGENCIES_OK
SIX_RATIONAL_DISTINCT_TRANSVERSE_LINE_PAIRS_OK
GF(3)_WIMAN3_POINTS_OK: 10
GF(9)_WIMAN3_POINTS_OK: 40
GF(27)_WIMAN3_POINTS_OK: 130
GRAPH_BETTI_6_AND_PICARD_DIMENSION_10_OK
VERIFY_OK
```

The verifier's finite tests are supplementary. The infinite all-extension zeta identity and the group-scheme identity follow from the written component, normalization, and local-unit arguments. No independent scientific audit or external certification has been performed.
