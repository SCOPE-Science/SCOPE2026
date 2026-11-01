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

# Reproducibility and verification
The standalone source `verify.py` requires only Python 3's standard library. From the same folder run:

```sh
python3 verify.py
```

It recomputes the moment of each transformed triangle by independently intersecting the triangle edges with projected chord levels, integrating the resulting polynomial fiber moments by three-node Gaussian quadrature, subtracting the transformed centroid, and averaging over a shifted uniform direction grid. This is not merely substitution into the analytic tent-fiber result. The checks cover four noncongruent triangles, four parameter values at one angular offset and two endpoint parameters at a second offset, with \(4800\) directions each, totalling \(115200\) one-direction evaluations.

Additional checks verify the rational area of the reference polar hexagon, five rational Heron identities, and five threshold signs/equalities. The actual completion message was:

`TRIANGLE_RECENTERING_CHECK_OK: 35 exact/algebraic or independent quadrature comparisons; 115200 direction-level evaluations; threshold=0.103894354853268`

Numerical comparisons use an explicitly nonzero absolute/relative tolerance \(3\cdot10^{-6}\) because directionwise moments have mild angular nonsmoothness. These finite checks confirm sample instances but are **not** a proof of the exact angular integral or its all-triangles sharpness. Those claims use the analytic fiber integration, the polar-difference-hexagon area and Heron's identity in `RESULT.md`. Independent mathematical auditing has not been performed.
