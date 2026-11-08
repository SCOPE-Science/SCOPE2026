---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The scalar fixed-point equation u=tanh(beta*u/4) has one globally attracting root for beta<=4 and 3 hyperbolic roots for beta>4. Acyclic follower recursion determines unique followers for each leader root assignment; the full Jacobian is triangular with leader index signs and follower -1 diagonals. Variation-of-constants inductively forces every follower to its input limit, hence the exact complete basin sets, including saddle equality cylinders. For beta>4 compact cube plus local IFT at all finite hyperbolic equilibria excludes additional nearby equilibria. Sampled two-leader two-follower numeric nine-equilibria and index checks at beta=4.6,8 independently corroborated the finite examples.

## originality

PASS

The source model and logistic scalar bistability are known; the claim limits novelty to arbitrary feedforward follower weights, full all-equilibria index and basin partition and robust equilibrium census. Existing block-based and small-circuit sources partly overlap, and the directly motivating arXiv full text remained inaccessible.

## value

PASS

An arbitrary-size non-equitable directed network family has a full dynamical phase portrait and exact basin-volume law with sharp bifurcation threshold and robust count, useful as a rigorous reference case in multistable influence/network models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
