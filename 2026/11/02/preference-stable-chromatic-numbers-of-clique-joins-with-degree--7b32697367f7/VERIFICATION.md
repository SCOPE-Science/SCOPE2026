---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For H nonempty and max degree <=2, components are paths/cycles and the published exact base stable chromatic numbers give sigma(H) in {1,2,3}. For any k=t+sigma(H) palette, color the t clique vertices sequentially with favorite not-yet-used colors; every clique envy arc points backward into the clique and no clique vertex envies H, so coloring H stably with the remaining palette yields the bound t+sigma. For edgeless H and short-path forests, clique K_(t+1) or K_(t+2) gives lower bound. For a core triangle K_(t+3) gives lower bound. Otherwise H contains P4 and the proper color vector (1,2,3,1) on P4 plus clique colors 4..t+3 is a Grundy certificate; published Grundy lower and non-induced subgraph monotonicity give t+3. Fresh construction checked all clique sizes t<=10; this does not replace the general proof. The result includes wheels, fans and disconnected cores and handles C4 as a subgraph case.

## originality

PASS

Koana–Oh–Yoneda (September 2026) already prove exact stable chromatic values for individual paths/cycles, Grundy inequality and subgraph monotonicity. Their full main results do not state this clique-join classification; a new preference-greedy construction proves the upper, and a joined-P4 Grundy witness proves sharpness. This is a natural simple corollary built from their framework, not a claim of inventing stable coloring. Search found a separate K_(2,3,3) stable chromatic exact computation, not an implication for K_t joined to max-degree-two cores.

## value

PASS

Clique joins encode ubiquitous universal agents and yield entire families of fans, wheels and disconnected path/cycle cores. The exact three-regime formula and sharp constructive universal preference-stable bound close a natural graph-family classification that is not merely the existing path/cycle theorem: joins introduce new envy interactions. Its proof is short and its significance bounded to this class; it need not be a paper-sized theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
