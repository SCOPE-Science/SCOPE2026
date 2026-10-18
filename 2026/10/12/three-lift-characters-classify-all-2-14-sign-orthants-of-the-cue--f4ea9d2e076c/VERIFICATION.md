---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the explicit fifteen valuation weights of the Springer paper Example 1.3 (the submitted references incorrectly call it Example 1.2), compute all lower facets: 16 unimodular triangles filling 4Δ2. For each of 2^14 coefficient signs with s00 fixed positive, Viro patchwork in four reflected copies connects midpoints on opposite-sign edges, antipodally identifying boundary of Newton diamond. Independently reimplemented exact integer-midpoint union-find (not source code) across all 16,384 assignments: #components=1+A+B+C for every assignment. Exactly 2048 assignments realize each triple (A,B,C), giving 2048/6144/6144/2048 one-/two-/three-/four-component cases. Cueto-Markwig Table 1 necessary-and-sufficient lift conditions give count 4(1+A+B+C+AB+AC+BC)=4,8,16,28. In classical genus-three real quartic classification, two components with 8 real bitangents must be two nonnested ovals; thus excludes empty and nested-two-oval four-bitangent cases in this fixed chamber. Exhaustion proves this finite classification for specified triangulation; it does not extend to arbitrary valuations.

## originality

PASS

Cueto-Markwig 2023 explicitly provide the 3 sign conditions and 4 sample rows, not the 16,384-sign pattern/topology joint census. Geiger-Panizzut 2023 evaluated all 2^15 sign vectors over all tropical triangulations and established allowed totals, so global bitangent-count possibilities are strictly PRIOR coverage and cannot count as new. Their detailed Example 16 uses another triangulation and their published computation does not state the exact k+1 Viro topology identity, 8 pattern multiplicities or fixed Example 1.3 joint stratification. Those finite geometric statistics survive best-of-knowledge originality; code/database may contain a hidden equivalent census.

## value

PASS

This is a complete, finite but nontrivial sign-chamber classification of a canonical explicitly published tropical quartic, combining topology and real bitangents, with a sharp exclusion of possible Plücker topological types from one tropical chamber. The invariant and finite parameter space are mathematically natural, not an arbitrary truncation; exhaustiveness and exact joint counts can be reused to test tropical-real lifting procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
