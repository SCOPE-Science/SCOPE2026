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

The standalone verifier `verify_icosahedral_neighborhood.py` uses only the Python standard library and reads the packaged `morse_certificate.json`. It reconstructs the explicit 12-vertex, 30-edge, 5-regular graph and its full Lovász neighborhood complex, checking the face vector \( (12,60,120,60,12) \) and all 264 nonempty simplices.

It regenerates the complete 120-pair face-poset matching from the archived vertex order, checks that every pair is a Hasse cover with no reused simplex, orients every one of the 780 Hasse covers according to Forman's rule, and verifies acyclicity by an exhaustive topological sort. The critical-cell vector is checked to be one cell in dimension 0, twenty-three in dimension 2, and zero in every other dimension present.

As a separate algebraic cross-check, it builds every simplicial boundary matrix over \(\mathbf F_2\) and obtains Betti vector \( (1,0,23,0,0) \). A successful replay begins with `VERIFY_OK`.

The verification is exact for the explicit finite graph. No independent audit has been performed.
