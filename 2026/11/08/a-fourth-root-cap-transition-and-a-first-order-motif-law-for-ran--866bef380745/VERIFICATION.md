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

# Verification of the cap-conditioned graph laws

The analytic proof uses exact spherical radial–tangent independence and a Gram-determinant expansion, whose integrated remainder is controlled by Gaussian and spherical marginal tails. Moment-convergent radial overshoots produce the critical cap coefficient, while truncated-normal radial moments give the equatorial coefficient. The proof treats each finite labelled graph, and the finite numerical checks are only corroboration.

Run `python check_cap_graph.py` after installing `requirements.txt`. The checker uses a fixed pseudorandom seed, analytic motif formulas for every labelled three- and four-vertex graph, and exact conditional beta-radial inversion for cap-uniform points. The tangential Gram entries use sequential independent spherical-coordinate sampling, rather than the asymptotic Gram density. The simulation samples 280,000 independent triangles for each of eight tested settings: dimensions 500 and 3000; critical cap parameters 0.7 and 1.0; equatorial parameters 0 and 2.0. It verifies the complete-graph, two-edge, one-edge and empty-graph pattern probabilities against the first-order formulas, and checks that the analytical correction terms sum to zero over all labelled patterns.

An observed successful run printed `CAP_GRAPH_PATTERN_EXPANSION_CHECKS_OK 32 0.014926`. This is a numerical consistency check with explicit tolerances accounting for finite-size second-order effects. It cannot establish error bounds or novelty. No independent mathematical audit has been performed.
