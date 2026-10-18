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

The free space on weighted graph vertices is isometric to weighted ell_1(E)/ker(partial) because the dual potential constraints are precisely edgewise Lipschitz inequalities. On a cactus, edge-disjoint cycles generate a direct-support kernel, and each spanning tree omits exactly one edge r_C per cycle. The quotient-map identity ||P||=max_e ||Pq(e)||/w_e reduces each suppressed tree basis projection to its images on generating edges. The omitted-edge image has norm inf_t[W_C(S)|1-t|+(L_C-W_C(S))|t|]=min(W_C(S),L_C-W_C(S)); selected basis edges and idempotence supply the 1 term. For unit weights each prefix count runs 0..|C|-1, giving max_C floor(|C|/2), independent of tree/ordering and monotonicity iff all cycles are triangles or absent. This also handles bridges and overlong presentation edges without assuming their direct metric costs.

## originality

PASS

Best-of-knowledge PASS for exact coordinate-suppression operator norms for all weighted cactus spanning-tree molecular bases. General cycle transport quotient formulas (Skandalis–Valette, Ostrovska–Ostrovskii, Cabrelli–Molter) and general Lipschitz-free Schauder decomposition existence (Lancien–Pernecká) are inputs, not the asserted full edge-projection constant. Other cycle-subspace projections target a different operator space. Resultary returned the specific claim and unrelated projection families, no stronger same-operator cactus classification found.

## value

PASS

PASS: coordinate projection constants are natural invariants of concrete Schauder bases in Lipschitz-free transportation spaces. Exact weighted-cycle formula and unconditional/partial-sum classification for all cactus graphs is a nontrivial sharp structural theorem covering bridges, cutvertices, arbitrary tree/ordering, and varying positive edge lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
