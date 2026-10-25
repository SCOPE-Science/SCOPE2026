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

The coefficient 3 is a unit mod 8, and x+5y=3z+3u is equivalent to u=3x+7y-z on each coordinate of G=(Z/8)^2, with every repeated-variable possibility included. Exact independent enumeration of all 64^3 triples gives 31,152 distinct forbidden supports (96 pairs,3456 triples,27600 quadruples). Increasing-label rooted independent-set DFS applies F2,F3,F4 masks when a new vertex is chosen and eliminates precisely those partial subsets containing forbidden supports; pruning by remaining allowed-bit count is sound. Independent enumeration found 12,288 independent rooted eight-subsets, zero rooted nine-subsets, with source-matching node counts 57,143 and 16,096. Translation sends every maximal subset to a rooted one; double-counting incidences gives 98,304 total. Exhaustively checking the 1,536 matrices with odd determinant (the exact GL2 over Z8) gives four rooted orbit sizes 3,072 and the source four representatives, hence 24,576 unrooted per orbit. These are complete finite certificates for this one ring/group, not claims for all moduli or ranks.

## originality

PASS

Best-of-knowledge scientific originality after checking statement-level equivalence, stronger coverage, exact-table aliases, prior implications and accessible primary text. Direct mathematical priority risks remain documented.

## value

PASS

The translation-invariant equation has a recent asymptotic motivating literature. The first noncyclic rank-two group (Z/8)^2 is a natural finite testbed. The exact maximum, total extremizer count, and complete four affine orbits identify small-rank geometric patterns unavailable from construction lower bounds. This is valuable as an exact finite extremal classification even without claiming any higher-rank optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
