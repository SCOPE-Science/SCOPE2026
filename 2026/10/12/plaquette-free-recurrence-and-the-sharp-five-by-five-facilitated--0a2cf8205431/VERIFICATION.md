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

Every legal occupied rear facilitator–occupied source–vacant forward target jump cannot create a newly empty 2x2 plaquette: a 2-site axial plaquette containing the old source but excluding the new target contains the still-occupied rear facilitator. The exact finite part is exhaustive over all binomial(25,h) states for h=1..8, all 100 directed geometric move templates, and strongly connected components. An independently written C++ Tarjan/Kosaraju-style transition-graph decomposition (not the submitted verifier) obtained for h=1..8 SCC counts 1,1,1,26,26,76,126,426; terminal counts all one; recurrent states 25,300,2300,12625,52605,171900,448450,941450; and zero statewise disagreement between the terminal SCC membership and no-empty-plaquette property. Largest h=8 sector 1,081,575 states/17,054,400 directed edges. This is a complete FINITE proof for N=5, not a simulation. The below-K=17 multiplicity portion invokes published Kim–Lee–Seo Theorem 2.1(2) at N=5,d=2; direct full-paper verification was blocked and is explicitly a dependency risk.

## originality

PASS

Kim–Lee–Seo give uniqueness only for K>=22 and nonuniqueness for K<=16 upon specialization to N=5,d=2, leaving intermediate K=17..21. The complete 5x5 terminal-SCC computation closes that exact gap, identifies every recurrent state and counts class sizes. Goldstein–Lebowitz–Speer concern one-dimensional fluctuations and a different higher-dimensional facilitation predicate; no theorem covering the same finite directed transition graph was located. The primary Kim–Lee–Seo full text was not independently retrievable through available access; its exact theorem usage remains a documented risk rather than an automatic O failure.

## value

PASS

Finite exact determination of a sharp conserved-density threshold and complete communicating-class decomposition for the first nontrivial odd 2D torus directly resolves five sectors left between the published lower and upper dynamical bounds; physically natural local plaquette invariant and recurrence make this a meaningful finite classification, not an arbitrary state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
