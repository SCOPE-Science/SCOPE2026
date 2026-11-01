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

Run `python3 verify.py` in the directory containing the accompanying `RESULT.md`. The verifier requires Python 3 and only standard-library modules. It constructs the 12 stated vertices; independently enumerates supporting planes from all vertex triples, finding 8 facets (4 triangles and 4 hexagons), and recovers the 18 edges from shared facets. It checks all vertex radii, edge lengths, and degree-three incidences with integer arithmetic.

It then lists all 12 vertex zero-hyperplanes and clips the fundamental triangle using exact `fractions.Fraction` arithmetic. Precisely four lines split the interior into six positive-area cells. Both the cyclic vertex lists and the resulting side counts are asserted against the explicit table in `RESULT.md`; this is an exhaustive finite calculation, not a numerical search. The spherical areas are evaluated with a stable analytic atan2 expression, checked to sum to \(\pi/12\), and normalized. Their weighted mean is compared to \(18\arccos(7/11)/\pi\), derived separately from the eighteen equal central edge angles.

Successful observed output:

```
Exact polyhedron: 12 vertices, 18 equal edges, 4 triangles, 4 hexagons.
Exact spherical-area evaluation: sides=4, probability=0.215936085312640
Exact spherical-area evaluation: sides=5, probability=0.520247465238937
Exact spherical-area evaluation: sides=6, probability=0.263816449448423
Mean sides from spherical areas=5.047880364135784; from 18 edge angles=5.047880364135783.
Independent isotropic Monte Carlo (35000 orientations): {4: 0.214514, 5: 0.520886, 6: 0.2646}.
PASS: exact combinatorics, all 6 spherical chambers, normalization,
independent mean identity, and finite numerical consistency.
```

## Scope of checks

Exact-arithmetic facet enumeration and rational clipping support the complete chamber census. Floating-point spherical areas and Monte Carlo are consistency tests; these finite checks are not proofs of assertions for infinitely many plane directions. The universal orientation law follows from the analytic chamber partition, the spherical triangle area identity, and Haar invariance. No independent proof audit or independent historical-priority assessment is represented.
