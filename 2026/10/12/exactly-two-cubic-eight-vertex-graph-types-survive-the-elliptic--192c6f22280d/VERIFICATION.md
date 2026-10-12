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

# Reproducibility of the finite classification

Run `python3 verify_cubic8.py` using the Python 3 standard library. This program contains all six representative edge lists, generates every labeled cubic eight-vertex graph by exhaustive degree saturation, generates full vertex-permutation orbits of the six representatives, and checks exact orbit partition equality.

Every representative has 12 edges. For each of the 4096 spanning edge-subgraphs, the first algorithm evaluates all 256 binary inputs of the associated quadratic form using exact integer bit operations; the second builds a complete Walsh--Hadamard transform of the 256 edge signatures and checks the same Gauss sums independently. Both are exact, not floating point. The six counts must be (54, 26, 17, 6, 0, 5), leaving exactly classes 2 and 5 with odd parity.

A regression independently enumerates all simple six-vertex edge sets and applies an exact characteristic-two zeta transform to the elliptic property, recovering 345 supported labeled graphs with 105, 180 and 60 graphs of edge counts 7, 8, 9. This agrees with the cited published four-type six-vertex result and independently checks the convention for fixed-vertex spanning edge-subgraphs.

Expected successful terminal string:

`VERIFY_OK graphs=19355 classes=6 orbit_cover=exact two_independent_Gauss_transforms=agree selected_classes=2,5`

The enumerations establish a finite, exact classification. They neither prove the transform is supported only on subcubic graphs in general nor exclude a previously published equivalent enumeration. Independent scientific audit has not been performed.
