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

For edge-supported alternating B on K_{a,b,c}, split first a-by-b rectangular block X at rank r, whose count is Rq(a,b,r). Congruence reduces its support to 2r-dimensional symplectic J plus d=a+b−2r-dimensional nullspace. Cross blocks to the c-part yield T (2r×c) and U (d×c). For rank(U)=s, eliminating 2s hyperbolic coordinates gives rank(B)=2r+2s+rank(T0ᵀJ^{-1}T0), with T0 restricted to ker U dimension c−s; q^{2rs} choices for T on the complement. Counting all maps T0 by image dimension k, isotropic radical h=k−2j (Iq(r,h) isotropic h-planes), symplectic nondegenerate quotient 2j-planes and surjections gives exact Hq(r,c−s,j). Summing r,s,j=t−r−s proves the formula for any finite field including char2. For odd q, standard class-two Heisenberg character decomposition gives q^{n−2t} times the rank counts. Independent direct edge-weight matrix enumeration matched formula on K222 over F2, K221 and K211 over F3, and K122 over F2; K222 F2 vector (1,135,2376,1584); all sums equal q^m. Finite checks corroborate; congruence/subspace argument supplies universal proof.

## originality

PASS

PASS best-of-knowledge with clear separation from prior character conversion. Rossmann 2022 Question 1.10 asks rank-specific graphical character multiplicities; general fixed-rank-to-character conversion is known and not credited as new. Rossmann–Voll 2025 Theorem A gives ask-zeta functions for arbitrary graph joins, encoding averages of kernel sizes, not a stated vector of all fixed-field rank fibers. Fully read published October 4 coning result gives exact rank recurrence for K1∨Γ and explicitly K_{1,a,b} and iterated universal vertices; K_{a,b,c} with a,b,c≥2 has no universal vertex and cannot be obtained as a cone of K_{a,b}. Full cycle-graph result is a distinct graph family. The new symplectic pullback census gives all rank fibers of these non-cones. Historical Gram-matrix equivalents and more involved consequences of join-zeta remain priority risks.

## value

PASS

PASS: Determining exact rank-by-rank degeneracy of a natural patterned alternating-matrix space is a motivated finite-field enumeration problem. The complete tripartite non-cone family is the next nontrivial multipartite case beyond bipartite and coning. The formula yields every irreducible character-degree multiplicity, not merely average kernel size or total character count, providing an exact structural classification of natural graphical class-two group invariants for all part sizes and prime powers within the claimed character range. A useful exact distribution need not resolve arbitrary graph joins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
