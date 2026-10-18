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

# Reproduction and scientific limits

The attached `verify.py` requires only Python 3.10+ with its standard library. Invoke `python3 verify.py` in the directory containing the file. The script enumerates the 12 regular-icosahedron vertices and all 30 length-two edges, generates 60 oriented-edge truncation positions, and operates in the exact quadratic ring \(\mathbb Z[\varphi]\). Expected observations are exactly 260072 nonnegative Bernstein certificates, 32509 triples with the first directed edge fixed and eight maximizing triples, 487635 full four-set determinant checks at \(t=1/4\), 120 vertex maximizers, and 60 edge-segment families; it ends with `PASS`.

The verifier checks both signs of the bound polynomial against every determinant cubic using strict exact sign arithmetic; its Bernstein certificate controls every real parameter in \([0,1/2]\), not just a finite grid. Its second combinatorial check identifies the full winner matching at one interior parameter; the analytic equality condition from strict interior Bernstein positivity shows this matching persists throughout the open parameter interval. The separate determinant-affinity and positive-support argument is required to extend the finite vertex result to every tetrahedron contained in the convex hull. The volume formula covers endpoints, but the all-maximizer classification does not claim either endpoint. Independently check the source, base symmetry transitivity and analytic bridge before relying on the result.

The checks are reproducibility aids and self-review evidence, **not** independent certification. Historical-priority conclusions rely on a bounded comparison of identified literature and relevant published results, with residual priority risk.
