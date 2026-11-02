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

# Reproducible supplementary checks

The assertion is proved analytically in `RESULT.md`; the finite checker is not an exhaustive certificate for all finite graphs. Running `python checker.py` requires NumPy and SciPy. The script reconstructs the unnormalized symmetric generator from each edge set, constructs Lipschitz dual potentials on the actual cone metric, computes the heat matrix with `scipy.linalg.expm`, and evaluates edge-pair \(W_1\) dual maxima. Difference-constraint integrality justifies enumerating \(\{-1,0,1\}\) for the finitely tested cones with the hub fixed at zero. Every labeled graph on \(d=2,3,4,5\) peripheral vertices is tested, including disconnected graphs and graphs with no isolates. Seven time values include zero; a separate test covers the peak identity for \(4\le d<300\).

Recorded replay: `CHECK_OK graphs=1098 supplementary_assertions=16556`.

Limits: floating-point matrix exponentials and finite tolerances cannot certify a universal theorem; all universal inequalities and the strict equality classification are proved symbolically in the main proof. No external independent audit was performed.
