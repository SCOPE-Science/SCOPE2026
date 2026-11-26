---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Condition on the endpoint labels (a,b) of the bridge. On the a side, a=3 protects all internal vertices; a=2 leaves only assignments with at least one zero and no internal 2 or 3 to delete. For a=0 or 1, internal validity requires a 3, two 2s, or one 2 and all remaining internal labels 1. The last case protects a=1 already, but protects a=0 only when b≥2. These give exactly the four matrix rows including the exceptional terms in G_n and J_n. The two sides involve disjoint choices conditioned on (a,b), so the weight exponents add and the sum of the products is tr(M_n²). For n≥4, a side weighing at most 2 necessarily leaves an undefended internal zero. A side of weight 3 without a 3 has either one 2 and one 1 (leaving an undefended internal zero) or only 1s and 0s (no defender for any internal vertex). Thus each side must contain one 3 at weight 6, giving n² choices. Fresh direct adjacency enumeration over all labelings for n=2 and 3 in /workspace/branches/769a392d-55ad-4d41-9a0d-d72547d36996/reproduce_barbell.py confirmed every coefficient: 114 and 2325 valid functions, with leading terms 4x⁵ and 13x⁶ respectively. The frozen verifier and recorded output were inspected, not executed; the independent finite test supports the boundary cases, not the all-n proof.

## originality

PASS

The distinct supported contribution is the full ordinary double-Roman weight polynomial on two K_n joined by one edge, including minimum-layer multiplicities. The strongest checked indexed hits either match the graph but not the domination rule, or match the rule but not the graph. Available primary descriptions of optimization do not give all-weight coefficients. This is a best-of-evidence pass for the coefficientwise result, not a priority claim for scalar minimum weights or for the transfer-matrix method.

## value

PASS

A barbell is a natural first case of two dense blocks interacting through a cut edge. The polynomial gives all feasible weights and multiplicities, not just an optimization number; it identifies the extra tied optima at n=3 and the rigid one-3-per-block classification from n=4 onward. These exact coefficients and boundary layers are useful for evaluating counting methods and for comparison with other glued-clique graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
