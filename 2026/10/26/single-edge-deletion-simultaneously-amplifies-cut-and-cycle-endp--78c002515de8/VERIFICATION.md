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

# Reproducibility and proof limits

The result follows for every \(n\ge4\) from the Walsh-character Laplacian decomposition, a rank-one inverse identity, exact sign alignment across directions, and positivity of the two displayed current-column gains. This is a proof for the infinite family and does not extrapolate finite calculations.

Run `python3 verify.py` using Python 3 and its standard library. This constructs the entire intact cut-current matrix with rational Walsh sums for each dimension \(2,3,4,5\). It then constructs the cut projector of the damaged graph a second way, by independently inverting its grounded Laplacian with fraction arithmetic, and compares all column entries to the rank-one formula. All 124 damaged-graph columns are compared. The same program checks complete row-column norms for \(n=2,3\), the four \(n=3\) edge-class values, exact kernel coefficients, and the adjacent witness increments for all tested dimensions.

Observed successful output ends with `EDGE_DELETED_CUBE_EXACT_OK dimensions=4 independent_grounded_columns=124`.

The checker is not a proof of any untested dimension, and the general theorem does not claim exact **maximizing** columns when \(n\ge4\). The result is specific to real, unweighted, single-edge-deleted hypercubes and canonical Euclidean-orthogonal projections. Independent mathematical validation has not been performed.
