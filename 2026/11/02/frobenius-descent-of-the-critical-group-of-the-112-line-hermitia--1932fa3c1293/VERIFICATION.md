---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed finite Hermitian F9 line model (280 points,112 totally isotropic lines) and strongly regular (112,30,2,10) adjacency, Frobenius involution with eight fixed lines and 52 pairs, 60x60 orbit quotient Laplacian with primitive left/right kernels. Independently enumerated all 112 lines and recomputed p-local Smith valuations at p=2,5,7: 2:[0:12,2:36,3:1,5:10], 5:[0:48,1:11],7:[0:12,1:47], giving precisely 36 copies 28, one 280, ten 1120, plus free rank1. CRITICAL PROOF-TEXT ERRATUM: RESULT.md step5 states H_1(C2,Z)=0; in fact H_1(C2,Z)=Z/2. The claim nevertheless follows because an actual Frobenius-fixed line supplies an invariant degree-one class in coker(L), splitting the equivariant degree map coker L→Z as Z[C2]-modules; hence coker(B)=Z⊕K(G)_sigma. The Frobenius-invariant monodromy pairing dualizes K(G)^sigma to K(G)_sigma. Without that corrected splitting, the written H1 step is unsound. Entire proof is finite exact graph calculation plus this standard module argument, not an unsupported infinite generalization.

## originality

PASS

Best-of-knowledge qualified PASS after comparing mathematical implications, high-relevance primary material and related Resultary records; no decisive prior domination identified. Residual risks explicit.

## value

PASS

An integral Galois-equivariant critical-group decomposition of a natural maximal-line Hermitian quartic is stronger than the untwisted sandpile group. Exact arithmetic fixed/coinvariant groups, distinct from Picard/Brauer theory, are meaningful invariants of a classical finite configuration and could inform equivariant chip-firing and polar generalized quadrangle arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
