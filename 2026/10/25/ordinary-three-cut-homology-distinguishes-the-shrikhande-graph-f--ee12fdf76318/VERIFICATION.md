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

# Verification details

Run the complete standalone, standard-library checker with `python3 verify.py`.

Observed successful output:

```
VERIFY_OK: 16 vertices, 48 graph edges, 32 graph triangles;
dual f-vector (16,120,176,60), 60 collapsible tetrahedra,
boundary ranks (15,105,60) mod 2,3,5, Betti vector (1,0,11,0).
```

The program explicitly enumerates all graph pairs and triples, dual faces up to cardinality five, counts all tetrahedron types, checks that every tetrahedron has globally free triangular faces, verifies that two coordinate generators bound tetrahedra, and evaluates signed boundary ranks over prime fields \(2,3,5\). This is a finite exact consistency test. It is **not** an integer Smith-normal-form computation, and three finite characteristics alone could not rule out other torsion. The structural two-dimensional collapse, the torus fundamental-group argument, Euler characteristic, Hurewicz and integral Alexander duality provide the mathematical proof of the integral claim. No independent review or external certification has occurred.
