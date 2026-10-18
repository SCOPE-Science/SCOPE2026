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

The reproducible calculation is supplied in `verify.py` and requires only Python 3.10+ standard library. Run `python3 verify.py`; expected status marker: `TRIANGULAR_T6_HIGHER_INDEPENDENCE_HOMOTOPY_VERIFIED`.

The checker performs two independently worded exact membership tests for each of the 32768 vertex subsets; verifies the augmented face count `(1,15,105,195,90)` and the 15 lower-dimensional facets; produces 185 legal matching pairs; checks all 1155 nonempty face-poset incidence arrows for acyclicity; and verifies critical counts `(1,0,24,10)`.

The signed integer Morse boundary from critical dimension three to critical dimension two is computed by eliminating unit matched incidences along acyclic gradient paths. Every coefficient is exactly zero. A separate mod-two Gaussian reduction on the unreduced simplicial chains checks boundary ranks `(14,91,80)`; the mod-two calculation is not substituted for the integral attaching-degree argument. The topological step uses the fact that all maps from the 2-sphere into a simply connected wedge of 2-spheres are classified by integral degree vectors.

These finite checks concern this single explicitly defined complex. They do not certify an arbitrary infinite graph family, an equivariant splitting, or independence from existing literature.
