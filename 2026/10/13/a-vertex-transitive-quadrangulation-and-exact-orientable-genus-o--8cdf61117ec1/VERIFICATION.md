---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: GF(8) with x³+x+1 and P={0,1,2} has 56 affine translates, representing every triple. Exactly 10 affine disjointness generators form the displayed 10-cycle. Direct independent GF(8) construction checks all 1120 directed darts and finds 280 distinct simple four-cycle facial orbits, connected graph V=112,E=560; Euler yields g=85. Graph is bridgeless, simple, bipartite, so every orientable cellular face has length at least four; F≤E/2=280 gives g≥85. Swapping class and affine translations establishes vertex transitivity. This is a complete finite certificate for exactly H(8,3), not an infinite approximation.

## originality

PASS

PASS: Best-of-knowledge PASS: the explicit GF(8) rotation yields H(8,3) genus exactly 85, not covered by Metzger–Ulrigg main H(h,2) family; their full paper Section 9 places k≥3 among open territory, identifying this exceptional affine-transitive graph without resolving its genus. General graph rotation methods supply background, not the ten-element closure witness or 280 facial four-cycles.

## value

PASS

PASS: Settles the previously bounded natural graph H(8,3) from 85≤genus≤143, with explicit symmetric minimal orientable quadrangulation and independently checkable rotations. An exact genus for an exceptional vertex-transitive bipartite Kneser graph is independently useful; does not need a general H(n,k) theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
