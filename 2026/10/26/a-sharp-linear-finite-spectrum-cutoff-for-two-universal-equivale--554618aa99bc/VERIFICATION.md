---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

**Direct proof checks.** There are at most \(t+1\le k+1\) equivalence-class incidence profiles outside a witness set of size \(u\le k\). If the whole model has at least \(2k+2\) points then it has at least \(2k+2-u>t+1\) outside points, so two profiles repeat. Universal quantifier-free satisfaction is inherited by the core induced on all witness values plus the selected pair. Enlarging that pair preserves every ordered two-variable atomic type relative to the witnesses, including diagonals, equality, both orientations of \(E\), and marked-class memberships.

**Equivalence check.** A marked profile forces every pair of clones into the same marked class. An unmarked profile gives either a single new class or singleton classes, according to whether the original pair is related. All three arrangements are reflexive, symmetric and transitive.

**Sharp construction check.** The displayed sentence has exactly \(k\) distinct witness classes, with at most one extra element each, and at most one unmarked element. Choosing additions freely realizes all orders from \(k\) through \(2k+1\); the zero-witness case yields size \(1\) only.

No numerical enumeration, external proof assistant, or unverified computational certificate is needed. The result does not settle formula-length complexity, additional symbols, or higher universal-variable fragments. Novelty remains contingent on the documented bounded literature comparison.
