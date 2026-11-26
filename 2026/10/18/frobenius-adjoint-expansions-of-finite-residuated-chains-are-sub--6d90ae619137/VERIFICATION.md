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

The adjunction gives monotonicity, unit/counit and preservation of the appropriate endpoints. F4 at y=0 and F1 imply fg=g, hence g is extensive; applying f to the counit and using extensivity gives gf=f. The common image is therefore the set to which f and g round. In the image F3 gives residual closure; for w=s⊗t, t≤s→w gives t=f(t)≤s→f(w) by F3, hence w≤f(w), proving fusion closure. In the converse, s→f(y) is in S and below s→y; if t=f(s→y), then s⊗t is in S and below y, giving the reverse F3 inequality by residuation. The two chain comparisons against a fixed s∈S give F4/F5, and the existence of an intervening element of S gives F2. Evaluating the floor or ceiling at elements of S recovers inclusion from pointwise order. In the integer-scaled Łukasiewicz chain, closure under truncated differences and sums forces every index to be a multiple of the least positive index, which must divide n−1. This proves the divisor count, including n=2. The frozen checker was inspected, not executed: its two enumerations are bounded corroboration, not the general proof. The docstring's alternate script name is incidental; the file is verify.py.

## originality

PASS

The distinct contribution supported by this comparison is the all-finite-chain converse and ordered classification for Wang–Shi–Wang's exact FARL axioms. The necessary fixed-image structure, the Gödel subcase, and the finite MV-subalgebra lattice are not new. A separately indexed record gives the same Łukasiewicz classification, not the general finite-chain result; its later displayed path provides no earlier priority evidence, and no independent novelty is assigned to the overlapping subcase.

## value

PASS

The result turns an operator-axiom search on a fixed finite chain into a complete, ordered subalgebra classification, including non-idempotent fusions where the Gödel/monadic result cannot simply be transferred. It proves that no further obstructions to realizing a subalgebra arise in that setting, and yields a useful closed census on the standard non-idempotent test family. The value is in realizability across finite chains, not in the familiar divisor arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
