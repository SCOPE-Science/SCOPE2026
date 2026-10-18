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

# Reproduction and checks

Run `python3 verify.py` with a standard Python 3 interpreter. The checker uses only integer arithmetic and the standard library; it prints `VERIFY_OK` after completing all assertions.

It independently enumerates both integer potential representatives and ordered partitions of a five-element set, obtaining identical sets of 389 graphical sign vectors. It enumerates the 26 connected cuts, computes the exact ray and determinant profile for each cone, and checks that all 361 simplicial cones are regular. It then verifies the 8 minimal nonsmooth three-cones and 4 minimal nonsmooth four-cones, their primitive integer relations, saturated lattice minors, maximal-cone incidences and the absence of intersections between distinct singular curves. The 78 fixed points split into 58 regular and 20 singular.

The finiteness argument for score enumeration and the connected-cut extremality criterion are stated in RESULT.md. The checker establishes the finite fan and lattice facts; identification with toric orbit closures, conifold charts and the Segre determinantal cone uses standard toric geometry. No claim is made to computer-assisted certification of unrelated cases, an infinite graph family, or independent external audit.
