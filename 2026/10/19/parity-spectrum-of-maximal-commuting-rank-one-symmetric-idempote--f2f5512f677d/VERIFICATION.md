---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Each normalized vector of coordinate sum one determines a unique rank-one symmetric projection; for distinct lines the two products cannot be equal and nonzero, so adjacency is orthogonality. A partial orthonormal frame has nonsingular complement W; it is terminal exactly when W is alternating, equivalently the canonical dot-product vector lies in the frame span. Nonalternating forms over this perfect field diagonalize: a remaining symplectic plane can be absorbed using [1]⊥H≅I₃. As a separate count check, for a nonterminal ordered prefix with residual dimension d there are q^(d−1) norm-one successors. Exactly one is terminal when d is odd (the residual canonical vector), and none when d is even. Thus nonterminal prefixes grow by q^(d−1)−1_{d odd}, which equals G_d/G_{d−1} for d≥2; for d=1 the only successor is terminal. This recovers the two ordered counts G_n/G_{n−k} and G_n/H_{n−k} on their allowed branches, including the zero alternating complement. Division by k! gives unordered cliques; the empty clique is separate and forbidden terms are omitted (G₀ is not used). Verified both n=4 example polynomials and m₂=16, m₄=160, m₆=32 for (6,2). Inspected VERIFICATION.md and verify.py without running them: all-size finite enumeration is configured for ten cases, with literal product checks on six, not a universal or formal certificate.

## originality

PASS

Bounded pass for exact all-size clique and terminal-frame enumeration of the specified ordinary-transpose rank-one graph, not for the classical projection correspondence, bilinear form classification or group orders. The closest checked graph theorems and indexed counts concern different adjacencies or allow different vertex classes, and none supplies the two residual-type enumerators for this graph.

## value

PASS

A natural question for the commuting graph is whether partial commuting families are extendible to maximal cardinality. The alternating complement gives a real obstruction, including isolated vertices or two-vertex terminal families in unbounded dimension. Resolving every terminal size and count together with the full counting polynomial quantifies this phenomenon across all characteristic-two orders; a maximum-clique calculation alone would miss it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
