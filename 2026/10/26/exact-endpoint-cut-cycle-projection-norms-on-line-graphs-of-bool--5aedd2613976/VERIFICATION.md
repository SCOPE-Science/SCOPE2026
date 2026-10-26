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

# Computational and analytical verification

Run `python check_line_cube.py` with Python 3.10 or later; no third-party packages are required.

The checker constructs each ordinary Boolean cube from its bit-flip edges and independently forms its line graph. It solves a grounded integer graph-Laplacian system with exact rational Gaussian elimination for 124 separately sourced line-graph edges: all 24 columns in dimension 3, all 96 in dimension 4, three in dimension 5, and one in dimension 6. These dimensions collectively have 1,400 line-graph edges. Every tested column matches both analytical endpoint norms and the projector diagonal forced by edge transitivity.

Independently, the checker evaluates the beta-type Green integrals using exact binomial-tail sums, verifies strict Green-level order, checks four current-enumeration sums, checks the closed formula for the Green level at one, and reproduces the projected cut-column norm for each of the 38 dimensions from 3 through 40.

Expected verified output:
`LINE_HYPERCUBE_HODGE_EXACT_OK integral_dimensions=38 grounded_graphs=4 grounded_columns=124 line_edges=1400`

These computations are finite consistency tests. The universal proof relies on the exact incidence reduction, heat-kernel integral, binomial summation and projection trace in `RESULT.md`; it does not infer all-dimensional truth from finite samples. No independent mathematical audit or external certification has been performed.
