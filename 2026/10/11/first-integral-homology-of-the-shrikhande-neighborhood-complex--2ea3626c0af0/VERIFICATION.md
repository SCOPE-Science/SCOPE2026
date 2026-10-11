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
The bundled verifier reconstructs the Shrikhande Cayley graph and its Lovász neighborhood complex directly from definitions. It checks degree \(6\), the two-common-neighbor property for every distinct vertex pair, all 808 nonempty faces, the face vector \((16,120,320,240,96,16)\), exact rational boundary ranks \((15,105,160,80,16)\), and the Smith diagonal \(1^{104},2\) for the triangle-boundary map expressed in an integral basis of \(\ker\partial_1\). It also recomputes boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\).

The verification establishes \(H_1(\mathcal N(\mathrm{Sh});\mathbb Z)\cong\mathbb Z/2\mathbb Z\) and the rational Betti vector \((1,0,55,0,0,0)\). It does not determine higher integral torsion or the homotopy type.
