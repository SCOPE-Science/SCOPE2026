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
# Reproduction of finite exact checks

Run `python3 verify_johnson.py` using the Python standard library. The script solves the full finite graph Laplace problem for five Johnson graphs and separately tests 308 parameter choices through a rational tridiagonal orbit system. It compares every reconstructed edge-current magnitude in the selected column and tests the diagonal effective resistance and both endpoint formulas.

Recorded result: `JOHNSON_PROJECTION_EXACT_OK orbit_cases=308 full_graph_cases=5 full_graph_edges=2036`.

The proof in `RESULT.md` establishes the unrestricted integer domain. The finite checker does not claim an exhaustive test of infinitely many parameter pairs, nor any independent audit. All norm claims concern canonical orthogonal projections, not unrestricted projection minima.
