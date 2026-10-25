---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Under lax team semantics, disjunction of n distinct constancy atoms means all relation tuples can be covered by n axis-parallel coordinate hyperplanes, one fixed value per coordinate. For infinite teams, a finite-character induction fixes a root tuple and one coordinate satisfying every finite subteam, reducing to n-1 coordinates. For finite inclusion-minimal un-coverable U, deletion of each u has a coordinate hyperplane cross-cover missing u; labeling finite values in Q gives tensor factors P(v)=tensor(1,h_i(v_i)) and Q(u)=tensor(-h_i(a_i^(u)),1), producing a diagonal pairing with all diagonal values nonzero. Thus |U|<=dim((Q^2)^tensor n)=2^n. The full Boolean cube is an inclusion-minimal obstruction of that size; any <=n tuples are coverable, and an n+1 point diagonal is minimally failing. Handles n=1, empty and infinite teams; do not confuse at-most-size coherence with exactly-k convention.

## originality

PASS

Fröhlich–Kolaitis–Meier Corollary 23 establishes the n=2 case (width4), which is credited, and their general scope is disjunctions of TWO atoms. Barlag et al treat finite-domain propositional team coherence and logic rewritability rather than domain-independent optimal 2^n for arbitrary numbers n of distinct constancy atoms. No definite stronger prior implication found; older database/Helly literature remains risk.

## value

PASS

An exact uniform forbidden-subteam/Helly number for cross-coverability on arbitrarily large coordinate domains is useful for finite witnesses, FO translation and logical coherence. The tensor bound with matching Boolean-cube obstruction is a natural complete classification of a parameterized family, not a trivial domain-cardinality bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
