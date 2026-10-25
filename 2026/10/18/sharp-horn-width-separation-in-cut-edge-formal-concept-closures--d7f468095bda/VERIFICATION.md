---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

For F⊆E(K_n), cuts containing F are exactly proper 2-colorings of graph (V,F). If F contains an odd cycle no cut exists and closure is all E; otherwise each component may flip independently and the forced edges are precisely pairs linked by an odd path within one bipartite component. Ternary rules from each three-edge path ab,bc,cd→ad shortcut all longer odd paths; triangle premises→E follow after shortcutting every odd cycle, giving iterative width≤3. A bare 3-edge path is not enlarged by any sound premise of width≤2, so width≥3. For direct application D=2 floor((n−2)/2)+1 is largest odd length ≤n−1; every bipartite forced edge has an odd simple path of length≤D. For inconsistent graphs, the shortest odd cycle is ≤D unless n is odd and it is Hamiltonian; in that case every missing edge is a chord forced by its odd arc of length≤n−2=D. A D-edge odd cycle with an isolated outside vertex forces a crossing edge requiring all D premises in one pass, establishing the matching lower bound for every n≥4. Independent exhaustive c_n(F) and iterative/direct comparison for all 64 F in K4 and all 1024 F in K5; not used for universal minimality.

## originality

PASS

General direct-versus-iterative Horn basis and hypergraph formal concept constructions are published. The specific closure of all graph cuts of K_n and its exact growing direct width versus constant iterative width were not given by the inspected general work. The auxiliary closed-set enumeration and EGF are already OEIS A307389 and expressly excluded from the new assertion.

## value

PASS

A natural cut-incidence closure gives a fully sharp explicit linear separation between one-shot and iterative Horn inference arities, with constructive matching bases and minimal obstruction witnesses for every n. Such a width gap matters in formal concept analysis and inference basis design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
