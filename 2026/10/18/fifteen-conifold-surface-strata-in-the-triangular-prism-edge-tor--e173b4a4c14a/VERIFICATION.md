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

Execute `python3 verify_prism.py` with standard Python 3, using the file accompanying this result. The script reproduces the 12 supporting facets, 135 faces, singular torus-orbit dimension census \((9,24,15)\), 12 unimodular triangular maximal singular faces, three primitive parallelograms, degree \(18\), and balanced four-ray conifold configurations for all 15 maximal singular faces. Its expected successful output is:

```
VERIFY_OK facets=12 faces=135 singular_orbits=(9,24,15) components=(12_P2,3_P1xP1) degree=18 conifold_transversals=15
```

The script verifies all finite combinatorial and integral-lattice calculations exactly, including affine lattice saturation. The projective orbit closures, toric normality implication, node-ring interpretation, and non-\(\mathbb Q\)-factorial criterion use standard toric geometry together with the cited Ohsugi--Hibi normality theorem. There is no numerical-to-infinite extrapolation: the graph and polytope are fixed and fully enumerated. A fresh independent audit is not included. The full Jacobian singular scheme and non-generic completed local structures are not computed.
