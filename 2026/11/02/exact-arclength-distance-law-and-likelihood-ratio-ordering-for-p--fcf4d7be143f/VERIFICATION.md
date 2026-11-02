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

# Reproducible checks and scope

Run `python VERIFY.py` with an ordinary Python 3 interpreter; only the standard library is needed. The script builds finite projective planes over prime fields of orders \(2,3,5\), verifies regularity and diameter of the incidence graph, and uses independently computed breadth-first-search vertex distances to compute four-route intrinsic geodesics at every ordered pair of edges and at \(25\) exact rational-coordinate pairs. The three complete ordered-edge-pair sweeps test \(11{,}025\), \(67{,}600\), and \(864{,}900\) geodesic values. Exact integer polynomial checks verify the displayed mean, second-moment, variance, and mean-monotonicity identities.

The finite checker is a reproducibility aid and not an exhaustive certificate for every plane, every real arclength parameter, or all existing orders. The written proof uses only projective-plane incidence axioms, all four endpoint routes, explicit density integration, and an elementary strict-likelihood-ratio argument. One historical background paper was inaccessible for full-text originality assessment. No independent scientific audit has been performed.
