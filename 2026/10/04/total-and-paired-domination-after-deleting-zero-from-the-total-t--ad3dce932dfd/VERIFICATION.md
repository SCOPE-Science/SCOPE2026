---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

When \(T(M)\) is a submodule, the nonzero torsion vertices form \(K_{\alpha-1}\) and have no edges to nontorsion vertices. Nontorsion adjacency depends only on quotient cosets and pairs a coset with its negative. If \(2\in Z(R)\), every quotient coset equals its negative and each nonzero coset induces \(K_\alpha\); if \(2\notin Z(R)\), nonzero cosets pair into \(K_{\alpha,\alpha}\) components. Therefore isolated vertices occur exactly for \(\alpha=2\), or for \(\alpha=1\) with \(2\in Z(R)\). Every other nontrivial component has total and paired domination number two, so summing componentwise gives the three displayed formulas. The bundled exact checker realizes all boundary regimes over small \(\mathbb Z/n\mathbb Z\) examples and checks bounded abstract parameter profiles; the arbitrary finite-module theorem rests on the coset proof.

## originality

PASS

Saraei's 2014 paper is the exact structural predecessor for the zero-deleted graph, while Goswami--Sarmah's complete 2023 paper studies domination for the full graph and its torsion/nontorsion induced subgraphs. The 2023 full text contains domination and bondage parameters but no total-domination terminology, and no paired-domination result was located. Deleting zero changes the torsion component from \(K_\alpha\) to \(K_{\alpha-1}\), creating the sharp new isolated-vertex obstruction at \(\alpha=2\). Current Resultary search returned the assigned record as the exact hit and no broader zero-deleted total/paired classification. The 2014 full body remained inaccessible after public routes and an authorized retrieval attempt timed out, so that overlap risk is explicit.

## value

PASS

The exact zero-deleted graph is an established module invariant, and total and paired domination are natural strengthened domination parameters. The deletion creates a genuine existence boundary absent from the full graph, while the theorem gives a complete algebraic classification of both parameters in every finite submodule case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
