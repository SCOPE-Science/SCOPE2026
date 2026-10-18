---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The given expected-payoff death–birth model has u=-cx+bPx, positive fitness exp(delta[u_i+lambda_i(Pu)_i]), and uniform death with proportional-neighbor reproduction. Equality of all individual replacement probabilities at each vacancy is precisely equality of lambda_i(Pu)_i for each pair of common-neighbor competitors (relative fitness ratios). Fully cooperative configuration x=1 and variable b!=c forces lambda_i=lambda_k on each common-neighbor pair. Varying c while using binary basis configurations forces P_i=P_k whenever their shared lambda is nonzero. The common-neighbor auxiliary graph is connected for connected nonbipartite G, has exactly the two bipartition parts as components for connected bipartite G. No adjacent vertices can have equal loopless stochastic rows; any nonzero invisible profile thus forces G complete bipartite. Conversely on K_{a,b} identical P rows within each side imply sidewise constant lambda cancels out of all competing fitness ratios. Includes stars and K1,1, all delta>0, b,c>0, all binary states, arbitrary real part constants; same entire transition kernel follows. Independently enumerated 771 connected labeled loopless graphs of orders 2..5 and all {-1,0,1}^V profiles and verified exact equivalence; source P4 strategy witness gives competitor log-fitness difference delta/4. The unrestricted theorem relies on analytic common-neighbor proof, not finite testing.

## originality

PASS

Xiong–Li–Kurths–Szolnoki–Feng (2026) introduce the same payoff and social-comparison fitness and derive weak-selection cooperation conditions; their abstract and methods description do not state an exact all-delta microscopic transition-kernel invariance classification. Peña–Rochat (2012), accessible full PMC text, use bipartite individual–group interaction hypergraphs in multiplayer games rather than exact cancellation in expected-payoff exponential fitness under death–birth. Szolnoki–Perc (2021) study strategy-dependent payoff averaging with imitation, not the specified fitness/update. The mathematical if-and-only-if complete-bipartite characterization and two-real-parameter nullspace are beyond the inspected prior claims, while uninspected portions of Xiong remain a material risk.

## value

PASS

Identifying every graph and nonzero susceptibility profile for which a seemingly nonlinear social-comparison perturbation leaves the entire microscopic Markov chain unchanged is a substantive structural invariance/boundary theorem. It distinguishes exact kernel invisibility for every positive selection strength from agreement of one weak-selection threshold, with direct consequences for parameter identifiability and games on stars/complete bipartite networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
