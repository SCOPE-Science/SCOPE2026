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
# Reproducibility and verification limits

The packaged `verify.py` uses Python's standard library only. It passed the sixteen-sign averaging identity on 2400 integer quadruples, reconstructed every ray in three sorted-coordinate linearity cones using exact rational determinants, tested the local Rademacher norm identity on 1331 integer triples, and checked the exact cuboctahedral tangent volume. Its independent simulation sampled 150000 uniformly oriented four-dimensional directions at threshold \(X\ge0.9\) and obtained an event frequency \(0.14789\), compared with the exact predicted probability approximately \(0.14954\). Its final output was `ALL_CHECKS_OK`.

The optional `verify_hulls.py` requires NumPy and SciPy. It directly projected all eight cross-polytope vertices onto five numerically constructed hyperplanes, computed each three-dimensional convex-hull volume, and compared the normalized result with the independently evaluated sixteen-sign sum; it passed with `HULL_VOLUME_NORMALIZATION_OK 5`.

None of these finite checks proves the small-threshold asymptotics. That mathematical conclusion uses the proved local signed-average identity, exact tangent-polytope volume, finite extremizer classification, homothetic sublevel sandwich, and sphere-Jacobian estimate in `RESULT.md`. No external or independent mathematical audit has been performed.
