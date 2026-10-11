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

The bundled `verify.py` uses only the Python standard library. It reconstructs the four published facet families, checks the ambient face vector, extracts the 60-facet symmetry orbit, closes it under faces, and verifies the exact face vector.

It then performs a deterministic elementary-collapse sequence. Before every deletion it checks that the proposed free face has a unique maximal coface. The sequence has exactly 270 pairs and leaves a two-dimensional complex with face vector \((32,210,270)\).

Finally, exact bitset Gaussian elimination over \(\mathbf F_2\) gives boundary ranks \(31\) and \(179\), hence Betti vector \((1,0,91)\). The verifier independently recomputes homology directly on the unreduced orbit subcomplex and obtains \((1,0,91,0,0)\). No floating-point or randomized computation is used.

Scientific limit: these checks prove the stated finite mod-two homology claim but do not establish integral homology, the fundamental group, or a wedge-of-spheres homotopy type.
