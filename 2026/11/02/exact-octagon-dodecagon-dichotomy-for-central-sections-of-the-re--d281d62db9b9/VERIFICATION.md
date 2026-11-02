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

# Verification

Run `python3 verify_rhombicuboctahedron.py` (Python 3 standard library only). The checker constructs all \(24\) vertices in exact \(\mathbb Q(\sqrt2)\) arithmetic, finds exactly \(48\) length-\(2\) edges with four at each vertex, clips every candidate sign pattern of the four critical lines against the full fundamental triangle, and checks the underlying original vertex-sign linear forms on every cell vertex. The six positive-area chambers have section counts \(8,12,12,12,12,12\). The unique octagonal chamber has planar vertices \((0,0)\), \((1/a,0)\), and \((1/(a+1),1/(a+1))\) with \(a=1+\sqrt2\). Exact dot products of its three inward spherical wall normals give the angles used in Girard's formula.

The current package's checker also executed an independent direct-edge Gaussian-normal diagnostic with \(80{,}000\) orientations, of which \(16{,}772\) yielded octagons. Each direct edge count matched the sharp coordinate-threshold classification; the observed octagon frequency \(0.20965\) is compatible with the exact \(0.207863937034156\). This finite diagnostic cannot prove the result for all directions. Numerical evaluations of transcendental functions are corroboration; the equality is established by exact symbolic identities and spherical geometry.

Limitations: exceptional plane orientations containing vertices are excluded, and no independent mathematical audit has been performed.
