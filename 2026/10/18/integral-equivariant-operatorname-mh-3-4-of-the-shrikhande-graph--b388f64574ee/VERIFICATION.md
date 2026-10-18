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

# Reproducible exact checks

Install the dependencies in `requirements.txt`, keep `certificate.json` alongside `verify.py`, and execute:

```
python verify.py
```

The script builds the full sixteen-vertex Cayley graph, computes shortest-path distances without assuming the diameter, generates all length-four magnitude-chain bases and signed boundaries for the four orbit representatives, and confirms their consecutive boundary compositions are zero. Integer Smith reduction checks that every nonzero third- or fourth-boundary Smith invariant is a unit, proving torsion-freeness, while exact rational ranks determine the free ranks. Every one of the six stabilizer elements across the two nonadjacent orbit types is tested on an explicit cocycle modulo coboundaries; each gives exactly the specified sign. The computed orbit sizes and group order exhaust the vertex-pair classes. The compact `certificate.json` is compared with these regenerated data.

The observed success marker was `VERIFY_SHRIKHANDE_INTEGRAL_MAGNITUDE_EQUIVARIANT_OK` followed by the four exact endpoint cases and both signed character tables. These are actual same-model tests, not independent audit, and no statements about other bidegrees are checked. The decisive pre-existing published rational rank and graph comparisons must not be mistaken for new discoveries.
